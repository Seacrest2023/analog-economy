"""
Base Biome - Abstract base class for biome-specific rules.

Each biome can tighten (never loosen) global ethics rules.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class BiomeContext:
    """Context information for biome rule evaluation."""

    biome_id: str
    ethics_level: str  # "normal", "elevated", "high", "maximum"
    classification: str  # "STANDARD", "SENSITIVE", "RESTRICTED", "CRITICAL"
    special_rules: list[str]


class BaseBiome(ABC):
    """
    Abstract base class for biome-specific ethics rules.

    Biomes can:
    - Add additional ethics checks
    - Tighten existing rules
    - Define special export restrictions

    Biomes CANNOT:
    - Loosen global ethics rules
    - Bypass critical safety checks
    """

    def __init__(self, config: dict[str, Any]):
        """Initialize biome with configuration."""
        self.config = config
        self.biome_id = config.get("id", "unknown")
        self.ethics_level = config.get("ethics_level", "normal")
        self.classification = config.get("classification", "STANDARD")
        self.special_rules = config.get("special_rules", [])

    @property
    def context(self) -> BiomeContext:
        """Get biome context for rule evaluation."""
        return BiomeContext(
            biome_id=self.biome_id,
            ethics_level=self.ethics_level,
            classification=self.classification,
            special_rules=self.special_rules,
        )

    @abstractmethod
    def apply_ethics_rules(self, telemetry: dict[str, Any]) -> list[str]:
        """
        Apply biome-specific ethics rules.

        Args:
            telemetry: Player action telemetry data

        Returns:
            List of ethics violations specific to this biome
        """
        pass

    @abstractmethod
    def get_export_restrictions(self) -> dict[str, Any]:
        """
        Get biome-specific export restrictions.

        Returns:
            Dictionary of export restrictions for this biome
        """
        pass

    def get_novelty_weight(self) -> float:
        """Get novelty scoring weight for this biome."""
        weight = self.config.get("novelty_weight", 1.0)
        return float(weight) if isinstance(weight, int | float) else 1.0

    def requires_human_review(self, record_count: int) -> bool:
        """Check if exports from this biome require human review."""
        restrictions = self.config.get("additional_restrictions", {})
        if not isinstance(restrictions, dict):
            return False
        threshold = restrictions.get("human_review_threshold", float("inf"))
        return bool(record_count >= float(threshold))
