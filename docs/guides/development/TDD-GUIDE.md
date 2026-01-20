# TDD Guide - The Analog Economy

> **Version:** 1.0
> **Last Updated:** 2026-01-20
> **Status:** Approved

> **The TDD Principle:** Write the test first. Watch it fail. Write code to make it pass. Refactor. The test is the specification.

---

## Overview

This document defines the Test-Driven Development (TDD) philosophy and patterns for The Analog Economy project. Our codebase spans two primary components:

| Component | Language | Test Framework | Location |
|-----------|----------|----------------|----------|
| **The Brain** | Python 3.11+ | pytest | `core-governance/` |
| **The Body** | C++ (UE5) | Unreal Automation Tool | `client-simulation/` |

**100% code coverage is mandatory.** This is an AI-coded project where tests serve as the specification. No code ships without tests.

---

## The Testing Pyramid

```
                        +---------------------------+
                        |     E2E Tests             |  <- Full workflow (Golden Spike)
                        |   (Slow, High Fidelity)   |
                        +-------------+-------------+
                                      |
                    +-----------------+-----------------+
                    |      Integration Tests            |  <- FastAPI TestClient / UE5 PIE
                    |    (Medium Speed, Real I/O)       |
                    +----------------+------------------+
                                     |
           +-------------------------+-------------------------+
           |                    Unit Tests                     |  <- Pure Core (No I/O)
           |          (Fast, No Database, No Network)          |
           +-------------------------+-------------------------+
                                     |
+--------------------------------------------------------------------+
|                        Governance Layer                             |
|   Iron Dome (Type Safety) + Rising Tide (Mock Tax) + Mock Conformance |
+--------------------------------------------------------------------+
```

### Layer Definitions

| Layer | What It Tests | I/O Allowed? | Speed | Python Example |
|-------|---------------|--------------|-------|----------------|
| **Unit** | Pure logic, single function | NO | Fast (ms) | `calculate_novelty_score(telemetry)` |
| **Integration** | Components wired together | TestClient only | Medium (s) | `POST /api/v1/telemetry` via TestClient |
| **E2E** | Full user workflow | Real DB, Real Redis | Slow (mins) | Complete player session flow |

---

## Directory Structure

```
core-governance/
+-- tests/
|   +-- unit/                    # Pure Core - NO database, NO FastAPI
|   |   +-- gaian/               # Gaian governance logic
|   |   |   +-- test_novelty_scorer.py
|   |   |   +-- test_ethics_filter.py
|   |   |   +-- test_karma_tracker.py
|   |   +-- services/            # Service layer logic
|   |   +-- schemas/             # Pydantic model validation
|   +-- integration/             # FastAPI TestClient tests
|   |   +-- api/
|   |   |   +-- test_telemetry_endpoints.py
|   |   |   +-- test_payout_endpoints.py
|   |   +-- adapters/            # Real I/O verification (temp dirs)
|   +-- e2e/                     # Full stack tests
|   |   +-- test_player_session_flow.py
|   +-- conftest.py              # Shared fixtures (create_autospec!)
|   +-- mocks/                   # Shared mock factories
|       +-- gaian_mocks.py
|       +-- database_mocks.py

client-simulation/
+-- Source/
    +-- AnalogEconomy/
        +-- Tests/               # UE5 Automation Tests
            +-- TelemetryTests.cpp
            +-- BiomeTests.cpp
```

---

## The Red-Green-Refactor Cycle

```
                    +----------+
                    |   RED    | <- Write failing test
                    +----+-----+
                         |
              Write test first, watch it fail
                         |
                         v
                    +----------+
                    |  GREEN   | <- Write minimum code to pass
                    +----+-----+
                         |
              Only enough code to make test green
                         |
                         v
                    +----------+
                    | REFACTOR | <- Clean up while tests protect
                    +----+-----+
                         |
              Improve design, tests catch regressions
                         |
                         +------------> REPEAT
```

### Example: Adding a New Gaian Rule

**Step 1: RED - Write the failing test first**

