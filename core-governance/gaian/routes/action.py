"""
Action Endpoint - The Golden Spike

This is the core endpoint that connects UE5 client to the Gaian governance layer.
Every player action flows through here for:
1. Validation
2. Scoring (SILA reward calculation)
3. Training data capture

This endpoint is the "Golden Spike" proving the pipeline works.
"""

import json
from datetime import datetime
from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, HTTPException, status
from loguru import logger

from gaian.config import settings
from gaian.models.action import ActionRequest, ActionResponse, ActionType

router = APIRouter(prefix="/api/v1", tags=["Actions"])


# Base rewards by action type (SILA)
ACTION_REWARDS: dict[ActionType, float] = {
    ActionType.PICKUP: 0.01,
    ActionType.DROP: 0.005,
    ActionType.USE: 0.02,
    ActionType.CRAFT: 0.05,
    ActionType.INTERACT: 0.02,
    ActionType.MOVE: 0.001,
    ActionType.ATTACK: 0.03,
    ActionType.TRADE: 0.04,
    ActionType.DIALOGUE: 0.03,
    ActionType.INSPECT: 0.01,
}


def calculate_sila_reward(request: ActionRequest) -> tuple[float, float, float]:
    """
    Calculate SILA reward for an action.

    Returns:
        tuple: (sila_reward, quality_score, novelty_score)

    Current implementation is simplified for Phase 1.
    Full implementation will use NoveltyScorer and training data pipeline.
    """
    # Base reward from action type
    base_reward = ACTION_REWARDS.get(request.action.type, 0.01)

    # Quality score (simplified - based on player state)
    quality_score = 0.5  # Default middle score

    # Bonus for providing reasoning (high-value training data)
    if request.reasoning:
        quality_score += 0.2
        base_reward *= 1.5

    # Karma multiplier
    karma = request.game_state.karma
    if karma > 100:
        base_reward *= 1.2
    elif karma < 0:
        base_reward *= 0.8

    # Novelty score (simplified - will use vector DB in full implementation)
    novelty_score = 0.1  # Default low novelty

    # Apply SILA base reward from settings
    if settings.sila_mock_enabled:
        final_reward = base_reward * settings.sila_base_reward * 100
    else:
        final_reward = base_reward

    return round(final_reward, 4), min(quality_score, 1.0), novelty_score


def log_training_data(request: ActionRequest, response: ActionResponse) -> None:
    """
    Log action as training data in JSONL format.

    This creates the raw training data that will be processed
    into SFT, DPO, and trajectory formats.
    """
    # Ensure training data directory exists
    training_path = Path(settings.training_data_path)
    training_path.mkdir(parents=True, exist_ok=True)

    # Create training record
    training_record = {
        "id": str(response.training_data_id),
        "timestamp": request.timestamp.isoformat(),
        "session_id": str(request.session_id),
        "player_id": request.player_id,
        "action": {
            "type": request.action.type.value,
            "target": request.action.target,
            "target_type": request.action.target_type,
            "position": request.action.position.model_dump() if request.action.position else None,
            "parameters": request.action.parameters,
        },
        "game_state": request.game_state.model_dump(),
        "reasoning": request.reasoning,
        "outcome": {
            "status": response.status,
            "sila_reward": response.sila_reward,
            "quality_score": response.quality_score,
            "novelty_score": response.novelty_score,
        },
    }

    # Append to JSONL file
    log_file = training_path / f"actions_{datetime.utcnow().strftime('%Y%m%d')}.jsonl"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(training_record) + "\n")

    logger.debug(f"Training data logged: {response.training_data_id}")


@router.post(
    "/action",
    response_model=ActionResponse,
    status_code=status.HTTP_200_OK,
    summary="Process Player Action",
    description="""
    Process a player action from the UE5 client.

    This endpoint:
    1. Validates the action
    2. Calculates SILA reward
    3. Logs training data
    4. Returns reward and feedback

    This is the "Golden Spike" endpoint proving the UE5-to-Python pipeline.
    """,
)
async def process_action(request: ActionRequest) -> ActionResponse:
    """
    Process a player action and return SILA reward.

    The core endpoint connecting UE5 client to Gaian governance.
    """
    logger.info(
        f"Action received: {request.action.type.value} "
        f"from player {request.player_id} "
        f"in session {request.session_id}"
    )

    # Validate action (basic validation for Phase 1)
    if not request.player_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="player_id is required")

    # Calculate reward
    sila_reward, quality_score, novelty_score = calculate_sila_reward(request)

    # Generate response
    response = ActionResponse(
        status="approved",
        sila_reward=sila_reward,
        feedback=f"Action recorded: {request.action.type.value}",
        training_data_id=uuid4(),
        quality_score=quality_score,
        novelty_score=novelty_score,
        state_updates={},
    )

    # Log training data
    try:
        log_training_data(request, response)
    except Exception as e:
        logger.error(f"Failed to log training data: {e}")
        # Don't fail the request if logging fails
        # Training data is important but not critical for gameplay

    logger.info(
        f"Action processed: {request.action.type.value} "
        f"-> {sila_reward} SILA "
        f"(quality: {quality_score}, novelty: {novelty_score})"
    )

    return response


@router.get(
    "/action/types",
    summary="List Action Types",
    description="Returns all valid action types.",
)
async def list_action_types() -> dict[str, list[str]]:
    """
    List all valid action types.

    Useful for UE5 client to validate actions before sending.
    """
    return {"action_types": [action_type.value for action_type in ActionType]}


@router.get(
    "/action/rewards",
    summary="List Base Rewards",
    description="Returns base SILA rewards for each action type.",
)
async def list_action_rewards() -> dict[str, dict[str, float]]:
    """
    List base SILA rewards for each action type.

    Useful for UE5 client UI to show potential rewards.
    Note: Actual rewards vary based on quality, novelty, and karma.
    """
    return {
        "base_rewards": {
            action_type.value: reward for action_type, reward in ACTION_REWARDS.items()
        },
        "note": "Actual rewards vary based on quality, novelty, and karma multipliers",
    }
