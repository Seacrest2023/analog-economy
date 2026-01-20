# Constraints: The Rules of Survival

> "Freedom without consequence is a sandbox. Freedom with consequence is a world."

## Table of Contents

1. [Design Philosophy](#1-design-philosophy)
2. [Core Survival Systems](#2-core-survival-systems)
3. [The Witness System (Sanity/Trauma)](#3-the-witness-system-sanitytrauma)
4. [Era Pressure: The Clock](#4-era-pressure-the-clock)
5. [Theft & Asset Protection](#5-theft--asset-protection)
6. [Violence & Combat Constraints](#6-violence--combat-constraints)
7. [Behavioral Consequences](#7-behavioral-consequences)
8. [Graduation Requirements](#8-graduation-requirements)
9. [Death & Permadeath](#9-death--permadeath)
10. [Karma & Reincarnation](#10-karma--reincarnation)
11. [Toxicity Prevention](#11-toxicity-prevention)
12. [Training Data Implications](#12-training-data-implications)

---

## 1. Design Philosophy

### 1.1 The Purpose of Constraints

Constraints exist not to punish players, but to:

| Purpose | How Constraints Achieve It |
|---------|---------------------------|
| Create meaningful decisions | Every choice has tradeoffs |
| Prevent degenerate gameplay | Griefing has real consequences |
| Generate valuable training data | Players face genuine dilemmas |
| Maintain world authenticity | Actions have realistic outcomes |
| Protect player investment | Real assets require real protection |

### 1.2 The Golden Rule

**Constraints should create interesting decisions, not frustrating barriers.**

Bad constraint: "You can only play 2 hours per day"
Good constraint: "Staying too long in one era attracts the attention of forces beyond your control"

### 1.3 Learning from Existing Games

| Game | Mechanic | What Works | What Doesn't |
|------|----------|------------|--------------|
| Darkest Dungeon | Stress/Afflictions | Creates tension, meaningful retreat decisions | Can feel punishing, RNG-heavy |
| Don't Starve | Sanity meter | Visible consequence, atmospheric | Binary (sane/insane) |
| The Long Dark | Multi-need survival | Interlocking systems, planning required | Can become micromanagement |
| EVE Online | Security zones | Risk/reward scaling, player choice | Grief-able in low-sec |
| Majora's Mask | Time loop | Creates urgency, forces prioritization | Frustrating if lose progress |
| Rust | Full loot PvP | High stakes | Extremely toxic, offline raiding |

**Our approach:** Take the tension-creating aspects while adding consequences that generate valuable behavioral data rather than pure punishment.

---

## 2. Core Survival Systems

### 2.1 The Four Meters

Every character has four survival meters that must be managed:

```
┌─────────────────────────────────────────────────────────────┐
│  SURVIVAL STATUS                                            │
│  ═══════════════════════════════════════════════════════    │
│                                                             │
│  HUNGER    ████████████████░░░░░░░░░░ 65%                  │
│            Status: Satisfied | Next meal needed: 4 hours    │
│                                                             │
│  THIRST    ██████████████████████░░░░ 85%                  │
│            Status: Hydrated | Water source nearby           │
│                                                             │
│  HEALTH    ███████████████████████░░░ 92%                  │
│            Status: Healthy | Minor scrape (-2%)             │
│                                                             │
│  STAMINA   ████████████████████░░░░░░ 75%                  │
│            Status: Rested | Recovering from labor           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Hunger System

```yaml
hunger:
  decay_rate: "10% per in-game day"

  thresholds:
    satisfied: [70, 100]      # Full effectiveness
    hungry: [40, 70]          # -10% work efficiency
    famished: [15, 40]        # -30% efficiency, -5% health/day
    starving: [0, 15]         # -50% efficiency, -15% health/day
    death: 0                  # After 3 days at 0%

  food_quality:
    raw_food: "+15% hunger, 20% disease chance"
    cooked_simple: "+25% hunger, 5% disease chance"
    cooked_quality: "+35% hunger, health bonus"
    preserved: "+20% hunger, lasts longer"
    spoiled: "+10% hunger, 60% disease chance"

  era_variations:
    ancient: "Food scarcity common, preservation difficult"
    classical: "Better storage, trade networks"
    medieval: "Famines periodic, food as status"
    industrial: "Quantity available, quality varies"
    modern: "Abundance, but crisis scenarios"
```

### 2.3 Thirst System

```yaml
thirst:
  decay_rate: "15% per in-game day (faster than hunger)"

  thresholds:
    hydrated: [60, 100]       # Full effectiveness
    thirsty: [30, 60]         # -15% efficiency
    dehydrated: [10, 30]      # -40% efficiency, -10% health/day
    critical: [0, 10]         # Hallucinations, -25% health/day
    death: 0                  # After 2 days at 0%

  water_sources:
    clean_spring: "100% safe"
    river_water: "30% disease chance without treatment"
    well_water: "10% disease chance (era-dependent)"
    rain_collection: "Safe but unreliable"
    purchased: "Safe, costs money"

  era_variations:
    ancient: "Water source = civilization"
    classical: "Aqueducts, public fountains"
    medieval: "Well contamination common"
    industrial: "Cholera epidemics, treated water emerging"
    modern: "Infrastructure, but crisis scenarios"
```

### 2.4 Health System

```yaml
health:
  base_regeneration: "5% per day if hunger/thirst satisfied"

  damage_sources:
    combat: "Variable, can be lethal"
    disease: "5-50% depending on illness"
    accident: "Labor, travel, exploration risks"
    environment: "Cold, heat, toxic exposure"
    starvation: "Hunger/thirst consequences"

  healing:
    natural: "5%/day if well-fed and rested"
    basic_medicine: "10%/day"
    skilled_healer: "15%/day"
    hospital_era: "20%/day (industrial+)"

  disease_system:
    contraction: "Food, water, contact, environment"
    progression: "Stages with increasing severity"
    treatment: "Era-appropriate medicine"
    contagion: "Can spread to others"

  injury_types:
    minor: "Heal naturally, -10% efficiency"
    moderate: "Requires treatment, -30% efficiency"
    severe: "Skilled healer needed, bedridden"
    critical: "Life-threatening, may cause death"
    permanent: "Disability, changes gameplay"
```

### 2.5 Stamina System

```yaml
stamina:
  decay_rate: "Varies by activity"
  recovery: "Sleep + food + rest"

  activities:
    light_work: "-5% per hour"
    heavy_labor: "-15% per hour"
    combat: "-25% per encounter"
    travel: "-10% per hour of walking"
    running: "-30% per hour"

  thresholds:
    energized: [70, 100]      # Full effectiveness
    tired: [40, 70]           # -10% efficiency
    exhausted: [15, 40]       # -35% efficiency, mistakes increase
    collapse: [0, 15]         # Cannot work, must rest

  sleep_requirement:
    minimum: "4 hours (exhausted next day)"
    normal: "6-8 hours (full recovery)"
    recovery: "10+ hours (healing bonus)"

  collapse_consequences:
    - "Pass out where standing"
    - "Vulnerable to theft"
    - "Health damage"
    - "Reputation impact (unreliable)"
```

### 2.6 Interlocking Systems

The survival systems interact:

```
Low Hunger → Reduced Health Regen → Slower Healing
Low Thirst → Faster Stamina Drain → Earlier Collapse
Low Health → Cannot Heavy Labor → Cannot Earn → Cannot Buy Food
Low Stamina → Cannot Travel → Stuck in Bad Location
```

**The Spiral:** If one system fails, others follow. This creates:
- Planning requirements (store food, secure water)
- Community dependence (can't do everything alone)
- Meaningful trade (survival goods have real value)
- Interesting decisions (work sick or rest and starve?)

---

## 3. The Witness System (Sanity/Trauma)

### 3.1 Design Intent

Unlike simple "sanity meters," the Witness System captures the psychological weight of living in harsh historical periods. It creates:
- Consequences for violence (even justified violence)
- Weight to witnessing suffering
- Mechanic that discourages constant combat
- Training data on trauma response

### 3.2 The Witness Meter

```
┌─────────────────────────────────────────────────────────────┐
│  THE WITNESS                                                │
│  ═══════════════════════════════════════════════════════    │
│                                                             │
│  COMPOSURE  ██████████████████░░░░░░░░░░ 72%               │
│             Status: Steady | Recent stress: Witnessed raid  │
│                                                             │
│  Active Effects: None                                       │
│  Pending: Nightmare risk tonight (15%)                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 3.3 Witness Events

Events that impact the Witness meter:

```yaml
witness_events:
  # Violence witnessed
  witness_death:
    stranger: -5
    acquaintance: -15
    friend: -30
    family_member: -50

  witness_violence:
    minor_fight: -2
    serious_assault: -10
    torture: -25
    mass_violence: -40

  # Violence committed
  commit_violence:
    self_defense: -5
    justified_combat: -10
    unprovoked_attack: -25
    killing_helpless: -50
    atrocity: -75

  # Other trauma
  near_death_experience: -20
  loss_of_home: -25
  betrayal_by_trusted: -30
  witness_plague_death: -15
  child_death_witnessed: -35

  # Positive recovery events
  recovery_events:
    good_night_sleep: +5
    community_celebration: +10
    religious_ritual: +8
    helping_others: +5
    artistic_expression: +7
    nature_peaceful: +3
    resolved_conflict: +15
```

### 3.4 Composure Thresholds

```yaml
composure_states:
  resolute: [85, 100]
    description: "Mentally strong, resistant to further stress"
    effects:
      - "Bonus to leadership"
      - "Can comfort others"
      - "Clear decision-making"

  steady: [60, 85]
    description: "Normal state, functional"
    effects:
      - "No bonuses or penalties"

  shaken: [35, 60]
    description: "Struggling but functional"
    effects:
      - "-10% work efficiency"
      - "Nightmare chance: 30%"
      - "May refuse violent actions"
      - "Dialogue options change (fearful, hesitant)"

  traumatized: [15, 35]
    description: "Severely affected, behavior changes"
    effects:
      - "-30% all efficiency"
      - "Nightmare chance: 60%"
      - "Cannot initiate violence"
      - "May flee from conflict"
      - "Affliction chance: 25%"

  broken: [0, 15]
    description: "Requires intervention"
    effects:
      - "Cannot work"
      - "Affliction certain"
      - "May harm self"
      - "Requires healer/community care"
      - "If untreated: permanent changes or death"
```

### 3.5 Afflictions

At low Composure, players develop afflictions (inspired by Darkest Dungeon):

```yaml
afflictions:
  # Negative afflictions (random when traumatized/broken)
  paranoid:
    trigger: "Composure drops below 35%"
    effects:
      - "Refuse to trade with strangers"
      - "Accuse allies of betrayal"
      - "Cannot sleep in shared spaces"
    duration: "Until Composure above 60% for 7 days"

  violent:
    trigger: "Committed violence while traumatized"
    effects:
      - "Random unprovoked attacks"
      - "Cannot de-escalate conflicts"
      - "Others avoid player"
    duration: "Until treatment or 14 days"
    consequence: "May commit crimes, face punishment"

  hopeless:
    trigger: "Repeated losses"
    effects:
      - "Refuses to plan for future"
      - "Gives away possessions"
      - "Doesn't eat properly"
    duration: "Until major positive event"

  cowardly:
    trigger: "Near-death without fighting back"
    effects:
      - "Cannot enter combat"
      - "Flee at first sign of danger"
      - "Others lose respect"
    duration: "Until successfully faces fear"

  numb:
    trigger: "Witnessed too much death"
    effects:
      - "Cannot form new relationships"
      - "No morale bonuses from positive events"
      - "Efficient but soulless"
    duration: "Until breakthrough moment"

  # Positive traits (can develop instead, ~25% chance)
  hardened:
    trigger: "Survived serious trauma with community support"
    effects:
      - "Reduced Composure loss from violence"
      - "Can comfort others"
      - "Bonus in crisis situations"

  compassionate:
    trigger: "Helped others while traumatized"
    effects:
      - "Bonus to healing others"
      - "Community reputation boost"
      - "Faster Composure recovery"
```

### 3.6 Recovery Mechanics

```yaml
recovery:
  natural:
    rate: "+5% Composure per day (if safe, fed, rested)"
    requirement: "No witness events for 24 hours"

  community:
    support_group: "+10% per session"
    religious_counsel: "+8% per session"
    celebration_feast: "+15% (once per week max)"

  professional:
    healer_treatment: "+12% per day"
    era_specific:
      ancient: "Priest/shaman rituals"
      classical: "Philosophy, baths, theater"
      medieval: "Religious confession, pilgrimage"
      industrial: "Early psychology, sanatoriums"
      modern: "Therapy, medication"

  self_care:
    artistic_expression: "+5% (crafting, music)"
    nature_retreat: "+7% per day in wilderness"
    helping_others: "+5% per act"
```

### 3.7 The Game Comes After You

If Composure stays critically low, the game world responds:

```yaml
broken_state_events:
  day_1_to_3:
    - "Nightmares prevent rest"
    - "Hallucinations begin"
    - "NPCs express concern"

  day_4_to_7:
    - "Cannot distinguish friend from foe"
    - "May attack allies"
    - "Community considers intervention"

  day_8_plus:
    - "Involuntary commitment (era-appropriate)"
    - "Character removed from play temporarily"
    - "Requires healing process (real-time days)"
    - "May emerge changed (new traits, lost skills)"

  permanent_if_untreated:
    - "Character death (narrative: lost to madness)"
    - "Or: Permanent affliction (playable but changed)"
```

---

## 4. Era Pressure: The Clock

### 4.1 The Core Mechanic

Players cannot stay in one era forever. Time pressure creates:
- Urgency to progress
- Meaningful skill/issue prioritization
- Prevention of farming/stagnation
- Training data on time-pressured decisions

### 4.2 Era Time Limits

```yaml
era_time_limits:
  ancient:
    soft_limit: 60 days
    hard_limit: 90 days
    extension_possible: "Yes, via achievements"
    max_extensions: 2
    extension_cost: "500 Legacy Points each"

  classical:
    soft_limit: 75 days
    hard_limit: 120 days
    extension_possible: "Yes"
    max_extensions: 2

  medieval:
    soft_limit: 90 days
    hard_limit: 150 days
    extension_possible: "Yes"
    max_extensions: 3

  renaissance:
    soft_limit: 90 days
    hard_limit: 150 days
    extension_possible: "Yes"
    max_extensions: 3

  industrial:
    soft_limit: 60 days
    hard_limit: 100 days
    extension_possible: "Limited"
    max_extensions: 1

  modern:
    soft_limit: 90 days
    hard_limit: 180 days
    extension_possible: "Yes"
    max_extensions: 3

  ai_era:
    soft_limit: "None"
    hard_limit: "None"
    note: "Endgame era, biome-specific challenges"
```

### 4.3 What Happens at Soft Limit

```yaml
soft_limit_effects:
  notification:
    - "The wheel of time turns. Your days in this age grow short."
    - "Forces beyond your control sense your lingering presence."

  mechanical_effects:
    day_1_to_14:
      - "Ominous signs (narrative only)"
      - "NPCs mention feeling of change"
      - "Increased difficulty of new challenges"

    day_15_to_30:
      - "Resource scarcity increases 25%"
      - "Random negative events increase"
      - "Catastrophe probability rises"
      - "New skills cannot be started"

    approaching_hard_limit:
      - "Major catastrophe guaranteed"
      - "Other players can see your 'marked' status"
      - "Era-appropriate 'forces' actively target you"
```

### 4.4 What Happens at Hard Limit

```yaml
hard_limit_catastrophe:
  mechanic: "Personal catastrophe forces transition"

  era_specific_events:
    ancient:
      - "The gods grow angry. Divine flood targets your holdings."
      - "Barbarian invasion specifically targets your settlement."
      - "Plague strikes your household with unusual severity."

    classical:
      - "Political enemies orchestrate your downfall."
      - "Accused of treason, must flee or face death."
      - "Your lands are seized by expanding empire."

    medieval:
      - "Accused of heresy by the Inquisition."
      - "The Black Death claims your community."
      - "Feudal lord strips your holdings."

    industrial:
      - "Factory fire destroys your business."
      - "Market crash wipes out your savings."
      - "Forced conscription into war."

    modern:
      - "Climate catastrophe destroys your region."
      - "Economic collapse targets your sector."
      - "Forced displacement by conflict."

  consequences:
    - "Lose 50-80% of era-specific assets"
    - "Forced reincarnation to next life"
    - "Can choose same era (new instance) or progress"
    - "Heirlooms preserved if prepared"
    - "Legacy Points still earned for time played"
```

### 4.5 Extensions

Players can buy time:

```yaml
extensions:
  first_extension:
    cost: 500 Legacy Points
    grants: "+30 days"
    requirement: "Must have completed 50% of graduation requirements"

  second_extension:
    cost: 1000 Legacy Points
    grants: "+30 days"
    requirement: "Must have completed 75% of graduation requirements"

  no_further_extensions:
    reason: "Prevents eternal stagnation"
    exception: "Keeper rank players can request review"
```

---

## 5. Theft & Asset Protection

> **See also:** [Asset Protection & Karma](asset-protection-karma.md) for complete details on the Control vs Ownership split, checkpoint system, and karma mechanics.

### 5.1 The Core Principle: Time, Not Assets

**When you're robbed, you lose TIME, not your possessions.**

Real assets (NFTs, tickets, heirlooms) create real incentive for theft. Our solution:
- Theft resets victim to last checkpoint (loses 1-4 hours progress)
- Victim KEEPS all items, currency, and possessions
- Thief gains game tokens (Shadow Marks), not victim's items
- This creates tension without devastation

### 5.2 Asset Classification

```yaml
asset_tiers:
  soul_bound:  # CANNOT be stolen
    - "Reincarnation Tickets (NFTs)"
    - "Legacy Points"
    - "Heirlooms"
    - "Codex contributions"
    - "Created IP/blueprints"

  deed_bound:  # Ownership protected, CONTROL can change
    - "Land/property NFTs"
    - "Business ownership"
    note: "Conquest takes control (80% income), owner keeps deed (20% royalty)"

  physical:  # Subject to checkpoint theft
    - "Inventory items"
    - "Currency"
    - "Crops and goods"
    note: "Victim resets to checkpoint but KEEPS these items"
```

### 5.3 The Checkpoint System

```yaml
checkpoint_theft:
  what_happens:
    1: "Thief successfully robs you"
    2: "You reset to last checkpoint"
    3: "ALL your items are still yours"
    4: "Progress since checkpoint is lost (1-4 hours)"
    5: "Thief receives Shadow Marks (game tokens)"

  checkpoints:
    auto_save: "Every 4 real-time hours"
    manual_save: "At settlements, shrines, banks"

  thief_rewards:
    pickpocket: "5-15 Shadow Marks"
    burglary: "20-40 Shadow Marks"
    heist: "50-100 Shadow Marks"

  shadow_marks_buy:
    - "Thief guild items (lockpicks, disguises)"
    - "Stealth cosmetics"
    - "Cannot buy NFTs or tradeable items"
```

### 5.3 Theft Deterrents

```yaml
theft_consequences:
  detection_chance:
    base: "40%"
    modifiers:
      witnessed: "+40%"
      victim_alert: "+30%"
      community_watch: "+25%"
      player_tracking: "+20%"  # Victim can invest in tracking

  if_detected:
    immediate:
      - "Thief marked with 'Wanted' status"
      - "Description shared with community"
      - "Victim can post bounty"

    reputation:
      - "Massive reputation loss (-50 to -80)"
      - "Banned from most communities"
      - "NPCs refuse service"
      - "Other players can attack without penalty"

    justice_system:
      ancient: "Community justice, often severe"
      classical: "Roman law, property seizure"
      medieval: "Lord's justice, corporal punishment"
      industrial: "Police, imprisonment"
      modern: "Legal system, asset seizure"

  punishment_if_caught:
    - "Stolen goods returned"
    - "Additional penalty (2-10x value)"
    - "Imprisonment (cannot play for hours/days)"
    - "Potential execution (permadeath in that era)"
    - "Permanent 'Thief' mark visible to other players"
```

### 5.4 Legitimate Acquisition

Alternatives to theft that create interesting gameplay:

```yaml
legitimate_alternatives:
  trade:
    - "Fair exchange of goods"
    - "Reputation-based pricing"
    - "Market speculation"

  contract_work:
    - "Hired for specific tasks"
    - "Reputation as reliable worker"

  competition:
    - "Sanctioned duels"
    - "Business competition"
    - "Political maneuvering"

  war_spoils:
    - "Legitimate conflict"
    - "Raid enemy settlements"
    - "Requires declaration, has rules"

  inheritance:
    - "From NPCs or players who quit"
    - "Succession planning"

  discovery:
    - "Exploration rewards"
    - "Archaeological finds"
    - "New resource locations"
```

### 5.5 Theft as Gameplay (Controlled)

For players who want thief gameplay:

```yaml
thief_gameplay:
  thief_guild:
    availability: "Classical era onwards"
    requirement: "Invitation only, reputation"
    benefits:
      - "Structured heist missions"
      - "Targets are NPCs or consenting players"
      - "Reduced detection chance"
      - "Fence services"
    constraints:
      - "Cannot steal from guild members"
      - "Cannot steal heirlooms"
      - "Must follow guild rules or be expelled"

  consenting_pvp_theft:
    mechanic: "PvP zones or mutual agreement"
    requirement: "Both parties opt-in"
    benefit: "Higher stakes, higher rewards"
    safety: "Cannot lose heirlooms or tickets"
```

---

## 6. Violence & Combat Constraints

### 6.1 Design Philosophy

Violence is part of historical life, but:
- We want strategic violence, not griefing
- Consequences must discourage casual violence
- Training data should capture decision-making, not murder simulators

### 6.2 Violence Initiation Rules

```yaml
violence_rules:
  unprovoked_attack:
    definition: "Attacking player who hasn't attacked or threatened you"
    consequences:
      - "Witness penalty (Composure -25)"
      - "Reputation loss (-30)"
      - "Marked as 'Aggressor' for 48 hours"
      - "Victim can retaliate without penalty"
      - "Community may intervene"

  self_defense:
    definition: "Responding to attack or credible threat"
    consequences:
      - "Witness penalty (Composure -5)"
      - "No reputation loss"
      - "Justified in community eyes"

  declared_conflict:
    definition: "War, raid, or duel with proper declaration"
    consequences:
      - "Witness penalty (Composure -10 per combat)"
      - "No reputation loss for declared actions"
      - "Rules of engagement apply"

  mutual_combat:
    definition: "Both parties agree to fight"
    consequences:
      - "Witness penalty (Composure -5)"
      - "No reputation loss"
      - "Spectators can watch"
```

### 6.3 Safe Zones

```yaml
safe_zones:
  settlement_core:
    protection: "No PvP combat"
    enforcement: "Guards intervene, instant reputation penalty"
    exceptions: "Declared duels in designated areas"

  trade_routes:
    protection: "Reduced but not eliminated"
    enforcement: "Patrols, reporting system"
    risk: "Bandits (NPCs) exist, player bandits heavily penalized"

  wilderness:
    protection: "None"
    note: "PvP possible but still has reputation consequences"
    recommendation: "Travel in groups"

  war_zones:
    protection: "None between declared enemies"
    note: "Civilians protected by rules of engagement"
```

### 6.4 Combat Frequency Limits

```yaml
combat_limits:
  witness_accumulation:
    problem: "Players who constantly fight lose Composure rapidly"
    effect: "Self-limiting through Witness system"

  physical_limits:
    stamina_cost: "-25% per combat"
    injury_risk: "Increases with each fight"
    recovery_needed: "Cannot chain fights indefinitely"

  social_limits:
    reputation: "Known fighters have fewer options"
    services: "Healers may refuse chronic fighters"
    community: "May be exiled for too much violence"

  era_specific:
    ancient: "Violence more accepted, but still has consequences"
    classical: "Structured (gladiators, legions) channels violence"
    medieval: "Church attempts to limit (Peace of God)"
    industrial: "Police force, civilization expectations"
    modern: "Strong legal system, high consequences"
```

---

## 7. Behavioral Consequences

### 7.1 Reputation System

```yaml
reputation:
  scale: [-100, 100]

  brackets:
    revered: [80, 100]
      effects:
        - "Best prices, first access to opportunities"
        - "Community defends you"
        - "Leadership positions available"

    respected: [50, 80]
      effects:
        - "Good prices, welcome everywhere"
        - "Benefit of the doubt in disputes"

    neutral: [0, 50]
      effects:
        - "Normal prices and access"
        - "Must prove yourself"

    distrusted: [-30, 0]
      effects:
        - "Higher prices, limited access"
        - "Watched by community"
        - "Harder to find work"

    outcast: [-60, -30]
      effects:
        - "Refused service by most"
        - "Cannot enter many settlements"
        - "Target for 'justice'"

    enemy: [-100, -60]
      effects:
        - "Kill on sight by community"
        - "No safe haven"
        - "Bounties placed automatically"
```

### 7.2 Reputation Actions

```yaml
reputation_changes:
  positive:
    help_stranger: +5
    fulfill_contract: +3
    donate_to_community: +5 to +20
    save_life: +15
    codex_contribution: +2
    resolve_conflict: +10
    defend_community: +20
    leadership_success: +15

  negative:
    break_contract: -10
    theft_attempted: -20
    theft_successful: -30
    unprovoked_violence: -30
    murder: -50
    betray_ally: -40
    harm_innocent: -35
    refuse_community_duty: -5
```

### 7.3 Community Response

```yaml
community_response:
  exile:
    trigger: "Reputation below -60 in a community"
    effect: "Banned from settlement"
    appeal: "Possible after 30 days + restitution"

  bounty:
    trigger: "Serious crimes against community members"
    effect: "Other players paid to capture/kill"
    duration: "Until fulfilled or paid off"

  blacklist:
    trigger: "Multiple communities exile you"
    effect: "Known troublemaker, word spreads"
    recovery: "Very difficult, requires major positive acts"

  redemption:
    available: "Always"
    method: "Time + positive actions + restitution"
    note: "The game always provides path back"
```

---

## 8. Graduation Requirements

### 8.1 What You Must Learn

Each era has skills that must be mastered before progression:

```yaml
graduation_skills:
  ancient:
    required_skills: [3 of 5]
    options:
      - basic_agriculture: "Grow enough food to survive"
      - basic_crafting: "Create tools and goods"
      - community_living: "Function in tribal society"
      - basic_trade: "Exchange goods fairly"
      - survival_basics: "Manage hunger, thirst, health"

    skill_mastery_requirement: "Level 3 (Competent)"

  classical:
    required_skills: [4 of 6]
    options:
      - specialized_craft: "Excel at one trade"
      - civic_participation: "Engage with governance"
      - advanced_trade: "Multi-party deals, contracts"
      - literacy: "Read and write (era-appropriate)"
      - military_basics: "Understand organized conflict"
      - philosophy: "Ethical reasoning"

  medieval:
    required_skills: [4 of 6]
    options:
      - guild_mastery: "Rise in guild hierarchy"
      - land_management: "Run an estate or farm"
      - religious_literacy: "Understand faith systems"
      - crisis_survival: "Survive plague, famine, war"
      - navigation: "Travel and trade routes"
      - record_keeping: "Manage accounts and documents"

  renaissance:
    required_skills: [4 of 6]
    options:
      - scientific_method: "Experiment and observe"
      - cultural_production: "Create art or literature"
      - exploration: "Navigate new territories"
      - banking: "Understand finance and credit"
      - cross_cultural: "Deal with different peoples"
      - printing: "Spread information"

  industrial:
    required_skills: [4 of 6]
    options:
      - factory_operations: "Manage industrial process"
      - labor_organization: "Worker or manager skills"
      - urban_survival: "Navigate city life"
      - technological_adaptation: "Adopt new technologies"
      - mass_communication: "Newspapers, telegraph"
      - social_reform: "Understand change movements"
```

### 8.2 What You Must Solve

Each era has "Keystone Challenges" - complex issues that must be addressed:

```yaml
keystone_challenges:
  ancient:
    required: 2 of 3
    challenges:
      the_great_flood:
        description: "Survive and help community recover from flood"
        skills_tested: ["crisis_leadership", "resource_management", "community_coordination"]
        training_data: "Disaster response decision-making"

      the_first_laws:
        description: "Help establish or reform community legal code"
        skills_tested: ["negotiation", "ethical_reasoning", "conflict_resolution"]
        training_data: "Justice system design"

      the_bronze_secret:
        description: "Adopt or spread new technology"
        skills_tested: ["learning", "teaching", "adaptation"]
        training_data: "Technology adoption patterns"

  classical:
    required: 2 of 3
    challenges:
      the_democratic_experiment:
        description: "Participate meaningfully in governance"
        skills_tested: ["rhetoric", "coalition_building", "civic_duty"]
        training_data: "Democratic participation"

      the_road_network:
        description: "Establish or maintain trade infrastructure"
        skills_tested: ["logistics", "diplomacy", "investment"]
        training_data: "Infrastructure decision-making"

      the_fall_prevention:
        description: "Address systemic problems threatening society"
        skills_tested: ["systems_thinking", "reform", "leadership"]
        training_data: "Civilizational maintenance"

  medieval:
    required: 2 of 3
    challenges:
      the_black_death:
        description: "Navigate pandemic response"
        skills_tested: ["crisis_management", "medical_knowledge", "community_care"]
        training_data: "Pandemic behavior"

      the_knowledge_preservation:
        description: "Protect and transmit knowledge through dark times"
        skills_tested: ["scholarship", "teaching", "resource_allocation"]
        training_data: "Knowledge preservation"

      the_guild_formation:
        description: "Organize workers for mutual benefit"
        skills_tested: ["organization", "negotiation", "quality_standards"]
        training_data: "Labor organization"

  industrial:
    required: 2 of 3
    challenges:
      the_labor_rights:
        description: "Navigate worker-owner tensions"
        skills_tested: ["negotiation", "organization", "ethical_business"]
        training_data: "Labor relations"

      the_urban_health:
        description: "Address public health in crowded cities"
        skills_tested: ["public_health", "infrastructure", "policy"]
        training_data: "Public health decision-making"

      the_displacement:
        description: "Adapt to technological unemployment"
        skills_tested: ["retraining", "entrepreneurship", "resilience"]
        training_data: "Technological disruption response"
```

### 8.3 Graduation Process

```yaml
graduation:
  requirements:
    skills: "Meet skill requirements for era"
    challenges: "Complete required keystone challenges"
    time_minimum: "30 days in era"
    time_maximum: "Hard limit (see Era Pressure)"
    standing: "Reputation above 0"

  process:
    1_eligible: "System notifies you're eligible"
    2_preparation: "7-day preparation window"
    3_final_challenge: "Era finale event (optional but rewarding)"
    4_transition: "Choose next era or repeat"

  rewards:
    legacy_points: "500-2000 depending on achievements"
    skill_carryover: "Knowledge adapts to new era"
    reputation_bonus: "Start with +20 in new era"
    ticket_progress: "Counts toward Ascension Ticket"
```

---

## 9. Death & Permadeath

### 9.1 Death Causes

```yaml
death_causes:
  survival_failure:
    starvation: "3 days at 0% hunger"
    dehydration: "2 days at 0% thirst"
    injury: "Health reaches 0%"
    disease: "Untreated severe illness"

  violence:
    combat: "Defeated in battle"
    execution: "Justice system punishment"
    assassination: "Targeted killing"

  accident:
    labor: "Industrial accident, construction collapse"
    travel: "Shipwreck, bandit attack, animal attack"
    environment: "Extreme weather, natural disaster"

  old_age:
    natural: "Characters age and eventually die"
    timeline: "40-80 years depending on era and care"

  psychological:
    broken: "Witness meter at 0% too long"
    result: "Death or permanent institutionalization"
```

### 9.2 Near-Death and Rescue

```yaml
near_death:
  downed_state:
    trigger: "Health reaches 5%"
    duration: "5 real-time minutes"
    can_be_rescued: true
    can_be_finished: true

  rescue_requirements:
    - "Another player or NPC nearby"
    - "Basic medical supplies"
    - "Time to stabilize"

  self_stabilization:
    possible: "If have medical supplies"
    success_rate: "30%"
    consequence: "Severe injury if successful"

  if_not_rescued:
    death: "Permanent for this character"
    transition: "To Legacy System / next life"
```

### 9.3 What Happens on Death

```yaml
death_process:
  immediate:
    - "Character control ends"
    - "Final moments narrated"
    - "Biography generated"

  transition:
    - "Death summary screen"
    - "Legacy Points awarded"
    - "Achievements logged"
    - "Heirloom fate determined"

  inheritance:
    - "Choose next character options"
    - "Inherit based on preparation"
    - "Bloodline continues"

  body:
    - "Can be looted (inventory only)"
    - "Can be buried (reputation for others)"
    - "Grave becomes memorial (if community does it)"
```

### 9.4 Anti-Griefing in Death

```yaml
death_protection:
  offline_protection:
    - "Characters 'sleep' when logged out"
    - "Cannot be killed while sleeping (safe zone)"
    - "Wake up if danger approaches (notification)"

  corpse_camping:
    - "Spawn point is protected zone"
    - "Killer flagged if loiters near spawn"
    - "Community alerts triggered"

  new_player_protection:
    - "First 48 hours: reduced death consequences"
    - "First 3 deaths: faster recovery"
    - "Tutorial zone: no PvP death"
```

---

## 10. Karma & Reincarnation

> **See also:** [Asset Protection & Karma](asset-protection-karma.md) for complete karma mechanics and animal reincarnation details.

### 10.1 The Karma Principle

**How you play determines how you reincarnate.**

Karma is not a punishment system - it's a consequence system that makes violence meaningful across lives.

```yaml
karma_scale: [-1000, 1000]

brackets:
  enlightened: [800, 1000]     # Choose next life
  virtuous: [400, 800]         # Human, favorable
  balanced: [-200, 400]        # Human, normal
  troubled: [-500, -200]       # Human, difficult start
  corrupted: [-800, -500]      # 50% chance animal life
  damned: [-1000, -800]        # 100% animal life
```

### 10.2 Karma Actions

```yaml
positive_karma:
  save_life: +25
  help_stranger: +5
  peaceful_resolution: +20
  sacrifice_for_others: +30
  codex_contribution: +5

negative_karma:
  murder: -50
  murder_innocent: -100
  theft: -15
  betrayal: -40
  torture: -100

neutral:
  self_defense: 0
  declared_war_combat: -5
```

### 10.3 Animal Reincarnation

If you die with severely negative karma, you reincarnate as an animal:

```yaml
animal_life:
  corrupted: [-800, -500]
    chance: "50%"
    animals: ["dog", "horse", "cat"]
    duration: "7-14 real-time days"

  damned: [-1000, -800]
    chance: "100%"
    animals: ["mule", "pig", "rat"]
    duration: "14-30 real-time days"

  experience:
    communication: "Cannot speak, limited emotes"
    autonomy: "Must follow owner commands"
    owner: "Random player or NPC (doesn't know you're a player)"

  ending_animal_life:
    duration_expires: "Reincarnate human (difficult circumstances)"
    owner_frees_you: "Immediate human reincarnation + karma bonus"
    heroic_act: "Immediate human reincarnation + major karma bonus"
    death_as_animal: "Reincarnate as different animal, duration resets"
```

### 10.4 Training Data Value

Animal reincarnation generates unique training data:
- How do humans experience loss of agency?
- How do owners treat beings they perceive as non-persons?
- What creates loyalty under constraint?
- How does perspective shift affect empathy?

---

## 11. Toxicity Prevention

### 11.1 Communication Rules

```yaml
communication:
  chat_moderation:
    automated:
      - "Slur filtering (blocked)"
      - "Spam detection (rate limited)"
      - "Scam pattern detection (flagged)"

    player_reporting:
      - "Report button on all messages"
      - "Context included automatically"
      - "Pattern detection across reports"

    human_review:
      - "All bans reviewed by human"
      - "Appeals process available"

  consequences:
    first_offense: "Warning + 24h chat mute"
    second_offense: "7-day chat restriction"
    third_offense: "30-day chat ban"
    severe: "Permanent ban (reviewed)"
    egregious: "Immediate permanent ban"
```

### 10.2 Harassment Prevention

```yaml
harassment:
  definition:
    - "Repeated unwanted contact"
    - "Following player between instances"
    - "Coordinated targeting"
    - "Doxxing or real-world threats"

  tools:
    block: "Completely hide player from view"
    report: "Flag for review"
    safe_mode: "Temporary instance where only friends visible"

  consequences:
    confirmed_harassment:
      - "Warning to permanent ban (severity dependent)"
      - "Victim's character relocated if desired"
      - "Harasser assets may be seized"
```

### 10.3 Exploits and Cheating

```yaml
cheating:
  detection:
    - "Statistical anomaly detection"
    - "Player reports"
    - "Automated behavior analysis"

  types:
    exploitation: "Using bugs for advantage"
    automation: "Bots, macros beyond simple"
    real_money_trading: "Unauthorized RMT"
    account_sharing: "Multiple users, one account"

  consequences:
    minor_exploit: "Warning, gains reversed"
    major_exploit: "Temporary ban, gains reversed"
    automation: "Permanent ban"
    rmt_selling: "Permanent ban"
    rmt_buying: "Warning → temp ban → permanent"
```

### 10.4 Positive Community Features

```yaml
positive_systems:
  honor_system:
    - "Players can commend good behavior"
    - "Visible honor level"
    - "Rewards for high honor"

  mentor_program:
    - "Experienced players help new"
    - "Mentor rewards for successful mentees"
    - "Mentee protection period"

  community_events:
    - "Cooperative challenges"
    - "Shared achievements"
    - "Community goals with collective rewards"

  positive_reputation:
    - "Being helpful is visible and rewarded"
    - "Community builders recognized"
    - "Good standing opens opportunities"
```

---

## 12. Training Data Implications

### 12.1 What Constraints Teach Us

Each constraint system generates valuable behavioral data:

```yaml
training_data_by_system:
  survival:
    data_type: "Resource management under scarcity"
    questions:
      - "How do humans prioritize competing needs?"
      - "When do people share vs hoard?"
      - "How does desperation change decisions?"

  witness:
    data_type: "Psychological response to trauma"
    questions:
      - "What helps humans recover from trauma?"
      - "How does violence change behavior?"
      - "What creates resilience vs breakdown?"

  era_pressure:
    data_type: "Decision-making under time pressure"
    questions:
      - "How do humans prioritize when time is limited?"
      - "What do people choose to accomplish vs abandon?"
      - "How does urgency affect quality of decisions?"

  theft_violence:
    data_type: "Moral boundaries and consequences"
    questions:
      - "What conditions lead to rule-breaking?"
      - "How do consequences affect behavior?"
      - "What's the threshold for 'justified' transgression?"

  graduation:
    data_type: "Skill acquisition and problem-solving"
    questions:
      - "How do humans approach complex multi-factor problems?"
      - "What learning strategies emerge?"
      - "How do people collaborate on challenges?"
```

### 12.2 Anti-Gaming the Data

```yaml
data_quality:
  concern: "Players might behave artificially to 'game' the system"

  mitigations:
    hidden_metrics:
      - "Never show exact training data value"
      - "Rewards based on engagement, not specific behaviors"

    variety_requirement:
      - "Same behavior patterns lose novelty value"
      - "Diverse approaches rewarded"

    authenticity_detection:
      - "Statistical analysis of behavior patterns"
      - "Flag suspicious uniformity"

    meaningful_stakes:
      - "Real consequences make decisions genuine"
      - "Can't just 'experiment' without cost"
```

---

## Appendix: Quick Reference

### Survival Thresholds

| Meter | Green | Yellow | Red | Critical |
|-------|-------|--------|-----|----------|
| Hunger | 70-100% | 40-70% | 15-40% | 0-15% |
| Thirst | 60-100% | 30-60% | 10-30% | 0-10% |
| Health | 50-100% | 25-50% | 10-25% | 0-10% |
| Stamina | 70-100% | 40-70% | 15-40% | 0-15% |
| Composure | 85-100% | 60-85% | 35-60% | 0-35% |

### Era Time Limits

| Era | Soft Limit | Hard Limit | Extensions |
|-----|------------|------------|------------|
| Ancient | 60 days | 90 days | 2 |
| Classical | 75 days | 120 days | 2 |
| Medieval | 90 days | 150 days | 3 |
| Renaissance | 90 days | 150 days | 3 |
| Industrial | 60 days | 100 days | 1 |
| Modern | 90 days | 180 days | 3 |

### Reputation Brackets

| Bracket | Range | Summary |
|---------|-------|---------|
| Revered | 80-100 | Best treatment everywhere |
| Respected | 50-80 | Welcome, good standing |
| Neutral | 0-50 | Normal treatment |
| Distrusted | -30-0 | Watched, limited access |
| Outcast | -60--30 | Refused most places |
| Enemy | -100--60 | Kill on sight |

---

*Constraints are not prison bars. They are the gravity that gives weight to your choices.*
