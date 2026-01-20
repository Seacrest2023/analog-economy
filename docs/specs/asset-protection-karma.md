# Asset Protection & Karma: What Can Be Taken

> "Your soul cannot be stolen. Your time can be wasted. Your karma follows you across lives."

## Table of Contents

1. [Design Philosophy](#1-design-philosophy)
2. [Asset Classification](#2-asset-classification)
3. [The Control vs Ownership Split](#3-the-control-vs-ownership-split)
4. [Theft Mechanics: Time, Not Assets](#4-theft-mechanics-time-not-assets)
5. [Conquest Mechanics](#5-conquest-mechanics)
6. [The Karma System](#6-the-karma-system)
7. [Animal Reincarnation](#7-animal-reincarnation)
8. [Game Token Economy (Conquest Rewards)](#8-game-token-economy-conquest-rewards)
9. [Training Data Value](#9-training-data-value)

---

## 1. Design Philosophy

### 1.1 The Three Guarantees

Players are guaranteed:

| Guarantee | What It Means |
|-----------|---------------|
| **Soul Security** | NFTs, tickets, account-bound items can NEVER be stolen |
| **Creation Protection** | Things you invented/designed (IP) are permanently yours |
| **Recovery Path** | Even worst-case theft/conquest doesn't end your game |

### 1.2 The Three Risks

Players accept risk on:

| Risk | What It Means |
|------|---------------|
| **Time** | Bad events can cost you progress, not possessions |
| **Control** | You may lose control of assets without losing ownership |
| **Karma** | How you play determines how you reincarnate |

### 1.3 Why This Design?

```
Problem: Real money on the line
├── If theft takes real assets → Players quit, legal issues
├── If theft is meaningless → No tension, boring gameplay
└── Solution: Theft/conquest takes TIME and CONTROL, not OWNERSHIP

Problem: Violence should have consequences
├── If violence is free → Game becomes murder simulator
├── If violence is forbidden → Unrealistic, boring
└── Solution: Karma system makes violence costly across LIVES
```

---

## 2. Asset Classification

### 2.1 The Four Tiers

```yaml
asset_tiers:
  # TIER 1: SOUL-BOUND (Cannot be stolen, lost, or transferred)
  soul_bound:
    examples:
      - "Reincarnation Tickets (Ascension, Destination, Genesis)"
      - "Legacy Points"
      - "Bloodline identity"
      - "Codex contributions"
      - "Achievement badges"
      - "Account credentials"

    protection: "ABSOLUTE"
    rationale: "These represent real money or permanent progress"

  # TIER 2: HEIRLOOM-BOUND (Protected but can be lost through specific events)
  heirloom_bound:
    examples:
      - "Designated heirloom items (max 3)"
      - "Family crests/insignia"
      - "Unique recipes/blueprints you created"

    protection: "VERY HIGH"
    can_be_lost: "Only if you die without preparing succession"
    cannot_be_stolen: true
    rationale: "Significant player investment, but death has meaning"

  # TIER 3: DEED-BOUND (Ownership protected, control can be lost)
  deed_bound:
    examples:
      - "Land/property NFTs"
      - "Business ownership"
      - "Intellectual property rights"
      - "Contracted services"

    protection: "OWNERSHIP protected, CONTROL can change"
    can_be_conquered: true
    can_be_stolen: false
    rationale: "Creates meaningful conflict without asset loss"

  # TIER 4: PHYSICAL (Can be stolen, lost, destroyed)
  physical:
    examples:
      - "Inventory items"
      - "In-game currency (local)"
      - "Crops and goods"
      - "Non-heirloom equipment"
      - "Consumables"

    protection: "LOW - but theft costs TIME not the items"
    can_be_stolen: true
    can_be_lost: true
    rationale: "Creates tension, but checkpoint system prevents devastation"
```

### 2.2 Visual Reference

```
ASSET PROTECTION PYRAMID

        ▲
       ╱ ╲      SOUL-BOUND
      ╱   ╲     NFTs, Tickets, Legacy Points
     ╱─────╲    [UNTOUCHABLE]
    ╱       ╲
   ╱ HEIRLOOM╲   Family items, created IP
  ╱───────────╲  [PROTECTED, succession required]
 ╱             ╲
╱   DEED-BOUND  ╲  Land, business, property
╱─────────────────╲  [OWN always, CONTROL can change]
╱                   ╲
╱     PHYSICAL        ╲  Inventory, currency, goods
╱───────────────────────╲  [Can lose, but costs TIME]
```

---

## 3. The Control vs Ownership Split

### 3.1 The Core Concept

**You can CONQUER land without TAKING it.**

```
OWNERSHIP (The NFT/Deed)           CONTROL (Who operates it)
─────────────────────────          ─────────────────────────
• Stays with original owner        • Can change through conquest
• Is an NFT on blockchain          • Is a game state variable
• Cannot be stolen or forced       • Can be taken by force
• Generates passive royalty        • Generates active income
• Permanent unless sold            • Temporary until retaken
```

### 3.2 How Conquest Works

```yaml
conquest_flow:
  before_conquest:
    owner: "PlayerA"
    controller: "PlayerA"
    income_split: "100% to PlayerA"

  conquest_happens:
    method: "Military victory, siege, political takeover"
    requirement: "Declared conflict, not random attack"

  after_conquest:
    owner: "PlayerA (unchanged)"
    controller: "PlayerB (conqueror)"
    income_split:
      to_owner: "20% royalty (passive)"
      to_controller: "80% operating income"
      note: "Owner still benefits, just less"

  restoration_options:
    reconquest: "PlayerA takes it back militarily"
    negotiation: "PlayerB agrees to return control"
    purchase: "PlayerB buys the deed from PlayerA"
    abandonment: "PlayerB leaves, control reverts"
    era_transition: "Control resets on era change"
```

### 3.3 Real-World Parallel

This mirrors historical situations:
- Occupied territories (owner vs occupier)
- Feudal systems (king owns, lord controls)
- Colonial extraction (native ownership, colonial control)
- Modern landlord/tenant (owner vs operator)

**Training data value:** Decisions about occupation, resistance, collaboration, negotiation.

### 3.4 Controller Rights and Limits

```yaml
controller_rights:
  can_do:
    - "Operate the land/business"
    - "Extract resources"
    - "Collect taxes/rent from others"
    - "Build structures (temporary)"
    - "Station troops/workers"
    - "Set local policies"

  cannot_do:
    - "Sell the underlying asset"
    - "Destroy the asset permanently"
    - "Transfer ownership"
    - "Prevent owner from receiving royalty"
    - "Build permanent structures without owner consent"

  owner_rights_while_not_controlling:
    - "Receive 20% royalty"
    - "View activity reports"
    - "Attempt reconquest"
    - "Sell to third party (controller becomes tenant)"
    - "Appeal to higher authority (era-dependent)"
```

### 3.5 Example Scenarios

**Scenario 1: Farm Conquest**
```
PlayerA owns a farm (NFT deed)
PlayerB conquers the farm in declared war

Result:
- PlayerA still owns the farm NFT
- PlayerB controls the farm, works it, sells crops
- PlayerA receives 20% of all farm income passively
- PlayerB can be kicked out if PlayerA reconquers
- If PlayerB leaves/dies, control reverts to PlayerA
```

**Scenario 2: City Takeover**
```
PlayerA owns a shop in a city
PlayerB's faction conquers the entire city

Result:
- PlayerA still owns the shop NFT
- PlayerB's faction controls the city, including the shop
- PlayerA receives 20% royalty
- PlayerA can keep operating shop (if faction allows)
- Or PlayerA can flee, collect passive income from afar
```

**Scenario 3: Hostile Buyout**
```
PlayerB controls PlayerA's property for 90 days
PlayerB offers to buy the deed

Options for PlayerA:
- Sell at market price (cash out, move on)
- Refuse, keep collecting 20% royalty
- Attempt reconquest to regain 100%
```

---

## 4. Theft Mechanics: Time, Not Assets

### 4.1 The Checkpoint System

**When you're robbed, you don't lose your stuff. You lose TIME.**

```yaml
theft_mechanics:
  what_happens:
    1_robbery_occurs: "Thief successfully steals from you"
    2_checkpoint_reset: "You reset to last checkpoint"
    3_items_preserved: "All your items are still yours"
    4_time_lost: "Progress since checkpoint is lost"
    5_thief_reward: "Thief gets game tokens, not your items"

  checkpoint_system:
    auto_save: "Every 4 real-time hours"
    manual_save: "At any settlement (costs small fee)"
    checkpoint_locations:
      - "Settlements (free)"
      - "Shrines (ancient/medieval)"
      - "Banks (classical onwards)"
      - "Any owned property"

  time_lost_calculation:
    minimum: "1 real-time hour of progress"
    maximum: "4 real-time hours (last checkpoint)"
    average: "~2 hours"

  what_resets:
    - "Character position (back to checkpoint)"
    - "Incomplete quest progress"
    - "Unsaved transactions"
    - "Recent relationship changes"

  what_does_not_reset:
    - "Inventory items"
    - "Currency"
    - "Owned property"
    - "Completed quests"
    - "Codex contributions"
    - "Legacy Points earned"
```

### 4.2 Why This Design?

```
Traditional Theft:
Thief steals your sword → You lose sword → You feel robbed → You quit

Analog Economy Theft:
Thief robs you → You lose 2 hours progress → You still have sword
                → Annoying but not devastating → You keep playing
                → Thief gets game tokens → Thief has alternative reward
```

**Benefits:**
- Theft is meaningful (time has value)
- Theft isn't devastating (no permanent loss)
- Thieves have incentive (game tokens)
- Training data is valuable (response to setbacks)

### 4.3 Thief Rewards: Game Tokens

```yaml
thief_rewards:
  currency: "Shadow Marks (SM)"

  earning:
    successful_theft: "10-50 SM based on difficulty"
    pickpocket: "5-15 SM"
    burglary: "20-40 SM"
    heist: "50-100 SM"

  spending:
    thief_guild_items:
      - "Lockpicks (better quality)"
      - "Disguise kits"
      - "Stealth gear"
      - "Fence services"
      - "Safe house access"
      - "Bribe funds"

    cosmetics:
      - "Thief-specific appearances"
      - "Shadow effects"
      - "Notoriety titles"

    cannot_buy:
      - "NFTs or real-value items"
      - "Regular game currency"
      - "Anything tradeable to non-thieves"

  rationale: |
    Shadow Marks are a closed economy within the thief playstyle.
    They provide progression without creating a theft-to-wealth pipeline
    that would encourage mass griefing.
```

### 4.4 Victim Protections

```yaml
victim_protections:
  cooldown:
    after_robbery: "24 real-time hours immunity from same thief"
    after_3_robberies: "48 hour general immunity"
    rationale: "Prevents targeted harassment"

  checkpoint_insurance:
    cost: "Small ongoing fee"
    benefit: "Checkpoints every 1 hour instead of 4"
    availability: "Industrial era onwards"

  community_response:
    reporting: "Victim can report to community"
    bounty: "Community may place bounty"
    tracking: "Thief becomes 'Wanted'"

  new_player_protection:
    duration: "First 7 days"
    effect: "Cannot be robbed"
```

---

## 5. Conquest Mechanics

### 5.1 Types of Conquest

```yaml
conquest_types:
  military:
    method: "Armed conflict, siege, battle"
    requirements:
      - "Declared war or raid"
      - "Sufficient forces"
      - "Supply lines"
    control_duration: "Until reconquered or abandoned"

  political:
    method: "Coup, election, manipulation"
    requirements:
      - "Influence in target community"
      - "Coalition of supporters"
      - "Trigger event (scandal, crisis)"
    control_duration: "Until overthrown or voted out"

  economic:
    method: "Buy controlling interest, debt acquisition"
    requirements:
      - "Significant capital"
      - "Target in financial distress"
      - "Legal framework (era-dependent)"
    control_duration: "Until debt repaid or bought out"

  legal:
    method: "Lawsuit, inheritance claim, royal decree"
    requirements:
      - "Valid legal claim"
      - "Court/authority decision"
      - "Era-appropriate legal system"
    control_duration: "Permanent unless overturned"
```

### 5.2 Conquest Rewards

```yaml
conquest_rewards:
  control_income:
    percentage: "80% of asset income"
    types: ["rent", "production", "taxes", "trade"]

  game_tokens:
    currency: "Dominion Marks (DM)"
    earning: "Based on difficulty and significance"

  reputation:
    type: "Conqueror reputation"
    effect: "Opens military/political paths"
    tradeoff: "May close peaceful paths"

  territory_bonuses:
    strategic_position: "+10% to adjacent operations"
    resource_access: "Control over local resources"
    population_access: "Labor pool"

  cannot_receive:
    - "Ownership of NFTs"
    - "Legacy Points from conquest alone"
    - "Victim's personal items"
```

### 5.3 Dominion Marks Economy

```yaml
dominion_marks:
  spending:
    military_equipment:
      - "Siege weapons"
      - "Fortifications"
      - "Army supplies"
      - "Naval vessels"

    governance_tools:
      - "Tax collection efficiency"
      - "Loyalty programs"
      - "Spy networks"
      - "Administrative staff"

    cosmetics:
      - "Conqueror titles"
      - "Military regalia"
      - "Victory monuments"
      - "Flag/banner customization"

    special_items:
      - "War elephants (classical+)"
      - "Siege engineers"
      - "Mercenary contracts"

  cannot_buy:
    - "NFTs or ownership deeds"
    - "Regular currency"
    - "Cross-faction tradeable items"
```

---

## 6. The Karma System

### 6.1 Design Intent

Karma is not a punishment system. It's a **consequence system** that:
- Makes violence meaningful across lives
- Creates alternative playstyles (high karma vs low karma)
- Generates unique training data (living as animal)
- Reflects philosophical traditions (Buddhist/Hindu concepts)

### 6.2 Karma Mechanics

```yaml
karma:
  scale: [-1000, 1000]

  starting_karma: 0

  brackets:
    enlightened: [800, 1000]
      description: "Exceptionally virtuous"
      reincarnation: "Choose your next life"

    virtuous: [400, 800]
      description: "Good standing"
      reincarnation: "Human, favorable circumstances"

    balanced: [-200, 400]
      description: "Normal range"
      reincarnation: "Human, normal circumstances"

    troubled: [-500, -200]
      description: "Significant negative karma"
      reincarnation: "Human, difficult circumstances"

    corrupted: [-800, -500]
      description: "Heavily negative karma"
      reincarnation: "50% chance animal life"

    damned: [-1000, -800]
      description: "Extreme negative karma"
      reincarnation: "Guaranteed animal life"
```

### 6.3 Karma Actions

```yaml
karma_changes:
  positive:
    help_stranger: +5
    save_life: +25
    donate_significantly: +15
    codex_contribution: +5
    mentor_new_player: +10
    peaceful_conflict_resolution: +20
    sacrifice_for_others: +30
    protect_innocent: +15
    heal_the_sick: +10
    feed_the_hungry: +10
    forgive_enemy: +25

  negative:
    theft_successful: -15
    unprovoked_violence: -20
    murder: -50
    murder_innocent: -100
    betrayal: -40
    exploitation: -25
    slavery_participation: -30
    war_crimes: -75
    torture: -100
    theft_from_poor: -25
    abandoning_dependents: -35

  neutral:
    self_defense: 0
    declared_war_combat: -5 (small penalty)
    executing_criminal: -10
    business_competition: 0
    defensive_theft: -5

  decay:
    positive_decay: "-1 per week (slow)"
    negative_decay: "+2 per week (faster recovery)"
    rationale: "Redemption is possible but requires time"
```

### 6.4 Karma Visibility

```yaml
karma_display:
  to_self:
    visible: "Always"
    detail: "Exact number and recent changes"

  to_others:
    visible: "Approximate bracket only"
    display: "Aura/visual indicator"
    detail: "Cannot see exact karma"

  visual_indicators:
    enlightened: "Subtle glow, serene expression"
    virtuous: "Clear eyes, upright posture"
    balanced: "Normal appearance"
    troubled: "Slightly haggard, shifty"
    corrupted: "Dark circles, twitchy"
    damned: "Visibly marked, others sense danger"
```

---

## 7. Animal Reincarnation

### 7.1 The Concept

**If you die with severely negative karma, you don't reincarnate as a human.**

You come back as an animal owned by another player or NPC. This is:
- A time penalty (must serve as animal)
- A perspective shift (experience servitude)
- A training data generator (animal behavior, obedience)
- A redemption path (work off karma)

### 7.2 Animal Types by Karma

```yaml
animal_reincarnation:
  corrupted_karma: [-800, -500]
    chance: "50%"
    animals:
      - dog: "Loyal, can assist owner"
      - horse: "Transportation, labor"
      - cat: "Independent, hunter"
    duration: "7-14 real-time days"

  damned_karma: [-1000, -800]
    chance: "100%"
    animals:
      - mule: "Heavy labor, less respect"
      - pig: "Eventually slaughtered or freed"
      - rat: "Street existence, scavenger"
    duration: "14-30 real-time days"
```

### 7.3 Animal Life Mechanics

```yaml
animal_life:
  ownership:
    assigned_to: "Random player or NPC"
    transfer: "Owner can sell/give you away"
    freedom: "Owner can free you (ends animal life)"

  capabilities:
    communication: "Cannot speak, limited emotes"
    actions: "Animal-appropriate only"
    autonomy: "Must follow owner commands (mostly)"

  commands:
    obedience_required: "80%+ compliance expected"
    disobedience_penalty: "Extended duration"
    cruel_commands: "Can refuse, no penalty"
    impossible_commands: "Auto-refuse"

  experience:
    perspective: "Third-person, animal height"
    UI: "Simplified, animal-appropriate"
    other_players: "See you as animal, not player"

  quality_of_life:
    good_owner:
      treatment: "Fed, sheltered, treated kindly"
      karma_recovery: "+5 per day"
      duration_reduction: "-10%"

    average_owner:
      treatment: "Basic care"
      karma_recovery: "+3 per day"
      duration_reduction: "0%"

    bad_owner:
      treatment: "Neglected or abused"
      karma_recovery: "+1 per day (slower)"
      duration_reduction: "0%"
      escape_option: "Can attempt escape"
```

### 7.4 Ending Animal Life

```yaml
animal_life_end:
  natural_completion:
    trigger: "Duration expires"
    result: "Reincarnate as human (difficult circumstances)"
    karma_reset_to: "-200 (troubled but not damned)"

  owner_frees_you:
    trigger: "Owner chooses to release"
    result: "Immediate human reincarnation"
    karma_bonus: "+50"
    owner_karma: "+25"

  death_as_animal:
    trigger: "Killed, starved, accident"
    result: "Reincarnate as different animal"
    duration: "Resets"
    karma_change: "None"

  escape:
    trigger: "Successfully flee cruel owner"
    result: "Become stray animal"
    duration: "Same, but can find new owner"
    new_owner: "Must be adopted or survive alone"

  special:
    exceptional_service:
      trigger: "Save owner's life, heroic act"
      result: "Immediate human reincarnation"
      karma_bonus: "+100"
      story: "Remembered as loyal companion"
```

### 7.5 Owner Experience

```yaml
animal_ownership:
  acquiring_animals:
    purchase: "Buy from market"
    find: "Adopt stray"
    inherit: "Previous owner dies/leaves"
    note: "Never told if animal is player"

  benefits:
    labor: "Animals can work"
    companionship: "+5 morale"
    transport: "Horses, mules"
    protection: "Dogs can guard"

  responsibilities:
    feeding: "Must feed animal"
    shelter: "Must provide shelter"
    karma_impact:
      good_treatment: "+2 karma per week"
      neglect: "-5 karma per incident"
      abuse: "-20 karma per incident"

  unknowing:
    design: "Owners don't know which animals are players"
    rationale: "Prevents gaming the system"
    effect: "All animals treated as potentially real"
```

### 7.6 Training Data Value

```yaml
animal_training_data:
  from_animal_player:
    - "Response to loss of agency"
    - "Obedience vs resistance decisions"
    - "Experience of servitude"
    - "Patience under constraint"
    - "Observation of human behavior from outside"

  from_owner:
    - "Treatment of perceived non-persons"
    - "Responsibility and care decisions"
    - "Power dynamics when unobserved"
    - "Kindness without expectation of reward"

  unique_scenarios:
    - "Animal witnesses crime, cannot report"
    - "Animal must choose: obey or protect innocent"
    - "Animal earns freedom through service"
```

---

## 8. Game Token Economy (Conquest Rewards)

### 8.1 Token Overview

```yaml
special_tokens:
  shadow_marks:
    earned_by: "Theft, espionage, smuggling"
    spent_on: "Thief guild items and cosmetics"
    tradeable: "Only within thief economy"
    rationale: "Provides thief progression without griefing incentive"

  dominion_marks:
    earned_by: "Conquest, military victory, territorial control"
    spent_on: "Military equipment, governance tools, cosmetics"
    tradeable: "Only within conquest economy"
    rationale: "Provides conqueror progression without forced asset transfer"

  karma_points:
    earned_by: "Positive actions only"
    spent_on: "Nothing (affects reincarnation only)"
    tradeable: "Never"
    rationale: "Pure moral accounting"
```

### 8.2 Company-Made Items

```yaml
company_items:
  description: |
    Items created and sold by the game company (Mault),
    purchasable only with special tokens (SM, DM).
    This creates a sink for conquest/theft rewards.

  thief_items:
    lockpick_sets:
      levels: ["Basic", "Advanced", "Master"]
      effect: "Improves theft success rate"

    disguise_kits:
      types: ["Merchant", "Guard", "Noble", "Servant"]
      effect: "Access restricted areas"

    shadow_cloak:
      effect: "Reduced detection chance"
      cosmetic: "Cool visual effect"

    safe_house_access:
      effect: "Protected rest location"

  conqueror_items:
    siege_equipment:
      types: ["Battering Ram", "Siege Tower", "Catapult"]
      effect: "Improves siege success"

    commander_gear:
      types: ["Battle Standard", "War Horn", "Command Tent"]
      effect: "Troop morale and coordination"

    governance_tools:
      types: ["Tax Ledger", "Spy Network", "Loyalty Shrine"]
      effect: "Controlled territory efficiency"

    war_mounts:
      types: ["War Horse", "War Elephant", "Chariot"]
      effect: "Combat bonuses"
```

### 8.3 Economic Flow

```
CONQUEST/THEFT ECONOMY
═══════════════════════════════════════════════════════════════

Player steals from victim
        │
        ├───► Victim: Loses TIME (checkpoint reset)
        │              Keeps all ITEMS
        │
        └───► Thief: Gains Shadow Marks
                     │
                     └───► Spends on thief items (company-made)
                                    │
                                    └───► Money flows to company
                                          (sustainable business)

Player conquers territory
        │
        ├───► Owner: Keeps OWNERSHIP (NFT)
        │             Receives 20% royalty
        │
        └───► Conqueror: Gains CONTROL
                         Gains 80% income
                         Gains Dominion Marks
                               │
                               └───► Spends on conquest items
                                            │
                                            └───► Money to company
```

---

## 9. Training Data Value

### 9.1 What This System Teaches AI

```yaml
training_data:
  from_theft_system:
    - "How do humans respond to setbacks that cost time?"
    - "What makes theft feel 'fair' vs 'unfair'?"
    - "How do communities self-organize against theft?"
    - "What drives some players to become thieves?"

  from_conquest_system:
    - "How do people behave when controlling others' property?"
    - "How do owners respond to loss of control?"
    - "What negotiation strategies emerge?"
    - "When do people choose violence vs diplomacy?"

  from_karma_system:
    - "Does karma affect behavior over time?"
    - "How do players respond to karma visibility?"
    - "What actions do players consider 'worth' negative karma?"
    - "How do players pursue redemption?"

  from_animal_life:
    - "How do humans experience loss of agency?"
    - "How do owners treat beings they perceive as non-persons?"
    - "What creates loyalty under constraint?"
    - "How does perspective shift affect empathy?"

  unique_scenarios:
    - "Player-animal witnesses their former enemy as owner"
    - "Conqueror must decide treatment of occupied population"
    - "Thief can steal from rich to give to poor - do they?"
    - "Owner discovers their animal is a damned player"
```

### 9.2 Ethical Guardrails

```yaml
ethics:
  animal_life:
    no_sexual_content: "Absolutely forbidden"
    no_graphic_violence: "Abstract only"
    abuse_consequences: "Severe karma penalty for owner"
    escape_always_possible: "Cannot be truly trapped"

  conquest:
    civilian_protection: "War crimes punished"
    occupation_limits: "Must maintain basic services"
    no_genocide: "Cannot eliminate populations"

  theft:
    no_targeting_new_players: "Protected first 7 days"
    no_harassment: "Cooldowns prevent repeated targeting"
    no_real_loss: "Never lose actual assets"
```

---

## Appendix: Quick Reference

### What Can Be Stolen?

| Asset Type | Can Be Stolen? | Consequence |
|------------|----------------|-------------|
| NFTs/Tickets | NO | - |
| Legacy Points | NO | - |
| Heirlooms | NO | - |
| Created IP | NO | - |
| Land Ownership | NO | - |
| Land Control | YES (conquest) | Owner gets 20% royalty |
| Inventory | SORT OF | Victim resets to checkpoint, keeps items |
| Currency | SORT OF | Victim resets to checkpoint, keeps currency |

### What Does the Thief Get?

| Theft Type | Victim Loses | Thief Gains |
|------------|--------------|-------------|
| Pickpocket | 1-4 hours progress | 5-15 Shadow Marks |
| Burglary | 2-4 hours progress | 20-40 Shadow Marks |
| Heist | 4 hours progress | 50-100 Shadow Marks |

### Karma Consequences

| Karma Range | Reincarnation |
|-------------|---------------|
| 800 to 1000 | Choose next life |
| 400 to 800 | Human, favorable |
| -200 to 400 | Human, normal |
| -500 to -200 | Human, difficult |
| -800 to -500 | 50% animal |
| -1000 to -800 | 100% animal |

### Animal Life Duration

| Karma | Animal Type | Duration |
|-------|-------------|----------|
| -500 to -800 | Dog, Horse, Cat | 7-14 days |
| -800 to -1000 | Mule, Pig, Rat | 14-30 days |

---

*Your possessions are protected. Your time is at risk. Your soul is shaped by your choices.*
