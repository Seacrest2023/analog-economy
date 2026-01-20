# SUPPLY-CHAIN-SECURITY.md — Defending Against AI Hallucinations

> **The Supply Chain Strategy:** AI assistants hallucinate package names ~5-10% of the time. Attackers register these names on PyPI with malware. Validate dependencies BEFORE installation.

---

## The Problem: The AI Hallucination Attack Vector

```
┌─────────────────────────────────────────────────────────────────────┐
│                    THE HALLUCINATION ATTACK                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   1. AI coding assistant suggests:                                  │
│      from utils_helper import process_data                          │
│        ↓                                                            │
│   2. Package 'utils-helper' doesn't exist (hallucination)           │
│        ↓                                                            │
│   3. Attacker monitors PyPI search traffic for non-existent names   │
│        ↓                                                            │
│   4. Attacker registers 'utils-helper' with malicious setup.py      │
│        ↓                                                            │
│   5. Developer runs `pip install -r requirements.txt`               │
│        ↓                                                            │
│   6. setup.py executes immediately with full system access          │
│        ↓                                                            │
│   COMPROMISED — Malware now has access to your machine              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Traditional tools don't catch this:**

| Tool | What It Catches | Blind Spot |
|------|-----------------|------------|
| `pip-audit` | Known CVEs in existing packages | New packages have no CVE history |
| `pip install --require-hashes` | Hash mismatches | Doesn't check if package is legitimate |
| Code review | Logic bugs | Humans don't memorize PyPI's 500K+ packages |
| Type checkers | Type errors | Import statements look syntactically valid |

---

## Attack Variants

### 1. Pure Hallucination

AI invents a package name that sounds plausible but never existed.

```python
# AI suggests (hallucinated):
from email_validator_utils import validate_email

# Real package is:
from email_validator import validate_email
```

### 2. Typosquatting

AI misspells a popular package name. Attackers pre-register typos.

```python
# AI typo:
import requets  # Wrong!

# Real package:
import requests
```

### 3. Namespace Confusion

AI uses wrong package name format.

```python
# AI suggests:
from python_dateutil import parser  # Doesn't exist!

# Real package:
from dateutil import parser  # Package name is python-dateutil
```

---

## Defense Strategy: Pre-Install Validation

The key insight: **Validate BEFORE pip runs.** Once `pip install` executes, setup.py runs immediately with full system access.

### Defense Layers

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SUPPLY CHAIN DEFENSE LAYERS                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Layer 1: PRE-COMMIT HOOK                                           │
│    • Runs when requirements.txt changes                             │
│    • Validates packages before they're committed                    │
│    • Blocks suspicious packages immediately                         │
│                                                                     │
│  Layer 2: CI STATIC CHECKS (Before pip install)                     │
│    • Runs BEFORE pip install                                        │
│    • No venv needed (pure Python with stdlib)                       │
│    • Prevents setup.py execution                                    │
│                                                                     │
│  Layer 3: LOCKFILE INTEGRITY (pip --require-hashes)                 │
│    • Fails if hashes don't match                                    │
│    • Prevents "magic" package substitution                          │
│                                                                     │
│  Layer 4: VULNERABILITY AUDIT (pip-audit)                           │
│    • Catches known CVEs in dependencies                             │
│    • Limited to packages with reported vulnerabilities              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Detection Criteria

The hallucination detector blocks packages that:

### 1. Don't Exist (True Hallucination)

Package not found in PyPI. This is the most dangerous scenario — if it doesn't exist yet, an attacker could register it.

```bash
$ pip index versions my-fake-package
ERROR: No matching distribution found for my-fake-package
```

**Action:** BLOCK immediately.

### 2. Are Very New (< 30 Days Old)

Legitimate packages have history. AI hallucinations get registered quickly by attackers monitoring PyPI upload traffic.

```python
# Query PyPI API
response = requests.get("https://pypi.org/pypi/suspicious-package/json")
data = response.json()
first_release = min(data["releases"].keys())
upload_time = data["releases"][first_release][0]["upload_time"]
# If created < 30 days ago → suspicious!
```

**Action:** BLOCK and require human review.

### 3. Have Very Low Downloads

Real packages have users. Ghost packages registered by attackers have no organic downloads.

```bash
# Real package:
requests: 300,000,000 downloads/month

