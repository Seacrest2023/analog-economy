/**
 * Telemetry Schema - TypeScript version
 *
 * SYNC WITH: shared/schemas/telemetry.py (source of truth)
 *
 * This file should be kept in sync with the Python version.
 * Any changes to the Python schema should be reflected here.
 */

/**
 * Valid biome identifiers.
 */
export enum BiomeId {
  ABYSS = "abyss",
  SCORCH = "scorch",
  RUINS = "ruins",
  AQUA = "aqua",
  BOTANY = "botany",
  THEATER = "theater",
  EXODUS = "exodus",
  BRINK = "brink",
  VECTOR = "vector",
  UPRISING = "uprising",
}

/**
 * Types of player actions.
 */
export enum ActionType {
  MOVEMENT = "movement",
  INTERACTION = "interaction",
  TOOL_USE = "tool_use",
  COMMUNICATION = "communication",
  COMBAT = "combat",
  CONSTRUCTION = "construction",
  PROBLEM_SOLVE = "problem_solve",
}

/**
 * 3D vector for positions and directions.
 */
export interface Vector3 {
  x: number;
  y: number;
  z: number;
}

/**
 * Raw player input data.
 */
export interface PlayerInput {
  timestampMs: number;
  inputType: string;
  value: number;
  device: "keyboard" | "mouse" | "controller";
}

/**
 * A single telemetry event from the game client.
 */
export interface TelemetryEvent {
  eventId: string;
  sessionId: string;
  playerIdHash: string;
  biomeId: BiomeId;
  timestamp: string; // ISO 8601 datetime
  actionType: ActionType;
  position: Vector3;
  velocity: Vector3;
  inputs: PlayerInput[];
  context?: Record<string, unknown>;
}

/**
 * Session start event.
 */
export interface SessionStart {
  sessionId: string;
  playerIdHash: string;
  biomeId: BiomeId;
  startedAt: string; // ISO 8601 datetime
  clientVersion: string;
  hardwareHash: string;
}

/**
 * Session end event.
 */
export interface SessionEnd {
  sessionId: string;
  endedAt: string; // ISO 8601 datetime
  reason: "normal" | "disconnect" | "timeout" | "kicked";
  durationSeconds: number;
  eventsCount: number;
}

/**
 * A player's attempt to solve a problem.
 */
export interface SolutionAttempt {
  attemptId: string;
  sessionId: string;
  playerIdHash: string;
  biomeId: BiomeId;
  problemId: string;
  startedAt: string; // ISO 8601 datetime
  completedAt: string | null; // ISO 8601 datetime or null
  success: boolean;
  solutionData: Record<string, unknown>;
  toolsUsed: string[];
  collaborators: string[];
}
