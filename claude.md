# The Analog Economy: Claude Code Project Instructions

> "Define the story first. The story is the roadmap. Code follows narrative."

---

## Project Philosophy

**The Analog Economy** is a high-fidelity survival simulation that functions as a "Proof-of-Intelligence" mining operation. Players solve complex problems across historical eras, generating training data for autonomous AI systems.

### Core Principle: Story First

We define every aspect of the game through documentation before writing code. The narrative, mechanics, and world-building are our blueprint. This approach ensures:

- **Coherent vision** - Every system fits the larger story
- **Reduced rework** - Fewer pivots when implementation begins
- **Clear scope** - We know what we're building before we build it
- **Quality training data** - Well-designed systems generate better AI training data

---

## The Source of Truth

### `docs/story-index.md`

This file is the **canonical index** of all project documentation. It must be treated as the source of truth for what exists in this project.

**Mandatory Rules:**

1. **When creating a new document:**
   - Add it to `story-index.md` immediately
   - Place it in the appropriate category
   - Include path and brief description

2. **When modifying an existing document:**
   - If the scope/purpose changes significantly, update its description in `story-index.md`
   - If you add major new sections, consider if the description still accurate

3. **When deleting or renaming a document:**
   - Update `story-index.md` to reflect the change
   - Update any cross-references in other documents

4. **Before starting work:**
   - Check `story-index.md` to understand what documentation exists
   - Avoid duplicating content that exists elsewhere
   - Link to existing docs rather than repeating information

---

## Documentation Standards

### File Locations

```
docs/
├── story-index.md          # The master index (SOURCE OF TRUTH)
├── guides/                  # Developer guides, setup instructions
│   ├── concepts/           # High-level concepts and overviews
│   └── architecture/       # Technical architecture docs
└── specs/                  # Game design specifications
    └── [feature].md        # One file per major system/feature
```

### Document Structure

Every specification document should follow this pattern:

```markdown
# [System Name]: [Evocative Subtitle]

> "A thematic quote that captures the essence"

## Table of Contents
[Numbered sections with anchor links]

---

## 1. Overview
[What this system is and why it exists]

## 2. Design Philosophy
[The principles guiding design decisions]

## 3-N. [Feature Sections]
[Detailed specifications using YAML blocks for data]

## N. Implementation Notes
[MVP scope, phasing, technical considerations]

---

## Appendix (if needed)
[Quick reference tables, glossaries]

*"Closing thematic quote"*
```

### YAML for Data Structures

Use YAML code blocks for game data, configurations, and structured information:

```yaml
example_system:
  property: "value"
  nested:
    - item_one
    - item_two
```

### Cross-Referencing

Link between documents using relative paths:

```markdown
See [Payments & Economic System](payments.md) for details.
See [Section 5.2](#52-subsection-name) for more information.
```

---

## Era & Setting Context

### Current Focus: Ancient Era (4500 BCE Eridu)

The Ancient Era is our MVP setting. All detailed specifications should prioritize this era:

- **Location:** Eridu, southern Mesopotamia
- **Time:** 4500 BCE (pre-Uruk dominance)
- **Patron Deity:** Enki (God of Water and Wisdom)
- **Key Themes:** Survival, first innovations, temple-city life

### Historical Accuracy

We strive for historical authenticity while allowing for engaging gameplay:

- Research real historical practices before designing systems
- Use period-appropriate materials, techniques, and social structures
- When in doubt, favor realism over convenience
- Document sources and reasoning for historical decisions

---

## Economic System Overview

### Two-Token Model

| Token | Type | Purpose |
|-------|------|---------|
| **SILA** | Off-chain (database) | Daily gameplay, NPC transactions, crafting |
| **ANALOG** | On-chain (ERC-20) | Governance, NFT minting, premium features |

### Key Economic Principles

- **Time is the ultimate cost** - Complex items take real time to produce
- **Scarcity through production limits** - Limited shops, limited craftsmen
- **Learn the Ways** - Players earn SILA by learning to craft (not just buying)
- **No pay-to-win** - Crypto enhances, never bypasses core gameplay

---

## Git Workflow (MANDATORY)

### The Branch-PR-Merge Rule

**NEVER push directly to `master`.** All changes must go through a Pull Request.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    THE ANALOG ECONOMY GIT WORKFLOW                   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   1. CREATE BRANCH                                                  │
│      git checkout -b feature/my-feature                             │
│        ↓                                                            │
│   2. MAKE CHANGES                                                   │
│      Write code, run pre-commit hooks locally                       │
│        ↓                                                            │
│   3. PUSH BRANCH                                                    │
│      git push -u origin feature/my-feature                          │
│        ↓                                                            │
│   4. CREATE PR                                                      │
│      gh pr create --title "feat: My feature" --body "..."           │
│        ↓                                                            │
│   5. CI RUNS                                                        │
│      Governance CI validates the changes                            │
│        ↓                                                            │
│   6. HUMAN MERGES                                                   │
│      The human reviews and merges the PR                            │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Branch Naming Convention

