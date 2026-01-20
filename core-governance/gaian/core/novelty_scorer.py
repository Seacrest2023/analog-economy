"""
Novelty Scorer - Evaluates solution value for token rewards.

This module determines how many Novelty Tokens a player earns
based on the creativity, efficiency, and uniqueness of their solutions.
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class NoveltyScore:
    """Result of novelty evaluation."""
    base_tokens: int
    multipliers_applied: dict[str, float]
    final_tokens: int
    novelty_factors: list[str]
    diminishing_returns_applied: bool


class NoveltyScorer:
    """
    Evaluates the novelty and value of player solutions.

    Scoring factors:
    - Efficiency: Solved faster than average
    - Creativity: Used tools in unexpected ways
    - Collaboration: Worked with other players
    - First solution: First to solve a new problem type
    - Edge case: Handled an unusual scenario
    """

    def __init__(self, config: dict[str, Any]):
        """Initialize novelty scorer with configuration."""
        self.config = config.get("novelty", {})
        self.baseline_tokens = self.config.get("baseline_tokens", 10)
        self.multipliers = self.config.get("multipliers", {})
        self.diminishing_config = self.config.get("diminishing_returns", {})

        # Solution history for diminishing returns calculation
        self._solution_history: dict[str, int] = {}

    def score(
        self,
        solution: dict[str, Any],
        biome_config: dict[str, Any],
        player_id: str
    ) -> NoveltyScore:
        """
        Calculate novelty score for a player solution.

        Args:
            solution: The player's solution data
            biome_config: Biome-specific scoring configuration
            player_id: Anonymized player identifier

        Returns:
            NoveltyScore with token calculation breakdown
        """
        multipliers_applied = {}
        novelty_factors = []

        # Start with baseline
        current_score = float(self.baseline_tokens)

        # Apply biome weight
        biome_weight = biome_config.get("novelty_weight", 1.0)
        current_score *= biome_weight
        multipliers_applied["biome_weight"] = biome_weight

        # TODO: Implement full novelty evaluation
        # - Check for efficiency (time to solve)
        # - Check for creativity (unexpected tool use)
        # - Check for collaboration
        # - Check for first solution
        # - Check for edge case handling

        # Apply diminishing returns if enabled
        diminishing_applied = False
        if self.diminishing_config.get("enabled", True):
            solution_type = solution.get("type", "unknown")
            history_key = f"{player_id}:{solution_type}"

            count = self._solution_history.get(history_key, 0)
            threshold = self.diminishing_config.get("threshold", 100)

            if count > threshold:
                decay_rate = self.diminishing_config.get("decay_rate", 0.95)
                floor = self.diminishing_config.get("floor", 0.1)

                decay_factor = max(floor, decay_rate ** (count - threshold))
                current_score *= decay_factor
                multipliers_applied["diminishing_returns"] = decay_factor
                diminishing_applied = True

            self._solution_history[history_key] = count + 1

        final_tokens = max(1, int(current_score))

        return NoveltyScore(
            base_tokens=self.baseline_tokens,
            multipliers_applied=multipliers_applied,
            final_tokens=final_tokens,
            novelty_factors=novelty_factors,
            diminishing_returns_applied=diminishing_applied
        )

    def reset_history(self, player_id: str | None = None) -> None:
        """Reset solution history for diminishing returns."""
        if player_id is None:
            self._solution_history.clear()
        else:
            keys_to_remove = [k for k in self._solution_history if k.startswith(f"{player_id}:")]
            for key in keys_to_remove:
                del self._solution_history[key]
