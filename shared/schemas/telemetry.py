"""
Telemetry Schema - Shared data structures for game telemetry.

This is the SOURCE OF TRUTH for telemetry data structures.
TypeScript and C++ versions should be kept in sync with this file.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any

import pendulum
from pendulum import DateTime


class BiomeId(str, Enum):
    """Valid biome identifiers."""
    ABYSS = "abyss"
    SCORCH = "scorch"
    RUINS = "ruins"
    AQUA = "aqua"
    BOTANY = "botany"
    THEATER = "theater"
    EXODUS = "exodus"
    BRINK = "brink"
    VECTOR = "vector"
    UPRISING = "uprising"


class ActionType(str, Enum):
    """Types of player actions."""
    MOVEMENT = "movement"
    INTERACTION = "interaction"
    TOOL_USE = "tool_use"
    COMMUNICATION = "communication"
    COMBAT = "combat"
    CONSTRUCTION = "construction"
    PROBLEM_SOLVE = "problem_solve"


@dataclass
class Vector3:
    """3D vector for positions and directions."""
    x: float
    y: float
    z: float


@dataclass
class PlayerInput:
    """Raw player input data."""
    timestamp_ms: int
    input_type: str
    value: float
    device: str  # "keyboard", "mouse", "controller"


@dataclass
class TelemetryEvent:
    """A single telemetry event from the game client."""
    event_id: str
    session_id: str
    player_id_hash: str  # Anonymized player identifier
    biome_id: BiomeId
    timestamp: DateTime
    action_type: ActionType
    position: Vector3
    velocity: Vector3
    inputs: list[PlayerInput]
    context: dict[str, Any] = field(default_factory=dict)


@dataclass
class SessionStart:
    """Session start event."""
    session_id: str
    player_id_hash: str
    biome_id: BiomeId
    started_at: DateTime
    client_version: str
    hardware_hash: str  # Anonymized hardware fingerprint


@dataclass
class SessionEnd:
    """Session end event."""
    session_id: str
    ended_at: DateTime
    reason: str  # "normal", "disconnect", "timeout", "kicked"
    duration_seconds: int
    events_count: int


@dataclass
class SolutionAttempt:
    """A player's attempt to solve a problem."""
    attempt_id: str
    session_id: str
    player_id_hash: str
    biome_id: BiomeId
    problem_id: str
    started_at: DateTime
    completed_at: DateTime | None
    success: bool
    solution_data: dict[str, Any]
    tools_used: list[str]
    collaborators: list[str]  # Other player hashes if collaborative
