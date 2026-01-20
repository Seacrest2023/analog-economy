# STRUCTURAL-GOVERNANCE.md — Enforcing Architectural Patterns

> **The Structural Governance Strategy:** AI coders follow patterns they see.
> If patterns are inconsistent, AI perpetuates inconsistency.
> Enforce structure before logic.

---

## The Problem: Architecturally Blind AI

```
┌─────────────────────────────────────────────────────────────────────┐
│                    THE PATTERN DRIFT CYCLE                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Day 1: Team agrees on layer architecture                          │
│        ↓                                                            │
│   AI generates new code following visible patterns                  │
│        ↓                                                            │
│   One developer imports Core from API layer (it works!)             │
│        ↓                                                            │
│   AI sees both patterns → picks randomly                            │
│        ↓                                                            │
│   More developers → more violations → AI confusion                  │
│        ↓                                                            │
│   ARCHITECTURAL CHAOS (Circular imports, spaghetti)                 │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**AI coding tools are fast but don't know your conventions:**
- They follow whatever patterns exist in the codebase (good or bad)
- They can't distinguish "works" from "maintainable"
- They don't enforce layer boundaries or dependency direction
- They perpetuate inconsistency when patterns conflict

---

## The Analog Economy Layer Architecture

### The Brain (Python/FastAPI)

```
┌─────────────────────────────────────────────────────────────────────┐
│                    PYTHON LAYER ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │                        API Layer                             │   │
│   │   gaian/api/                                                 │   │
│   │   • FastAPI routers                                          │   │
│   │   • Request/Response handling                                │   │
│   │   • Depends() for DI                                         │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                              ▼                                      │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │                      Service Layer                           │   │
│   │   gaian/services/                                            │   │
│   │   • Business logic orchestration                             │   │
│   │   • Calls Core for pure logic                                │   │
│   │   • Calls Repository for persistence                         │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                              ▼                                      │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │                        Core Layer                            │   │
│   │   gaian/core/                                                │   │
│   │   • Pure business logic (NO I/O)                             │   │
│   │   • Domain models                                            │   │
│   │   • Calculation engines                                      │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                              ▼                                      │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │                     Repository Layer                         │   │
│   │   gaian/repositories/                                        │   │
│   │   • Database operations                                      │   │
│   │   • External API clients                                     │   │
│   │   • File system access                                       │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

DEPENDENCY FLOW (arrows show allowed imports):
  API → Services → Core
  API → Services → Repositories
  Core → (nothing - pure)
  Repositories → Core (for domain models only)

FORBIDDEN:
  ❌ Core → API (circular)
  ❌ Core → Services (circular)
  ❌ Core → Repositories (I/O in pure layer)
  ❌ Repositories → API (bypass layers)
```

### The Body (UE5/C++)

```
┌─────────────────────────────────────────────────────────────────────┐
│                    UE5 LAYER ARCHITECTURE                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │                      UI Layer                                │   │
│   │   Source/AnalogEconomy/UI/                                   │   │
│   │   • Widgets (UMG)                                            │   │
│   │   • HUD elements                                             │   │
│   │   • Menus                                                    │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                              ▼                                      │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │                    Gameplay Layer                            │   │
│   │   Source/AnalogEconomy/Gameplay/                             │   │
│   │   • Actors, Components                                       │   │
│   │   • Game state                                               │   │
│   │   • Player controller                                        │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                              ▼                                      │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │                   Subsystem Layer                            │   │
│   │   Source/AnalogEconomy/Subsystems/                           │   │
│   │   • GaianSubsystem (network bridge)                          │   │
│   │   • Manages Brain communication                              │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                              ▼                                      │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │                    Network Layer                             │   │
│   │   Source/AnalogEconomy/Network/                              │   │
│   │   • HTTP client                                              │   │
│   │   • WebSocket handling                                       │   │
│   │   • Serialization                                            │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

FORBIDDEN:
  ❌ Gameplay → Network directly (must go through GaianSubsystem)
  ❌ UI → Network (must go through Gameplay → GaianSubsystem)
```

---

## Python Enforcement: import-linter

[import-linter](https://github.com/seddonym/import-linter) is a Python tool that enforces import rules at the module level.

### Installation

```bash
pip install import-linter
```

### Configuration

```toml
# pyproject.toml
[tool.importlinter]
root_package = "gaian"

[[tool.importlinter.contracts]]
name = "Core cannot import API or Services"
type = "forbidden"
source_modules = ["gaian.core"]
forbidden_modules = ["gaian.api", "gaian.services"]

