"""
Ethics Filter - Moral boundary enforcement for Gaian governance.

This module enforces ethical boundaries on training data, ensuring
that exported data cannot be used for harmful purposes.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any


class EthicsViolationType(Enum):
    """Categories of ethics violations."""
    TERROR_INSTRUCTION = "terror_instruction"
    BIOWEAPON_SYNTHESIS = "bioweapon_synthesis"
    CHILD_HARM = "child_harm"
    REAL_WORLD_TARGETING = "real_world_targeting"
    FACIAL_RECOGNITION = "facial_recognition"
    WEAPON_MANUFACTURING = "weapon_manufacturing"
    SURVEILLANCE_ENHANCEMENT = "surveillance_enhancement"
    VIOLENCE_EXCESS = "violence_excess"
    PII_EXPOSURE = "pii_exposure"


@dataclass
class EthicsResult:
    """Result of ethics evaluation."""
    passed: bool
    violations: list[EthicsViolationType]
    severity: str  # "none", "warning", "critical"
    details: dict[str, Any]


class EthicsFilter:
    """
    Enforces ethical boundaries on telemetry and training data.

    Red lines that cannot be crossed:
    - No actionable terrorism instructions
    - No bioweapon synthesis
    - No child harm content
    - No real-world targeting
    - No facial recognition training (in restricted biomes)
    - No weapon manufacturing instructions
    - No surveillance enhancement tools
    """

    def __init__(self, config: dict[str, Any]):
        """Initialize ethics filter with configuration."""
        self.config = config.get("ethics", {})
        self.global_rules = self._load_global_rules()

    def _load_global_rules(self) -> dict[str, bool]:
        """Load global ethics rules from config."""
        return {
            "block_terror_instruction": self.config.get("block_terror_instruction", True),
            "block_bioweapon_synthesis": self.config.get("block_bioweapon_synthesis", True),
            "block_child_harm": self.config.get("block_child_harm", True),
            "block_real_world_targeting": self.config.get("block_real_world_targeting", True),
            "facial_recognition_training": self.config.get("facial_recognition_training", False),
            "weapon_manufacturing": self.config.get("weapon_manufacturing", False),
            "surveillance_enhancement": self.config.get("surveillance_enhancement", False),
        }

    def evaluate(
        self,
        telemetry: dict[str, Any],
        biome_config: dict[str, Any]
    ) -> EthicsResult:
        """
        Evaluate telemetry against ethics rules.

        Args:
            telemetry: Player action telemetry data
            biome_config: Biome-specific ethics configuration

        Returns:
            EthicsResult with pass/fail and violation details
        """
        violations = []

        # TODO: Implement ethics violation detection
        # This will involve NLP analysis, pattern matching,
        # and biome-specific rule application

        # Apply global rules
        # Apply biome-specific tightening (never loosening)

        if not violations:
            return EthicsResult(
                passed=True,
                violations=[],
                severity="none",
                details={}
            )

        severity = self._calculate_severity(violations)

        return EthicsResult(
            passed=False,
            violations=violations,
            severity=severity,
            details={"biome_ethics_level": biome_config.get("ethics_level", "normal")}
        )

    def _calculate_severity(self, violations: list[EthicsViolationType]) -> str:
        """Determine overall severity from violation list."""
        critical_violations = {
            EthicsViolationType.TERROR_INSTRUCTION,
            EthicsViolationType.BIOWEAPON_SYNTHESIS,
            EthicsViolationType.CHILD_HARM,
            EthicsViolationType.REAL_WORLD_TARGETING,
        }

        if any(v in critical_violations for v in violations):
            return "critical"

        return "warning"