```python
# core-governance/tests/unit/gaian/test_novelty_scorer.py
import pytest
from gaian.core.novelty_scorer import NoveltyScorer
from shared.schemas.telemetry import TelemetryEvent

class TestNoveltyScorer:
    def test_scores_creative_resource_combination_higher(self):
        """Novel resource combinations should score higher than routine ones."""
        # ARRANGE
        scorer = NoveltyScorer()
        creative_event = TelemetryEvent(
            action="craft",
            resources=["volcanic_glass", "lunar_dust"],  # Rare combination
            biome="the_scorch"
        )
        routine_event = TelemetryEvent(
            action="craft",
            resources=["wood", "stone"],  # Common combination
            biome="the_scorch"
        )

        # ACT
        creative_score = scorer.calculate(creative_event)
        routine_score = scorer.calculate(routine_event)

        # ASSERT
        assert creative_score > routine_score
        assert creative_score >= 0.7  # High novelty threshold
```

**Step 2: GREEN - Write minimum code to pass**

```python
# core-governance/gaian/core/novelty_scorer.py
from shared.schemas.telemetry import TelemetryEvent

class NoveltyScorer:
    RARE_RESOURCES = {"volcanic_glass", "lunar_dust", "abyssal_crystal"}

    def calculate(self, event: TelemetryEvent) -> float:
        rare_count = sum(1 for r in event.resources if r in self.RARE_RESOURCES)
        if rare_count >= 2:
            return 0.8
        elif rare_count == 1:
            return 0.5
        return 0.2
```

**Step 3: REFACTOR - Improve while tests protect**

```python
# Refactored with proper abstraction
class NoveltyScorer:
    def __init__(self, rarity_db: RarityDatabase):
        self._rarity_db = rarity_db

    def calculate(self, event: TelemetryEvent) -> float:
        rarities = [self._rarity_db.get_rarity(r) for r in event.resources]
        return self._compute_novelty_score(rarities, event.biome)
```

---

## Pure Core Pattern (The Brain)

### Why This Matters

Unit tests are easiest to write when code has **no I/O dependencies**. The Pure Core pattern separates:

- **Pure Core:** Business logic with no I/O imports (easy to test)
- **Adapters:** Thin wrappers for I/O (tested via integration tests)

### What Makes Code "Pure" in Analog Economy?

| Pure Core (Unit Testable) | NOT Pure (Integration Test) |
|---------------------------|------------------------------|
| Pydantic models | SQLAlchemy queries |
| Gaian scoring algorithms | Redis cache operations |
| Ethics filter rules | FastAPI Request/Response |
| Data transformation | External API calls |
| Karma calculations | File system operations |

### Example: Pure vs Impure

**BEFORE (Hard to Test):**

```python
# BAD: I/O mixed with logic
class TelemetryProcessor:
    def process(self, event_id: str) -> ProcessingResult:
        # I/O - hard to test
        event = self.db.query(TelemetryEvent).get(event_id)

        # Business logic buried in I/O
        if event.action in PROHIBITED_ACTIONS:
            return ProcessingResult(rejected=True, reason="prohibited")

        # More I/O
        self.redis.set(f"processed:{event_id}", "true")
        return ProcessingResult(accepted=True)
```

**AFTER (Easy to Test):**

```python
# GOOD: Pure Core separated from I/O

# Pure Core (unit testable)
class TelemetryValidator:
    """Pure logic - no database, no cache, no network."""

    def validate(self, event: TelemetryEvent) -> ValidationResult:
        if event.action in PROHIBITED_ACTIONS:
            return ValidationResult(valid=False, reason="prohibited")
        return ValidationResult(valid=True)


# Adapter (integration testable)
class TelemetryProcessor:
    def __init__(self, validator: TelemetryValidator, db: Database, cache: Cache):
        self._validator = validator
        self._db = db
        self._cache = cache

    def process(self, event_id: str) -> ProcessingResult:
        event = self._db.query(TelemetryEvent).get(event_id)
        result = self._validator.validate(event)  # Pure call
        if result.valid:
            self._cache.set(f"processed:{event_id}", "true")
        return ProcessingResult(accepted=result.valid, reason=result.reason)
```

**Unit Test (No Mocks Needed):**

```python
# tests/unit/test_telemetry_validator.py
class TestTelemetryValidator:
    def test_rejects_prohibited_actions(self):
        validator = TelemetryValidator()
        event = TelemetryEvent(action="exploit_glitch", player_id="123")

        result = validator.validate(event)

        assert not result.valid
        assert result.reason == "prohibited"
```

---

## Integration Tests (FastAPI TestClient)

### Gold Standard Pattern

For FastAPI endpoints, use the TestClient with dependency injection:

