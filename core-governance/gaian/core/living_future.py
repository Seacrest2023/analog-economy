"""
Living Future - Real-world events become game content.

This module handles the integration of current events into the game,
ensuring appropriate delays, ethical review, and categorization.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any

import pendulum
from pendulum import DateTime


class EventCategory(Enum):
    """Categories for real-world events."""

    NATURAL_DISASTER = "natural_disaster"
    WATER_CRISIS = "water_crisis"
    FOOD_INSECURITY = "food_insecurity"
    MIGRATION = "migration"
    CONFLICT = "conflict"
    PANDEMIC = "pandemic"
    TECH_BREAKTHROUGH = "tech_breakthrough"
    SPACE_EXPLORATION = "space_exploration"
    AI_DEVELOPMENT = "ai_development"
    CLIMATE = "climate"
    ECONOMIC = "economic"


class EventStatus(Enum):
    """Processing status for events."""

    PENDING = "pending"
    DELAYED = "delayed"
    IN_REVIEW = "in_review"
    APPROVED = "approved"
    REJECTED = "rejected"
    BLOCKED = "blocked"
    LIVE = "live"


@dataclass
class WorldEvent:
    """Represents a real-world event for potential game integration."""

    event_id: str
    title: str
    description: str
    category: EventCategory
    occurred_at: DateTime
    source: str
    is_sensitive: bool
    status: EventStatus
    target_biomes: list[str]
    ethics_reviewed: bool
    reviewer_notes: str | None


@dataclass
class ChallengeProposal:
    """Community-proposed challenge based on current events."""

    proposal_id: str
    event_id: str | None
    title: str
    description: str
    proposed_by: str  # Anonymized player ID
    proposed_at: DateTime
    votes: int
    status: EventStatus
    reward_if_approved: int


class LivingFutureManager:
    """
    Manages integration of real-world events into game content.

    Responsibilities:
    - Ingest events from news sources
    - Enforce delay periods for sensitive content
    - Route events through ethics review
    - Categorize events to appropriate biomes
    - Handle community proposals
    """

    # Biome mapping for event categories
    CATEGORY_BIOME_MAP = {
        EventCategory.NATURAL_DISASTER: ["ruins"],
        EventCategory.WATER_CRISIS: ["aqua"],
        EventCategory.FOOD_INSECURITY: ["botany"],
        EventCategory.MIGRATION: ["exodus"],
        EventCategory.CONFLICT: ["theater"],
        EventCategory.PANDEMIC: ["vector"],
        EventCategory.TECH_BREAKTHROUGH: ["all"],
        EventCategory.SPACE_EXPLORATION: ["scorch"],
        EventCategory.AI_DEVELOPMENT: ["uprising"],
        EventCategory.CLIMATE: ["aqua", "ruins", "scorch"],
        EventCategory.ECONOMIC: ["all"],
    }

    # Events that are always blocked
    BLOCKED_EVENT_TYPES = {
        "mass_shootings",
        "terrorist_attacks_recent",
        "child_harm_events",
        "ongoing_active_conflicts",
    }

    def __init__(self, config: dict[str, Any]):
        """Initialize living future manager with configuration."""
        self.config = config
        self.lf_config = config.get("living_future", {})

        self.standard_delay_days = self.lf_config.get("news_integration", {}).get(
            "delay_period_days", 14
        )
        self.sensitive_delay_days = self.lf_config.get("news_integration", {}).get(
            "sensitive_event_delay_days", 90
        )

        # Event storage
        self._events: dict[str, WorldEvent] = {}
        self._proposals: dict[str, ChallengeProposal] = {}

    def ingest_event(
        self,
        title: str,
        description: str,
        category: EventCategory,
        occurred_at: DateTime,
        source: str,
        is_sensitive: bool = False,
    ) -> WorldEvent:
        """
        Ingest a new world event for potential game integration.

        Args:
            title: Event title
            description: Event description
            category: Event category
            occurred_at: When the event occurred
            source: News source
            is_sensitive: Whether this is a sensitive event

        Returns:
            Created WorldEvent
        """
        event_id = f"EVT-{pendulum.now('UTC').format('YYYYMMDDHHmmss')}"

        # Determine target biomes
        target_biomes = self.CATEGORY_BIOME_MAP.get(category, ["all"])
        if "all" in target_biomes:
            target_biomes = [
                "abyss",
                "scorch",
                "ruins",
                "aqua",
                "botany",
                "theater",
                "exodus",
                "brink",
                "vector",
                "uprising",
            ]

        event = WorldEvent(
            event_id=event_id,
            title=title,
            description=description,
            category=category,
            occurred_at=occurred_at,
            source=source,
            is_sensitive=is_sensitive,
            status=EventStatus.PENDING,
            target_biomes=target_biomes,
            ethics_reviewed=False,
            reviewer_notes=None,
        )

        # Check if event type is blocked
        if self._is_blocked_event(title, description):
            event.status = EventStatus.BLOCKED
        else:
            event.status = EventStatus.DELAYED

        self._events[event_id] = event
        return event

    def check_event_eligibility(self, event_id: str) -> tuple[bool, str]:
        """
        Check if an event is eligible for game integration.

        Args:
            event_id: Event identifier

        Returns:
            Tuple of (eligible, reason)
        """
        event = self._events.get(event_id)
        if event is None:
            return False, "Event not found"

        if event.status == EventStatus.BLOCKED:
            return False, "Event type is blocked"

        if event.status == EventStatus.REJECTED:
            return False, "Event was rejected by ethics review"

        # Check delay period
        now = pendulum.now("UTC")
        delay_days = self.sensitive_delay_days if event.is_sensitive else self.standard_delay_days

        eligible_at = event.occurred_at.add(days=delay_days)
        if now < eligible_at:
            days_remaining = (eligible_at - now).days
            return False, f"Delay period: {days_remaining} days remaining"

        # Check ethics review
        if not event.ethics_reviewed:
            return False, "Awaiting ethics review"

        return True, "Eligible for integration"

    def submit_for_ethics_review(self, event_id: str) -> bool:
        """
        Submit an event for ethics review.

        Args:
            event_id: Event identifier

        Returns:
            True if submitted successfully
        """
        event = self._events.get(event_id)
        if event is None or event.status == EventStatus.BLOCKED:
            return False

        event.status = EventStatus.IN_REVIEW
        return True

    def complete_ethics_review(self, event_id: str, approved: bool, reviewer_notes: str) -> bool:
        """
        Complete ethics review for an event.

        Args:
            event_id: Event identifier
            approved: Whether event is approved
            reviewer_notes: Notes from reviewer

        Returns:
            True if review completed
        """
        event = self._events.get(event_id)
        if event is None:
            return False

        event.ethics_reviewed = True
        event.reviewer_notes = reviewer_notes
        event.status = EventStatus.APPROVED if approved else EventStatus.REJECTED

        return True

    def activate_event(self, event_id: str) -> bool:
        """
        Activate an approved event, making it live in the game.

        Args:
            event_id: Event identifier

        Returns:
            True if activated
        """
        eligible, reason = self.check_event_eligibility(event_id)
        if not eligible:
            return False

        event = self._events.get(event_id)
        if event and event.status == EventStatus.APPROVED:
            event.status = EventStatus.LIVE
            return True

        return False

    def submit_community_proposal(
        self,
        player_id: str,
        title: str,
        description: str,
        event_id: str | None = None,
    ) -> ChallengeProposal:
        """
        Submit a community proposal for a new challenge.

        Args:
            player_id: Anonymized player ID
            title: Proposal title
            description: Proposal description
            event_id: Optional related world event

        Returns:
            Created ChallengeProposal
        """
        proposal_id = f"PROP-{pendulum.now('UTC').format('YYYYMMDDHHmmss')}"

        proposer_reward = self.lf_config.get("community_proposals", {}).get("proposer_reward", 500)

        proposal = ChallengeProposal(
            proposal_id=proposal_id,
            event_id=event_id,
            title=title,
            description=description,
            proposed_by=player_id,
            proposed_at=pendulum.now("UTC"),
            votes=0,
            status=EventStatus.PENDING,
            reward_if_approved=proposer_reward,
        )

        self._proposals[proposal_id] = proposal
        return proposal

    def vote_on_proposal(self, proposal_id: str, votes: int = 1) -> int:
        """
        Add votes to a community proposal.

        Args:
            proposal_id: Proposal identifier
            votes: Number of votes to add

        Returns:
            New total vote count
        """
        proposal = self._proposals.get(proposal_id)
        if proposal is None:
            return 0

        proposal.votes += votes

        # Check if threshold reached
        voting_threshold = self.lf_config.get("community_proposals", {}).get(
            "voting_threshold", 1000
        )

        if proposal.votes >= voting_threshold:
            proposal.status = EventStatus.IN_REVIEW

        return proposal.votes

    def get_active_events(self) -> list[WorldEvent]:
        """Get all currently live events."""
        return [event for event in self._events.values() if event.status == EventStatus.LIVE]

    def get_events_for_biome(self, biome_id: str) -> list[WorldEvent]:
        """Get all live events relevant to a specific biome."""
        return [
            event
            for event in self._events.values()
            if event.status == EventStatus.LIVE and biome_id in event.target_biomes
        ]

    def _is_blocked_event(self, title: str, description: str) -> bool:
        """Check if event matches blocked patterns."""
        combined = f"{title} {description}".lower()

        for blocked_type in self.BLOCKED_EVENT_TYPES:
            # Simple keyword matching - production would use NLP
            keywords = blocked_type.replace("_", " ")
            if keywords in combined:
                return True

        return False
