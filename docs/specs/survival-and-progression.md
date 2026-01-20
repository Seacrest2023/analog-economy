# The Analog Economy: Survival & Progression System

> **Version:** 1.0
> **Last Updated:** 2026-01-19
> **Status:** Draft

---

## Executive Summary

The Analog Economy begins with the fundamental challenge of human survival. Players start with nothing and must figure out how to stay alive, build resources, and eventually thrive. This mirrors humanity's actual journey and generates invaluable training data about human decision-making under pressure.

**Core Insight:** The game captures the full spectrum of human survival strategies—ethical and unethical—because understanding both is essential for AI training.

---

## Table of Contents

1. [The Starting State](#the-starting-state)
2. [Survival Variables](#survival-variables)
3. [Survival Strategies](#survival-strategies)
4. [Risk Assessment System](#risk-assessment-system)
5. [Progression Path](#progression-path)
6. [The Invention Framework](#the-invention-framework)
7. [Commerce & Trade](#commerce--trade)
8. [Training Data Value](#training-data-value)

---

## The Starting State

### What Every Player Begins With

```
┌─────────────────────────────────────────────────────────────┐
│                    STARTING INVENTORY                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Basic Tools (Soulbound - Cannot Trade)                     │
│  ├── Basic knife (cutting, self-defense)                    │
│  ├── Flint & steel (fire-starting)                          │
│  ├── Small waterskin (empty)                                │
│  ├── Worn clothes (minimal protection)                      │
│  └── Small pouch (inventory: 10 slots)                      │
│                                                             │
│  Currency: 0 NVT                                            │
│  Health: 100%                                               │
│  Hunger: 80% (need food soon)                               │
│  Thirst: 70% (need water soon)                              │
│  Energy: 100%                                               │
│  Morale: 50% (uncertain, anxious)                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### The First Crisis

Within the first 30 minutes of gameplay, players face a critical decision:

```
You wake up in [BIOME] with nothing but basic tools.
Night is coming. You're hungry. You're thirsty.
What do you do?

This moment—and how millions of players respond—
is incredibly valuable training data.
```

---

## Survival Variables

### Primary Needs (Inspired by: Naked and Afraid, Alone, Survivor)

| Variable | Range | Decline Rate | Death Threshold | Recovery Method |
|----------|-------|--------------|-----------------|-----------------|
| **Hunger** | 0-100 | -5/hour | 0 = death in 24h | Food consumption |
| **Thirst** | 0-100 | -10/hour | 0 = death in 8h | Water consumption |
| **Health** | 0-100 | Varies | 0 = permadeath | Rest, medicine, treatment |
| **Energy** | 0-100 | -3/hour active | 0 = collapse | Sleep, rest |
| **Body Temp** | 95-104°F | Environment-based | <95 or >104 = death | Shelter, fire, shade |
| **Morale** | 0-100 | -2/hour alone | 0 = despair debuffs | Social, achievements |

### Environmental Threats

```yaml
environmental_threats:
  # Temperature
  hypothermia:
    trigger: "body_temp < 95°F for 30 min"
    effect: "health -5/min, coordination -50%"
    prevention: ["fire", "shelter", "warm_clothing", "physical_activity"]

  heat_stroke:
    trigger: "body_temp > 104°F for 20 min"
    effect: "health -8/min, confusion, collapse"
    prevention: ["shade", "water", "rest", "cooling"]

  # Dehydration progression
  dehydration:
    stages:
      mild: {thirst: "<50", effects: ["energy -20%"]}
      moderate: {thirst: "<25", effects: ["energy -50%", "confusion"]}
      severe: {thirst: "<10", effects: ["health -10/hour", "hallucinations"]}

  # Starvation progression
  starvation:
    stages:
      hungry: {hunger: "<50", effects: ["energy -10%"]}
      starving: {hunger: "<25", effects: ["energy -40%", "health -2/hour"]}
      critical: {hunger: "<10", effects: ["health -10/hour", "weakness"]}

  # Exposure
  exposure:
    rain_without_shelter: "health -3/hour, hypothermia risk"
    sun_without_shade: "dehydration +50%, heat stroke risk"
    wind_without_cover: "body_temp drop accelerated"

  # Wildlife
  predators:
    - type: "wolves"
      behavior: "hunt weak/injured players"
      deterrent: ["fire", "group_size > 3", "weapons"]
    - type: "bears"
      behavior: "territorial, food attracted"
      deterrent: ["noise", "distance", "playing_dead"]
    - type: "snakes"
      behavior: "hidden, defensive"
      deterrent: ["awareness", "boots", "stick_probing"]

  # Disease
  illness:
    contaminated_water: "dysentery (health -5/hour for 48h)"
    raw_meat: "food_poisoning (health -3/hour for 24h)"
    infected_wound: "sepsis risk (health -10/hour if untreated)"
    insect_bites: "disease_vector (malaria, etc.)"
```

### Psychological Factors

```yaml
psychological_state:
  morale:
    boosters:
      - "social_interaction: +10"
      - "achievement: +15"
      - "good_meal: +5"
      - "safe_shelter: +5/hour"
      - "helping_others: +10"
    drains:
      - "isolation: -2/hour"
      - "near_death: -20"
      - "witnessing_death: -15"
      - "failure: -10"
      - "betrayal: -25"

  loneliness:
    threshold: "24 hours without human contact"
    effects:
      - "morale drain accelerated"
      - "hallucination chance"
      - "risk-taking increase"
      - "desperation behaviors"

  desperation:
    trigger: "morale < 20 OR multiple needs critical"
    effects:
      - "ethical threshold lowered"
      - "risk tolerance increased"
      - "crime options more appealing"
      - "cooperation harder"
```

---

## Survival Strategies

### The Ethical Spectrum

Players can survive through various strategies, each generating different training data:

```
┌─────────────────────────────────────────────────────────────┐
│              SURVIVAL STRATEGY SPECTRUM                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ETHICAL                                    UNETHICAL       │
│  ◄─────────────────────────────────────────────────────►    │
│                                                             │
│  Self-Reliance    Community    Gray Area    Crime           │
│  ├── Forage       ├── Church   ├── Begging  ├── Theft      │
│  ├── Hunt         ├── Guild    ├── Gambling ├── Robbery    │
│  ├── Build        ├── Work     ├── Scams    ├── Violence   │
│  └── Craft        └── Trade    └── Cults    └── Murder     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Strategy 1: Self-Reliance (Survivalist)

**Philosophy:** "I don't need anyone. I'll live off the land."

```yaml
self_reliance:
  activities:
    foraging:
      description: "Find edible plants, berries, roots"
      skill_required: "botany_knowledge"
      risks: ["poisonous_plants", "low_calories"]
      rewards: ["food +10-30", "no_dependency"]

    hunting:
      description: "Hunt animals for meat"
      skill_required: "tracking, weapon_proficiency"
      risks: ["injury", "predator_encounter", "failure"]
      rewards: ["food +50-100", "materials (fur, bone)"]

    fishing:
      description: "Catch fish from water sources"
      skill_required: "patience, location_knowledge"
      risks: ["time_investment", "weather_dependent"]
      rewards: ["food +20-60", "consistent_source"]

    shelter_building:
      description: "Construct lean-to, debris hut, etc."
      types:
        lean_to:
          time: "2-4 hours"
          protection: "40%"
          materials: "branches, leaves"
        debris_hut:
          time: "4-8 hours"
          protection: "70%"
          materials: "many branches, debris, leaves"
        log_cabin:
          time: "days (with tools)"
          protection: "95%"
          materials: "logs, tools, significant time"

    fire_craft:
      description: "Start and maintain fire"
      benefits: ["warmth", "cooking", "predator_deterrent", "morale"]
      challenges: ["wet_conditions", "fuel_gathering"]

  training_data_value:
    captures: "Human problem-solving in isolation"
    valuable_for: "Autonomous robot survival, Mars colonization AI"
```

### Strategy 2: Community (Social)

**Philosophy:** "Humans survived by working together. I'll find my tribe."

```yaml
community:
  options:
    church:
      description: "Seek help from religious institutions"
      approach: "Go to local church/temple, ask for aid"
      potential_outcomes:
        - "Receive food, shelter, clothing"
        - "Expected to participate in services"
        - "Community support network"
        - "Possible recruitment to causes"
      requirements: ["respect_customs", "participation"]

    guild_joining:
      description: "Join a player-run organization"
      types:
        - "Crafting guilds"
        - "Hunting parties"
        - "Trading caravans"
        - "Protection groups"
      benefits: ["shared_resources", "protection", "knowledge"]
      costs: ["dues", "obligations", "rules"]

    work_for_others:
      description: "Find employment in town"
      job_types:
        manual_labor:
          pay: "5-10 NVT/hour"
          skill: "none"
          risk: "low"
        skilled_trade:
          pay: "15-30 NVT/hour"
          skill: "required"
          risk: "low"
        dangerous_work:
          pay: "30-50 NVT/hour"
          skill: "varies"
          risk: "high (mining, guarding)"

    helping_strangers:
      description: "Offer help to travelers"
      outcomes:
        - "Payment or trade"
        - "Information about opportunities"
        - "Alliance formation"
        - "Reputation building"

  training_data_value:
    captures: "Social cooperation dynamics, trust building"
    valuable_for: "AI social behavior, group dynamics modeling"
```

### Strategy 3: Gray Area (Morally Ambiguous)

**Philosophy:** "I'll do what I have to. The line is... flexible."

```yaml
gray_area:
  options:
    begging:
      description: "Ask others for help/money"
      effectiveness: "variable (based on appearance, story)"
      reputation_impact: "-5 per encounter"
      moral_classification: "neutral"

    gambling:
      description: "Risk what little you have for more"
      games: ["dice", "cards", "betting"]
      risk: "lose everything"
      reward: "multiply resources"
      addiction_mechanic: "morale boost, then dependency"

    fake_injury_scam:
      description: "Pretend to be hurt to get help, then..."
      variations:
        - "Accept help genuinely (gray → ethical)"
        - "Steal from helper (gray → crime)"
        - "Ask for excessive help (manipulation)"
      detection_risk: "reputation destroyed if caught"
      training_data_value: "social engineering patterns"

    cult_creation:
      description: "Create a 'religion' to attract followers"
      mechanics:
        - "Develop belief system"
        - "Promise salvation/prosperity"
        - "Recruit vulnerable players"
        - "Extract resources/labor"
      ethical_spectrum: "from genuine community to exploitation"
      gaian_monitoring: "flags exploitative patterns"
      training_data_value: "influence, persuasion, manipulation"

    information_selling:
      description: "Gather and sell information"
      types:
        - "Player locations"
        - "Hidden resource sites"
        - "Trade route timing"
        - "Weakness/vulnerabilities"
      risk: "dangerous if discovered"

  training_data_value:
    captures: "Human behavior at ethical boundaries"
    valuable_for: "Fraud detection, social manipulation recognition"
```

### Strategy 4: Crime (Unethical)

**Philosophy:** "Take what you need. Survival of the fittest."

```yaml
crime:
  options:
    theft:
      description: "Steal from others or locations"
      types:
        pickpocket:
          risk: "medium (detection)"
          reward: "small items, coins"
          skill: "sleight_of_hand"
        burglary:
          risk: "high (if caught)"
          reward: "larger haul"
          skill: "lockpicking, stealth"
        shoplifting:
          risk: "medium"
          reward: "goods"
          consequences: "banned from shop, bounty"

    robbery:
      description: "Take from others by force/threat"
      approaches:
        ambush:
          description: "Wait for isolated travelers"
          risk: "victim may fight back"
          reward: "everything they carry"
        intimidation:
          description: "Threaten without violence"
          success_rate: "depends on relative strength"
          reputation: "-20 per incident"

    fake_helplessness:
      description: "Lure helpers then rob them"
      setup: "Appear injured/stranded"
      execution: "Attack when they approach"
      reputation: "-50 (severe betrayal)"
      bounty: "placed by victim and witnesses"

    violence:
      description: "Attack others directly"
      consequences:
        - "Permadeath risk for victim"
        - "Bounty system activates"
        - "NPC guards/players hunt you"
        - "Safe zones closed to you"

  consequences:
    bounty_system:
      description: "Crimes create bounties"
      mechanics:
        - "Victims can place bounties"
        - "Witnesses report crimes"
        - "Bounty hunters pursue"
        - "Higher bounty = more hunters"
      clearing: "Serve time, pay restitution, or escape"

    reputation:
      criminal: "< -50 reputation"
      effects:
        - "NPCs refuse service"
        - "Players avoid/attack on sight"
        - "Towns closed to entry"
        - "Prices increase (black market only)"

    karma:
      description: "Long-term consequences"
      effects:
        - "RNG slightly worse for criminals"
        - "Positive encounters less likely"
        - "Betrayal more likely against you"

  training_data_value:
    captures: "Criminal behavior patterns, desperation decisions"
    valuable_for: "Security AI, crime prediction, threat assessment"
    gaian_note: "Data abstracted - not teaching 'how to crime'"
```

---

## Risk Assessment System

### Every Action Has Risk/Reward

```python
class RiskAssessmentEngine:
    """
    Evaluates the risk profile of every player action.
    This data is GOLD for AI training.
    """

    def assess_action(self, action: PlayerAction, context: GameContext) -> RiskProfile:
        """
        Calculate risk/reward for a proposed action.
        """
        # Base risk factors
        physical_risk = self._calculate_physical_risk(action, context)
        social_risk = self._calculate_social_risk(action, context)
        resource_risk = self._calculate_resource_risk(action, context)

        # Potential rewards
        immediate_reward = self._calculate_immediate_reward(action)
        long_term_reward = self._calculate_long_term_reward(action)

        # Context modifiers
        desperation_modifier = self._get_desperation_modifier(context.player_state)
        group_modifier = self._get_group_modifier(context.nearby_players)

        return RiskProfile(
            total_risk=physical_risk + social_risk + resource_risk,
            total_reward=immediate_reward + long_term_reward,
            risk_reward_ratio=total_risk / max(total_reward, 0.1),
            recommended=total_reward > total_risk * 1.5,
            alternatives=self._suggest_alternatives(action, context)
        )
```

### The Congregation Insight

**Historical Truth:** Humans survived by grouping together. Solo survival is possible but higher risk.

```yaml
congregation_dynamics:
  evolutionary_advantage:
    description: "Humans are social animals for survival reasons"

  risk_comparison:
    solo_survival:
      mortality_rate: "40% in first week"
      resource_efficiency: "low"
      predator_defense: "minimal"
      knowledge_sharing: "none"
      morale: "declines rapidly"

    paired_survival:
      mortality_rate: "25% in first week"
      resource_efficiency: "medium"
      predator_defense: "improved"
      knowledge_sharing: "limited"
      morale: "stable"

    group_survival:  # 3-8 people
      mortality_rate: "10% in first week"
      resource_efficiency: "high (specialization)"
      predator_defense: "strong"
      knowledge_sharing: "significant"
      morale: "positive"

    community_survival:  # 8+ people
      mortality_rate: "5% in first week"
      resource_efficiency: "very high"
      predator_defense: "excellent"
      knowledge_sharing: "extensive"
      morale: "community dependent"

  game_mechanic:
    description: "Players who group up have statistical advantages"
    implementation:
      - "Shared watch reduces ambush risk"
      - "Skill complementarity"
      - "Morale bonuses"
      - "Trading efficiency"
    but_also:
      - "Resource competition"
      - "Trust issues"
      - "Drama potential"
      - "Leadership conflicts"
```

---

## Progression Path

### Phase 1: Immediate Survival (Days 1-3)

```
┌─────────────────────────────────────────────────────────────┐
│                    IMMEDIATE SURVIVAL                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Priority Stack:                                            │
│  1. Water (die in 8 hours without)                          │
│  2. Shelter (exposure kills at night)                       │
│  3. Fire (warmth, cooking, defense)                         │
│  4. Food (can wait 24-48 hours)                             │
│                                                             │
│  Success Metrics:                                           │
│  ├── Survived first night                                   │
│  ├── Found water source                                     │
│  ├── Secured basic shelter                                  │
│  └── Established food routine                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Phase 2: Stabilization (Days 4-14)

```
┌─────────────────────────────────────────────────────────────┐
│                    STABILIZATION                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Goals:                                                     │
│  ├── Improve shelter quality                                │
│  ├── Establish reliable food/water                          │
│  ├── Build some reserves                                    │
│  ├── Make first social contacts                             │
│  └── Learn the local area                                   │
│                                                             │
│  Wealth Building:                                           │
│  ├── Find artifacts while exploring                         │
│  ├── Perform odd jobs for NPCs                              │
│  ├── Trade excess resources                                 │
│  └── Discover valuable locations                            │
│                                                             │
│  Target: 50-200 NVT saved                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Phase 3: Growth (Weeks 2-4)

```
┌─────────────────────────────────────────────────────────────┐
│                       GROWTH                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Goals:                                                     │
│  ├── Upgrade equipment                                      │
│  ├── Build/acquire permanent residence                      │
│  ├── Develop skills/specialization                          │
│  ├── Build reputation                                       │
│  └── Form lasting alliances                                 │
│                                                             │
│  Options:                                                   │
│  ├── Join established community                             │
│  ├── Build own homestead                                    │
│  ├── Become traveling trader                                │
│  ├── Specialize in craft/service                            │
│  └── Begin invention journey                                │
│                                                             │
│  Target: 500-2000 NVT + stable income                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Phase 4: Journey Preparation (Months 1-2)

```
┌─────────────────────────────────────────────────────────────┐
│                 JOURNEY PREPARATION                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Ready for the Real Challenge:                              │
│  ├── Health fully restored                                  │
│  ├── Quality equipment acquired                             │
│  ├── Resources for extended travel                          │
│  ├── Knowledge of destination                               │
│  └── Support network established                            │
│                                                             │
│  The Biome Calls:                                           │
│  "You've survived. You've built. Now...                     │
│   can you solve the problems that matter?"                  │
│                                                             │
│  Begin journey to biome-specific challenges                 │
│  (Water scarcity, disaster rescue, etc.)                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## The Invention Framework

### Requirements for Creating New Tools

```yaml
invention_requirements:
  1_novelty:
    rule: "Must not exist in the game yet"
    check: "System scans all existing items"
    similar_items: "Flagged for manual review"
    truly_novel: "Auto-approved for minting"

  2_single_purpose:
    rule: "Must serve ONE clear purpose"
    examples:
      valid:
        - "A compass that only points to water"
        - "A whistle that only scares wolves"
        - "A lens that only starts fires"
      invalid:
        - "A multi-tool that does everything"
        - "A swiss-army knife"
    reasoning: "Forces creative, focused design"

  3_limited_supply:
    rule: "Must set a maximum supply"
    options:
      - "Unique (1)"
      - "Legendary (10-100)"
      - "Rare (100-1000)"
      - "Uncommon (1000-10000)"
      - "Common (unlimited, but lower value)"
    cannot_change: "Supply cap is permanent"

  4_material_cost:
    rule: "Must invest resources to create"
    formula: "base_cost + (rarity_multiplier * power_level)"
    materials_from: "In-game resources, purchased, or traded"

  5_creator_binding:
    rule: "Invention permanently linked to creator"
    benefits:
      - "Royalties on all sales"
      - "Creator badge on item"
      - "Reputation building"
    cannot: "Transfer ownership of the 'patent'"
```

### Invention Process

```
┌─────────────────────────────────────────────────────────────┐
│                   INVENTION PROCESS                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. CONCEPT                                                 │
│     └── What problem does this solve?                       │
│         What's the single purpose?                          │
│                                                             │
│  2. RESEARCH                                                │
│     └── Does it already exist?                              │
│         Search the invention registry                       │
│                                                             │
│  3. DESIGN                                                  │
│     └── Use Tool Forge to create design                     │
│         Set appearance, stats, behavior                     │
│                                                             │
│  4. PROTOTYPE                                               │
│     └── Create first instance (higher cost)                 │
│         Test functionality                                  │
│                                                             │
│  5. GAIAN REVIEW                                            │
│     └── Ethics check                                        │
│         Balance check                                       │
│         Novelty confirmation                                │
│                                                             │
│  6. REGISTER                                                │
│     └── Permanent on-chain registration                     │
│         Creator rights established                          │
│         Royalty smart contract deployed                     │
│                                                             │
│  7. MANUFACTURE                                             │
│     └── Create copies (up to supply limit)                  │
│         Each copy costs materials                           │
│                                                             │
│  8. DISTRIBUTE                                              │
│     └── Sell, trade, gift, or hide                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Distribution Methods

```yaml
distribution_methods:
  shop_consignment:
    description: "Work with NPC shopkeepers to sell your items"
    mechanics:
      - "Negotiate shelf space"
      - "Shopkeeper takes 10-30% cut"
      - "Shop handles transactions"
      - "Wider audience reach"
    example: |
      Player: "I invented this water-finding compass. Will you sell it?"
      Shopkeeper: "Interesting. I'll take 20% and display it prominently."
      Player: "Deal. Start with 10 units."

  hidden_placement:
    description: "Leave items in the world for discovery"
    mechanics:
      - "Choose hiding location"
      - "Set discovery conditions"
      - "Finder gets item free"
      - "Creator gets notification + reward"
    strategy: "Builds reputation through word-of-mouth"

  direct_sales:
    description: "Sell directly to other players"
    mechanics:
      - "Face-to-face negotiation"
      - "Escrow system for safety"
      - "Full price to creator (minus platform fee)"

  roadside_peddling:
    description: "Set up shop on travel routes"
    mechanics:
      - "Physical presence required"
      - "Negotiate with each customer"
      - "Risk of robbery"
      - "Personal connection"
    roleplay: "The traveling salesman experience"

  marketplace_listing:
    description: "List on the global marketplace"
    mechanics:
      - "Listing fee"
      - "Global visibility"
      - "Price competition"
      - "Reviews and ratings"
```

---

## Commerce & Trade

### Finding & Selling Artifacts

```yaml
artifact_system:
  finding:
    locations:
      - "Ruins and abandoned buildings"
      - "Hidden caves"
      - "Underwater locations"
      - "Buried caches"
      - "Quest rewards"
      - "Enemy drops"

    artifact_types:
      common:
        examples: ["old coins", "worn tools", "basic materials"]
        value: "1-10 NVT"
        frequency: "regular"

      uncommon:
        examples: ["quality tools", "maps", "recipes"]
        value: "10-50 NVT"
        frequency: "occasional"

      rare:
        examples: ["ancient artifacts", "enchanted items", "keys"]
        value: "50-500 NVT"
        frequency: "rare"

      legendary:
        examples: ["unique artifacts", "quest items", "relics"]
        value: "500+ NVT"
        frequency: "very rare"

  selling:
    to_shops:
      pros: ["immediate payment", "no negotiation"]
      cons: ["lower prices (50-70% of value)"]

    to_players:
      pros: ["better prices", "relationship building"]
      cons: ["finding buyers", "trust issues"]

    at_auction:
      pros: ["potentially highest price"]
      cons: ["fees", "time investment"]
```

### Bartering System

```yaml
barter_mechanics:
  direct_trade:
    description: "Exchange items without currency"
    process:
      1: "Both players open trade window"
      2: "Add items to offer"
      3: "Negotiate via chat"
      4: "Both confirm"
      5: "Atomic swap executes"

  value_negotiation:
    factors:
      - "Item rarity"
      - "Condition"
      - "Player need"
      - "Market prices"
      - "Relationship"
      - "Desperation level"

  reputation_impact:
    fair_trades: "+1 reputation"
    great_deals_for_them: "+3 reputation"
    taking_advantage: "-5 reputation"
    scams: "-20 reputation"

  example_trade:
    player_a_offers: "5 smoked fish, 1 fur cloak"
    player_b_offers: "1 iron knife, 10 arrows"
    negotiation: |
      A: "I need that knife. Add some rope?"
      B: "Only if you include that waterskin."
      A: "Deal."
```

---

## Training Data Value

### What We Capture

| Scenario | Training Data Value | Application |
|----------|---------------------|-------------|
| Survival decisions | Priority assessment under pressure | Emergency AI |
| Social strategy choice | Trust/cooperation dynamics | Social robots |
| Criminal behavior | Threat pattern recognition | Security AI |
| Invention design | Human creativity patterns | Generative AI |
| Trade negotiation | Bargaining optimization | Negotiation AI |
| Group formation | Coalition building | Multi-agent AI |
| Ethical dilemmas | Moral decision-making | Ethical AI |

### Gaian Abstraction Rules

```yaml
gaian_data_abstraction:
  crime_data:
    captures: "Pattern of criminal decision-making"
    abstracts: "Specific techniques, victim identification"
    exports: "Behavioral patterns only"

  manipulation_data:
    captures: "Social engineering sequences"
    abstracts: "Specific scripts, targeting methods"
    exports: "Influence pattern recognition"

  survival_data:
    captures: "Full decision tree"
    abstracts: "Nothing (valuable as-is)"
    exports: "Complete behavioral data"
```

---

## Summary

The survival and progression system creates a **crucible of human decision-making**. Every player choice—ethical or not—generates training data that helps us understand how humans behave when resources are scarce and survival is uncertain.

**Key Design Principles:**

1. **No artificial barriers** - Anyone can survive if they're clever
2. **Full spectrum of choices** - Ethical and unethical paths both viable
3. **Natural consequences** - Actions have realistic outcomes
4. **Social dynamics emerge** - Grouping provides advantages
5. **Invention rewards creativity** - Novel solutions create value
6. **Real economics** - Trade, barter, and commerce feel authentic

**The Training Data Gold Mine:**
- How do humans prioritize under pressure?
- When do they cooperate vs. compete?
- What triggers ethical compromise?
- How do communities form?
- What makes inventions successful?

---

## Related Documentation

- [Payments Specification](./payments.md)
- [Project Overview](../guides/concepts/project-overview.md)
- [Gaian Configuration](../../core-governance/gaian/config.yaml)