| Type | Pattern | Example |
|------|---------|---------|
| Feature | `feature/short-description` | `feature/crafting-system` |
| Bug fix | `fix/short-description` | `fix/login-timeout` |
| Documentation | `docs/short-description` | `docs/api-reference` |
| Refactor | `refactor/short-description` | `refactor/scoring-engine` |

### Quick Reference

```bash
# Create feature branch
git checkout -b feature/my-feature

# Make changes, then commit
git add -A && git commit -m "feat: Add my feature"

# Push and create PR
git push -u origin feature/my-feature
gh pr create --title "feat: Add my feature" --body "Description here"

# After human merges, clean up
git checkout master && git pull
git branch -d feature/my-feature
```

### Why PRs?

1. **CI Validation** — Governance CI runs on every PR
2. **Human Review** — The human maintains final control
3. **Clean History** — Atomic, reviewable changes
4. **Rollback Safety** — Easy to revert specific PRs

---

## Working with This Codebase

### Before Making Changes

1. Read `story-index.md` to understand the documentation landscape
2. Read relevant specification documents for the area you're working on
3. Check for cross-references that might be affected
4. Understand the "why" before changing the "what"

### When Adding Features

1. **Create branch** — `git checkout -b feature/my-feature`
2. **Document first** — Create or update the specification
3. **Update the index** — Add to `story-index.md`
4. **Implement** — Code follows documentation
5. **Push and PR** — Let CI validate, human merges

### When Reviewing Content

Ask these questions:
- Does this fit the Ancient Era setting?
- Is this historically plausible?
- Does this generate interesting training data?
- Is there a simpler way to achieve the same goal?
- Does this conflict with existing specifications?

---

## Key Documents to Know

| Document | Why It Matters |
|----------|----------------|
| `docs/story-index.md` | Master index of all documentation |
| `docs/guides/concepts/project-overview.md` | The full vision and business model |
| `docs/specs/eridu-setting.md` | The starting city in exhaustive detail |
| `docs/specs/inventory-system.md` | Items, crafting, shops, production |
| `docs/specs/blockchain-economy.md` | Token economics and NFT systems |
| `docs/specs/survival-and-progression.md` | Core gameplay loop |
| `docs/specs/world-lore.md` | Mythology, mystery, and meaning |

---

## Pending Documentation Gaps

These areas need dedicated specifications (in priority order):

1. **Character Creation System** - Backgrounds, starting conditions, identity
2. **Combat & Conflict Mechanics** - Fighting, defense, consequences
3. **Skills & Abilities Framework** - How competencies develop over time
4. **NPC Behavior System** - Individual AI, schedules, relationships
5. **Quest & Mission Framework** - Types, triggers, rewards, tracking
6. **Multiplayer Architecture** - Instancing, player interaction, servers
7. **Housing & Building System** - Construction, ownership, customization

When creating these, follow the documentation standards above and immediately add to `story-index.md`.

---

## Remember

> "In a world where AI handles predictable work, the scarce resource becomes human improvisation, creativity, and edge-case problem-solving."

Every system we design should:
- Create meaningful choices for players
- Generate valuable training data
- Respect historical authenticity
- Fit coherently into the larger story

**The story is the roadmap. Define it completely. Then build it.**

---

## MANDATORY: Test-Driven Development (TDD)

### The Iron Rule

**NEVER write production code without a failing test first.**

This is a 100% AI-coded project. Tests ARE the specification. Without tests, code is speculation.

### The TDD Cycle

```
1. RED    - Write a failing test that defines the expected behavior
2. GREEN  - Write the MINIMUM code to make the test pass
3. REFACTOR - Clean up while tests protect you
4. REPEAT
```

### Before Writing ANY Code

Ask yourself:
1. "What test would prove this feature works?"
2. "What test would catch the bug I'm fixing?"
3. "Have I written that test first?"

If the answer to #3 is "no", STOP and write the test.

---

## The Testing Pyramid

```
                        +---------------------------+
                        |     E2E Tests             |  <- Rare, expensive
                        |   (Golden Spike only)     |
                        +-------------+-------------+
                                      |
                    +-----------------+-----------------+
                    |      Integration Tests            |  <- FastAPI TestClient
                    |    (API endpoints, DB queries)    |
                    +----------------+------------------+
                                     |
           +-------------------------+-------------------------+
           |                    Unit Tests                     |  <- MOST tests here
           |          (Pure Core - No I/O, No Mocks)           |
           +-------------------------+-------------------------+
                                     |
+--------------------------------------------------------------------+
|                        Governance Layer                             |
|          Iron Dome + Rising Tide + Mock Conformance                 |
+--------------------------------------------------------------------+
```