# Ghost package:
utils-helper: 5 downloads/month  # Suspicious!
```

**Action:** WARN and flag for review.

---

## Implementation

### The Hallucination Detector Script

```python
#!/usr/bin/env python3
"""
Supply Chain Security: AI Hallucination/Typosquat Detector

Purpose: Detect potentially malicious packages BEFORE pip install runs.
         This runs in CI before installation, preventing setup.py
         script execution from potentially malicious packages.

Detection criteria:
  - Package doesn't exist in PyPI registry (true hallucination)
  - Package is < 30 days old (AI hallucinations are brand new)

Usage:
  python check_supply_chain.py requirements.txt
  python check_supply_chain.py --verbose

Exit codes:
  0 - All packages passed validation
  1 - Suspicious packages detected (BLOCKED)
"""

import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import urlopen

# Configuration
MIN_DAYS_OLD = 30
EXEMPTIONS_FILE = ".supply-chain-exemptions.json"

# Well-known packages that don't need checking (core ecosystem)
TRUSTED_PACKAGES = {
    # Core Python
    "setuptools", "wheel", "pip",
    # Web frameworks
    "fastapi", "uvicorn", "starlette", "pydantic", "httpx",
    # Database
    "sqlalchemy", "asyncpg", "psycopg2", "alembic",
    # Testing
    "pytest", "pytest-cov", "pytest-asyncio", "coverage",
    # Code quality
    "black", "isort", "ruff", "mypy", "pre-commit",
    # Utilities
    "python-dotenv", "structlog", "click", "rich",
}


def load_exemptions() -> list[dict]:
    """Load exemptions from file."""
    exemptions_path = Path(EXEMPTIONS_FILE)
    if not exemptions_path.exists():
        return []
    try:
        content = exemptions_path.read_text()
        exemptions = json.loads(content)
        return exemptions if isinstance(exemptions, list) else []
    except Exception:
        print(f"Warning: Could not parse {EXEMPTIONS_FILE}")
        return []


def get_package_info(package_name: str) -> dict:
    """Query PyPI registry for package metadata."""
    url = f"https://pypi.org/pypi/{package_name}/json"
    try:
        with urlopen(url, timeout=10) as response:
            data = json.loads(response.read())

            # Get first upload date
            releases = data.get("releases", {})
            if not releases:
                return {"exists": True, "age_days": None}

            # Find earliest release
            earliest_date = None
            for version, files in releases.items():
                if files:
                    upload_time = files[0].get("upload_time")
                    if upload_time:
                        dt = datetime.fromisoformat(upload_time.replace("Z", "+00:00"))
                        if earliest_date is None or dt < earliest_date:
                            earliest_date = dt

            if earliest_date:
                age = (datetime.now(timezone.utc) - earliest_date).days
                return {"exists": True, "age_days": age, "created_at": earliest_date.isoformat()}

            return {"exists": True, "age_days": None}

    except HTTPError as e:
        if e.code == 404:
            return {"exists": False, "age_days": None}
        raise
    except Exception:
        # Network error - assume OK to avoid blocking on transient issues
        return {"exists": True, "age_days": None}


def parse_requirements(filepath: Path) -> list[str]:
    """Parse package names from requirements.txt."""
    packages = []
    content = filepath.read_text()

    for line in content.splitlines():
        line = line.strip()
        # Skip comments and empty lines
        if not line or line.startswith("#") or line.startswith("-"):
            continue
        # Skip editable installs and URLs
        if line.startswith("git+") or line.startswith("http"):
            continue

        # Extract package name (before version specifier)
        # Handles: package==1.0, package>=1.0, package~=1.0, package[extra]
        match = re.match(r"^([a-zA-Z0-9_-]+)", line)
        if match:
            packages.append(match.group(1).lower())

    return packages