```python
# tests/integration/api/test_telemetry_endpoints.py
import pytest
from fastapi.testclient import TestClient
from unittest.mock import create_autospec

from app.main import app
from app.dependencies import get_db, get_gaian_engine
from gaian.core.policy_engine import PolicyEngine


@pytest.fixture
def mock_policy_engine():
    """GOOD: create_autospec enforces interface conformance."""
    engine = create_autospec(PolicyEngine, instance=True)
    engine.evaluate.return_value = PolicyResult(approved=True)
    return engine


@pytest.fixture
def client(mock_policy_engine):
    """TestClient with dependency overrides."""
    app.dependency_overrides[get_gaian_engine] = lambda: mock_policy_engine

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()


class TestTelemetryEndpoints:
    def test_submit_telemetry_returns_201(self, client):
        # ARRANGE
        payload = {
            "player_id": "player_123",
            "action": "harvest",
            "biome": "the_botany",
            "timestamp": "2026-01-20T12:00:00Z"
        }

        # ACT
        response = client.post("/api/v1/telemetry", json=payload)

        # ASSERT
        assert response.status_code == 201
        assert "telemetry_id" in response.json()

    def test_submit_telemetry_validates_biome(self, client):
        """Invalid biome should return 422."""
        payload = {
            "player_id": "player_123",
            "action": "harvest",
            "biome": "invalid_biome",  # Not a valid biome
            "timestamp": "2026-01-20T12:00:00Z"
        }

        response = client.post("/api/v1/telemetry", json=payload)

        assert response.status_code == 422
```

### Mock Conformance: create_autospec vs Mock()

**CRITICAL:** Always use `create_autospec()` instead of bare `Mock()`. This is enforced by our pre-commit hooks.

```python
# BAD - Mock() accepts any method (mock drift)
mock = Mock()
mock.nonexistent_method()  # Silently passes - BUG WAITING TO HAPPEN

# GOOD - create_autospec enforces real interface
from unittest.mock import create_autospec

mock = create_autospec(PolicyEngine, instance=True)
mock.nonexistent_method()  # Raises AttributeError immediately
```

### Shared Fixtures (conftest.py)

```python
# tests/conftest.py
import pytest
from unittest.mock import create_autospec
from sqlalchemy.orm import Session

from gaian.core.policy_engine import PolicyEngine
from gaian.core.novelty_scorer import NoveltyScorer
from app.services.telemetry_service import TelemetryService


@pytest.fixture
def mock_db_session():
    """Database session mock with interface enforcement."""
    return create_autospec(Session, instance=True)


@pytest.fixture
def mock_policy_engine():
    """Policy engine mock - use create_autospec to prevent drift."""
    engine = create_autospec(PolicyEngine, instance=True)
    engine.evaluate.return_value = PolicyResult(approved=True)
    return engine


@pytest.fixture
def mock_novelty_scorer():
    """Novelty scorer mock."""
    scorer = create_autospec(NoveltyScorer, instance=True)
    scorer.calculate.return_value = 0.5
    return scorer


@pytest.fixture
def telemetry_service(mock_db_session, mock_policy_engine, mock_novelty_scorer):
    """Fully wired service with mocked dependencies."""
    return TelemetryService(
        db=mock_db_session,
        policy_engine=mock_policy_engine,
        novelty_scorer=mock_novelty_scorer
    )
```

---

## UE5 Testing (The Body)

### Automation Test Framework

Unreal Engine 5 uses the Automation Test Framework for C++ testing.

```cpp
// Source/AnalogEconomy/Tests/TelemetryTests.cpp
#include "Misc/AutomationTest.h"
#include "AnalogEconomy/Telemetry/TelemetryCollector.h"

IMPLEMENT_SIMPLE_AUTOMATION_TEST(
    FTelemetryCollectorTest,
    "AnalogEconomy.Telemetry.Collector.BasicCapture",
    EAutomationTestFlags::ApplicationContextMask | EAutomationTestFlags::ProductFilter
)

bool FTelemetryCollectorTest::RunTest(const FString& Parameters)
{
    // ARRANGE
    UTelemetryCollector* Collector = NewObject<UTelemetryCollector>();

    // ACT
    Collector->RecordAction(TEXT("harvest"), TEXT("the_botany"));

    // ASSERT
    TestEqual(TEXT("Event count"), Collector->GetEventCount(), 1);
    TestEqual(TEXT("Last action"), Collector->GetLastAction(), TEXT("harvest"));

    return true;
}
```

### Latent Automation Tests (Async Operations)

