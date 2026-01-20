# Phase 1: The Golden Spike

> *"The Golden Spike connected two railroads and unified a continent. Our Golden Spike connects Unreal Engine to Python and proves the training data pipeline is possible."*

**Phase Start Date:** 2026-01-20
**Status:** Planning Complete → Implementation Ready

---

## Strategic Context

### Why We're Here

After 50 design documents, we've reached **Concept Complete**. The specifications for The Analog Economy are comprehensive:
- World building and lore
- All professions and supply chains
- Karma, sanity, and ascension systems
- Training data architecture with anti-gaming validation
- Player engagement loops

**The risk is no longer insufficient design. The risk is unvalidated assumptions.**

We don't know if:
- UE5 can communicate with our Python backend at the required latency (<100ms)
- The training data capture feels seamless or intrusive
- The SILA reward feedback creates the dopamine loop we designed
- The core interaction of "do action → get rewarded" is satisfying

### The Vertical Slice Philosophy

We are NOT building the whole game. We are building ONE perfect interaction to prove the architecture works:

```
Player picks up rock → Game sends action to Python → Python scores → Player sees SILA reward
```

If this works, everything else is scale. If this fails, we learn what to fix before investing months of development.

---

## Phase 1 Goals

### Primary Objective
**Validate the end-to-end pipeline from UE5 client to Python governance layer.**

### Success Criteria
1. UE5 client successfully sends HTTP/WebSocket request to Python server
2. Python server receives, processes, and responds within 100ms
3. UE5 displays the response to the player (SILA reward on screen)
4. Action is logged in format compatible with training-data-architecture.md

### Non-Goals (Explicitly Out of Scope)
- Beautiful graphics (greybox is fine)
- Multiple actions (one action is enough)
- Persistence (in-memory is fine)
- Authentication (skip for now)
- Real training data processing (mock the scoring)

---

## Implementation Plan

### Spike 0: "Hello Gaian" (Foundation)

**Goal:** Prove UE5 and Python can talk to each other.

#### Python Side
```
Location: core-governance/gaian/
Files to create:
  - server.py (FastAPI application)
  - routes/health.py (health check endpoint)
  - routes/action.py (action validation endpoint)
```

**Endpoints:**
| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/health` | GET | Verify server is running |
| `/api/v1/action` | POST | Receive action, return score |

**Request Schema (from UE5):**
```json
{
  "session_id": "uuid",
  "player_id": "string",
  "timestamp": "ISO8601",
  "action": {
    "type": "pickup",
    "target": "rock_01",
    "position": {"x": 0, "y": 0, "z": 0}
  },
  "game_state": {
    "hunger": 100,
    "karma": 50
  }
}
```

**Response Schema (to UE5):**
```json
{
  "status": "approved",
  "sila_reward": 0.01,
  "feedback": "Action recorded",
  "training_data_id": "uuid"
}
```

#### UE5 Side
```
Location: client-simulation/Source/AnalogEconomy/
Files to create:
  - GaianClient.h/.cpp (HTTP client wrapper)
  - GaianSubsystem.h/.cpp (Game instance subsystem)
```

**Components:**
| Component | Purpose |
|-----------|---------|
| `AGaianClient` | Handles HTTP requests to Python server |
| `UGaianSubsystem` | Manages connection lifecycle |

#### Success Metric
- [ ] UE5 prints "Hello from Gaian!" in the log after receiving response
- [ ] Round-trip time logged and < 100ms on localhost

---

### Spike 1: "The First SILA" (Core Loop)

**Goal:** Complete the reward loop that makes the game feel alive.

#### Python Side Additions
```
Files to create/modify:
  - services/action_scorer.py (scoring logic)
  - services/training_logger.py (log to file/DB)
  - models/action.py (Pydantic models)
```

**Scoring Logic (Simplified):**
```python
def score_action(action: Action) -> float:
    base_reward = ACTION_REWARDS.get(action.type, 0.01)
    # Future: novelty scoring, karma multipliers
    return base_reward
```

#### UE5 Side Additions
```
Files to create:
  - Actors/PickupableItem.h/.cpp (base class for items)
  - Actors/Rock.h/.cpp (first pickupable)
  - UI/SilaRewardWidget.h/.cpp (floating +SILA text)
  - Components/PlayerInventoryComponent.h/.cpp