def should_skip(package_name: str, exemptions: list[dict]) -> bool:
    """Check if package should be skipped."""
    # Normalize package name
    normalized = package_name.lower().replace("_", "-")

    # Trusted packages
    if normalized in TRUSTED_PACKAGES:
        return True

    # Exempted packages
    return any(e.get("package", "").lower() == normalized for e in exemptions)


def main() -> int:
    args = sys.argv[1:]
    verbose = "--verbose" in args or "-v" in args

    # Find requirements file
    req_files = [a for a in args if not a.startswith("-")]
    req_file = Path(req_files[0]) if req_files else Path("requirements.txt")

    print("Supply Chain Security: Hallucination Detector")
    print("=" * 60 + "\n")

    if not req_file.exists():
        print(f"No {req_file} found. Skipping check.\n")
        return 0

    exemptions = load_exemptions()
    all_packages = parse_requirements(req_file)

    print(f"Total packages: {len(all_packages)}")

    packages_to_check = [p for p in all_packages if not should_skip(p, exemptions)]
    print(f"Packages to validate: {len(packages_to_check)}\n")

    if not packages_to_check:
        print("All packages are trusted. No validation needed.\n")
        return 0

    print("Validating packages...\n")

    violations = []

    for package in packages_to_check:
        info = get_package_info(package)

        if not info["exists"]:
            violations.append({
                "package": package,
                "reason": "Package does not exist in PyPI registry",
                "severity": "critical",
            })
            print(f"  [CRITICAL] {package} - NOT FOUND")
        elif info["age_days"] is not None and info["age_days"] < MIN_DAYS_OLD:
            violations.append({
                "package": package,
                "reason": f"Package is only {info['age_days']} days old",
                "severity": "high",
                "created_at": info.get("created_at"),
            })
            print(f"  [HIGH] {package} - Only {info['age_days']} days old")
        elif verbose:
            age = info.get("age_days", "?")
            print(f"  [OK] {package} ({age} days old)")

    print("")

    if not violations:
        print("All packages passed supply chain validation.\n")
        return 0

    # BLOCKED
    print("-" * 60)
    print(f"\nBLOCKED: {len(violations)} suspicious package(s) detected.\n")

    print("VIOLATIONS:\n")
    for v in violations:
        print(f"  Package: {v['package']}")
        print(f"  Reason: {v['reason']}")
        print(f"  Severity: {v['severity'].upper()}")
        if v.get("created_at"):
            print(f"  Created: {v['created_at']}")
        print("")

    print("FIX OPTIONS:")
    print("  1. Remove the suspicious package")
    print("  2. Use a well-known alternative")
    print("  3. If legitimate, add to .supply-chain-exemptions.json:\n")
    print('     [{"package": "name", "reason": "Verified by human",')
    print('       "addedBy": "your-name", "date": "YYYY-MM-DD"}]\n')
    print("-" * 60 + "\n")

    return 1


if __name__ == "__main__":
    sys.exit(main())
```

---

## Pre-commit Configuration

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: supply-chain-security
        name: Supply Chain Security (Hallucination Detector)
        entry: python scripts/governance/python/check_supply_chain.py
        language: system
        files: requirements.*\.txt$
        pass_filenames: true
        stages: [pre-commit]
```

---

## CI Configuration (GitHub Actions)

The detector MUST run BEFORE `pip install` in your CI pipeline:

```yaml
# .github/workflows/governance-ci.yml
jobs:
  supply-chain:
    name: "Supply Chain Security"
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      # CRITICAL: Run BEFORE pip install
      - name: "Supply Chain: Hallucination Detector"
        run: python scripts/governance/python/check_supply_chain.py requirements.txt

      # Now safe to install
      - name: Install dependencies
        run: pip install -r requirements.txt
```