[[tool.importlinter.contracts]]
name = "Core cannot import Repositories"
type = "forbidden"
source_modules = ["gaian.core"]
forbidden_modules = ["gaian.repositories"]

[[tool.importlinter.contracts]]
name = "Repositories cannot import API"
type = "forbidden"
source_modules = ["gaian.repositories"]
forbidden_modules = ["gaian.api"]

[[tool.importlinter.contracts]]
name = "Layer dependency direction"
type = "layers"
layers = [
    "gaian.api",
    "gaian.services",
    "gaian.core",
]
# Top can import from bottom, not reverse
```

### Running import-linter

```bash
# Check all contracts
lint-imports

# With details
lint-imports --verbose
```

### Example Output

```
=============
Import Linter
=============

Checking contracts...

Contracts: 4 found
-------------------

Core cannot import API or Services  KEPT
Core cannot import Repositories     KEPT
Repositories cannot import API      KEPT
Layer dependency direction          BROKEN

Contracts broken: 1

--------------------------------------------------
Broken contract: Layer dependency direction
--------------------------------------------------

gaian.core.scoring imports gaian.services.user_service
  in gaian/core/scoring.py (line 5)

This is not allowed because gaian.services is a higher layer than gaian.core.
```

### Pre-commit Integration

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: import-linter
        name: Import Linter (Layer Architecture)
        entry: lint-imports
        language: system
        pass_filenames: false
        types: [python]
```

---

## UE5 Enforcement: The GaianSubsystem Rule

### The Problem

```cpp
// WRONG: Gameplay directly accessing Network
// Source/AnalogEconomy/Gameplay/CraftingStation.cpp

#include "Network/GameHttpClient.h"  // ❌ FORBIDDEN

void ACraftingStation::StartCrafting(const FCraftingRecipe& Recipe)
{
    // Direct network call - bypasses subsystem!
    UGameHttpClient* Client = NewObject<UGameHttpClient>();
    Client->Post("/api/craft", Recipe.ToJson());  // ❌ BAD
}
```

### The Solution

```cpp
// RIGHT: Gameplay goes through GaianSubsystem
// Source/AnalogEconomy/Gameplay/CraftingStation.cpp

#include "Subsystems/GaianSubsystem.h"  // ✅ ALLOWED

void ACraftingStation::StartCrafting(const FCraftingRecipe& Recipe)
{
    UGaianSubsystem* Gaian = GetWorld()->GetSubsystem<UGaianSubsystem>();
    Gaian->RequestCraft(Recipe);  // ✅ Subsystem handles network
}
```

### UE5 Include Guard Script

Create a custom Unreal build script that blocks forbidden includes:

```python
#!/usr/bin/env python3
"""
UE5 Include Guard

Enforces layer architecture by blocking forbidden #include directives.
Run as part of pre-commit or UBT custom step.
"""

import re
import sys
from pathlib import Path

# Define layer rules
LAYER_RULES = {
    "Gameplay": {
        "allowed": ["Subsystems", "Core", "Validation"],
        "forbidden": ["Network"],
    },
    "UI": {
        "allowed": ["Gameplay"],
        "forbidden": ["Network", "Subsystems"],
    },
}


def get_layer(filepath: Path) -> str | None:
    """Determine which layer a file belongs to."""
    path_str = str(filepath)
    for layer in LAYER_RULES:
        if f"/{layer}/" in path_str or f"\\{layer}\\" in path_str:
            return layer
    return None


def get_included_layer(include_line: str) -> str | None:
    """Extract layer from #include directive."""
    # Match: #include "Layer/SomeFile.h"
    match = re.search(r'#include\s+"([^/]+)/', include_line)
    if match:
        return match.group(1)
    return None


def check_file(filepath: Path) -> list[dict]:
    """Check a file for forbidden includes."""
    layer = get_layer(filepath)
    if not layer or layer not in LAYER_RULES:
        return []

    rules = LAYER_RULES[layer]
    violations = []

    content = filepath.read_text()
    for i, line in enumerate(content.splitlines(), 1):
        if not line.strip().startswith("#include"):
            continue

        included_layer = get_included_layer(line)
        if included_layer and included_layer in rules["forbidden"]:
            violations.append({
                "file": str(filepath),
                "line": i,
                "include": line.strip(),
                "issue": f"{layer} cannot include {included_layer}",
            })

    return violations


def main() -> int:
    source_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("Source/AnalogEconomy")

    if not source_dir.exists():
        print(f"Source directory not found: {source_dir}")
        return 0

    all_violations: list[dict] = []

    for cpp_file in source_dir.rglob("*.cpp"):
        violations = check_file(cpp_file)
        all_violations.extend(violations)

    for h_file in source_dir.rglob("*.h"):
        violations = check_file(h_file)
        all_violations.extend(violations)

    if all_violations:
        print("\n🚫 UE5 LAYER VIOLATION: Forbidden Includes Detected\n")
        for v in all_violations:
            print(f"  {v['file']}:{v['line']}")
            print(f"    {v['include']}")
            print(f"    {v['issue']}\n")
        print("REMEDIATION:")
        print("  Gameplay code must use GaianSubsystem for network access.")
        print("  See: docs/guides/architecture/STRUCTURAL-GOVERNANCE.md\n")
        return 1

    print("✓ UE5 layer check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

---

## Biome Isolation (Future)

As the game grows, different biomes (eras, regions) will have isolated code:

```
gaian/
├── core/                    # Shared pure logic
│   ├── scoring.py
│   └── economy.py
├── biomes/                  # Era-specific code
│   ├── ancient/            # Eridu 4500 BCE
│   │   ├── crafting.py
│   │   └── resources.py
│   ├── classical/          # Future era
│   │   └── ...
│   └── medieval/           # Future era
│       └── ...
```

### Biome Import Rules

```toml
# pyproject.toml
[[tool.importlinter.contracts]]
name = "Biomes are isolated"
type = "independence"
modules = [
    "gaian.biomes.ancient",
    "gaian.biomes.classical",
    "gaian.biomes.medieval",
]
# No biome can import from another biome