```cpp
// For tests that need multiple frames or async operations
IMPLEMENT_COMPLEX_AUTOMATION_TEST(
    FBiomeTransitionTest,
    "AnalogEconomy.Biomes.Transition",
    EAutomationTestFlags::ApplicationContextMask | EAutomationTestFlags::ProductFilter
)

void FBiomeTransitionTest::GetTests(TArray<FString>& OutBeautifiedNames, TArray<FString>& OutTestCommands) const
{
    OutBeautifiedNames.Add(TEXT("TheAbyss to TheScorch"));
    OutTestCommands.Add(TEXT("abyss_to_scorch"));
}

bool FBiomeTransitionTest::RunTest(const FString& Parameters)
{
    // Setup latent commands for async testing
    ADD_LATENT_AUTOMATION_COMMAND(FLoadBiomeCommand(TEXT("TheAbyss")));
    ADD_LATENT_AUTOMATION_COMMAND(FWaitForBiomeLoadedCommand());
    ADD_LATENT_AUTOMATION_COMMAND(FTransitionToBiomeCommand(TEXT("TheScorch")));
    ADD_LATENT_AUTOMATION_COMMAND(FVerifyBiomeActiveCommand(TEXT("TheScorch")));

    return true;
}
```

### PIE (Play In Editor) Testing

For full gameplay testing:

```cpp
// Tests that require a running game world
IMPLEMENT_SIMPLE_AUTOMATION_TEST(
    FPlayerTelemetryIntegrationTest,
    "AnalogEconomy.Integration.PlayerTelemetry",
    EAutomationTestFlags::EditorContext | EAutomationTestFlags::ProductFilter
)

bool FPlayerTelemetryIntegrationTest::RunTest(const FString& Parameters)
{
    // This runs in PIE context
    ADD_LATENT_AUTOMATION_COMMAND(FStartPIECommand(true));
    ADD_LATENT_AUTOMATION_COMMAND(FWaitLatentCommand(2.0f));  // Wait for world setup
    ADD_LATENT_AUTOMATION_COMMAND(FSimulatePlayerActionCommand(TEXT("harvest")));
    ADD_LATENT_AUTOMATION_COMMAND(FVerifyTelemetrySentCommand());
    ADD_LATENT_AUTOMATION_COMMAND(FEndPIECommand());

    return true;
}
```

---

## The Governance Layer

The Governance Layer validates that tests themselves are reliable. This prevents the most common AI-coder failure mode: tests that **look correct** but test against **stale or incorrect mocks**.

### Components

| Component | What It Validates | Pre-commit Hook |
|-----------|-------------------|-----------------|
| **Iron Dome** | Type safety ratchet (`Any` can only decrease) | `iron-dome-py` |
| **Rising Tide** | Mock Tax (tests cannot be >2x source size) | `mock-tax-py` |
| **Mock Conformance** | `create_autospec()` required | `mock-conformance-py` |
| **SRP Guardrails** | File size limits (300/600 LOC) | `srp-check-py` |

### Mock Tax (Rising Tide)

**Rule:** Test files using mocks cannot exceed 2x the size of their source file.

```
Source file: 100 lines (gaian/core/novelty_scorer.py)
Test file:   Maximum 200 lines (tests/unit/gaian/test_novelty_scorer.py)
```

**Why?** Oversized test files indicate:
- Over-mocking (testing implementation, not behavior)
- Missing Pure Core extraction
- Tests that will be expensive to maintain

**Escape Hatch:** If you exceed 2x, extract pure logic into a separate file.

### Type Safety (Iron Dome)

Type holes (`Any`, `type: ignore`, `cast()`) can only decrease, never increase.

```python
# BAD - Adding type holes
from typing import Any

def process_data(data: Any) -> Any:  # 2 type holes added
    return data

# GOOD - Proper typing
from shared.schemas.telemetry import TelemetryEvent, ProcessingResult

def process_data(data: TelemetryEvent) -> ProcessingResult:
    return ProcessingResult(...)
```

---

## Testing Anti-Patterns

### DO NOT

| Anti-Pattern | Why It's Bad | Do This Instead |
|--------------|--------------|-----------------|
| `Mock()` without spec | Accepts any method call | `create_autospec(RealClass)` |
| Testing private methods | Couples test to implementation | Test public interface |
| Mocking the thing under test | Test proves nothing | Mock dependencies only |
| `time.sleep()` in tests | Slow, flaky | Use proper async/await |
| Hardcoded test data in code | Hard to maintain | Use fixtures or factories |
| Testing framework code | FastAPI already tested | Test your logic |

### DO

