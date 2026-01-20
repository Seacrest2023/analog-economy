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

## Working with This Codebase

### Before Making Changes

1. Read `story-index.md` to understand the documentation landscape
2. Read relevant specification documents for the area you're working on
3. Check for cross-references that might be affected
4. Understand the "why" before changing the "what"

### When Adding Features

1. **Document first** - Create or update the specification
2. **Update the index** - Add to `story-index.md`
3. **Then implement** - Code follows documentation

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