```

**Interaction Flow:**
1. Player walks to rock
2. Player presses E (interact key)
3. `APickupableItem::OnInteract()` called
4. Item sends action to `UGaianSubsystem`
5. Subsystem makes HTTP call to Python
6. Response received with SILA amount
7. `USilaRewardWidget` displays "+0.01 SILA" floating text
8. Item is added to inventory (or destroyed)

#### Success Metric
- [ ] Player can pick up rock
- [ ] Python receives action and responds
- [ ] "+0.01 SILA" appears on screen
- [ ] Action logged in JSONL format matching SFT schema

---

## Technical Architecture

### Communication Protocol

**Option A: HTTP (Simpler, Higher Latency)**
```
UE5 → HTTP POST → FastAPI → Response → UE5
Latency: 10-50ms localhost, 50-200ms remote
Pro: Simple, stateless
Con: Connection overhead per request
```

**Option B: WebSocket (Complex, Lower Latency)**
```
UE5 ←→ WebSocket ←→ FastAPI
Latency: 1-10ms after connection
Pro: Persistent connection, bidirectional
Con: Connection management complexity
```

**Decision:** Start with HTTP for Spike 0/1. Migrate to WebSocket if latency is unacceptable.

### Data Flow

```
┌─────────────────┐     HTTP POST      ┌─────────────────┐
│                 │ ─────────────────→ │                 │
│   UE5 Client    │                    │  Python/Gaian   │
│                 │ ←───────────────── │                 │
└─────────────────┘     JSON Response  └─────────────────┘
        │                                      │
        │                                      │
        ▼                                      ▼
┌─────────────────┐                    ┌─────────────────┐
│  Player sees    │                    │  training.jsonl │
│  +0.01 SILA     │                    │  (logged data)  │
└─────────────────┘                    └─────────────────┘
```

---

## File Structure After Phase 1

```
analog-economy/
├── core-governance/
│   └── gaian/
│       ├── server.py              # FastAPI entry point
│       ├── config.py              # Server configuration
│       ├── requirements.txt       # Python dependencies
│       ├── routes/
│       │   ├── __init__.py
│       │   ├── health.py          # Health check
│       │   └── action.py          # Action validation
│       ├── services/
│       │   ├── __init__.py
│       │   ├── action_scorer.py   # Scoring logic
│       │   └── training_logger.py # Data capture
│       └── models/
│           ├── __init__.py
│           └── action.py          # Pydantic schemas
│
├── client-simulation/
│   └── Source/
│       └── AnalogEconomy/
│           ├── Network/
│           │   ├── GaianClient.h
│           │   ├── GaianClient.cpp
│           │   ├── GaianSubsystem.h
│           │   └── GaianSubsystem.cpp
│           ├── Actors/
│           │   ├── PickupableItem.h
│           │   ├── PickupableItem.cpp
│           │   ├── Rock.h
│           │   └── Rock.cpp
│           ├── Components/
│           │   ├── PlayerInventoryComponent.h
│           │   └── PlayerInventoryComponent.cpp
│           └── UI/
│               ├── SilaRewardWidget.h
│               └── SilaRewardWidget.cpp
│
└── development/
    └── phase-1-golden-spike.md    # This document
```

---

## Testing Checklist

### Spike 0 Tests
- [ ] Python server starts without errors
- [ ] `curl http://localhost:8000/health` returns 200
- [ ] `curl -X POST http://localhost:8000/api/v1/action -d '{...}'` returns valid response
- [ ] UE5 compiles without errors
- [ ] UE5 can make HTTP request (check Output Log)
- [ ] Round-trip latency < 100ms

### Spike 1 Tests
- [ ] Rock actor spawns in level
- [ ] Player can approach rock
- [ ] E key triggers interaction
- [ ] HTTP request sent on interaction
- [ ] SILA reward displayed on screen
- [ ] Action logged to training.jsonl
- [ ] Log format matches SFT schema from training-data-architecture.md

---

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| UE5 HTTP module issues | Medium | High | Fall back to libcurl integration |
| Latency > 100ms | Low | Medium | Switch to WebSocket |
| JSON parsing errors | Medium | Low | Strict Pydantic validation |
| CORS issues | High | Low | Configure FastAPI CORS middleware |

---

## Dependencies

### Python
```
fastapi>=0.100.0
uvicorn>=0.23.0
pydantic>=2.0.0
python-dotenv>=1.0.0
```

### UE5
- Unreal Engine 5.3+ (HTTP module included)
- No external plugins required for Spike 0/1

---

## Next Steps After Phase 1

Once the Golden Spike is validated:

1. **Phase 2: The Training Facility**
   - Build the greybox version of the Sumerian Training Facility
   - Add 3-5 more interactable objects
   - Implement basic survival loop (hunger drain)

2. **Phase 3: Data Validation**
   - Review captured training data quality
   - Implement novelty scoring (currently mocked)
   - Add peer prediction hooks

3. **Phase 4: Visual Pass**
   - Replace greybox with actual Mesopotamian assets
   - Implement art direction from art-direction.md

---

## Decision Log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-01-20 | Start with HTTP, not WebSocket | Simpler implementation, latency acceptable for MVP |
| 2026-01-20 | Greybox graphics | Validate mechanics before investing in art |
| 2026-01-20 | Skip authentication | Security can wait until multiplayer |

---

## Session Notes

*Use this section to log progress, blockers, and learnings during implementation.*

### 2026-01-20
- Created phase-1-golden-spike.md
- Ready to begin Spike 0 implementation
- Next action: Create Python server scaffold

---

*"A journey of 6,000 years begins with a single pickup action."*
