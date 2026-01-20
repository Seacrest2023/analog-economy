"""
Action Models

Request and response models for the /api/v1/action endpoint.
Designed to capture training data in SFT-compatible format.

Architecture Rules:
- NEVER use datetime. ALWAYS use pendulum.
- NEVER use json. ALWAYS use orjson.
"""

from enum import Enum
from typing import Any
from uuid import UUID, uuid4

import pendulum
from pydantic import AwareDatetime, BaseModel, Field


class ActionType(str, Enum):
    """Types of player actions."""

    PICKUP = "pickup"
    DROP = "drop"
    USE = "use"
    CRAFT = "craft"
    INTERACT = "interact"
    MOVE = "move"
    ATTACK = "attack"
    TRADE = "trade"
    DIALOGUE = "dialogue"
    INSPECT = "inspect"


class Position(BaseModel):
    """3D position in game world."""

    x: float = Field(..., description="X coordinate")
    y: float = Field(..., description="Y coordinate")
    z: float = Field(..., description="Z coordinate")


class GameState(BaseModel):
    """
    Snapshot of player's game state at action time.
    Used for training data context.
    """

    hunger: float = Field(default=100.0, ge=0, le=100, description="Hunger level")
    thirst: float = Field(default=100.0, ge=0, le=100, description="Thirst level")
    health: float = Field(default=100.0, ge=0, le=100, description="Health level")
    stamina: float = Field(default=100.0, ge=0, le=100, description="Stamina level")
    sanity: float = Field(default=100.0, ge=0, le=100, description="Sanity level")
    karma: int = Field(default=50, description="Karma points")
    sila_balance: float = Field(default=0.0, ge=0, description="SILA token balance")

    # Profession and skills
    profession: str | None = Field(default=None, description="Primary profession")
    skill_levels: dict[str, int] = Field(default_factory=dict, description="Skill levels")

    # Inventory summary
    inventory_count: int = Field(default=0, ge=0, description="Items in inventory")
    equipped_tool: str | None = Field(default=None, description="Currently equipped")


class ActionDetails(BaseModel):
    """Details specific to the action being performed."""

    type: ActionType = Field(..., description="Type of action")
    target: str | None = Field(default=None, description="Target object/entity ID")
    target_type: str | None = Field(default=None, description="Type of target")
    position: Position | None = Field(default=None, description="Action position")
    parameters: dict[str, Any] = Field(
        default_factory=dict, description="Action-specific parameters"
    )


class ActionRequest(BaseModel):
    """
    Request from UE5 client reporting a player action.

    This is the core data structure for capturing training data.
    Each action creates a potential training record.
    """

    # Identifiers
    session_id: UUID = Field(..., description="Game session identifier")
    player_id: str = Field(..., min_length=1, description="Player identifier")

    # Timing (AwareDatetime for Pydantic, pendulum.now for UTC timestamp)
    timestamp: AwareDatetime = Field(
        default_factory=lambda: pendulum.now("UTC"),
        description="When action occurred (UTC)",
    )
    game_time: float | None = Field(default=None, description="In-game time (days since start)")

    # The action itself
    action: ActionDetails = Field(..., description="Action being performed")

    # Context for training data
    game_state: GameState = Field(
        default_factory=GameState, description="Player state at action time"
    )

    # Optional reasoning (high-value for training)
    reasoning: str | None = Field(
        default=None,
        max_length=1000,
        description="Player's explanation of why they took this action",
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "session_id": "550e8400-e29b-41d4-a716-446655440000",
                    "player_id": "player_001",
                    "timestamp": "2026-01-20T14:30:00Z",
                    "game_time": 5.5,
                    "action": {
                        "type": "pickup",
                        "target": "rock_01",
                        "target_type": "resource",
                        "position": {"x": 100.5, "y": 50.2, "z": 0.0},
                        "parameters": {},
                    },
                    "game_state": {
                        "hunger": 85.0,
                        "karma": 50,
                        "profession": "gatherer",
                        "inventory_count": 5,
                    },
                }
            ]
        }
    }


class ActionResponse(BaseModel):
    """
    Response to UE5 client after processing an action.

    Contains the SILA reward and any feedback for the player.
    """

    # Status
    status: str = Field(
        default="approved", description="Action status: approved, rejected, pending"
    )

    # Reward
    sila_reward: float = Field(default=0.0, ge=0, description="SILA tokens earned for this action")

    # Feedback
    feedback: str | None = Field(default=None, description="Optional feedback message for player")

    # Training data tracking
    training_data_id: UUID = Field(
        default_factory=uuid4, description="ID of the training record created"
    )

    # Quality metrics (for debugging/tuning)
    quality_score: float | None = Field(
        default=None, ge=0, le=1, description="Quality score of the action (0-1)"
    )
    novelty_score: float | None = Field(
        default=None, ge=0, le=1, description="Novelty score of the action (0-1)"
    )

    # Game state updates (if action modified state)
    state_updates: dict[str, Any] = Field(
        default_factory=dict, description="Any game state changes to apply"
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "status": "approved",
                    "sila_reward": 0.01,
                    "feedback": "Action recorded",
                    "training_data_id": "550e8400-e29b-41d4-a716-446655440001",
                    "quality_score": 0.85,
                    "novelty_score": 0.15,
                    "state_updates": {"inventory_add": "rock_01"},
                }
            ]
        }
    }