---

## Lockfile Best Practices

### Use pip-compile for Reproducible Builds

```bash
# Install pip-tools
pip install pip-tools

# Generate locked requirements with hashes
pip-compile --generate-hashes requirements.in -o requirements.txt
```

### requirements.in (What you want)

```
fastapi>=0.109.0
uvicorn[standard]
sqlalchemy>=2.0
pydantic>=2.5
```

### requirements.txt (What pip installs - locked with hashes)

```
fastapi==0.109.1 \
    --hash=sha256:abc123...

uvicorn==0.27.0 \
    --hash=sha256:def456...

# etc.
```

### CI with Hash Verification

```yaml
- name: Install dependencies with hash verification
  run: pip install --require-hashes -r requirements.txt
```

---

## Exemptions File

For legitimate packages that trigger false positives:

```json
[
  {
    "package": "internal-company-utils",
    "reason": "Internal package from our private PyPI",
    "addedBy": "john.doe",
    "date": "2025-01-15"
  },
  {
    "package": "new-framework-beta",
    "reason": "New but legitimate framework, verified on GitHub",
    "addedBy": "security-team",
    "date": "2025-01-20"
  }
]
```

### Exemption Requirements

1. **Human verification** — Only humans can add exemptions
2. **Justification** — Must explain why package is legitimate
3. **Attribution** — Must include who approved
4. **Audit trail** — Date of approval for future review

---

## Common Typosquatting Targets

Packages frequently typosquatted on PyPI:

| Real Package | Common Typos |
|--------------|--------------|
| `requests` | `requets`, `request`, `reqeusts` |
| `beautifulsoup4` | `beautifulsoup`, `beautiful-soup` |
| `python-dateutil` | `dateutil`, `python_dateutil` |
| `scikit-learn` | `sklearn`, `scikit_learn` |
| `Pillow` | `pillow`, `PIL` |
| `opencv-python` | `opencv`, `cv2` |

---

## The Rising Tide Protocol

### Green Zone: New Projects

**Mandatory enforcement from day one.**

```yaml
# CI enforces before every pip install
- name: "Supply Chain Check"
  run: python scripts/governance/python/check_supply_chain.py
```

Configuration:
- Block non-existent packages
- Block packages < 30 days old
- No exemptions without human review

### Yellow Zone: Active Development

**Add detector to existing CI pipeline.**

1. Run detector in warning mode first
2. Audit flagged packages manually
3. Add legitimate packages to exemptions file
4. Switch to blocking mode

### Red Zone: Legacy Projects

**Document and freeze.**

For projects with many dependencies:

1. Generate baseline of current packages
2. Block NEW package additions without review
3. Don't retroactively audit all existing packages

---

## Summary

| Concept | Description |
|---------|-------------|
| **Hallucination Attack** | AI suggests non-existent packages that attackers weaponize |
| **Pre-Install Validation** | Check packages BEFORE pip runs setup.py |
| **Age Gate** | Block packages < 30 days old (new = suspicious) |
| **Lockfiles** | Use pip-compile with --generate-hashes |
| **Exemptions** | Human-verified exceptions with audit trail |

---

## Related

- [IRON-DOME.md](../project%20setup/IRON-DOME.md) — Type safety and governance layers
- [SCHEMA-VALIDATION.md](./SCHEMA-VALIDATION.md) — Runtime type safety with Pydantic
- [PRECOMMIT-SETUP.md](../project%20setup/PRECOMMIT-SETUP.md) — Pre-commit hook configuration

> **Note:** Supply Chain Security defends against external package threats. For internal code quality, see [IRON-DOME.md](../project%20setup/IRON-DOME.md).

---

*Part of The Analog Economy Production-Readiness Kit*
