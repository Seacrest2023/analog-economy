"""
Era Manager - Handles historical progression through civilization eras.

This module manages player progression from Ancient Sumer through to the
AI Era and Living Future, ensuring era-appropriate experiences and ethics.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any


class EraId(Enum):
    """Enumeration of playable eras."""

    ANCIENT = "ancient"
    CLASSICAL = "classical"
    MEDIEVAL = "medieval"
    RENAISSANCE = "renaissance"
    INDUSTRIAL = "industrial"
    MODERN = "modern"
    AI_ERA = "ai_era"
    LIVING_FUTURE = "living_future"


class ProgressionMode(Enum):
    """How players can progress through eras."""

    CHRONOLOGICAL = "chronological"
    ERA_SELECT = "era_select"
    TIME_TRAVELER = "time_traveler"
    MODERN_START = "modern_start"


@dataclass
class EraState:
    """Current era state for a player."""

    current_era: EraId
    progression_mode: ProgressionMode
    milestones_completed: list[str]
    era_achievements: dict[str, int]
    can_transition: bool
    next_era: EraId | None


@dataclass
class EraTransitionResult:
    """Result of attempting era transition."""

    success: bool
    from_era: EraId
    to_era: EraId | None
    items_carried: list[str]
    items_lost: list[str]
    message: str


class EraManager:
    """
    Manages player progression through historical eras.

    Responsibilities:
    - Track current era for each player
    - Validate era transitions
    - Handle item/skill persistence across eras
    - Apply era-specific ethics rules
    """

    # Era sequence for chronological progression
    ERA_SEQUENCE = [
        EraId.ANCIENT,
        EraId.CLASSICAL,
        EraId.MEDIEVAL,
        EraId.RENAISSANCE,
        EraId.INDUSTRIAL,
        EraId.MODERN,
        EraId.AI_ERA,
        EraId.LIVING_FUTURE,
    ]

    # Items that persist across all eras
    TIMELESS_ITEMS = {"gold", "gems", "jewelry", "precious_stones", "silver"}

    def __init__(self, config: dict[str, Any]):
        """Initialize era manager with configuration."""
        self.config = config
        self.era_config = config.get("historical_eras", {})
        self.progression_config = config.get("era_progression", {})

        # Player era states
        self._player_states: dict[str, EraState] = {}

    def get_era_state(self, player_id: str) -> EraState | None:
        """Get current era state for a player."""
        return self._player_states.get(player_id)

    def initialize_player(
        self,
        player_id: str,
        mode: ProgressionMode = ProgressionMode.MODERN_START,
        starting_era: EraId | None = None,
    ) -> EraState:
        """
        Initialize a new player's era state.

        Args:
            player_id: Anonymized player identifier
            mode: Progression mode (defaults to modern start)
            starting_era: Override starting era (optional)

        Returns:
            Initial EraState for the player
        """
        if starting_era is None:
            if mode == ProgressionMode.CHRONOLOGICAL:
                starting_era = EraId.ANCIENT
            elif mode == ProgressionMode.TIME_TRAVELER:
                # Random era assignment would happen here
                starting_era = EraId.MEDIEVAL  # Placeholder
            else:
                starting_era = EraId.AI_ERA

        state = EraState(
            current_era=starting_era,
            progression_mode=mode,
            milestones_completed=[],
            era_achievements={era.value: 0 for era in EraId},
            can_transition=False,
            next_era=self._get_next_era(starting_era),
        )

        self._player_states[player_id] = state
        return state

    def record_milestone(self, player_id: str, milestone_id: str) -> EraState:
        """
        Record a milestone completion and check transition eligibility.

        Args:
            player_id: Anonymized player identifier
            milestone_id: The milestone that was completed

        Returns:
            Updated EraState
        """
        state = self._player_states.get(player_id)
        if state is None:
            state = self.initialize_player(player_id)

        if milestone_id not in state.milestones_completed:
            state.milestones_completed.append(milestone_id)
            state.era_achievements[state.current_era.value] = (
                state.era_achievements.get(state.current_era.value, 0) + 1
            )

        # Check if player can now transition
        min_achievements = self.progression_config.get("transition_triggers", {}).get(
            "minimum_achievements_per_era", 5
        )

        current_achievements = state.era_achievements.get(state.current_era.value, 0)
        state.can_transition = current_achievements >= min_achievements

        return state

    def attempt_transition(
        self, player_id: str, player_inventory: list[str]
    ) -> EraTransitionResult:
        """
        Attempt to transition player to the next era.

        Args:
            player_id: Anonymized player identifier
            player_inventory: List of item IDs the player currently has

        Returns:
            EraTransitionResult with outcome details
        """
        state = self._player_states.get(player_id)

        if state is None:
            return EraTransitionResult(
                success=False,
                from_era=EraId.ANCIENT,
                to_era=None,
                items_carried=[],
                items_lost=[],
                message="Player not initialized",
            )

        if not state.can_transition:
            return EraTransitionResult(
                success=False,
                from_era=state.current_era,
                to_era=None,
                items_carried=[],
                items_lost=[],
                message="Insufficient milestones to transition",
            )

        if state.next_era is None:
            return EraTransitionResult(
                success=False,
                from_era=state.current_era,
                to_era=None,
                items_carried=[],
                items_lost=[],
                message="Already at final era (Living Future)",
            )

        # Determine what items carry forward
        items_carried = []
        items_lost = []

        for item in player_inventory:
            item_type = self._get_item_type(item)
            if item_type in self.TIMELESS_ITEMS:
                items_carried.append(item)
            else:
                items_lost.append(item)

        # Perform transition
        from_era = state.current_era
        to_era = state.next_era

        state.current_era = to_era
        state.next_era = self._get_next_era(to_era)
        state.milestones_completed = []  # Reset for new era
        state.can_transition = False

        return EraTransitionResult(
            success=True,
            from_era=from_era,
            to_era=to_era,
            items_carried=items_carried,
            items_lost=items_lost,
            message=f"Transitioned from {from_era.value} to {to_era.value}",
        )

    def get_era_ethics(self, era: EraId) -> dict[str, Any]:
        """
        Get ethics configuration for a specific era.

        Args:
            era: The era to get ethics for

        Returns:
            Ethics configuration dictionary
        """
        era_data = self.era_config.get(era.value, {})
        return {
            "ethics_level": era_data.get("ethics_level", "normal"),
            "special_rules": era_data.get("special_rules", []),
            "additional_restrictions": era_data.get("additional_restrictions", {}),
        }

    def get_available_challenges(self, era: EraId) -> list[str]:
        """
        Get available challenges for an era.

        Args:
            era: The era to get challenges for

        Returns:
            List of challenge identifiers
        """
        era_data = self.era_config.get(era.value, {})
        return era_data.get("challenges", [])

    def get_novelty_weight(self, era: EraId) -> float:
        """
        Get novelty token weight for an era.

        Args:
            era: The era to get weight for

        Returns:
            Novelty weight multiplier
        """
        era_data = self.era_config.get(era.value, {})
        return era_data.get("novelty_weight", 1.0)

    def _get_next_era(self, current: EraId) -> EraId | None:
        """Get the next era in sequence."""
        try:
            current_index = self.ERA_SEQUENCE.index(current)
            if current_index < len(self.ERA_SEQUENCE) - 1:
                return self.ERA_SEQUENCE[current_index + 1]
        except ValueError:
            pass
        return None

    def _get_item_type(self, item_id: str) -> str:
        """Extract item type from item ID."""
        # Items are expected to be formatted as "type_specific_id"
        # e.g., "gold_coin_001" -> "gold"
        parts = item_id.split("_")
        return parts[0] if parts else item_id