| Pattern | Why It's Good | Example |
|---------|---------------|---------|
| AAA structure | Clear, readable | Arrange, Act, Assert |
| One assertion focus | Easy to debug | `test_rejects_invalid_biome` |
| Descriptive names | Self-documenting | `test_scores_rare_combination_higher` |
| Fixtures for setup | DRY, maintainable | `@pytest.fixture` |
| Parameterized tests | Cover edge cases | `@pytest.mark.parametrize` |

---

## Running Tests

### Python (The Brain)

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=gaian --cov-report=html

# Run specific test file
pytest tests/unit/gaian/test_novelty_scorer.py

# Run tests matching pattern
pytest -k "novelty"

# Run with verbose output
pytest -v

# Run only unit tests (fast)
pytest tests/unit/

# Run integration tests
pytest tests/integration/
```

### UE5 (The Body)

```bash
# Run from command line
UnrealEditor-Cmd.exe "ProjectPath" -ExecCmds="Automation RunTests AnalogEconomy"

# Run specific test group
UnrealEditor-Cmd.exe "ProjectPath" -ExecCmds="Automation RunTests AnalogEconomy.Telemetry"
```

Or via the Session Frontend in UE5 Editor:
1. Window > Developer Tools > Session Frontend
2. Select Automation tab
3. Check tests to run
4. Click "Start Tests"

---

## Process Isolation

**ALL tests run in isolated processes. This is non-negotiable.**

| Framework | Isolation Setting |
|-----------|-------------------|
| pytest | Default (each test file in subprocess) |
| UE5 | Each test class isolated |

**Why?** Without isolation:
- Singleton state leakage
- Mock registry collisions
- Heisenbugs requiring human debugging

---

## E2E Tests (Golden Spike)

E2E tests validate the full stack works together. Run these sparingly (slow, expensive).

```python
# tests/e2e/test_player_session_flow.py
import pytest
from testcontainers.postgres import PostgresContainer
from testcontainers.redis import RedisContainer

@pytest.fixture(scope="module")
def containers():
    """Real database and cache for E2E tests."""
    with PostgresContainer("postgres:15") as postgres:
        with RedisContainer() as redis:
            yield {"postgres": postgres, "redis": redis}


class TestPlayerSessionFlow:
    def test_complete_session_generates_payout(self, containers, e2e_client):
        """
        Golden Spike: Full player session from login to payout.

        This test validates:
        1. Player can authenticate
        2. Telemetry events are recorded
        3. Gaian evaluates novelty
        4. Payout is calculated correctly
        """
        # Login
        login_response = e2e_client.post("/auth/login", json={
            "wallet_address": "0x1234..."
        })
        assert login_response.status_code == 200
        token = login_response.json()["token"]

        # Submit telemetry
        headers = {"Authorization": f"Bearer {token}"}
        telemetry_response = e2e_client.post(
            "/api/v1/telemetry",
            json={
                "action": "craft",
                "resources": ["volcanic_glass", "lunar_dust"],
                "biome": "the_scorch"
            },
            headers=headers
        )
        assert telemetry_response.status_code == 201

        # Check payout
        payout_response = e2e_client.get(
            "/api/v1/payouts/pending",
            headers=headers
        )
        assert payout_response.status_code == 200
        assert payout_response.json()["amount"] > 0
```

---

## TDD Setup Checklist

When starting a new feature:

- [ ] Write the test file first (RED)
- [ ] Run test to confirm it fails
- [ ] Write minimum code to pass (GREEN)
- [ ] Run test to confirm it passes
- [ ] Refactor if needed (tests protect you)
- [ ] Verify coverage: `pytest --cov`
- [ ] Run pre-commit: `pre-commit run --all-files`

---

## Summary

| Concept | Description |
|---------|-------------|
| **TDD** | Write test first, then code |
| **Red-Green-Refactor** | Fail -> Pass -> Clean |
| **Pure Core** | Business logic with no I/O (unit testable) |
| **TestClient** | FastAPI integration testing |
| **create_autospec** | Mock with interface enforcement |
| **Iron Dome** | Type safety ratchet |
| **Rising Tide** | Mock Tax (2x rule) |
| **Process Isolation** | No shared state between tests |
| **Golden Spike** | E2E tests for full flow validation |

---

## Related Documentation

- [CI/CD Guide](./CICD.md) - Pipeline setup for test execution
- [Pre-commit Setup](../project%20setup/PRECOMMIT-SETUP.md) - Governance hooks
- [Directory Structure](../architecture/directory-structure.md) - Project organization
