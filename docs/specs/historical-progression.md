# The Analog Economy: Historical Progression System

> **Version:** 1.0
> **Last Updated:** 2026-01-19
> **Status:** Vision Draft

---

## Executive Summary

The Analog Economy spans the entirety of human civilization—from ancient Sumer (~4000 BCE) through the modern AI era and into the evolving future. Players don't just survive; they experience humanity's journey, solving era-appropriate problems and witnessing (and influencing) the arc of human progress.

**The Game Never Ends:** As real-world events unfold, new challenges are added. The game is a living simulation of human civilization.

---

## Table of Contents

1. [The Vision](#the-vision)
2. [Era Structure](#era-structure)
3. [Era Instance Scaling: Many Worlds, Infinite Data](#era-instance-scaling-many-worlds-infinite-data)
4. [The Great Filter: A Meritocratic Journey](#the-great-filter-a-meritocratic-journey)
5. [One Engine, Many Games](#one-engine-many-games)
6. [Era Progression Mechanics](#era-progression-mechanics)
7. [Ancient Era: The Cradle](#ancient-era-the-cradle)
8. [Classical Era: Empires](#classical-era-empires)
9. [Medieval Era: Survival & Faith](#medieval-era-survival--faith)
10. [Renaissance Era: Discovery](#renaissance-era-discovery)
11. [Industrial Era: Revolution](#industrial-era-revolution)
12. [Modern Era: Complexity](#modern-era-complexity)
13. [AI Era: The Biomes](#ai-era-the-biomes)
14. [Living Future: Current Events](#living-future-current-events)
15. [Training Data Across Time](#training-data-across-time)
16. [Reincarnation Mechanics](#reincarnation-mechanics)
17. [Reincarnation Tickets: The Bottleneck Economy](#reincarnation-tickets-the-bottleneck-economy)
18. [Era Scarcity Constraints](#era-scarcity-constraints)
19. [Player-Owned Assets](#player-owned-assets-metaverse-layer)
20. [Era Timeout & Catastrophe Mechanics](#era-timeout--catastrophe-mechanics)
21. [War & Conflict Re-enactments](#war--conflict-re-enactments)
22. [Religion & Ritual Systems](#religion--ritual-systems)
23. [Era Transition Auctions](#era-transition-auctions)

---

## The Vision

### The Full Arc of Humanity

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    THE ANALOG ECONOMY TIMELINE                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ANCIENT        CLASSICAL      MEDIEVAL       RENAISSANCE    INDUSTRIAL    │
│  4000 BCE       500 BCE        500 CE         1400 CE        1750 CE       │
│     │              │              │              │              │           │
│     ▼              ▼              ▼              ▼              ▼           │
│  ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐         │
│  │Sumer │ ──▶  │Greece│ ──▶  │Dark  │ ──▶  │Age of│ ──▶  │Facto-│         │
│  │Egypt │      │Rome  │      │Ages  │      │Disco-│      │ries  │         │
│  │Indus │      │Persia│      │Plague│      │very  │      │Labor │         │
│  └──────┘      └──────┘      └──────┘      └──────┘      └──────┘         │
│                                                                             │
│  MODERN         AI ERA         LIVING FUTURE                               │
│  1900 CE        2020 CE        NOW + ONGOING                               │
│     │              │              │                                         │
│     ▼              ▼              ▼                                         │
│  ┌──────┐      ┌──────┐      ┌──────┐                                      │
│  │World │ ──▶  │The   │ ──▶  │Real  │                                      │
│  │Wars  │      │Biomes│      │World │                                      │
│  │Tech  │      │Crisis│      │Events│                                      │
│  └──────┘      └──────┘      └──────┘                                      │
│                                                                             │
│  "From the first cities to the last frontier"                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Why Historical Progression?

| Benefit | Description |
|---------|-------------|
| **Training Data Depth** | See how humans solve problems across technological contexts |
| **Educational Value** | Learn history by experiencing it |
| **Timeless Patterns** | Identify strategies that work in ANY era |
| **Era-Specific Innovation** | Solutions that only work with period technology |
| **Endless Content** | New eras, new events, game never stagnates |
| **Emotional Journey** | Players feel humanity's progress |

---

## Era Structure

### Overview

| Era | Time Period | Core Challenge | Technology Level |
|-----|-------------|----------------|------------------|
| **Ancient** | 4000 BCE - 500 BCE | Civilization founding | Stone, bronze, irrigation |
| **Classical** | 500 BCE - 500 CE | Empire building | Iron, roads, aqueducts |
| **Medieval** | 500 CE - 1400 CE | Survival & faith | Castles, guilds, plague |
| **Renaissance** | 1400 CE - 1750 CE | Discovery & science | Ships, printing, gunpowder |
| **Industrial** | 1750 CE - 1900 CE | Revolution & labor | Steam, factories, railways |
| **Modern** | 1900 CE - 2020 CE | Global complexity | Electricity, computing, nuclear |
| **AI Era** | 2020 CE - Present | The Biomes | AI, robotics, biotech |
| **Living Future** | Present - Ongoing | Current events | Evolving |

### Player Journey Options

```yaml
progression_modes:
  chronological:
    description: "Start in Sumer, progress through all eras"
    time_to_complete: "Hundreds of hours"
    rewards: "Full historical understanding, era-specific items carry forward"

  era_select:
    description: "Choose starting era"
    unlocked_by: "Completing previous eras OR premium"
    benefit: "Jump to preferred period"

  time_traveler:
    description: "Random era placement"
    challenge: "Adapt to any period"
    reward: "Special achievements for era-hopping"

  modern_start:
    description: "Begin in AI Era directly"
    default_for: "New players who want immediate relevance"
    can_unlock: "Historical eras through gameplay"
```

---

## Era Instance Scaling: Many Worlds, Infinite Data

### The Parallel Civilizations Model

Historical eras had finite populations—Ancient Sumer wasn't a billion people. But we need massive scale to generate valuable training data. The solution: **run many parallel instances of each era**, each slightly different.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PARALLEL INSTANCE MODEL                                   │
│              "One Sumer? No. A hundred Sumers."                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  THE PROBLEM:                                                               │
│  • Ancient Sumer had ~50,000 people in major cities                         │
│  • We want 1,000,000+ players generating data                               │
│  • Can't cram 1M players into one "Sumer" — breaks immersion                │
│                                                                             │
│  THE SOLUTION:                                                              │
│  • Spin up PARALLEL INSTANCES of each era                                   │
│  • Each instance has realistic population                                   │
│  • Instances are slightly different (procedural variation)                  │
│  • Scale horizontally as player base grows                                  │
│                                                                             │
│  EXAMPLE - ANCIENT ERA AT SCALE:                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                                                                     │   │
│  │   Sumer-001    Sumer-002    Sumer-003    ...    Sumer-127          │   │
│  │   ┌───────┐    ┌───────┐    ┌───────┐          ┌───────┐          │   │
│  │   │ 5,000 │    │ 5,000 │    │ 5,000 │          │ 5,000 │          │   │
│  │   │players│    │players│    │players│          │players│          │   │
│  │   │ 5,000 │    │ 5,000 │    │ 5,000 │          │ 5,000 │          │   │
│  │   │ NPCs  │    │ NPCs  │    │ NPCs  │          │ NPCs  │          │   │
│  │   └───────┘    └───────┘    └───────┘          └───────┘          │   │
│  │                                                                     │   │
│  │   Total: 127 instances × 10,000 pop = 635,000 real players         │   │
│  │   + 635,000 NPCs = 1.27M total population experiencing Ancient era │   │
│  │                                                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  "Same mechanics. Same challenges. Different neighbors. Different data."    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Population Composition

Each era instance maintains a **balanced ratio of real players to NPCs** to ensure:
- Enough real human interactions for quality training data
- Realistic population density for immersion
- Gameplay that functions even with player fluctuations

```yaml
population_model:
  # Target ratio of real players to NPCs
  player_npc_ratio:
    minimum_players: 0.30          # At least 30% real players
    target_players: 0.50           # Ideal: 50% real, 50% NPC
    maximum_players: 0.80          # Cap at 80% to maintain NPC economy

  # NPC functions
  npc_roles:
    population_filler:
      description: "Maintain realistic population density"
      behavior: "Background activity, economy participation"

    interaction_partners:
      description: "Trade, quest, social interactions"
      behavior: "Responsive to player actions, memory of interactions"

    economy_stabilizers:
      description: "Prevent market crashes, ensure liquidity"
      behavior: "Buy/sell at reasonable prices, provide services"

    training_data_baseline:
      description: "Provide comparison data for player behavior"
      behavior: "Predictable patterns vs novel human decisions"

  # When player count drops, NPCs fill in
  dynamic_balancing:
    player_leaves:
      action: "Spawn NPC to maintain population"
      delay: "Immediate for economy roles, gradual for social"

    player_joins:
      action: "Despawn excess NPCs"
      priority: "Remove least-interactive NPCs first"

    minimum_player_threshold:
      description: "Below this, instance may be merged or paused"
      threshold: 0.20               # 20% real players minimum
```

### Instance Spawning Rules

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    INSTANCE LIFECYCLE                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SPAWN TRIGGER: Player queue for era exceeds threshold                      │
│                                                                             │
│  ┌─────────────┐                                                            │
│  │ Player Pool │ ──▶ 100,000 players want to play Ancient Era              │
│  │   (Queue)   │                                                            │
│  └─────────────┘                                                            │
│         │                                                                   │
│         ▼                                                                   │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  INSTANCE MANAGER                                                    │   │
│  │                                                                      │   │
│  │  Current Ancient instances: 8                                        │   │
│  │  Current capacity: 8 × 10,000 = 80,000 players                       │   │
│  │  Current load: 78,000 players (97.5% capacity)                       │   │
│  │                                                                      │   │
│  │  Queue: 22,000 waiting                                               │   │
│  │                                                                      │   │
│  │  Decision: SPAWN 3 NEW INSTANCES                                     │   │
│  │                                                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│         │                                                                   │
│         ▼                                                                   │
│  ┌───────┐  ┌───────┐  ┌───────┐                                           │
│  │Sumer  │  │Sumer  │  │Sumer  │  ◀── New instances with procedural       │
│  │  009  │  │  010  │  │  011  │      variation (different geography,      │
│  └───────┘  └───────┘  └───────┘      resources, starting conditions)      │
│                                                                             │
│  MERGE TRIGGER: Instance drops below minimum viable population              │
│                                                                             │
│  ┌───────┐                                                                  │
│  │Sumer  │ ──▶ Only 1,500 players (15% of capacity)                        │
│  │  003  │     Too few for quality training data                           │
│  └───────┘                                                                  │
│         │                                                                   │
│         ▼                                                                   │
│  Migration event: Players offered choice to relocate to active instance    │
│  Assets converted or auctioned, history preserved                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Era-Specific Instance Parameters

```yaml
instance_scaling:
  # Each era has different population characteristics

  ancient:
    target_population: 10000        # Per instance
    max_players: 5000               # 50% cap
    min_players_viable: 2000        # Below this, consider merge
    spawn_threshold: 4500           # Spawn new when queue > this
    max_instances: 500              # Cap total instances

    procedural_variation:
      geography: ["river_delta", "highland", "coastal"]
      climate: ["arid", "temperate", "monsoon"]
      resources: ["copper_rich", "timber_rich", "fertile"]
      neighbors: ["peaceful", "raiding", "trading"]

  classical:
    target_population: 25000        # Larger cities
    max_players: 12500
    min_players_viable: 5000
    spawn_threshold: 11000
    max_instances: 300

    procedural_variation:
      setting: ["greek_polis", "roman_city", "persian_province", "han_district"]
      political_climate: ["democratic", "imperial", "oligarchic"]
      trade_position: ["hub", "frontier", "agricultural"]

  medieval:
    target_population: 15000        # Smaller due to plague/war
    max_players: 7500
    min_players_viable: 3000
    spawn_threshold: 6500
    max_instances: 400

    procedural_variation:
      region: ["western_europe", "eastern_europe", "middle_east", "silk_road"]
      lord_type: ["benevolent", "harsh", "absent"]
      church_influence: ["dominant", "moderate", "contested"]
      plague_status: ["untouched", "recovering", "endemic"]

  renaissance:
    target_population: 30000        # Growing cities
    max_players: 15000
    min_players_viable: 6000
    spawn_threshold: 13000
    max_instances: 250

    procedural_variation:
      setting: ["italian_city_state", "northern_port", "new_world_colony", "ottoman_city"]
      economy: ["banking", "trade", "manufacturing", "colonial"]
      religious_tension: ["low", "reforming", "counter_reforming"]

  industrial:
    target_population: 50000        # Urban explosion
    max_players: 25000
    min_players_viable: 10000
    spawn_threshold: 22000
    max_instances: 200

    procedural_variation:
      city_type: ["factory_town", "port_city", "mining_region", "frontier"]
      labor_conditions: ["early_industrial", "reform_era", "union_active"]
      technology_level: ["steam", "early_electric", "steel_age"]

  modern:
    target_population: 100000       # Mass society
    max_players: 50000
    min_players_viable: 20000
    spawn_threshold: 45000
    max_instances: 150

    procedural_variation:
      period: ["pre_war", "interwar", "cold_war", "digital_age"]
      region: ["western", "eastern_bloc", "developing", "neutral"]
      crisis_type: ["economic", "political", "environmental"]

  ai_era:
    target_population: 50000        # Biome-based
    max_players: 25000
    min_players_viable: 10000
    spawn_threshold: 22000
    max_instances: 200              # Per biome

    procedural_variation:
      biome_variant: "unique_per_instance"
      ai_presence: ["cooperative", "competitive", "absent"]
      crisis_severity: ["mild", "moderate", "severe"]
```

### Data Diversity Through Variation

The parallel instance model doesn't just scale—it **multiplies data diversity**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DATA DIVERSITY BENEFITS                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SAME CHALLENGE, DIFFERENT CONTEXTS:                                        │
│                                                                             │
│  "The Great Flood" challenge in Ancient Era:                                │
│                                                                             │
│  Sumer-001 (River Delta):     Sumer-047 (Highland):    Sumer-089 (Coastal): │
│  • Warning time: 2 days       • Warning time: 1 week   • Warning: none      │
│  • Escape routes: boats       • Escape routes: peaks   • Escape: inland     │
│  • Resource loss: 80%         • Resource loss: 40%     • Resource loss: 90% │
│  • Social dynamic: panic      • Social dynamic: calm   • Social: chaos      │
│                                                                             │
│  TRAINING DATA VALUE:                                                       │
│  "How do humans respond to the SAME crisis with DIFFERENT constraints?"     │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│  EMERGENT VARIATION:                                                        │
│                                                                             │
│  Even identical instances diverge based on player choices:                  │
│                                                                             │
│  Sumer-001 (Week 4):          Sumer-002 (Week 4):                           │
│  • Theocratic governance      • Council of elders                           │
│  • Isolationist trade         • Trade hub                                   │
│  • Warrior culture            • Artisan culture                             │
│  • Survived 2 floods          • Survived 1 flood, 1 raid                    │
│                                                                             │
│  TRAINING DATA VALUE:                                                       │
│  "What path dependencies emerge from early decisions?"                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Instance Discovery and Reputation

Players can build reputation that carries across instances:

```yaml
cross_instance_systems:
  reputation:
    scope: "era-wide"               # Reputation in "Ancient" applies to all Ancient instances
    transfer: "automatic"           # Move instances, keep reputation

  leaderboards:
    instance_specific:
      - "Fastest flood response"
      - "Largest community"
      - "Most trade volume"

    era_wide:
      - "Total keystone challenges completed"
      - "Cross-instance reputation"
      - "Data quality score"

  instance_selection:
    new_player:
      method: "auto_assign"
      criteria: ["lowest_queue", "friend_presence", "language_preference"]

    returning_player:
      method: "choice"
      options:
        - "Return to previous instance"
        - "Join friend's instance"
        - "Start fresh in new instance"

    instance_transfer:
      allowed: true
      cost: "50 NVT"                # Prevent constant hopping
      cooldown_days: 7
      assets: "liquidated_or_transferred"
```

### Minimum Viable Training Data

The key constraint: **enough real players to generate meaningful training data**.

```yaml
training_data_requirements:
  minimum_player_density:
    description: "Below this, interactions are too sparse for quality data"
    per_instance:
      ancient: 2000                 # Minimum real players
      classical: 5000
      medieval: 3000
      renaissance: 6000
      industrial: 10000
      modern: 20000
      ai_era: 10000

  interaction_thresholds:
    player_to_player:
      minimum_daily: 10             # Each player should interact with 10+ others
      target_daily: 25

    decision_points:
      minimum_per_session: 5        # Meaningful choices per play session
      target_per_session: 15

    group_activities:
      minimum_participation: 0.30   # 30% of players in group activities
      target_participation: 0.60

  data_quality_triggers:
    # If metrics fall below these, consider instance merge
    interaction_rate_warning: 0.5   # 50% of target
    interaction_rate_critical: 0.3  # 30% of target = merge

    novelty_score_warning: 0.4      # Data becoming repetitive
    novelty_score_critical: 0.2     # Urgent: not enough novel behavior
```

### Instance Economics

```yaml
instance_economics:
  # Economies are instance-local but currency is global

  currency:
    nvt: "global"                   # Novelty tokens work everywhere
    local_currency: "instance_specific"  # Era-appropriate money

  markets:
    scope: "instance_local"         # Can't trade Sumer-001 grain to Sumer-047
    exception: "reincarnation_auctions"  # Cross-instance when transitioning

  scarcity:
    per_instance: true              # Each Sumer has its own 20 communities max
    total_supply: "instances × per_instance_limit"

  arbitrage_prevention:
    transfer_costs: "high"          # Moving between instances costs NVT
    asset_conversion: "auction_required"
    cooldowns: "prevent_rapid_flipping"
```

---

## The Great Filter: A Meritocratic Journey

### The Three Phases of Civilization

The Analog Economy isn't just a game—it's a **meritocratic vetting system** that identifies players with the cognitive patterns, behavioral resilience, and collaborative intelligence that enterprises need to train their AI systems.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          THE GREAT FILTER                                    │
│                  "Prove your worth through the ages"                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PHASE 1: THE FILTER (Ancient → Medieval)                                   │
│  ═══════════════════════════════════════                                    │
│  • 80% of players wash out                                                  │
│  • Purpose: Weed out griefers, bots, low-engagement players                 │
│  • Survivors demonstrate: Patience, problem-solving, commitment             │
│  • Data quality: Moderate (high volume, filtering signal from noise)        │
│                                                                             │
│  PHASE 2: THE CRUCIBLE (Industrial → Modern)                                │
│  ═══════════════════════════════════════════                                │
│  • Grinders stay, only top 5% ascend                                        │
│  • Purpose: Identify elite problem-solvers                                  │
│  • Survivors demonstrate: Strategic thinking, adaptability, leadership      │
│  • Data quality: High (refined behavioral patterns)                         │
│                                                                             │
│  PHASE 3: THE DESTINATION (AI Era / Biomes)                                 │
│  ═════════════════════════════════════════                                  │
│  • Elite tier—the cream of the cream                                        │
│  • Purpose: Generate highest-fidelity training data                         │
│  • Participants: Proven intellects solving future problems                  │
│  • Data quality: Premium (enterprise-grade behavioral data)                 │
│                                                                             │
│  "The game is the interview. The data is the product."                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Why the Filter Matters

| Phase | Entry | Exit Rate | Data Value | Enterprise Buyers |
|-------|-------|-----------|------------|-------------------|
| **Phase 1: The Filter** | Everyone | 80% wash out | $0.001/action | Broad market research |
| **Phase 2: The Crucible** | 20% of starters | 75% of Phase 2 | $0.01/action | Decision modeling |
| **Phase 3: The Destination** | Top 5% overall | Ongoing elite | $0.10+/action | Premium AI training |

### The Economics of Merit

```yaml
great_filter_economics:
  phase_1_the_filter:
    entry: "Free to play / low barrier"
    duration: "Ancient through Medieval eras"
    player_experience:
      - "Learn basic mechanics"
      - "Discover if game resonates"
      - "Build initial reputation"
    exit_reasons:
      - "Lack of engagement (natural churn)"
      - "Griefing behavior (Gaian enforcement)"
      - "Bot detection (automated removal)"
      - "Era timeout (didn't solve keystones)"
    data_value: "High volume, moderate quality"
    monetization: "Ads, cosmetics, convenience items"

  phase_2_the_crucible:
    entry: "Survived The Filter"
    duration: "Industrial through Modern eras"
    player_experience:
      - "Complex strategic challenges"
      - "High-stakes asset management"
      - "Community leadership opportunities"
    advancement_criteria:
      - "Solve era-defining problems"
      - "Maintain positive reputation"
      - "Demonstrate collaborative intelligence"
    data_value: "Refined behavioral patterns"
    monetization: "Premium features, asset marketplace"

  phase_3_the_destination:
    entry: "Top 5% of all players"
    duration: "AI Era and beyond"
    player_experience:
      - "Elite challenges based on current events"
      - "Direct influence on game content"
      - "Highest rewards and recognition"
    data_value: "Premium AI training data"
    monetization: "Enterprise data licensing, B2B contracts"
```

### Founder's Generation: The Alpha Cohort

Before the public launch, a **Founder's Generation** of players will generate the initial training data that proves the concept to enterprise buyers.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     FOUNDER'S GENERATION (ALPHA COHORT)                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PURPOSE: Bootstrap the Biomes with high-quality initial data               │
│                                                                             │
│  SELECTION CRITERIA:                                                        │
│  ├── Invited testers and early community members                            │
│  ├── Demonstrated engagement during beta periods                            │
│  ├── Diversity of backgrounds and problem-solving approaches                │
│  └── Commitment to providing feedback and iterating                         │
│                                                                             │
│  BENEFITS:                                                                  │
│  ├── Lifetime "Founder" status and recognition                              │
│  ├── Permanent bonus to NVT earnings (10-25%)                               │
│  ├── First access to new content and features                               │
│  ├── Governance rights in game development decisions                        │
│  └── Genesis Reincarnation Tickets (limited supply)                         │
│                                                                             │
│  RESPONSIBILITIES:                                                          │
│  ├── Play through all Biomes, generating initial data                       │
│  ├── Provide detailed feedback on game mechanics                            │
│  ├── Help identify bugs, exploits, and balance issues                       │
│  └── Seed the community culture and norms                                   │
│                                                                             │
│  "The Founders don't just play the game—they shape it."                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

```yaml
alpha_cohort:
  size: "1,000-5,000 initial players"
  duration: "6-12 months before public launch"

  deliverables:
    - "Validated gameplay loops for all Biomes"
    - "Initial training dataset for enterprise demos"
    - "Community guidelines and culture established"
    - "Economy balance tested and refined"

  founder_rewards:
    genesis_tickets:
      description: "First-ever Reincarnation Tickets"
      quantity_per_founder: 3
      tradeable: true
      permanent_value: "Historical significance"

    founder_badge:
      description: "Permanent in-game recognition"
      effects: ["Cosmetic distinction", "Trust signal", "Beta access"]

    governance_tokens:
      description: "Vote on game development"
      weight: "Proportional to contribution"

    nvt_multiplier:
      base_bonus: 0.15  # 15% bonus on all earnings
      duration: "Lifetime"
```

---

## One Engine, Many Games

### Unified Mechanics Across Eras

The genius of The Analog Economy is that **the same mechanics power every era**. The skills you learn in Ancient Sumer transfer to Medieval Europe to the AI-driven Biomes.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      ONE ENGINE, MANY GAMES                                  │
│            "Dig a hole in Sumer. Dig a hole on Mars. Same dig."             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CORE MECHANIC: RESOURCE EXTRACTION                                         │
│  ├── Ancient: Dig irrigation canals by hand                                 │
│  ├── Medieval: Dig mine shafts with picks                                   │
│  ├── Industrial: Operate steam-powered excavators                           │
│  ├── Modern: Deploy automated mining equipment                              │
│  └── AI Era: Program AI-driven resource harvesters                          │
│                                                                             │
│  THE MECHANIC IS THE SAME. THE ASSETS CHANGE.                               │
│                                                                             │
│  CORE MECHANIC: TRADE                                                       │
│  ├── Ancient: Barter grain for bronze at the temple market                  │
│  ├── Medieval: Negotiate with guild merchants                               │
│  ├── Industrial: Place orders via telegraph                                 │
│  ├── Modern: Execute transactions on global exchanges                       │
│  └── AI Era: Algorithmic trading with AI counterparties                     │
│                                                                             │
│  CORE MECHANIC: COMMUNITY BUILDING                                          │
│  ├── Ancient: Convince tribes to settle together                            │
│  ├── Medieval: Attract serfs to your manor                                  │
│  ├── Industrial: Recruit workers to your factory town                       │
│  ├── Modern: Build online communities and networks                          │
│  └── AI Era: Coordinate human-AI collaborative teams                        │
│                                                                             │
│  CORE MECHANIC: SURVIVAL                                                    │
│  ├── Ancient: Find food, water, shelter                                     │
│  ├── Medieval: Same, plus avoid plague                                      │
│  ├── Industrial: Same, plus navigate urban dangers                          │
│  ├── Modern: Same, plus manage information overload                         │
│  └── AI Era: Same, plus coexist with artificial intelligence                │
│                                                                             │
│  "Master the engine once. Apply it forever."                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Mechanic Mapping

```yaml
unified_mechanics:
  # The same player skills apply across all eras
  # Only the context and assets change

  resource_management:
    description: "Gather, store, allocate limited resources"
    ancient: "Grain, water, bronze"
    medieval: "Food, wool, iron"
    industrial: "Coal, steel, capital"
    modern: "Data, energy, attention"
    ai_era: "Compute, bandwidth, trust"
    training_data: "How humans prioritize under scarcity"

  social_coordination:
    description: "Organize groups for collective action"
    ancient: "Tribal councils, temple hierarchies"
    medieval: "Feudal obligations, guild rules"
    industrial: "Unions, corporations, governments"
    modern: "Networks, platforms, movements"
    ai_era: "Human-AI teams, distributed orgs"
    training_data: "How humans build and maintain cooperation"

  risk_assessment:
    description: "Evaluate threats and opportunities"
    ancient: "Read weather, watch for raiders"
    medieval: "Avoid plague routes, assess lord's mood"
    industrial: "Market analysis, labor conditions"
    modern: "Information filtering, threat modeling"
    ai_era: "AI behavior prediction, system vulnerabilities"
    training_data: "How humans process uncertainty"

  innovation:
    description: "Create new solutions to problems"
    ancient: "Invent irrigation, develop writing"
    medieval: "Improve farming, build better tools"
    industrial: "Engineer machines, optimize processes"
    modern: "Software, biotech, new materials"
    ai_era: "Human-AI collaborative creation"
    training_data: "How humans generate novel solutions"

  conflict_resolution:
    description: "Navigate disputes and competition"
    ancient: "Negotiate water rights, settle blood feuds"
    medieval: "Mediate lord disputes, guild conflicts"
    industrial: "Labor negotiations, market competition"
    modern: "Legal systems, diplomatic relations"
    ai_era: "Human-AI boundaries, resource allocation"
    training_data: "How humans resolve disagreements"

benefits:
  for_players:
    - "Skills transfer across eras—never start from zero"
    - "Intuitive progression—same core loops"
    - "Deep mastery rewarded—nuances compound"

  for_training_data:
    - "Consistent behavioral signatures across contexts"
    - "Isolate what changes (technology) from what doesn't (human nature)"
    - "Cross-era patterns reveal timeless strategies"

  for_development:
    - "One codebase, many experiences"
    - "New eras = new assets, not new systems"
    - "Balance once, apply everywhere"
```

---

## Era Progression Mechanics

### Advancing Through Time

```
┌─────────────────────────────────────────────────────────────┐
│                  ERA PROGRESSION                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Within Each Era:                                           │
│  ├── Survive initial challenges                             │
│  ├── Master era-specific skills                             │
│  ├── Contribute to civilization milestones                  │
│  ├── Accumulate era achievements                            │
│  └── Trigger "Era Transition Event"                         │
│                                                             │
│  Era Transition:                                            │
│  ├── Major historical event occurs                          │
│  ├── Player witnesses civilization shift                    │
│  ├── Some items/skills carry forward                        │
│  ├── New technologies unlock                                │
│  └── New challenges emerge                                  │
│                                                             │
│  Persistence Across Eras:                                   │
│  ├── Reputation (modified by era context)                   │
│  ├── Certain "timeless" items (gold, gems)                  │
│  ├── Knowledge and skills (contextual)                      │
│  └── Family/bloodline (optional mechanic)                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Era Milestones

Each era has civilization milestones that players contribute to:

```yaml
era_milestones:
  ancient:
    - "First irrigation system"
    - "Writing invented"
    - "Bronze tools widespread"
    - "First legal code"
    - "Monumental architecture"

  classical:
    - "Democracy experiments"
    - "Philosophy schools"
    - "Engineering marvels"
    - "Trade networks"
    - "Military innovations"

  medieval:
    - "Feudal systems"
    - "Religious institutions"
    - "Guild formation"
    - "Agricultural advances"
    - "Surviving the plague"

  renaissance:
    - "Scientific method"
    - "Printing press adoption"
    - "New world exploration"
    - "Banking systems"
    - "Artistic flourishing"

  industrial:
    - "Factory systems"
    - "Labor movements"
    - "Urban migration"
    - "Railway networks"
    - "Mass production"

  modern:
    - "World wars survival"
    - "Space race"
    - "Digital revolution"
    - "Globalization"
    - "Climate awareness"

  ai_era:
    - "The 10 Biomes"  # Our existing biome system
```

---

## Ancient Era: The Cradle

### Setting: Mesopotamia, Egypt, Indus Valley (4000-500 BCE)

```
┌─────────────────────────────────────────────────────────────┐
│                    ANCIENT ERA                              │
│               "The Dawn of Civilization"                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Starting Location: Village near Euphrates River            │
│                                                             │
│  Core Challenges:                                           │
│  ├── FLOODING: Rivers flood unpredictably                   │
│  ├── FAMINE: Crops fail without irrigation                  │
│  ├── RAIDERS: Nomadic groups attack settlements             │
│  ├── DISEASE: No understanding of medicine                  │
│  └── GOVERNANCE: How to organize beyond tribes              │
│                                                             │
│  Available Technology:                                      │
│  ├── Stone and bronze tools                                 │
│  ├── Basic agriculture                                      │
│  ├── Domesticated animals                                   │
│  ├── Simple construction (mud brick)                        │
│  └── Early writing (cuneiform)                              │
│                                                             │
│  Training Data Value:                                       │
│  "How do humans build civilization from scratch?"           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Ancient Era Challenges

```yaml
ancient_challenges:
  the_flood:
    description: "Annual river flooding destroys crops and homes"
    solutions:
      primitive: "Move to higher ground (loses everything)"
      intermediate: "Build levees (requires coordination)"
      advanced: "Irrigation canals (redirects water productively)"
    training_data: "Infrastructure planning under uncertainty"

  the_famine:
    description: "Drought or pest destroys harvest"
    solutions:
      primitive: "Forage and hunt (individual survival)"
      intermediate: "Grain storage (requires planning)"
      advanced: "Trade networks (requires trust)"
    training_data: "Resource management, social cooperation"

  the_raiders:
    description: "Nomadic groups attack your settlement"
    solutions:
      primitive: "Hide or flee"
      intermediate: "Walls and watchtowers"
      advanced: "Diplomacy, tribute, or alliance"
    training_data: "Defense strategies, negotiation"

  the_plague:
    description: "Unknown illness spreads through village"
    solutions:
      primitive: "Blame spirits, exile sick"
      intermediate: "Quarantine (accidental discovery)"
      advanced: "Herbal remedies, clean water"
    training_data: "Disease response without modern knowledge"

  the_succession:
    description: "Leader dies, who rules now?"
    solutions:
      primitive: "Strongest takes over (violence)"
      intermediate: "Council of elders"
      advanced: "Written laws, hereditary rules"
    training_data: "Governance formation"
```

### Ancient Era Economy

```yaml
ancient_economy:
  currency:
    primary: "Barter (grain, livestock)"
    emerging: "Silver rings, clay tokens"
    tracking: "Cuneiform tablets"

  trade_goods:
    local: ["grain", "pottery", "textiles", "beer"]
    luxury: ["lapis lazuli", "cedar wood", "copper"]
    rare: ["tin", "gold", "obsidian"]

  property:
    land: "Communal → Temple → Private (evolution)"
    livestock: "Personal wealth marker"
    slaves: "Captured enemies, debt bondage"

  professions:
    farmer: "Most common, backbone of society"
    craftsman: "Potters, weavers, smiths"
    priest: "Intermediary with gods, literate"
    scribe: "Record keepers, valuable skill"
    merchant: "Long-distance traders"
    soldier: "Protectors, raiders"
```

---

## Classical Era: Empires

### Setting: Greece, Rome, Persia, Han China (500 BCE - 500 CE)

```
┌─────────────────────────────────────────────────────────────┐
│                   CLASSICAL ERA                             │
│                "The Age of Empires"                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Starting Locations:                                        │
│  ├── Athens: Democracy, philosophy, trade                   │
│  ├── Rome: Military, engineering, law                       │
│  ├── Persia: Administration, tolerance, roads               │
│  └── Chang'an: Bureaucracy, silk, invention                 │
│                                                             │
│  Core Challenges:                                           │
│  ├── POLITICS: Navigate complex power structures            │
│  ├── WARFARE: Empires expand and clash                      │
│  ├── SLAVERY: Ubiquitous, morally complex                   │
│  ├── CITIZENSHIP: Rights and responsibilities               │
│  └── DECLINE: Empires fall, what survives?                  │
│                                                             │
│  Available Technology:                                      │
│  ├── Iron tools and weapons                                 │
│  ├── Roads and aqueducts                                    │
│  ├── Advanced architecture (concrete, arches)               │
│  ├── Written philosophy and law                             │
│  └── Military formations and siege warfare                  │
│                                                             │
│  Training Data Value:                                       │
│  "How do humans scale organization? What causes collapse?"  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Classical Era Challenges

```yaml
classical_challenges:
  the_forum:
    description: "Political debate determines city's future"
    solutions:
      rhetoric: "Persuade through speech"
      bribery: "Buy votes and influence"
      populism: "Appeal to masses"
      force: "Intimidate opposition"
    training_data: "Political strategy, persuasion"

  the_legion:
    description: "Called to military service"
    solutions:
      serve: "Fight, possibly die, gain citizenship"
      avoid: "Bribery, exemption, exile"
      excel: "Rise through ranks"
      desert: "Risk execution"
    training_data: "Duty, survival, institutional pressure"

  the_slave_question:
    description: "Your neighbor offers to sell you slaves"
    moral_complexity: "Historically accurate ethical dilemma"
    solutions:
      accept: "Economic advantage (era-normal)"
      decline: "Philosophical objection (rare)"
      free: "Manumission (possible in Rome)"
    training_data: "Moral decisions in historical context"
    gaian_note: "Present without glorifying; capture player reasoning"

  the_fall:
    description: "Empire is collapsing, what do you save?"
    solutions:
      flee: "Take what you can, find safety"
      fight: "Defend to the end"
      adapt: "Negotiate with invaders"
      preserve: "Hide knowledge for future"
    training_data: "Civilizational collapse response"
```

---

## Medieval Era: Survival & Faith

### Setting: Europe, Middle East, Asia (500 CE - 1400 CE)

```
┌─────────────────────────────────────────────────────────────┐
│                   MEDIEVAL ERA                              │
│              "The Age of Faith and Survival"                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Starting Locations:                                        │
│  ├── Feudal Manor: Peasant life, lord's protection          │
│  ├── Monastery: Learning, brewing, copying texts            │
│  ├── Guild Town: Crafts, trade, emerging middle class       │
│  ├── Crusader States: Religious warfare, cultural clash     │
│  └── Silk Road: Trade caravans, cultural exchange           │
│                                                             │
│  Core Challenges:                                           │
│  ├── THE PLAGUE: Black Death kills 1/3 of population        │
│  ├── FEUDALISM: Bound to the land, limited mobility         │
│  ├── FAITH: Church dominates all aspects of life            │
│  ├── WARFARE: Constant local conflicts, crusades            │
│  └── FAMINE: Poor harvests, no reserves                     │
│                                                             │
│  Available Technology:                                      │
│  ├── Heavy plow, three-field rotation                       │
│  ├── Watermills, windmills                                  │
│  ├── Castle construction                                    │
│  ├── Guilds and apprenticeship                              │
│  └── Early gunpowder (late period)                          │
│                                                             │
│  Training Data Value:                                       │
│  "How do humans survive institutional collapse?"            │
│  "What role does faith play in crisis?"                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### The Black Death Challenge

```yaml
black_death:
  description: "The plague has reached your region"
  mortality_rate: "30-60% of population"

  symptoms_progression:
    day_1: "Fever, chills, weakness"
    day_2: "Buboes appear (swollen lymph nodes)"
    day_3_4: "Hemorrhaging, delirium"
    day_5_7: "Death (if untreated, ~70% mortality)"

  response_options:
    flee:
      description: "Leave the infected area"
      effectiveness: "High if early, low if late"
      consequences: "Spread plague to new areas"

    quarantine:
      description: "Isolate the sick"
      effectiveness: "Moderate"
      consequences: "Ethical dilemmas (family abandonment)"

    flagellation:
      description: "Religious penance to appease God"
      effectiveness: "None (historical accuracy)"
      social_impact: "Community cohesion or scapegoating"

    medicine:
      description: "Herbal remedies, bloodletting"
      effectiveness: "Minimal (historical)"
      knowledge: "Plant-based palliatives help"

    burn_the_dead:
      description: "Prevent corpse transmission"
      effectiveness: "Helpful (accidentally correct)"
      consequences: "Religious objections"

  training_data_value:
    captures: "Pandemic response without modern knowledge"
    valuable_for: "CDC, WHO behavioral modeling"
    historical_parallel: "Direct relevance to modern pandemics"
```

---

## Renaissance Era: Discovery

### Setting: Europe, Americas, Global Trade Routes (1400 CE - 1750 CE)

```
┌─────────────────────────────────────────────────────────────┐
│                  RENAISSANCE ERA                            │
│              "The Age of Discovery"                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Starting Locations:                                        │
│  ├── Florence: Art, banking, intrigue                       │
│  ├── Lisbon: Exploration, navigation, trade                 │
│  ├── Amsterdam: Commerce, tolerance, finance                │
│  ├── New World: Colonization, indigenous encounter          │
│  └── Ottoman Empire: Crossroads of civilizations            │
│                                                             │
│  Core Challenges:                                           │
│  ├── EXPLORATION: Unknown lands, navigation hazards         │
│  ├── COLONIZATION: Ethical nightmares, resource extraction  │
│  ├── REFORMATION: Religious wars tear Europe apart          │
│  ├── SCIENCE vs FAITH: New ideas clash with doctrine        │
│  └── FINANCE: Banking, debt, economic bubbles               │
│                                                             │
│  Available Technology:                                      │
│  ├── Printing press (information revolution)                │
│  ├── Advanced sailing (caravels, navigation)                │
│  ├── Gunpowder weapons (muskets, cannons)                   │
│  ├── Scientific instruments (telescope, microscope)         │
│  └── Early manufacturing                                    │
│                                                             │
│  Training Data Value:                                       │
│  "How do humans handle paradigm shifts?"                    │
│  "What happens when civilizations collide?"                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Industrial Era: Revolution

### Setting: Britain, America, Europe (1750 CE - 1900 CE)

```
┌─────────────────────────────────────────────────────────────┐
│                  INDUSTRIAL ERA                             │
│              "The Age of Revolution"                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Starting Locations:                                        │
│  ├── Manchester: Factory life, labor struggle               │
│  ├── New York: Immigration, opportunity, tenements          │
│  ├── Paris: Revolution, upheaval, ideas                     │
│  ├── American Frontier: Expansion, displacement             │
│  └── Colonial Outpost: Empire's edge, extraction            │
│                                                             │
│  Core Challenges:                                           │
│  ├── LABOR: 16-hour days, child labor, no rights            │
│  ├── URBANIZATION: Slums, disease, crime                    │
│  ├── REVOLUTION: Political upheaval, class conflict         │
│  ├── IMPERIALISM: Global exploitation, resistance           │
│  └── TECHNOLOGY: Rapid change, skill obsolescence           │
│                                                             │
│  Available Technology:                                      │
│  ├── Steam power (engines, railways, ships)                 │
│  ├── Factories and mass production                          │
│  ├── Telegraph and early communication                      │
│  ├── Modern medicine emerging                               │
│  └── Photography, early electrical experiments              │
│                                                             │
│  Training Data Value:                                       │
│  "How do humans adapt to technological displacement?"       │
│  "What sparks revolutionary change?"                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Modern Era: Complexity

### Setting: Global (1900 CE - 2020 CE)

```
┌─────────────────────────────────────────────────────────────┐
│                    MODERN ERA                               │
│              "The Age of Extremes"                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Key Periods:                                               │
│  ├── World Wars (1914-1945): Total war, genocide            │
│  ├── Cold War (1945-1991): Nuclear fear, proxy wars         │
│  ├── Digital Revolution (1990-2020): Internet, globalization│
│  └── Climate Awakening (2000-2020): Environmental crisis    │
│                                                             │
│  Core Challenges:                                           │
│  ├── TOTAL WAR: Survive world conflicts                     │
│  ├── NUCLEAR: Cold War tensions, MAD doctrine               │
│  ├── TECHNOLOGY: Computing, automation, obsolescence        │
│  ├── GLOBALIZATION: Connected world, inequality             │
│  └── CLIMATE: Growing environmental crisis                  │
│                                                             │
│  Available Technology:                                      │
│  ├── Electricity, automobiles, aviation                     │
│  ├── Nuclear power (and weapons)                            │
│  ├── Computers, internet, smartphones                       │
│  ├── Modern medicine, vaccines                              │
│  └── Early AI and automation                                │
│                                                             │
│  Training Data Value:                                       │
│  "How do humans handle existential risks?"                  │
│  "What happens with information abundance?"                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## AI Era: The Biomes

### Setting: Near Future / Present (2020 CE - Present)

This is where our **existing biome system** lives:

| Biome | Theme | Historical Continuity |
|-------|-------|----------------------|
| The Abyss | Deep Ocean | Humanity reaches into new frontiers |
| The Scorch | Mars/Desert | Expansion beyond Earth |
| The Ruins | Disaster | Climate disasters intensify |
| The Aqua | Water Scarcity | Ancient irrigation → modern crisis |
| The Botany | Food Security | Agriculture's future |
| The Theater | Geopolitics | Wars continue, new forms |
| The Exodus | Migration | Human movement, eternal pattern |
| The Brink | Nuclear | Cold War never ended |
| The Vector | Bio-Warfare | Plague returns, weaponized |
| The Uprising | Man vs Machine | New frontier of conflict |

**Training Data Value:** This is where players apply all historical learning to current/future problems.

---

## Living Future: Current Events

### The Game That Never Ends

```yaml
living_future:
  description: "Game content updates with real-world events"

  content_sources:
    news_integration:
      description: "Major world events become challenges"
      delay: "1-4 weeks (ethical review period)"
      examples:
        - "Earthquake in X → Disaster response scenario"
        - "Political crisis in Y → Diplomacy challenge"
        - "Tech breakthrough → New tools available"

    community_proposals:
      description: "Players suggest scenarios"
      voting: "Community votes on additions"
      reward: "Proposers earn if scenario approved"

    expert_partnerships:
      description: "Work with NGOs, governments for realistic scenarios"
      partners: ["FEMA", "Red Cross", "UN agencies"]
      benefit: "Training data directly useful to partners"

  ethical_guardrails:
    delay_period: "Minimum time before sensitive events become content"
    no_exploitation: "Recent tragedies not gamified insensitively"
    educational_framing: "Context and learning emphasized"
    gaian_review: "Ethics filter on all new content"

  example_events_to_scenarios:
    pandemic: "The Vector biome updates"
    climate_disaster: "The Aqua, Scorch, Ruins update"
    political_instability: "The Theater, Exodus update"
    tech_breakthrough: "New tools, new challenges"
    space_exploration: "The Scorch expands"
```

### Seasonal Content

```yaml
seasonal_updates:
  quarterly_events:
    description: "Major content updates every 3 months"
    includes:
      - "New challenges based on recent events"
      - "Historical era expansions"
      - "Community-created content featured"

  annual_themes:
    description: "Yearly focus areas"
    examples:
      - "2027: Year of Water Crisis"
      - "2028: Year of Space Expansion"
      - "2029: Year of AI Coexistence"

  historical_anniversaries:
    description: "Commemorate historical events"
    examples:
      - "100 years since X → Special challenge"
      - "Ancient event anniversary → Era highlight"
```

---

## Training Data Across Time

### The Ultimate Dataset

```
┌─────────────────────────────────────────────────────────────┐
│           CROSS-ERA TRAINING DATA VALUE                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  TIMELESS PATTERNS (Same across all eras):                  │
│  ├── Trust and cooperation emergence                        │
│  ├── Leadership and governance formation                    │
│  ├── Resource allocation under scarcity                     │
│  ├── Conflict resolution strategies                         │
│  ├── Family and community bonds                             │
│  └── Innovation and problem-solving                         │
│                                                             │
│  ERA-SPECIFIC PATTERNS:                                     │
│  ├── How technology changes strategy                        │
│  ├── What solutions work only in context                    │
│  ├── How scale affects organization                         │
│  └── What causes civilizational collapse                    │
│                                                             │
│  EVOLUTION TRACKING:                                        │
│  ├── Same problems, different solutions across eras         │
│  ├── What persists vs. what changes                         │
│  ├── Human nature constants                                 │
│  └── Progress patterns and setbacks                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Data Categories by Era

| Era | Primary Data Value | Enterprise Buyers |
|-----|-------------------|-------------------|
| Ancient | Civilization building, basic survival | City planners, development orgs |
| Classical | Governance, empire management | Political scientists, governments |
| Medieval | Crisis survival, institutional collapse | Disaster response, NGOs |
| Renaissance | Innovation adoption, paradigm shifts | R&D organizations |
| Industrial | Labor dynamics, technological change | Workforce planning |
| Modern | Complex systems, existential risk | Risk analysts, think tanks |
| AI Era | Future challenges | Tech companies, governments |
| Living Future | Current events | Real-time applicability |

---

## Reincarnation Mechanics

### The Path Forward

Players don't simply "complete" an era—they must **solve the defining problems of their time** to earn the right to reincarnate into the next era.

**But there's a catch:** Solving the problems isn't enough. You also need a **Reincarnation Ticket**.

---

## Reincarnation Tickets: The Bottleneck Economy

### Limited Supply, Infinite Demand

Reincarnation Tickets are **NFTs with capped supply**. They are the key that unlocks era transitions—and they create the scarcity that makes progression meaningful.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      REINCARNATION TICKET ECONOMY                            │
│                   "The right to advance must be earned"                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  WHAT IS A REINCARNATION TICKET?                                            │
│  ├── An NFT that grants ONE era transition                                  │
│  ├── Consumed on use (burned from supply)                                   │
│  ├── Tradeable on the marketplace                                           │
│  └── The ONLY way to advance to the next era                                │
│                                                                             │
│  SUPPLY MODEL:                                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │  Phase 1 → Phase 2:  10,000 tickets ever minted                       │ │
│  │  Phase 2 → Phase 3:   2,000 tickets ever minted                       │ │
│  │  Genesis Tickets:       500 tickets (Founder's Generation only)       │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│  ACQUISITION METHODS:                                                       │
│  ├── EARN: Complete exceptional achievements (rare drops)                   │
│  ├── BUY: Purchase from marketplace (player-to-player)                     │
│  ├── WIN: Tournament rewards, special events                               │
│  └── MINT: Platform releases new supply (governance-controlled)            │
│                                                                             │
│  PRICE DYNAMICS:                                                            │
│  • Early game: Tickets affordable (low demand, fresh supply)               │
│  • Mid game: Prices rise as supply depletes and demand grows               │
│  • Late game: Tickets become status symbols and investments                 │
│                                                                             │
│  "Everyone can play. Not everyone can ascend."                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Ticket Economics

```yaml
reincarnation_tickets:
  ticket_types:
    phase_1_to_2:
      name: "Ascension Ticket"
      description: "Graduate from The Filter to The Crucible"
      total_supply: 10000
      burn_on_use: true
      initial_price: "100 NVT"
      expected_floor: "500-2000 NVT at maturity"

    phase_2_to_3:
      name: "Destination Ticket"
      description: "Graduate from The Crucible to The Destination"
      total_supply: 2000
      burn_on_use: true
      initial_price: "1000 NVT"
      expected_floor: "5000-20000 NVT at maturity"

    genesis:
      name: "Genesis Ticket"
      description: "Founder's Generation exclusive"
      total_supply: 500
      burn_on_use: true
      tradeable: true
      special: "Works for ANY phase transition"
      collectible_value: "Historical significance"

  acquisition_methods:
    achievement_drops:
      description: "Exceptional play rewards tickets"
      rate: "~1 ticket per 10,000 player-hours of elite play"
      criteria:
        - "Complete all keystone challenges in record time"
        - "Achieve max reputation in era"
        - "Lead community to major milestone"
        - "Innovative problem solution (Gaian-recognized)"

    marketplace_purchase:
      description: "Buy from other players"
      fees: "5% platform fee on all sales"
      price_discovery: "Auction and fixed-price listings"

    tournament_rewards:
      description: "Win competitive events"
      events:
        - "Seasonal championships"
        - "Era-specific challenges"
        - "Cross-era olympics"

    special_events:
      description: "Limited-time opportunities"
      events:
        - "Anniversary celebrations"
        - "Partnership promotions"
        - "Community milestones"

  supply_governance:
    minting_authority: "DAO vote required for new supply"
    inflation_cap: "Max 5% annual supply increase"
    burn_mechanism: "Every use permanently removes from supply"
    deflationary: true

  anti_speculation_measures:
    holding_limit: "Max 10 tickets per wallet"
    cooldown: "30-day cooldown after purchase before resale"
    utility_focus: "Primary value is USE, not hoarding"
```

### Why Tickets Create Better Gameplay

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                  WHY THE TICKET SYSTEM WORKS                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  FOR PLAYERS:                                                               │
│  ├── Clear goal: "I need to earn/buy a ticket to advance"                  │
│  ├── Meaningful choice: "Do I rush for a ticket or build wealth first?"    │
│  ├── Status signal: "Ticket holders have proven their worth"               │
│  └── Investment opportunity: "Tickets may appreciate in value"             │
│                                                                             │
│  FOR THE ECOSYSTEM:                                                         │
│  ├── Scarcity drives engagement: Players work harder to qualify            │
│  ├── Economy circulation: NVT flows through ticket marketplace             │
│  ├── Quality filter: Only committed players reach elite tiers              │
│  └── Deflationary pressure: Burned tickets reduce supply over time         │
│                                                                             │
│  FOR DATA QUALITY:                                                          │
│  ├── Elite tiers guaranteed quality: Ticket cost = commitment filter       │
│  ├── Long-term players prioritized: Can't speedrun to premium data         │
│  ├── Diverse strategies: Some earn, some buy, some wait                    │
│  └── Natural segmentation: Phase clearly separates player cohorts          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Ticket + Keystone Requirements

To reincarnate, players must have BOTH:

```yaml
reincarnation_requirements:
  phase_1_to_2:
    keystones_required: 2          # From Ancient, Classical, or Medieval
    ticket_required: "Ascension Ticket"
    asset_auction: "Required if holding non-portable assets"
    reputation_minimum: 0.5        # At least neutral standing

  phase_2_to_3:
    keystones_required: 2          # From Industrial or Modern
    ticket_required: "Destination Ticket"
    asset_auction: "Required"
    reputation_minimum: 0.7        # Good standing required
    special_criteria:
      - "At least one community leadership role"
      - "Positive contribution to at least 3 other players"

  within_phase_transitions:
    # Moving between eras WITHIN a phase doesn't require tickets
    # Ancient → Classical → Medieval (all Phase 1, ticket-free)
    # Industrial → Modern (Phase 2, ticket-free within phase)
    keystones_required: 2
    ticket_required: false
    asset_handling: "Auction optional, can carry some items"
```

---

### The Reincarnation Cycle (Updated)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         REINCARNATION CYCLE                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                  │
│  │   SURVIVE    │    │    BUILD     │    │    SOLVE     │                  │
│  │              │ ─▶ │              │ ─▶ │              │                  │
│  │ Master basic │    │ Establish    │    │ Crack era's  │                  │
│  │ era survival │    │ your legacy  │    │ key problems │                  │
│  └──────────────┘    └──────────────┘    └──────────────┘                  │
│         │                   │                   │                           │
│         ▼                   ▼                   ▼                           │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                  │
│  │   Food       │    │  Community   │    │  The Flood   │                  │
│  │   Shelter    │    │  Farm        │    │  The Plague  │                  │
│  │   Safety     │    │  Shop        │    │  The War     │                  │
│  │   Health     │    │  Workshop    │    │  The Crisis  │                  │
│  └──────────────┘    └──────────────┘    └──────────────┘                  │
│                                                 │                           │
│                                                 ▼                           │
│                                    ┌──────────────────────┐                │
│                                    │    REINCARNATE       │                │
│                                    │                      │                │
│                                    │  Auction your goods  │                │
│                                    │  Carry forward gold  │                │
│                                    │  Begin next era      │                │
│                                    └──────────────────────┘                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Era-Defining Problems

Each era has **Keystone Challenges**—problems that shaped human history. Players must contribute meaningfully to solving these:

```yaml
keystone_challenges:
  ancient:
    challenges:
      - "the_great_flood"         # Build irrigation that saves the city
      - "the_first_laws"          # Help establish fair governance
      - "the_bronze_secret"       # Discover/spread metallurgy
    required_to_advance: 2        # Must solve at least 2

  classical:
    challenges:
      - "the_democratic_experiment"  # Make governance work
      - "the_road_network"           # Infrastructure that connects
      - "the_fall_prevention"        # Delay the collapse
    required_to_advance: 2

  medieval:
    challenges:
      - "the_black_death"         # Survive and help others survive
      - "the_knowledge_preservation"  # Save texts from destruction
      - "the_guild_formation"     # Organize labor for mutual benefit
    required_to_advance: 2

  renaissance:
    challenges:
      - "the_printing_revolution"  # Spread knowledge
      - "the_new_world_ethics"     # Navigate colonization morally
      - "the_scientific_method"    # Establish evidence-based thinking
    required_to_advance: 2

  industrial:
    challenges:
      - "the_labor_rights"         # Fight for worker dignity
      - "the_urban_health"         # Clean water, sanitation
      - "the_displacement"         # Help those made obsolete
    required_to_advance: 2

  modern:
    challenges:
      - "the_world_wars"           # Survive, resist, rebuild
      - "the_nuclear_dilemma"      # Navigate MAD without destruction
      - "the_digital_divide"       # Technology for all
    required_to_advance: 2
```

---

## Era Scarcity Constraints

### Limited World, Limited Opportunities

Just as in real history, **not everyone can own land**. Each era has hard caps on player-owned assets, reflecting historical scarcity.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       ERA SCARCITY MODEL                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  "The world has limits. So does each era."                                  │
│                                                                             │
│  Per Server Instance (10,000 active players):                               │
│                                                                             │
│  ┌─────────────┬───────────┬─────────┬─────────┬──────────┬─────────┐      │
│  │    Era      │Communities│  Farms  │  Shops  │Workshops │ Estates │      │
│  ├─────────────┼───────────┼─────────┼─────────┼──────────┼─────────┤      │
│  │ Ancient     │     20    │   100   │   50    │    25    │    5    │      │
│  │ Classical   │     50    │   200   │   150   │    75    │   15    │      │
│  │ Medieval    │     75    │   300   │   200   │   150    │   25    │      │
│  │ Renaissance │    100    │   400   │   400   │   300    │   40    │      │
│  │ Industrial  │    150    │   200*  │   800   │   600    │   75    │      │
│  │ Modern      │    200    │   100*  │  1000   │   800    │  150    │      │
│  │ AI Era      │    250    │    50*  │  1200   │  1000    │  200    │      │
│  └─────────────┴───────────┴─────────┴─────────┴──────────┴─────────┘      │
│                                                                             │
│  * Farms decrease in later eras (urbanization, industrialized agriculture) │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Asset Types & Historical Accuracy

```yaml
player_owned_assets:
  community:
    description: "A settlement you founded or lead"
    max_members: "5-500 depending on era"
    requirements:
      ancient: "Claim unclaimed river land"
      classical: "Charter from authority or conquest"
      medieval: "Land grant or frontier settlement"
      renaissance: "Colonial charter or guild backing"
      industrial: "Corporate town or utopian experiment"
      modern: "Zoning approval or commune formation"
    value_drivers: ["population", "productivity", "strategic_location"]

  farm:
    description: "Agricultural land you cultivate"
    size_range: "1-1000 acres depending on era"
    requirements:
      ancient: "Clear and irrigate"
      classical: "Citizenship or slave labor"
      medieval: "Feudal obligation or freedom purchase"
      renaissance: "Enclosure or new world claim"
      industrial: "Mechanization investment"
      modern: "Agribusiness or organic niche"
    value_drivers: ["fertility", "water_access", "labor_efficiency"]

  shop:
    description: "Commercial establishment"
    types: ["general_store", "specialty", "tavern", "services"]
    requirements:
      ancient: "Temple district or market square access"
      classical: "Forum license or street corner"
      medieval: "Guild membership required"
      renaissance: "Merchant charter"
      industrial: "Storefront lease"
      modern: "Business license"
    value_drivers: ["location", "inventory", "reputation"]

  workshop:
    description: "Production facility"
    outputs: ["tools", "weapons", "textiles", "crafts"]
    requirements:
      ancient: "Master craftsman status"
      classical: "Apprentice-to-master progression"
      medieval: "Guild journeyman completion"
      renaissance: "Patent or trade secret"
      industrial: "Capital investment"
      modern: "Specialized equipment"
    value_drivers: ["output_quality", "efficiency", "uniqueness"]

  estate:
    description: "Large landholding with multiple functions"
    ultra_rare: true
    requirements: "Major contribution to era advancement"
    value_drivers: ["prestige", "diversification", "defensibility"]
```

### Acquiring Assets

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      ASSET ACQUISITION PATHS                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. CLAIM (Early eras, frontier areas)                                      │
│     └── Find unclaimed land, invest labor to develop                        │
│                                                                             │
│  2. PURCHASE (When available on market)                                     │
│     └── Buy from player leaving era or NPC                                  │
│                                                                             │
│  3. EARN (Rewards for keystone challenges)                                  │
│     └── Solve major era problem → land grant                                │
│                                                                             │
│  4. INHERIT (Bloodline mechanic if enabled)                                 │
│     └── Previous character's assets pass to new one                         │
│                                                                             │
│  5. CONQUER (Where era-appropriate)                                         │
│     └── Warfare, hostile takeover (high risk)                               │
│                                                                             │
│  6. AUCTION (Era transition events)                                         │
│     └── Bid on assets from reincarnating players                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Player-Owned Assets (Metaverse Layer)

### Real Value, Real Stakes

Player assets are **NFTs with real economic value**. Your medieval bakery has worth because:
- It generates income (NVT) while you play
- Limited supply (only 200 shops in Medieval era)
- Can be sold or auctioned when you reincarnate
- Carries historical provenance ("Founded in 1347, survived the Plague")

```yaml
asset_economics:
  income_generation:
    shop:
      passive_income: "1-10 NVT per day based on location/traffic"
      active_income: "5-50 NVT per transaction you facilitate"

    farm:
      harvest_income: "10-100 NVT per harvest cycle"
      cycle_length: "Era-dependent (weeks to months)"

    workshop:
      production_income: "Per item created and sold"
      efficiency_bonus: "Quality multipliers"

    community:
      tax_income: "Small % of member activity"
      milestone_bonuses: "Community achievements"

  appreciation:
    factors:
      - "Strategic location (trade routes, resources)"
      - "Historical significance (major events occurred here)"
      - "Improvements made (upgrades, expansions)"
      - "Reputation (famous products, notable customers)"

  valuation_formula: |
    Asset Value = Base Value
                  × Location Multiplier
                  × History Multiplier
                  × Improvement Multiplier
                  × Era Scarcity Factor
```

### Asset NFT Structure

```yaml
asset_nft:
  # Example: Medieval Bakery
  token_id: "ASSET-MEDIEVAL-SHOP-00142"
  type: "shop"
  subtype: "bakery"
  era: "medieval"

  location:
    region: "Florence"
    district: "Market Quarter"
    coordinates: [x, y]
    neighbors: ["blacksmith_00089", "tavern_00056"]

  history:
    founded: "Era Year 847 (1347 CE equivalent)"
    founded_by: "player_0x7a3f..."
    previous_owners:
      - owner: "player_0x7a3f..."
        from: "847"
        to: "862"
        events: ["Survived Black Death", "Supplied Medici"]

  current_state:
    condition: 0.85              # 85% condition
    upgrades: ["stone_oven", "expanded_storage"]
    reputation: 4.2              # Out of 5
    employees: 3                 # NPC workers

  economics:
    purchase_price: 500          # What current owner paid
    estimated_value: 1200        # Current market estimate
    daily_income: 8              # Average NVT/day
    monthly_expenses: 45         # Upkeep costs
```

---

## Era Timeout & Catastrophe Mechanics

### The Clock is Ticking

**You cannot stay in an era forever.** History marches on, and those who don't advance face consequences.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        ERA TIMEOUT MECHANICS                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Each era has a SOFT LIMIT and a HARD LIMIT:                                │
│                                                                             │
│  ┌─────────────┬────────────┬────────────┬──────────────────────────────┐  │
│  │    Era      │ Soft Limit │ Hard Limit │ What Happens                 │  │
│  ├─────────────┼────────────┼────────────┼──────────────────────────────┤  │
│  │ Ancient     │  60 days   │  90 days   │ Bronze Age Collapse          │  │
│  │ Classical   │  75 days   │  120 days  │ Fall of Rome                 │  │
│  │ Medieval    │  90 days   │  150 days  │ Black Death sweep            │  │
│  │ Renaissance │  90 days   │  150 days  │ Religious wars               │  │
│  │ Industrial  │  60 days   │  100 days  │ World War eruption           │  │
│  │ Modern      │  90 days   │  180 days  │ Climate/nuclear catastrophe  │  │
│  └─────────────┴────────────┴────────────┴──────────────────────────────┘  │
│                                                                             │
│  SOFT LIMIT: Warning signs begin, increasing pressure                       │
│  HARD LIMIT: Catastrophic event, forced transition (with penalties)         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Localized Catastrophes (Not Global Wipes)

**Key Principle:** Catastrophes don't wipe out everyone. Like a real hurricane, they affect *regions*. Players positioned well **survive with their assets intact**—and inherit a less populated world full of opportunity.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CATASTROPHE IMPACT MODEL                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  "A plague doesn't kill everyone. A war doesn't burn every city."           │
│                                                                             │
│  IMPACT ZONES:                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                                                                     │   │
│  │    ████████████  DEVASTATION ZONE (20% of map)                     │   │
│  │    ████████████  - 80-100% asset loss                              │   │
│  │                  - Forced evacuation or death                       │   │
│  │                                                                     │   │
│  │    ▓▓▓▓▓▓▓▓▓▓▓▓  DAMAGE ZONE (30% of map)                          │   │
│  │    ▓▓▓▓▓▓▓▓▓▓▓▓  - 30-60% asset damage                             │   │
│  │                  - Survivable with preparation                      │   │
│  │                                                                     │   │
│  │    ░░░░░░░░░░░░  DISRUPTION ZONE (30% of map)                      │   │
│  │    ░░░░░░░░░░░░  - 10-30% economic impact                          │   │
│  │                  - Trade disruption, refugees                       │   │
│  │                                                                     │   │
│  │    ············  SAFE ZONE (20% of map)                            │   │
│  │    ············  - Minimal direct impact                           │   │
│  │                  - Opportunity for expansion                        │   │
│  │                                                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  SURVIVORS inherit a less crowded world with abandoned assets to claim.    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Post-Catastrophe Opportunities

```yaml
survivor_opportunities:
  land_claims:
    description: "Abandoned farms, shops, estates become claimable"
    window: "7-14 days after catastrophe"
    priority:
      - "Adjacent property owners"
      - "Community members of affected area"
      - "Anyone (open claim)"

  labor_shortage:
    description: "Fewer workers = higher wages"
    effects:
      - "Workshop output multipliers increase"
      - "Farm labor costs rise (but so do crop prices)"
      - "Skilled trades become premium"
    historical_example: "Post-Black Death peasant prosperity"

  infrastructure_rebuilding:
    description: "Reconstruction creates demand"
    opportunities:
      - "Builders earn bonus NVT"
      - "Material suppliers profit"
      - "New trade routes emerge"

  power_vacuum:
    description: "Old authorities weakened or gone"
    effects:
      - "Community leadership positions open"
      - "Guild hierarchies disrupted"
      - "New political factions emerge"

  refugee_integration:
    description: "Displaced players need homes"
    opportunities:
      - "Landlords can house refugees (income + reputation)"
      - "Communities that accept refugees grow faster"
      - "Skilled refugees bring new techniques"
```

### Catastrophe Types by Era

```yaml
era_catastrophes:
  ancient:
    natural:
      - name: "The Great Flood"
        type: "regional"
        affected: "River valley settlements"
        safe_zones: "Highland communities"
        opportunity: "Irrigated land becomes premium"

      - name: "Drought & Famine"
        type: "regional"
        affected: "Agricultural areas"
        safe_zones: "Trade hub cities, coastal fishing"
        opportunity: "Food suppliers become wealthy"

    conflict:
      - name: "Sea Peoples Invasion"
        type: "coastal"
        affected: "Port cities, coastal settlements"
        safe_zones: "Inland communities, mountain fortresses"
        opportunity: "Abandoned coastal land"

  classical:
    natural:
      - name: "Plague of Justinian"
        type: "spreading"
        affected: "Dense urban areas first"
        safe_zones: "Rural isolation, quarantined cities"
        opportunity: "Labor shortage, wage increases"

    conflict:
      - name: "Barbarian Invasions"
        type: "frontier_to_core"
        affected: "Border regions first, then capitals"
        safe_zones: "Fortified cities, distant provinces"
        opportunity: "New kingdoms forming, land grants"

  medieval:
    natural:
      - name: "Black Death"
        type: "pandemic"
        affected: "Trade routes spread it"
        safe_zones: "Isolated villages, strict quarantine"
        opportunity: "Survivors inherit, labor scarcity"
        special: "Some assets INCREASE in value"

    conflict:
      - name: "Crusades"
        type: "military_campaign"
        affected: "Participants, route communities"
        safe_zones: "Non-participating regions"
        opportunity: "War profiteering, land of the fallen"

  renaissance:
    natural:
      - name: "Smallpox in New World"
        type: "epidemic"
        affected: "Indigenous populations, colonizers"
        safe_zones: "Those with immunity"
        opportunity: "Land claims (ethically complex)"

    conflict:
      - name: "Wars of Religion"
        type: "regional_conflict"
        affected: "Areas of religious mixing"
        safe_zones: "Homogeneous regions, neutral cities"
        opportunity: "Refugees bring skills, abandoned property"

  industrial:
    natural:
      - name: "Cholera Outbreaks"
        type: "urban"
        affected: "Industrial cities with poor sanitation"
        safe_zones: "Clean water access, rural areas"
        opportunity: "Sanitation entrepreneurs"

    conflict:
      - name: "World War"
        type: "total_war"
        affected: "Combatant nations"
        safe_zones: "Neutral countries, distant colonies"
        opportunity: "War production, neutral profiteering"

  modern:
    natural:
      - name: "Climate Disasters"
        type: "regional"
        affected: "Coastal (flooding), interior (drought)"
        safe_zones: "Climate-resilient locations"
        opportunity: "Climate adaptation tech"

    conflict:
      - name: "Nuclear Standoff"
        type: "threatened"
        affected: "Major cities (potential targets)"
        safe_zones: "Remote areas, bunker communities"
        opportunity: "Post-crisis rebuilding"
```

---

## War & Conflict Re-enactments

### Historical Battles Become Gameplay

Wars aren't just catastrophes—they're **playable historical re-enactments** that generate valuable training data about human conflict behavior.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         WAR SYSTEM                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  "History's conflicts, relived. Every decision captured."                   │
│                                                                             │
│  WAR TYPES:                                                                 │
│  ├── DECLARED WAR: Formal conflict between communities/factions             │
│  ├── RAIDS: Quick strikes for resources                                     │
│  ├── SIEGES: Extended blockades of fortified positions                      │
│  ├── CIVIL WAR: Internal faction conflicts                                  │
│  └── WORLD WAR: Multi-faction, multi-region conflicts (rare)               │
│                                                                             │
│  PARTICIPATION:                                                             │
│  ├── COMBATANT: Fight directly (high risk, high reward)                    │
│  ├── SUPPLIER: Provide weapons, food, medicine                             │
│  ├── REFUGEE: Flee conflict zone (lose assets, save life)                  │
│  ├── PROFITEER: Trade with both sides (risky if caught)                    │
│  └── RESISTER: Underground opposition (era-dependent)                       │
│                                                                             │
│  TRAINING DATA VALUE:                                                       │
│  "How do humans behave in conflict? What drives cooperation vs betrayal?"  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Era-Specific Conflicts

```yaml
historical_wars:
  ancient:
    - name: "City-State Rivalries"
      type: "territorial"
      example: "Ur vs Lagash water rights"
      player_roles: ["warrior", "diplomat", "spy", "merchant"]

    - name: "Empire Expansion"
      type: "conquest"
      example: "Akkadian conquest"
      player_roles: ["conqueror", "defender", "collaborator", "refugee"]

  classical:
    - name: "Persian Wars"
      type: "invasion"
      example: "Greek defense against Persia"
      player_roles: ["hoplite", "strategist", "messenger", "traitor"]

    - name: "Civil Wars"
      type: "internal"
      example: "Roman civil wars"
      player_roles: ["legionary", "senator", "assassin", "neutral"]

  medieval:
    - name: "Feudal Warfare"
      type: "local"
      example: "Baron vs Baron"
      player_roles: ["knight", "peasant_levy", "siege_engineer", "healer"]

    - name: "Crusades"
      type: "religious"
      example: "Holy Land campaigns"
      player_roles: ["crusader", "defender", "merchant", "pilgrim"]

  renaissance:
    - name: "Colonial Conflicts"
      type: "imperial"
      example: "European powers vs indigenous, vs each other"
      player_roles: ["conquistador", "native_warrior", "missionary", "trader"]

    - name: "Religious Wars"
      type: "ideological"
      example: "Thirty Years War"
      player_roles: ["soldier", "civilian", "cleric", "mercenary"]

  industrial:
    - name: "Colonial Rebellions"
      type: "independence"
      example: "American/French/Latin American revolutions"
      player_roles: ["revolutionary", "loyalist", "neutral", "opportunist"]

    - name: "World Wars"
      type: "total_war"
      example: "WW1 trenches"
      player_roles: ["soldier", "nurse", "spy", "civilian"]

  modern:
    - name: "Proxy Wars"
      type: "cold_war"
      example: "Superpower conflicts fought elsewhere"
      player_roles: ["operative", "local_fighter", "journalist", "civilian"]

    - name: "Asymmetric Warfare"
      type: "guerrilla"
      example: "Insurgency/counterinsurgency"
      player_roles: ["insurgent", "soldier", "civilian", "aid_worker"]
```

### War Mechanics

```yaml
war_mechanics:
  declaration:
    requirements:
      - "Community leader vote"
      - "Casus belli (justification)"
      - "Resource stockpile"
    types:
      - "Border dispute"
      - "Resource control"
      - "Religious difference"
      - "Succession claim"
      - "Defensive alliance"

  combat:
    system: "Abstracted tactical"
    factors:
      - "Numbers"
      - "Equipment quality"
      - "Leadership skill"
      - "Terrain advantage"
      - "Supply lines"
      - "Morale"
    player_agency: "Strategic decisions, not twitch combat"

  consequences:
    victory:
      - "Territory gains"
      - "Resource extraction"
      - "Reputation boost"
      - "War reparations"
    defeat:
      - "Territory loss"
      - "Asset destruction"
      - "Population displacement"
      - "Tribute payments"
    stalemate:
      - "Resource depletion"
      - "Economic damage"
      - "Negotiated peace"

  ethics_guardrails:
    - "Violence abstracted, not glorified"
    - "Civilian harm consequences (reputation, karma)"
    - "War crimes have in-game punishment"
    - "Focus on strategic decisions, not violence"
```

---

## Religion & Ritual Systems

### Faith Shapes Survival

Religion isn't just flavor—it **mechanically impacts survival, community cohesion, and player behavior**.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    RELIGION & RITUAL SYSTEM                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  "What people believe shapes how they act—especially in crisis."            │
│                                                                             │
│  FUNCTIONS OF RELIGION IN-GAME:                                             │
│  ├── COMMUNITY COHESION: Shared rituals bond groups                        │
│  ├── MORALE BOOST: Faith provides hope in dark times                       │
│  ├── ETHICAL FRAMEWORK: Rules for behavior (some helpful, some not)        │
│  ├── SOCIAL HIERARCHY: Priests have power, influence decisions             │
│  ├── CRISIS RESPONSE: Prayer, sacrifice, scapegoating                      │
│  └── CONFLICT TRIGGER: Religious differences cause wars                     │
│                                                                             │
│  TRAINING DATA VALUE:                                                       │
│  "How does belief shape behavior under stress?"                             │
│  "What role do rituals play in community resilience?"                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Era-Specific Religious Systems

```yaml
religious_systems:
  ancient:
    type: "Polytheistic"
    practices:
      - name: "Temple Offerings"
        effect: "Community morale +10%"
        cost: "Resources to temple"

      - name: "Divination"
        effect: "Hints about upcoming events"
        accuracy: "50% (mystical flavor)"

      - name: "Sacrificial Rituals"
        effect: "Appease gods during crisis"
        player_choice: "Animal vs grain vs... darker options"
        training_data: "Crisis response under superstition"

    roles:
      priest: "Intermediary with gods, literate, powerful"
      oracle: "Provides prophecy (system hints)"
      devotee: "Regular practitioner, community member"

  classical:
    type: "State Religion + Philosophy"
    practices:
      - name: "Public Festivals"
        effect: "City-wide morale, trade boost"
        timing: "Seasonal events"

      - name: "Mystery Cults"
        effect: "Secret knowledge, underground network"
        player_choice: "Join for benefits, risk persecution"

      - name: "Philosophical Schools"
        effect: "Rational approach to problems"
        competition: "Faith vs Reason tension"

    roles:
      pontiff: "State religious authority"
      philosopher: "Rationalist alternative"
      cultist: "Mystery religion member"

  medieval:
    type: "Monotheistic Dominance"
    practices:
      - name: "Church Attendance"
        effect: "Community standing, reduced suspicion"
        requirement: "Expected behavior"

      - name: "Pilgrimage"
        effect: "Reputation boost, network building"
        risk: "Travel dangers"

      - name: "Tithing"
        effect: "Church protection, afterlife insurance"
        cost: "10% of income"

      - name: "Flagellation/Penance"
        effect: "Response to plague (ineffective but historically accurate)"
        training_data: "Irrational crisis response"

    roles:
      clergy: "Literate, powerful, tax-exempt"
      heretic: "Alternative beliefs, persecution risk"
      inquisitor: "Enforces orthodoxy"

  renaissance:
    type: "Reformation & Counter-Reformation"
    practices:
      - name: "Choose Your Faith"
        effect: "Alignment with faction"
        consequences: "Determines allies and enemies"

      - name: "Religious Debate"
        effect: "Influence community belief"
        skill: "Rhetoric and theology"

      - name: "Iconoclasm"
        effect: "Destroy old symbols, embrace new"
        training_data: "Revolutionary behavior"

    roles:
      reformer: "Challenge established order"
      defender: "Protect tradition"
      tolerant: "Accept diversity (rare, valuable)"

  industrial:
    type: "Secularization Begins"
    practices:
      - name: "Sunday Observance"
        effect: "Rest day, community time"
        erosion: "Factory work disrupts"

      - name: "Revival Movements"
        effect: "Counter to industrialization alienation"
        appeal: "Working class community"

      - name: "Scientific Worldview"
        effect: "Alternative to religion"
        tension: "Faith vs Progress"

    roles:
      preacher: "Moral authority, social reformer"
      scientist: "New priesthood of knowledge"
      skeptic: "Questions all authority"

  modern:
    type: "Pluralism & Fundamentalism"
    practices:
      - name: "Religious Freedom"
        effect: "Choose any or none"
        protected: "In most regions"

      - name: "Fundamentalist Revival"
        effect: "Counter to modern uncertainty"
        tension: "Tradition vs Change"

      - name: "Spiritual but not Religious"
        effect: "Individual practice"
        community: "Weaker bonds"

    roles:
      pluralist: "Accepts all paths"
      fundamentalist: "One true way"
      atheist: "No supernatural belief"
```

### Ritual Mechanics

```yaml
ritual_mechanics:
  types:
    daily:
      - "Morning prayers (morale +2%)"
      - "Meal blessings (community bond)"
      - "Evening reflection (stress reduction)"

    weekly:
      - "Sabbath/Holy Day (mandatory rest, community gathering)"
      - "Market day blessings (trade bonus)"

    seasonal:
      - "Harvest festival (food storage bonus)"
      - "New year rituals (reset, fresh start)"
      - "Solstice celebrations (morale peak)"

    crisis:
      - "Plague prayers (morale, but spreads disease via gathering)"
      - "War blessings (combat morale)"
      - "Funeral rites (community grief processing)"

  participation_effects:
    active_participant:
      morale: "+15%"
      community_standing: "+10%"
      suspicion: "-20%"

    occasional:
      morale: "+5%"
      community_standing: "neutral"
      suspicion: "neutral"

    non_participant:
      morale: "0%"
      community_standing: "-10%"
      suspicion: "+30% (era-dependent)"

  training_data_capture:
    - "Do players follow rituals for benefit or belief?"
    - "How does ritual participation change under stress?"
    - "What triggers abandonment of traditional practices?"
    - "How do communities enforce religious conformity?"
```

### Religion & Catastrophe Interaction

```yaml
religion_crisis_response:
  plague:
    historical_responses:
      - "Flagellant processions (spreads disease)"
      - "Scapegoating minorities (pogroms)"
      - "Prayer and fasting (morale only)"
      - "Quarantine as divine will (actually effective)"
    training_data: "Irrational vs rational crisis response"

  famine:
    historical_responses:
      - "Sacrifice to gods (resource waste)"
      - "Prayer for rain (no effect)"
      - "Food sharing as religious duty (helps community)"
      - "Hoarding as sin (social pressure to share)"
    training_data: "Religion as resource distribution mechanism"

  war:
    historical_responses:
      - "Holy war justification (increases commitment)"
      - "Peace through religion (negotiation path)"
      - "Martyrdom ideology (extreme sacrifice)"
      - "Sanctuary in religious buildings (protection)"
    training_data: "How faith intensifies or moderates conflict"

  positioning_benefit:
    temple_locations: "Often in safe zones (central, protected)"
    religious_networks: "Communication across regions"
    sanctuary_tradition: "Churches as refuge during conflict"
```

---

### Survival Positioning

Players who position themselves well don't just survive—they **thrive post-catastrophe**:

```yaml
positioning_strategies:
  geographic:
    highlands: "Safe from floods, visible from invasion"
    isolation: "Disease spreads slower"
    trade_routes: "Economic opportunity but disease risk"
    fortifications: "Protection but siege vulnerability"

  economic:
    diversified_assets: "Not all eggs in one basket"
    liquid_wealth: "Portable, survives displacement"
    essential_goods: "Food, medicine always valuable"
    debt_free: "No obligations during crisis"

  social:
    community_ties: "Mutual aid networks"
    religious_standing: "Church protection"
    guild_membership: "Professional network"
    political_allies: "Powerful protectors"

  information:
    early_warning: "Know what's coming"
    trade_intelligence: "Know where it's safe"
    historical_knowledge: "Patterns repeat"

  post_catastrophe_actions:
    first_48_hours:
      - "Assess damage to your assets"
      - "Check on alliance members"
      - "Identify abandoned properties"

    first_week:
      - "File claims on abandoned assets"
      - "Recruit displaced skilled workers"
      - "Establish new trade routes"

    first_month:
      - "Expand into vacated territories"
      - "Rebuild infrastructure (earn bonuses)"
      - "Position for new power structure"
```

---

## Era Transition Auctions

### Reincarnation Day Markets

When a player completes their keystone challenges and chooses to reincarnate, their **non-portable assets go to auction**.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      ERA TRANSITION AUCTION                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Player "MerchantQueen" is reincarnating from Medieval → Renaissance        │
│                                                                             │
│  ASSETS FOR AUCTION:                                                        │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  🏪 The Golden Loaf Bakery (Florence, Est. 1302)                   │    │
│  │     Location: Prime market square                                  │    │
│  │     History: Survived Black Death, supplied Medici family          │    │
│  │     Condition: 92%                                                 │    │
│  │     Monthly Income: ~45 NVT                                        │    │
│  │                                                                    │    │
│  │     Starting Bid: 800 NVT                                          │    │
│  │     Current Bid: 1,450 NVT (by Apprentice_Baker)                   │    │
│  │     Time Left: 2h 34m                                              │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │  🌾 Riverside Farm (Tuscany, 40 acres)                             │    │
│  │     Features: Irrigation, olive grove, vineyard                    │    │
│  │     History: Family-owned 3 generations                            │    │
│  │                                                                    │    │
│  │     Starting Bid: 1,200 NVT                                        │    │
│  │     Current Bid: 2,100 NVT (by VineyardDreamer)                    │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  WHAT SELLER KEEPS:                                                         │
│  ├── 90% of auction proceeds (10% platform fee)                             │
│  ├── All gold, gems, jewelry (portable wealth)                              │
│  ├── Reputation score (carries forward)                                     │
│  └── Achievement badges (permanent)                                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Auction Mechanics

```yaml
auction_system:
  types:
    standard:
      duration: "24-72 hours"
      bidding: "English auction (ascending)"
      reserve_price: true

    flash:
      duration: "1-4 hours"
      bidding: "Rapid-fire"
      trigger: "Emergency reincarnation (catastrophe)"

    dutch:
      duration: "Variable"
      bidding: "Price descends until someone bids"
      use_case: "Clearing low-demand assets"

  seller_benefits:
    auction_fee: 0.10             # 10% to platform
    seller_receives: 0.90         # 90% of final price
    minimum_guarantee: 0.50       # At least 50% of estimated value

  buyer_protections:
    inspection_period: true       # Can view asset details
    history_verification: true    # Provenance confirmed
    condition_report: true        # Current state documented

  special_auctions:
    estate_sales:
      description: "When player leaves game entirely"
      includes: "All assets across all eras"

    catastrophe_liquidation:
      description: "Forced sale due to era timeout"
      discount: "20-40% below market"

    legendary_auctions:
      description: "Historically significant assets"
      marketing: "Platform-promoted event"
      minimum_bid: "Set by committee"
```

### Cross-Era Value Conversion

```yaml
value_conversion:
  # When you sell Medieval assets, you get NVT
  # NVT carries forward to Renaissance
  # But purchasing power changes

  purchasing_power_by_era:
    ancient:
      baseline: 1.0
      note: "1 NVT buys basic daily supplies"

    classical:
      baseline: 0.9
      note: "Slight inflation, more goods available"

    medieval:
      baseline: 0.85
      note: "Guild prices, controlled markets"

    renaissance:
      baseline: 0.75
      note: "Expanding economy, more competition"

    industrial:
      baseline: 0.6
      note: "Mass production reduces costs"

    modern:
      baseline: 0.4
      note: "Abundant goods, different scarcity"

    ai_era:
      baseline: 0.3
      note: "Automation, but new scarcities emerge"

  # Example: 1000 NVT from Medieval auction
  # In Renaissance: 1000 × (0.75/0.85) = ~882 NVT purchasing power equivalent
  # But tokens remain 1000—just prices are different
```

---

## Summary

The Historical Progression System transforms The Analog Economy from a game into a **simulation of human civilization itself**.

**Key Principles:**

1. **Learn by Living** - Experience history, don't just read it
2. **Problems are Eternal** - Same challenges, different technologies
3. **The Arc Matters** - See how humanity evolved (and didn't)
4. **Never Ending** - Current events keep the game fresh
5. **Data Goldmine** - Training data across all of human experience

**The Vision:**
> "What if you could live through all of human history, solving the problems that shaped our world, and then face the challenges that will define our future?"

---

## Related Documentation

- [Survival & Progression](./survival-and-progression.md)
- [Payments Specification](./payments.md)
- [Project Overview](../guides/concepts/project-overview.md)
- [Biome Documentation](../biomes/)
