# Legacy System: Bloodlines Across Time

> "You do not play a character. You play a lineage. Every death is a comma, not a period."

## Table of Contents

1. [Overview](#1-overview)
2. [Design Philosophy](#2-design-philosophy)
3. [Bloodline Mechanics](#3-bloodline-mechanics)
4. [Inheritance System](#4-inheritance-system)
5. [Cross-Era Progression](#5-cross-era-progression)
6. [Reincarnation Integration](#6-reincarnation-integration)
   - [Karma and Reincarnation](#63-karma-and-reincarnation)
7. [Legacy Achievements](#7-legacy-achievements)
8. [The Ancestor Hall](#8-the-ancestor-hall)
9. [Training Data Value](#9-training-data-value)
10. [Implementation](#10-implementation)

---

## 1. Overview

The Legacy System is the meta-progression layer that connects all of a player's lives across eras and instances. It transforms permadeath from a setback into a transition, and gives meaning to player investment that persists beyond any single character's existence.

### Core Concepts

| Concept | Definition |
|---------|------------|
| **Bloodline** | A player's persistent lineage across all characters |
| **Ancestor** | A previous character in the player's bloodline |
| **Inheritance** | What carries forward when a character dies |
| **Legacy Points** | Meta-currency earned through meaningful lives |
| **The Great Filter** | The vetting system that gates era progression |
| **Ascension** | Moving your bloodline to a later era |

### What Persists vs. What Resets

```
PERSISTS (Bloodline Level)          RESETS (Character Level)
────────────────────────────────    ────────────────────────────────
• Legacy Points                     • Physical items/inventory
• Unlocked eras                     • Character relationships
• Bloodline reputation              • Settlement position
• Codex contributions               • Skill levels
• Achievement badges                • In-game currency
• Inherited knowledge hints         • Health/age
• Ancestral memories (lore)         • Faction standing
```

---

## 2. Design Philosophy

### 2.1 Death as Transition

Most games treat death as failure. In The Analog Economy:

```
Traditional Game Death:
[Progress] ──────────────────────────X Game Over
                                      ↓
                                [Start Over]

Analog Economy Death:
[Life 1] ───────────────────────╮
                                ↓ Death
[Life 2] ───────────────────────╮ (Inheritance carried)
                                ↓ Death
[Life 3] ───────────────────────→ (Lineage continues)
```

Death should feel:
- **Meaningful**: This character's story matters
- **Transitional**: Not the end, but a passing of the torch
- **Consequential**: Some things are lost forever
- **Hopeful**: The next generation can do better

### 2.2 Long-Term Investment

Players who invest hundreds of hours should feel:
- Their bloodline has become powerful and influential
- Ancestors are remembered and honored
- Knowledge accumulated benefits future generations
- The journey through eras is an epic saga

### 2.3 Anti-Grinding Philosophy

Legacy Points are earned through **quality**, not quantity:
- Living a meaningful life (not just a long one)
- Making impactful decisions (not just many decisions)
- Contributing to the Codex (not just playing)
- Helping the community (not just personal advancement)

---

## 3. Bloodline Mechanics

### 3.1 Bloodline Identity

Each player account has one persistent bloodline:

```yaml
bloodline:
  bloodline_id: "BL-2024-0001234"
  created_at: "2025-03-15"
  name: "House of the Rising Sun"  # Player-chosen

  # Progression
  legacy_points: 47250
  bloodline_level: 23
  highest_era_unlocked: "industrial"

  # History
  total_ancestors: 47
  longest_lived: "Enki-Sharra" (lived 82 years, Sumer)
  most_impactful: "Marcus Aurelius Chen" (industrial revolution leader)

  # Reputation
  global_reputation: 0.78  # 0-1 scale
  faction_affinities:
    builders: 0.82
    explorers: 0.65
    scholars: 0.91

  # Codex
  total_contributions: 312
  knowledge_domains: ["flora", "agriculture", "medicine"]
  archivist_rank: "master"
```

### 3.2 Bloodline Levels

```yaml
bloodline_levels:
  1-5:    "Nascent Bloodline"
  6-10:   "Established Lineage"
  11-15:  "Respected House"
  16-20:  "Noble Dynasty"
  21-25:  "Legendary Bloodline"
  26-30:  "Immortal Legacy"
  31+:    "Eternal House"

  level_requirements:
    level_2: 500 LP
    level_3: 1500 LP
    level_5: 5000 LP
    level_10: 25000 LP
    level_15: 75000 LP
    level_20: 150000 LP
    level_25: 300000 LP
    level_30: 500000 LP
```

### 3.3 Bloodline Traits

As bloodlines level up, they develop persistent traits:

```yaml
bloodline_traits:
  # Earned through patterns of play
  scholar_blood:
    requirement: "50+ Codex contributions across 3+ domains"
    benefit: "10% faster knowledge recovery, +5% Codex rewards"

  merchant_blood:
    requirement: "10,000+ successful trades across bloodline"
    benefit: "Better starting trade reputation, +5% trade margins"

  warrior_blood:
    requirement: "Win 500+ conflicts across bloodline"
    benefit: "Combat learning bonus, starting weapon proficiency"

  healer_blood:
    requirement: "Save 1000+ lives through medicine"
    benefit: "Faster medicine crafting, herb identification bonus"

  builder_blood:
    requirement: "Construct 100+ significant structures"
    benefit: "Blueprint inheritance, construction efficiency"

  wanderer_blood:
    requirement: "Explore 80%+ of map across 3+ eras"
    benefit: "Starting map knowledge, travel speed bonus"

  # Traits are not exclusive - bloodlines can have multiple
  max_active_traits: 3  # At any time
  trait_switching: "Once per character life"
```

---

## 4. Inheritance System

### 4.1 What Transfers on Death

When a character dies, the following transfers to the next character:

```yaml
inheritance:
  automatic:
    - legacy_points_earned_this_life
    - codex_contributions (permanent)
    - bloodline_trait_progress
    - achievement_badges
    - ancestral_memory_fragments

  conditional:
    - family_heirlooms (if not destroyed/lost)
    - inherited_knowledge (skill hints, not full skills)
    - reputation_echoes (diminished faction standing)
    - property_deeds (if succession established)

  lost_forever:
    - physical_inventory (unless heirloom)
    - character_relationships (NPCs remember bloodline, not you)
    - in_game_currency (unless cached)
    - character_specific_achievements
```

### 4.2 Inheritance Preparation

Characters can prepare for death:

```yaml
succession_planning:
  designate_heir:
    description: "Name an NPC or create next character template"
    benefit: "Smoother transition, property preserved"
    cost: "50 Legacy Points"

  create_heirloom:
    description: "Enchant item to persist across generations"
    benefit: "Item transfers to next character"
    limit: "3 active heirlooms per bloodline"
    cost: "100 Legacy Points per item"

  establish_house:
    description: "Create persistent family structure"
    benefit: "NPCs remember and assist family members"
    requirement: "Bloodline level 10+"

  write_testament:
    description: "Record knowledge for descendants"
    benefit: "Next character receives skill hints"
    cost: "Time investment"
```

### 4.3 Heirloom System

Heirlooms are items that persist across generations:

```yaml
heirloom:
  item_id: "HEIR-001"
  original_owner: "Enki-Sharra"
  creation_era: "sumer"
  current_holder: "Marcus Chen"
  generations_held: 12

  base_item: "Bronze Dagger"
  heirloom_properties:
    - name: "Ancestor's Blessing"
      effect: "+5% learning speed"
    - name: "Memory of Enki"
      effect: "Visions of Sumer (lore unlocks)"

  history:
    - "Forged by Enki-Sharra in the temple of An"
    - "Carried through the fall of Ur"
    - "Lost for 3 generations, recovered by Lucia"
    - "Defended the family through the plague of 1348"

  condition: 0.85  # Can degrade, must be maintained
  can_be_lost: true  # Theft, destruction still possible
```

### 4.4 Ancestral Memories

Previous lives leave memory traces:

```yaml
ancestral_memory:
  # Passive effects
  deja_vu:
    trigger: "Visiting location where ancestor died"
    effect: "Brief vision of ancestor's final moments"
    benefit: "Potential clue to hidden knowledge or danger"

  inherited_instinct:
    trigger: "Facing situation ancestor faced"
    effect: "Gut feeling about correct choice"
    benefit: "Subtle guidance, not answer"

  # Active invocation (costs LP)
  commune_with_ancestors:
    cost: 10 LP
    cooldown: "Once per in-game month"
    effect: "Ask one question, receive cryptic answer"
    examples:
      - "Where did Enki-Sharra hide the tablets?"
      - "How did grandmother survive the famine?"
```

---

## 5. Cross-Era Progression

### 5.1 Era Unlocking

Eras are unlocked through The Great Filter, not time played:

```yaml
era_progression:
  starting_era: "ancient"  # Sumer, Egypt, etc.

  ancient_to_classical:
    requirement: "Complete Phase 1 of Great Filter"
    filter_criteria:
      - "Survive 3 complete character lives"
      - "Achieve community standing of Respected"
      - "Contribute 25+ Codex entries"
      - "Accumulate 5000+ Legacy Points"
    ticket_required: "Ascension Ticket (10,000 available)"

  classical_to_medieval:
    requirement: "Complete Phase 2 of Great Filter"
    filter_criteria:
      - "Lead successful settlement (100+ residents)"
      - "Master 3 crafting disciplines"
      - "Contribute 100+ Codex entries"
      - "Accumulate 25000+ Legacy Points"
    ticket_required: "Ascension Ticket"

  medieval_to_industrial:
    requirement: "Demonstrate exceptional play"
    filter_criteria:
      - "Top 5% of player community"
      - "Significant Codex contribution"
      - "Community leadership demonstrated"
    ticket_required: "Destination Ticket (2,000 available)"

  industrial_to_ai:
    requirement: "Elite player status"
    filter_criteria:
      - "Top 1% of player community"
      - "Major Codex contributor"
      - "Proven positive community impact"
    ticket_required: "Genesis Ticket (500 available)"
```

### 5.2 Era Experience

Each era plays differently while building on previous experience:

```yaml
era_experience:
  ancient:
    focus: "Survival basics, tribal society"
    learning: "Agriculture, basic crafts, social bonds"
    knowledge_gained: "Foundation skills"

  classical:
    focus: "Civilization building, politics"
    learning: "Advanced crafts, trade, governance"
    builds_on: "Ancient survival skills"

  medieval:
    focus: "Systems of knowledge, institutions"
    learning: "Complex economics, technology chains"
    builds_on: "Classical organization"

  industrial:
    focus: "Rapid change, mass coordination"
    learning: "Scale, efficiency, social upheaval"
    builds_on: "Medieval institutional knowledge"

  ai_era:
    focus: "Existential adaptation, post-scarcity"
    learning: "Human purpose, AI coordination"
    builds_on: "All previous eras"
```

### 5.3 Cross-Era Bloodline Play

Bloodlines can have active characters in multiple eras:

```yaml
multi_era_play:
  enabled: true

  rules:
    - "One active character per era at a time"
    - "Characters cannot directly interact"
    - "Legacy Points pool across all characters"
    - "Codex contributions shared"

  benefits:
    - "Experience multiple historical periods"
    - "Faster Legacy Point accumulation"
    - "Broader Codex contribution capability"

  restrictions:
    - "Cannot transfer items between eras"
    - "Knowledge doesn't directly transfer"
    - "Each character must prove themselves"
```

---

## 6. Reincarnation Integration

### 6.1 Ticket System Review

From the existing Reincarnation Ticket spec:

```yaml
ticket_tiers:
  ascension_ticket:
    supply: 10000
    grants: "Move from Ancient → Classical, or Classical → Medieval"
    earning: "Great Filter Phase 1/2 completion"
    tradeable: true

  destination_ticket:
    supply: 2000
    grants: "Move from Medieval → Industrial"
    earning: "Great Filter Phase 3 (top 5%)"
    tradeable: true

  genesis_ticket:
    supply: 500
    grants: "Move from Industrial → AI Era"
    earning: "Elite status (top 1%)"
    tradeable: true
```

### 6.2 Legacy System Integration

```yaml
ticket_and_legacy:
  earning_tickets:
    - Legacy Points contribute to Great Filter score
    - Bloodline level provides bonus multipliers
    - Ancestral achievements count toward qualification

  using_tickets:
    - Ticket attached to bloodline, not character
    - Once used, era permanently unlocked
    - Descendants start in unlocked era

  ticket_value:
    - Higher bloodline level = more valuable ticket (tradeable)
    - Tickets can be traded between players
    - Market price reflects scarcity and demand
```

### 6.3 Karma and Reincarnation

> **See also:** [Asset Protection & Karma](asset-protection-karma.md) for complete karma mechanics.

Karma affects reincarnation options:

```yaml
karma_reincarnation:
  enlightened: [800, 1000]    # Choose any next life
  virtuous: [400, 800]        # Human, favorable circumstances
  balanced: [-200, 400]       # Human, normal circumstances
  troubled: [-500, -200]      # Human, difficult start
  corrupted: [-800, -500]     # 50% chance animal life
  damned: [-1000, -800]       # Guaranteed animal life

animal_life:
  duration: "7-30 real-time days depending on karma"
  experience: "Cannot speak, follow owner commands"
  ending: "Duration expires, owner frees you, or heroic act"
  after: "Reincarnate human with karma reset to -200"
```

### 6.4 The Choice on Death

When a character dies:

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  YOUR ANCESTOR HAS PASSED                                   │
│  ═══════════════════════════════════════════════════════    │
│                                                             │
│  Kira of House Rising Sun                                   │
│  Lived: 47 years                                            │
│  Era: Classical Rome                                        │
│  Cause: Fever during the plague of Antoninus               │
│                                                             │
│  LEGACY EARNED THIS LIFE:                                   │
│  • 2,340 Legacy Points                                      │
│  • 12 Codex contributions                                   │
│  • Merchant blood progress: 78%                             │
│  • Heirloom preserved: Family Seal                          │
│  • Karma: 245 (Balanced)                                    │
│                                                             │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│  WHERE WILL YOUR NEXT DESCENDANT BE BORN?                   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  [SAME ERA: Classical]                              │    │
│  │  Start as Kira's grandchild in Rome                 │    │
│  │  • Family reputation preserved                      │    │
│  │  • Heirloom waiting                                 │    │
│  │  • Property succession active                       │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  [DIFFERENT INSTANCE: Classical]                    │    │
│  │  Start fresh in Constantinople                      │    │
│  │  • New location, new opportunities                  │    │
│  │  • Heirloom carried                                 │    │
│  │  • No family connections                            │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  [EARLIER ERA: Ancient]                             │    │
│  │  Return to Sumer as distant ancestor                │    │
│  │  • Different gameplay experience                    │    │
│  │  • Knowledge feels like "prophecy"                  │    │
│  │  • Explore different paths                          │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  [NEXT ERA: Medieval] 🔒                            │    │
│  │  Requires: 5000 more LP or Ascension Ticket         │    │
│  │  Your bloodline approaches this threshold           │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 7. Legacy Achievements

### 7.1 Achievement Categories

```yaml
legacy_achievements:
  longevity:
    - "Centenarian" - Live to 100 years
    - "Seven Generations" - 7 consecutive lives in same era
    - "Eternal House" - Bloodline survives 1000 years total

  impact:
    - "City Founder" - Found settlement that reaches 1000 residents
    - "Dynasty Maker" - 5 descendants reach leadership positions
    - "History Changer" - Decision altered era-wide event

  knowledge:
    - "Grand Archivist" - 500 Codex contributions
    - "Domain Master" - Complete 90% of one Codex domain
    - "Polymath Lineage" - Contributions in all domains

  social:
    - "Beloved House" - Maximum reputation in 3+ factions
    - "Peacemaker" - Resolve 50 conflicts diplomatically
    - "Mentor Lineage" - Help 100 new players

  challenge:
    - "Against All Odds" - Survive 3 near-extinction events
    - "Phoenix" - Recover from total loss (no heirlooms, no property)
    - "Era Conqueror" - Top 1% in every unlocked era
```

### 7.2 Achievement Display

```
┌─────────────────────────────────────────────────────────────┐
│  HOUSE OF THE RISING SUN                                    │
│  ═══════════════════════════════════════════════════════    │
│                                                             │
│  Bloodline Level: 23 (Legendary Bloodline)                  │
│  Total Ancestors: 47                                        │
│  Eras Unlocked: Ancient, Classical, Medieval, Industrial    │
│                                                             │
│  ACHIEVEMENTS                                               │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│  🏆 LEGENDARY                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ [City Founder] Founded New Alexandria (pop. 2,847) │    │
│  │ [Grand Archivist] 523 Codex contributions          │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  🥇 EPIC                                                    │
│  [Seven Generations] [Against All Odds] [Mentor Lineage]   │
│                                                             │
│  🥈 RARE                                                    │
│  [Merchant Prince] [Healer's Touch] [Explorer's Heart]     │
│  [Scholar's Dedication] [Builder's Legacy]                  │
│                                                             │
│  Progress: 34/52 achievements unlocked                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 8. The Ancestor Hall

### 8.1 Physical Space

Each settlement has an Ancestor Hall where players can:
- View their bloodline history
- Commune with ancestors
- Display achievements
- Plan succession

**Visual Design:**

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│     THE ANCESTOR HALL                                       │
│     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░     │
│                                                             │
│         ┌─────────────────────────────────────┐             │
│         │                                     │             │
│         │    [Bloodline Tapestry]             │             │
│         │    Visual family tree               │             │
│         │    spanning generations             │             │
│         │                                     │             │
│         │         ┌───┐                       │             │
│         │         │ 1 │ Enki-Sharra           │             │
│         │         └─┬─┘ (Founder)             │             │
│         │           │                         │             │
│         │       ┌───┴───┐                     │             │
│         │       │       │                     │             │
│         │     ┌─┴─┐   ┌─┴─┐                   │             │
│         │     │ 2 │   │ 3 │                   │             │
│         │     └───┘   └───┘                   │             │
│         │                                     │             │
│         └─────────────────────────────────────┘             │
│                                                             │
│     [Ancestor Shrines]     [Achievement Wall]               │
│         ┌───┐                  ┌─────────┐                  │
│         │ ⚱ │ Commune          │ 🏆 🥇 🥈│                  │
│         └───┘                  └─────────┘                  │
│                                                             │
│     [Heirloom Vault]       [Succession Planning]            │
│         ┌───┐                  ┌─────────┐                  │
│         │ 📦│ 3 items          │ ✍️ Plan │                  │
│         └───┘                  └─────────┘                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 8.2 Bloodline Tapestry

Interactive visualization of family history:

```yaml
tapestry_features:
  display:
    - All ancestors as portraits
    - Connecting lines showing lineage
    - Era color coding
    - Achievement badges on portraits

  interaction:
    - Click ancestor for biography
    - See their achievements
    - View their Codex contributions
    - Hear ancestral memory voice lines

  filters:
    - By era
    - By achievement type
    - By cause of death
    - By impact level
```

### 8.3 Ancestor Biographies

Each ancestor has an auto-generated biography:

```
┌─────────────────────────────────────────────────────────────┐
│  ANCESTOR: ENKI-SHARRA                                      │
│  ═══════════════════════════════════════════════════════    │
│                                                             │
│  Founder of House Rising Sun                                │
│  Era: Sumer | Lived: 82 years                               │
│                                                             │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│  BIOGRAPHY                                                  │
│  Enki-Sharra was born in the village of Eridu during the   │
│  reign of Ur-Nammu. A farmer's child who became a temple   │
│  scribe, they devoted their life to preserving the old     │
│  knowledge of plants and medicines.                         │
│                                                             │
│  Known for: Founding the first healing garden in Eridu     │
│  Greatest achievement: Discovered treatment for river      │
│  fever that saved over 200 lives                            │
│                                                             │
│  Died peacefully, surrounded by grandchildren, having      │
│  lived the longest life in the village's memory.           │
│                                                             │
│  LEGACY                                                     │
│  • 47 Codex contributions (medicinal plants)               │
│  • 3 heirlooms created (2 still held)                      │
│  • Bloodline trait unlocked: Healer Blood                  │
│  • 2,847 Legacy Points earned                               │
│                                                             │
│  MEMORABLE MOMENT                                           │
│  "When the plague came, Enki-Sharra alone knew which       │
│   herbs could ease the suffering. They worked without      │
│   rest for seven days, and when it passed, the village     │
│   built this hall in their honor."                         │
│                                                             │
│  [Commune with Ancestor] [View Contributions] [Close]       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 9. Training Data Value

### 9.1 Multi-Generational Decision Making

The Legacy System creates unique training data:

```yaml
training_data_unique:
  long_term_planning:
    description: "Decisions made for future generations, not just now"
    examples:
      - "Investing in education for grandchildren"
      - "Building infrastructure that outlives the builder"
      - "Sacrificing personal gain for family reputation"
    ai_value: "Long-horizon planning, intergenerational ethics"

  identity_continuity:
    description: "How humans relate to past and future selves"
    examples:
      - "Honoring ancestor commitments"
      - "Continuing family traditions"
      - "Breaking with harmful patterns"
    ai_value: "Identity, commitment, personal narrative"

  succession_decisions:
    description: "Preparing for and managing transitions"
    examples:
      - "Choosing heirs"
      - "Writing testaments"
      - "Distributing resources"
    ai_value: "Transition management, fairness, foresight"

  legacy_motivation:
    description: "Actions taken for reputation beyond death"
    examples:
      - "Building monuments"
      - "Creating lasting institutions"
      - "Sacrificing for historical impact"
    ai_value: "Meaning-making, purpose, mortality awareness"
```

### 9.2 Behavioral Patterns

```yaml
legacy_behaviors:
  tracked_patterns:
    - "How do players balance personal vs family goals?"
    - "What motivates heirloom creation?"
    - "How does ancestor memory affect decisions?"
    - "What prompts era progression vs staying?"

  valuable_scenarios:
    - "Choosing between personal advancement and family stability"
    - "Deciding what knowledge to preserve for descendants"
    - "Managing family reputation after ancestor's mistake"
    - "Starting fresh vs continuing family legacy"
```

---

## 10. Implementation

### 10.1 Data Model

```python
@dataclass
class Bloodline:
    bloodline_id: str
    account_id: str
    name: str
    created_at: DateTime

    # Progression
    legacy_points: int
    bloodline_level: int
    unlocked_eras: list[str]

    # Traits
    active_traits: list[BloodlineTrait]
    trait_progress: dict[str, float]

    # History
    ancestors: list[Ancestor]
    heirlooms: list[Heirloom]
    achievements: list[Achievement]

    # Reputation
    global_reputation: float
    faction_affinities: dict[str, float]

    # Codex
    total_contributions: int
    archivist_rank: str


@dataclass
class Ancestor:
    ancestor_id: str
    bloodline_id: str
    name: str
    era: str
    instance_id: str

    # Life
    birth_date: DateTime
    death_date: DateTime
    cause_of_death: str
    years_lived: int

    # Achievements
    legacy_points_earned: int
    codex_contributions: int
    achievements: list[str]
    notable_events: list[str]

    # Biography
    generated_biography: str
    memorable_moment: str


@dataclass
class Heirloom:
    heirloom_id: str
    bloodline_id: str
    original_owner: str
    creation_era: str

    # Item
    base_item_id: str
    heirloom_properties: list[HeirloomProperty]

    # History
    generations_held: int
    history_entries: list[str]
    current_holder: str | None

    # State
    condition: float
    is_lost: bool
```

### 10.2 MVP Scope

```yaml
mvp_legacy:
  included:
    - Basic bloodline tracking
    - Legacy Points accumulation
    - Single era (Ancient)
    - Character death transition
    - Simple inheritance (LP + Codex)
    - Ancestor list (no tapestry)
    - 3 achievements

  excluded:
    - Heirlooms
    - Bloodline traits
    - Multi-era play
    - Ancestor Hall building
    - Communion system
    - Complex succession planning
    - Achievement wall
    - Trading tickets

  metrics_to_prove:
    - Players feel continuity across deaths
    - Legacy Points motivate quality play
    - Death feels transitional, not punishing
    - Ancestor connection is meaningful
```

### 10.3 Configuration

```yaml
# legacy_config.yaml

legacy:
  enabled: true

  points:
    base_life_completion: 100
    per_year_lived: 5
    codex_contribution: 25
    achievement_bonus:
      common: 50
      rare: 150
      epic: 500
      legendary: 2000

  inheritance:
    reputation_decay: 0.5  # 50% of reputation carries
    knowledge_hint_chance: 0.25
    max_heirlooms: 3

  traits:
    max_active: 3
    switch_cost_lp: 500

  ancestors:
    biography_generation: "on_death"
    memorable_moment_selection: "highest_impact_decision"
    voice_line_generation: false  # MVP

  thresholds:
    classical_unlock: 5000
    medieval_unlock: 25000
    industrial_unlock: 75000
    ai_era_unlock: 200000
```

---

## Appendix: Legacy Point Economy

```yaml
lp_earning:
  # Life events
  survive_year: 5
  reach_adulthood: 50
  reach_elder: 100
  die_peacefully: 50
  die_heroically: 200

  # Achievements
  per_codex_contribution: 25
  per_community_help: 10
  per_settlement_milestone: 100
  per_leadership_success: 150

  # Special
  first_era_completion: 500
  great_filter_phase: 1000
  rare_scenario_survival: 200

lp_spending:
  # Succession
  designate_heir: 50
  create_heirloom: 100
  establish_house: 500

  # Active abilities
  commune_with_ancestor: 10
  ancestral_guidance: 25

  # Unlocks
  trait_switch: 500
  extra_heirloom_slot: 1000
```

---

*Your ancestors live through you. Your descendants will remember. This is not one life - it is the story of a house that spans the ages.*
