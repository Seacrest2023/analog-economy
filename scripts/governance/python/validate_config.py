#!/usr/bin/env python3
"""
Layer 0: Config File Validation

Validates that configuration files parse correctly BEFORE running heavy tools.
If pyproject.toml or any config is corrupted, all downstream governance layers
fail-open. This catches config corruption first.

Usage:
    python scripts/governance/validate_config.py
"""
import json
import sys
from pathlib import Path

try:
    import tomllib
except ImportError:
    import tomli as tomllib  # Python < 3.11 fallback


def validate_toml(path: Path) -> bool:
    """Validate a TOML file parses correctly."""
    if not path.exists():
        return True  # File doesn't exist, nothing to validate
    try:
        with open(path, "rb") as f:
            tomllib.load(f)
        return True
    except Exception as e:
        print(f"FATAL: {path} is invalid TOML")
        print(f"  Error: {e}")
        return False


def validate_json(path: Path) -> bool:
    """Validate a JSON file parses correctly."""
    if not path.exists():
        return True
    try:
        with open(path) as f:
            json.load(f)
        return True
    except Exception as e:
        print(f"FATAL: {path} is invalid JSON")
        print(f"  Error: {e}")
        return False


def validate_yaml(path: Path) -> bool:
    """Validate a YAML file parses correctly."""
    if not path.exists():
        return True
    try:
        import yaml
        with open(path) as f:
            yaml.safe_load(f)
        return True
    except ImportError:
        # yaml not installed, skip validation
        return True
    except Exception as e:
        print(f"FATAL: {path} is invalid YAML")
        print(f"  Error: {e}")
        return False


def main():
    print("=" * 60)
    print("LAYER 0: Config File Validation")
    print("=" * 60)

    root = Path(__file__).parent.parent.parent
    errors = []

    # Python configs
    configs = [
        (root / "pyproject.toml", validate_toml),
        (root / "core-governance" / "pyproject.toml", validate_toml),
        # JSON configs
        (root / ".secrets.baseline", validate_json),
        (root / ".governance" / "type-safety-baseline.json", validate_json),
        (root / ".governance" / "mock-tax-baseline.json", validate_json),
        # YAML configs
        (root / "core-governance" / "gaian" / "config.yaml", validate_yaml),
    ]

    for config_path, validator in configs:
        if config_path.exists():
            print(f"  Validating {config_path.relative_to(root)}...")
            if not validator(config_path):
                errors.append(config_path)

    if errors:
        print()
        print("=" * 60)
        print("CONFIG VALIDATION FAILED")
        print("=" * 60)
        print()
        print("All downstream governance checks are DISABLED until fixed.")
        print("Fix the above config file errors before committing.")
        print()
        sys.exit(1)

    print()
    print("Config files valid")
    print("=" * 60)
    sys.exit(0)


if __name__ == "__main__":
    main()