[[tool.importlinter.contracts]]
name = "Biomes can import core"
type = "layers"
layers = [
    "gaian.biomes",
    "gaian.core",
]
```

---

## Why This Matters

### The Physics Principle

> **"Agents obey Physics, not Policy"**

- **Policy:** Architecture docs, wiki pages, team agreements → AI ignores these
- **Physics:** Import errors, failed builds, blocked commits → AI must fix these

Structural Governance converts architectural policy into physics:
- `import-linter` rules = physics (AI cannot bypass)
- Team wiki = policy (AI doesn't read)

### Pattern Consistency

When AI generates code, it samples from visible patterns. If 3 patterns exist for "how to call the database," AI picks randomly.

With Structural Governance:
- Only 1 pattern is valid (Services → Repositories)
- Violations surface immediately
- AI learns to use the correct pattern

### Preventing Circular Imports

Python's circular import problem is brutal. Without enforcement:

```python
# gaian/core/scoring.py
from gaian.services.user import get_user  # ❌ Circular!

# gaian/services/user.py
from gaian.core.scoring import calculate_score  # ❌ Circular!

# Result: ImportError at runtime
```

With import-linter, this is caught at commit time.

---

## CI Integration

```yaml
# .github/workflows/governance-ci.yml
jobs:
  structural-governance:
    name: "Structural Governance"
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install import-linter
        run: pip install import-linter

      - name: Check import contracts
        run: lint-imports --verbose
        working-directory: core-governance

      - name: Check UE5 layer rules
        run: python scripts/governance/python/check_ue5_layers.py
        if: hashFiles('client-simulation/Source/**') != ''
```

---

## Troubleshooting

### Import-linter Not Finding Violations

1. Ensure `root_package` matches your package name
2. Check that the module paths in contracts are correct
3. Run with `--verbose` to see what's being scanned

### False Positives

Use `ignore_imports` for legitimate exceptions:

```toml
[[tool.importlinter.contracts]]
name = "Core cannot import Services"
type = "forbidden"
source_modules = ["gaian.core"]
forbidden_modules = ["gaian.services"]
ignore_imports = [
    "gaian.core.exceptions -> gaian.services.errors",  # Legacy, will fix
]
```

### Performance

For large codebases:
- Use specific module paths instead of wildcards
- Run import-linter only on changed files in pre-commit
- Full scan in CI only

---

## Summary

| Layer | Can Import | Cannot Import |
|-------|------------|---------------|
| **API** | Services, Core | - |
| **Services** | Core, Repositories | API |
| **Core** | Nothing (pure) | API, Services, Repositories |
| **Repositories** | Core (models only) | API, Services |
| **UE5 Gameplay** | GaianSubsystem | Network directly |
| **UE5 UI** | Gameplay | Network, Subsystems |

---

## Related

- [TDD-GUIDE.md](../development/TDD-GUIDE.md) — Pure Core pattern enforcement
- [IRON-DOME.md](../project%20setup/IRON-DOME.md) — Type safety governance
- [directory-structure.md](./directory-structure.md) — Project organization

---

*Part of The Analog Economy Production-Readiness Kit*