### Test Categories

| Category | Location | What It Tests | I/O? |
|----------|----------|---------------|------|
| **Unit** | `tests/unit/` | Pure logic, Pydantic models | NO |
| **Integration** | `tests/integration/` | API endpoints, services | TestClient only |
| **E2E** | `tests/e2e/` | Full player workflows | Real DB/Redis |

---

## Pure Core Pattern (CRITICAL)

### What is "Pure"?

Pure code has NO:
- Database calls (`db.query()`, `session.execute()`)
- Network requests (`requests.get()`, `httpx.post()`)
- File system operations (`open()`, `pathlib.Path().read_text()`)
- FastAPI dependencies (`Request`, `Response`, `Depends`)
- External service calls (Redis, message queues)

Pure code ONLY has:
- Function arguments (input)
- Return values (output)
- Pydantic models
- Data transformations
- Business logic calculations

### Example: WRONG vs RIGHT

**WRONG (Impure - Hard to Test):**
```python
class NoveltyScorer:
    def calculate(self, event_id: str) -> float:
        # BAD: Database call inside logic
        event = self.db.query(TelemetryEvent).get(event_id)
        if event.action in RARE_ACTIONS:
            return 0.8
        return 0.2
```

**RIGHT (Pure - Easy to Test):**
```python
class NoveltyScorer:
    """Pure logic - no database, no network, no files."""

    def calculate(self, event: TelemetryEvent) -> float:
        # GOOD: Receives data, returns result
        if event.action in RARE_ACTIONS:
            return 0.8
        return 0.2
```

---

## Mock Conformance (CRITICAL)

### The Rule

**ALWAYS use `create_autospec()` instead of bare `Mock()`.**

This is enforced by pre-commit hooks. Violations will be blocked.

```python
# BAD - Silent bugs
mock = Mock()
mock.nonexistent_method()  # Passes silently - BUG!

# GOOD - Catches interface violations
from unittest.mock import create_autospec
mock = create_autospec(PolicyEngine, instance=True)
mock.nonexistent_method()  # Raises AttributeError immediately
```

---

## Governance Rules (Pre-commit Enforced)

### 1. Iron Dome (Type Safety)

Type safety ratchet - violations can only go DOWN:
- No new `Any` annotations
- No new `# type: ignore` comments
- No new `cast()` calls

### 2. Rising Tide (Mock Tax)

Test files using mocks cannot exceed 2x the size of source:
- Source: 100 lines → Test: max 200 lines
- If exceeded, extract pure logic into separate file

### 3. SRP Guardrails

Single Responsibility Principle enforcement:
- Files: warn at 300 lines, fail at 600 lines
- Functions: max 75 lines

### 4. Mock Conformance

All mocks must use `create_autospec()`:
- Bare `Mock()` is forbidden
- `MagicMock()` is forbidden

---

## Code Style

### Python (The Brain)

- **Formatter:** Black (line-length: 100)
- **Import sorter:** isort (profile: black)
- **Linter:** Ruff
- **Type checker:** mypy

### Type Hints Required

All new code MUST have type hints:

```python
# GOOD
def calculate_payout(
    events: list[TelemetryEvent],
    multiplier: float = 1.0
) -> PayoutResult:
    ...

# BAD
def calculate_payout(events, multiplier=1.0):
    ...
```

---

## Running Tests

```bash
# All tests
pytest

# With coverage
pytest --cov=gaian --cov-report=html

# Only unit tests (fast)
pytest tests/unit/

# Pre-commit hooks
pre-commit run --all-files
```

---

## TDD Checklist (Before Every Commit)

- [ ] Wrote failing test FIRST
- [ ] Test uses `create_autospec()` for mocks
- [ ] Pure logic extracted (no I/O in business logic)
- [ ] All functions have type hints
- [ ] `pre-commit run --all-files` passes
- [ ] Test file < 2x source file size
- [ ] No new `Any` or `type: ignore`

---

## Key Documentation

| Document | Purpose |
|----------|---------|
| `docs/guides/development/TDD-GUIDE.md` | Full TDD philosophy and patterns |
| `docs/guides/development/CICD.md` | CI/CD pipeline configuration |
| `docs/guides/project setup/PRECOMMIT-SETUP.md` | Pre-commit hook setup |
| `docs/guides/architecture/directory-structure.md` | Project organization |
