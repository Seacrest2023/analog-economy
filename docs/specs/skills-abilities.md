# Skills & Abilities: Learn the Ways

> "The land does not care that you own it. The forge does not care that you bought it. Mastery is earned, never purchased."

## Table of Contents

1. [Overview](#1-overview)
2. [Design Philosophy](#2-design-philosophy)
3. [The Knowledge System](#3-the-knowledge-system)
4. [Skill Categories](#4-skill-categories)
5. [Learning Mechanics](#5-learning-mechanics)
6. [Trade Mastery: The Simug (Smith)](#6-trade-mastery-the-simug-smith)
7. [Trade Mastery: The Engar (Farmer)](#7-trade-mastery-the-engar-farmer)
8. [Trade Mastery: Other Professions](#8-trade-mastery-other-professions)
9. [Supply Chain Knowledge](#9-supply-chain-knowledge)
10. [The Tech Tree Structure](#10-the-tech-tree-structure)
11. [Skill Progression & Rewards](#11-skill-progression--rewards)
12. [Training Data Value](#12-training-data-value)
13. [Implementation Notes](#13-implementation-notes)

---

## 1. Overview

The Skills & Abilities system is the educational heart of The Analog Economy. Players don't just click buttons to craft—they learn actual historical techniques, understand supply chains, and develop mastery that mirrors real-world competency.

### The Core Promise

> "By the time you finish building a fully functional bronze forge in the game, you should know enough to build a real one in the outside world."

### Core Principles

| Principle | Implementation |
|-----------|----------------|
| **Ownership ≠ Competency** | Buying land/equipment doesn't mean you can use it |
| **Knowledge is discovered** | Skills learned through gameplay, NPCs, or purchased intel |
| **Mastery takes time** | Complex skills require multiple prerequisites |
| **Real-world applicable** | Game skills teach authentic historical techniques |
| **Learn the Ways** | Players earn SILA for learning instead of buying |

---

## 2. Design Philosophy

### 2.1 The Land Purchase Paradox

```yaml
the_paradox:
  scenario: "Player buys land with ANALOG, wants to run a smithy"

  what_they_get:
    - "Legal ownership of the property"
    - "A building (possibly with equipment)"
    - "NPC workers (basic)"
    - "Social status of landowner"

  what_they_dont_get:
    - "Knowledge of how to smelt copper"
    - "Understanding of bronze alloy ratios"
    - "Skill to operate a bellows efficiently"
    - "Relationships with material suppliers"
    - "Reputation as a quality craftsman"

  the_gap: |
    You own a forge but cannot make a sword.
    You must LEARN THE WAYS or hire those who know.
    This is intentional—it mirrors real business ownership.
```

### 2.2 Educational Intent

```yaml
educational_mission:
  goal: |
    Every major skill tree should teach players enough that they could
    theoretically apply the knowledge in real life. Not to create
    professional blacksmiths, but to give genuine understanding.

  examples:
    bronze_smelting:
      game_teaches:
        - "Copper + tin ratio (90:10)"
        - "Temperature requirements (1,085°C)"
        - "Bellows operation (forced air principle)"
        - "Why charcoal works but wood doesn't"
        - "Lost-wax casting process"
      real_world_value: "Understand metallurgy basics"

    agriculture:
      game_teaches:
        - "Crop rotation necessity"
        - "Irrigation engineering"
        - "Soil salinization problems"
        - "Animal husbandry basics"
        - "Storage and preservation"
      real_world_value: "Understand food production"

    textile_production:
      game_teaches:
        - "Fiber preparation (carding, spinning)"
        - "Loom operation"
        - "Dye sources and application"
        - "Weave patterns and strength"
      real_world_value: "Understand cloth manufacturing"
```

### 2.3 Training Data Through Learning

```yaml
learning_training_data:
  questions_studied:
    - "How do humans acquire complex skills?"
    - "What teaching methods work best?"
    - "How do people troubleshoot failures?"
    - "What motivates skill development?"
    - "How is knowledge transferred between players?"

  data_captured:
    - "Learning curves for different skill types"
    - "Common mistakes and how they're corrected"
    - "Optimal teaching sequences"
    - "Knowledge trading behaviors"
    - "Apprenticeship dynamics"
```

---

## 3. The Knowledge System

### 3.1 Knowledge Sources

```yaml
knowledge_sources:
  experimentation:
    description: "Trial and error discovery"
    speed: "Slowest"
    cost: "Materials wasted on failures"
    benefit: "Full SILA reward, deep understanding"
    example: "Trying different copper/tin ratios until bronze works"

  observation:
    description: "Watching others work"
    speed: "Slow"
    cost: "Time investment"
    benefit: "Partial SILA reward, good understanding"
    example: "Standing in a smithy watching the master work"

  apprenticeship:
    description: "Formal learning under a master"
    speed: "Moderate"
    cost: "Time + labor for master"
    benefit: "Structured learning, relationship built"
    example: "Working for a Simug, learning as you assist"

  clay_tablets:
    description: "Written knowledge (if you can read)"
    speed: "Fast (if available)"
    cost: "Must find/buy tablets, requires literacy"
    benefit: "Rapid knowledge transfer"
    example: "Temple tablet on bronze alloy ratios"

  player_teaching:
    description: "Another player teaches you"
    speed: "Fast"
    cost: "SILA payment to teacher"
    benefit: "Both parties can earn SILA"
    example: "Veteran player teaches newbie fishing"

  purchase_intelligence:
    description: "Buy knowledge directly"
    speed: "Instant"
    cost: "SILA (no 'Learn the Ways' reward)"
    benefit: "Skip the learning process"
    example: "Pay Dam-gar for trade route information"
```

### 3.2 Knowledge Tiers

```yaml
knowledge_tiers:
  tier_0_awareness:
    description: "You know this skill exists"
    capability: "Cannot perform, can recognize"
    example: "You've seen bronze but can't make it"

  tier_1_novice:
    description: "Basic understanding, many failures"
    capability: "50% success rate, poor quality"
    example: "Can attempt bronze, often ruins materials"

  tier_2_apprentice:
    description: "Working knowledge, occasional failures"
    capability: "75% success rate, acceptable quality"
    example: "Can make bronze tools, sometimes imperfect"

  tier_3_journeyman:
    description: "Reliable skill, rare failures"
    capability: "90% success rate, good quality"
    example: "Consistently produces quality bronze"

  tier_4_master:
    description: "Expert level, innovations possible"
    capability: "98% success rate, excellent quality"
    example: "Can teach others, develop new techniques"

  tier_5_grandmaster:
    description: "Legendary skill, unique abilities"
    capability: "Near-perfect, can attempt impossible"
    example: "Creates items of exceptional quality"
```

---

## 4. Skill Categories

### 4.1 Category Overview

```yaml
skill_categories:
  survival_skills:
    description: "Staying alive in the world"
    examples:
      - "Fire starting"
      - "Water finding"
      - "Shelter building"
      - "Foraging"
      - "Basic cooking"
    learning_curve: "Relatively quick, essential for all"

  craft_skills:
    description: "Making things"
    examples:
      - "Pottery"
      - "Weaving"
      - "Metallurgy"
      - "Carpentry"
      - "Leather working"
    learning_curve: "Long, specialized"

  agricultural_skills:
    description: "Growing and raising"
    examples:
      - "Farming"
      - "Animal husbandry"
      - "Irrigation"
      - "Food preservation"
    learning_curve: "Seasonal learning required"

  social_skills:
    description: "Interacting with others"
    examples:
      - "Bargaining"
      - "Leadership"
      - "Diplomacy"
      - "Teaching"
    learning_curve: "Learned through interaction"

  knowledge_skills:
    description: "Understanding the world"
    examples:
      - "Literacy (cuneiform)"
      - "Mathematics"
      - "Medicine"
      - "Astronomy"
      - "Law"
    learning_curve: "Long, requires instruction"

  combat_skills:
    description: "Fighting"
    examples:
      - "Spear"
      - "Axe"
      - "Bow"
      - "Shield"
      - "Formation fighting"
    learning_curve: "Moderate, practice essential"
```

### 4.2 Skill Dependencies

```yaml
skill_dependencies:
  example_metallurgy:
    bronze_casting:
      requires:
        - "Fire management (Tier 2)"
        - "Copper smelting (Tier 2)"
        - "Basic metallurgy theory (Tier 1)"
      unlocks:
        - "Weapon smithing"
        - "Tool smithing"
        - "Jewelry making"

  example_agriculture:
    advanced_irrigation:
      requires:
        - "Basic farming (Tier 2)"
        - "Water management (Tier 2)"
        - "Basic construction (Tier 1)"
      unlocks:
        - "Large-scale farming"
        - "Specialty crops"
        - "Flood management"

  example_literacy:
    contract_writing:
      requires:
        - "Cuneiform (Tier 3)"
        - "Mathematics (Tier 2)"
        - "Legal knowledge (Tier 1)"
      unlocks:
        - "Temple administration"
        - "Merchant accounting"
        - "Land registry"
```

---

## 5. Learning Mechanics

### 5.1 The Learning Loop

```yaml
learning_loop:
  step_1_exposure:
    description: "Encounter the skill"
    trigger:
      - "See someone perform it"
      - "Hear about it from NPC"
      - "Find a clay tablet"
      - "Fail at attempting it"
    result: "Skill appears in journal (Tier 0)"

  step_2_instruction:
    description: "Gain theoretical knowledge"
    methods:
      - "NPC teaches you"
      - "Player teaches you"
      - "Read clay tablet"
      - "Extended observation"
    result: "Can attempt skill (Tier 1)"

  step_3_practice:
    description: "Repeated attempts"
    mechanics:
      - "Each attempt uses materials/time"
      - "Success/failure tracked"
      - "Experience points accumulate"
    result: "Gradual tier improvement"

  step_4_mastery:
    description: "Achieve competency"
    requirements:
      - "Reach success rate threshold"
      - "Demonstrate to NPC master (optional)"
      - "Complete mastery challenge"
    result: "Tier advancement, new abilities unlock"
```

### 5.2 Practice Mechanics

```yaml
practice_mechanics:
  success_calculation:
    base_chance: "Determined by tier"
    modifiers:
      - "Tool quality (+/- 10%)"
      - "Material quality (+/- 10%)"
      - "Teacher present (+15%)"
      - "Fatigue (-5% per hour worked)"
      - "Environmental conditions (+/- 10%)"

  failure_consequences:
    materials: "Partially or fully consumed"
    time: "Always consumed"
    learning: "Still gain experience from failures"
    special: "Critical failures can cause injury"

  experience_gain:
    success: "Full experience for tier"
    partial_success: "50% experience"
    failure: "25% experience"
    critical_failure: "10% experience, possible injury"

  tier_advancement:
    requirements:
      tier_1_to_2: "20 successful attempts"
      tier_2_to_3: "50 successful attempts"
      tier_3_to_4: "100 successful attempts + master validation"
      tier_4_to_5: "250 successful attempts + innovation"
```

### 5.3 Teaching Mechanics

```yaml
teaching_mechanics:
  requirements_to_teach:
    - "Must be at least Tier 3 in the skill"
    - "Must be Tier 4 to advance students past Tier 2"
    - "Must be Tier 5 for mastery-level teaching"

  teaching_process:
    1: "Teacher demonstrates technique"
    2: "Student attempts with guidance"
    3: "Teacher provides corrections"
    4: "Repeat until skill check passed"

  rewards:
    teacher:
      - "SILA payment from student (negotiated)"
      - "Reputation as teacher"
      - "Apprentice labor (if formal apprenticeship)"
    student:
      - "Faster skill acquisition"
      - "Reduced material waste"
      - "Relationship with teacher"

  limitations:
    - "Teacher cannot advance student past (teacher tier - 1)"
    - "Teaching takes real time"
    - "Teacher's productivity reduced while teaching"
```

---

## 6. Trade Mastery: The Simug (Smith)

### 6.1 The Smith's Journey

> "First, a vital correction: In 3000 BCE, you would not make brass (copper + zinc). You are a master of Bronze (copper + tin) or Arsenical Copper."

```yaml
smith_overview:
  title: "Simug"
  description: "The magician of metal who transforms raw ore into tools and weapons"
  social_status: "Respected artisan, vital to society"
  learning_time: "2-5 years apprenticeship (game-accelerated)"
  equipment_required:
    - "Smelting furnace (not a kiln)"
    - "Bellows (goat-skin)"
    - "Crucibles (clay)"
    - "Molds (stone or clay)"
    - "Hammers, tongs, anvil"
```

### 6.2 The Smith's Supply Chain

```yaml
smith_supply_chain:
  copper:
    source: "Dilmun boats from Magan (Oman)"
    form: "Bun ingots (round cakes)"
    availability: "Regular, seasonal"
    storage: "Protected warehouse"
    skill_needed: "Trade negotiation, quality assessment"

  tin:
    source: "Donkey caravan from Zagros Mountains (Iran/Afghanistan)"
    availability: "Rare, expensive, routes can be blocked"
    storage: "Secure, high-value"
    skill_needed: "Trade contacts, scarcity management"
    critical_note: "No tin = no bronze = back to copper tools"

  fuel:
    source: "Charcoal (imported or made from fruit trees)"
    problem: "Reeds don't reach 1,100°C; wood is scarce"
    skill_needed: "Fuel management, charcoal production"

  scrap_metal:
    source: "Farmers bring broken tools"
    economics: "Cheaper than fresh ore"
    skill_needed: "Weighing, assessment, recycling"
```

### 6.3 The Smith's Skill Tree

```yaml
smith_skill_tree:
  foundation_skills:
    fire_management:
      tier_1: "Light and maintain fire"
      tier_2: "Control temperature zones"
      tier_3: "Judge temperature by flame color"
      tier_4: "Master temperature control"
      key_knowledge: "1,085°C melts copper; judge by color alone"

    bellows_operation:
      tier_1: "Pump bellows (exhausting)"
      tier_2: "Maintain steady airflow"
      tier_3: "Coordinate with smelting phases"
      tier_4: "Train apprentices, design improvements"
      key_knowledge: "Forced air raises temperature 300-400°C"

  metallurgy_skills:
    copper_smelting:
      requires: ["Fire management (2)", "Bellows operation (2)"]
      tier_1: "Melt raw copper (often impure)"
      tier_2: "Remove slag, produce clean copper"
      tier_3: "Consistent quality output"
      tier_4: "Maximize yield from ore"

    alloying:
      requires: ["Copper smelting (2)"]
      tier_1: "Basic bronze (10:1 ratio, variable quality)"
      tier_2: "Consistent bronze alloy"
      tier_3: "Adjust ratios for hardness/workability"
      tier_4: "Experimental alloys"
      critical_knowledge:
        bronze: "90% copper + 10% tin"
        arsenical_copper: "Copper + arsenic (poisonous!)"
        warning: "Arsenic fumes cause nerve damage"

  shaping_skills:
    open_mold_casting:
      requires: ["Copper smelting (1)"]
      tier_1: "Simple shapes (ingots)"
      tier_2: "Tools (axe heads, sickles)"
      tier_3: "Weapons (spearheads, arrowheads)"
      tier_4: "Complex shapes with multiple pours"

    lost_wax_casting:
      requires: ["Open mold casting (3)", "Alloying (2)"]
      tier_1: "Simple hollow objects"
      tier_2: "Detailed figures"
      tier_3: "Complex multi-part casting"
      tier_4: "Masterwork statues"
      process:
        1: "Carve shape in beeswax"
        2: "Cover in clay"
        3: "Bake to melt wax out"
        4: "Pour bronze into hollow"
        5: "Break clay to reveal metal"

    socketed_tools:
      requires: ["Open mold casting (2)"]
      tier_1: "Basic socket design"
      tier_2: "Reliable socket strength"
      tier_3: "Optimized socket fitting"
      tier_4: "Innovative socket designs"
      key_innovation: "Socket = handle inside metal = unbreakable"
```

### 6.4 The Smith's Inventory Progression

```yaml
smith_inventory_tiers:
  tier_1_mass_production:
    description: "Your bread and butter"
    items:
      - "Arrowheads (50/day possible)"
      - "Simple axe heads"
      - "Sickle blades"
      - "Fishing hooks"
    method: "Reusable stone/clay open molds"
    skill_required: "Open mold casting (Tier 2)"
    margin: "Low per-item, volume business"

  tier_2_quality_tools:
    description: "Better tools for better customers"
    items:
      - "Socketed axe heads (unbreakable)"
      - "Quality sickles"
      - "Adzes and chisels"
      - "Awls and needles"
    method: "Careful casting, finishing work"
    skill_required: "Socketed tools (Tier 2), Alloying (Tier 2)"
    margin: "Moderate, reputation builder"

  tier_3_temple_contracts:
    description: "The big money"
    items:
      - "Copper foundation pegs (god faces)"
      - "Offering stands"
      - "Bronze mirrors"
      - "Ceremonial vessels"
    method: "Lost-wax casting, decorative finishing"
    skill_required: "Lost-wax casting (Tier 3)"
    margin: "High, but requires Temple relationship"

  tier_4_composite_luxury:
    description: "For kings and generals"
    items:
      - "Bronze dagger with lapis handle"
      - "Gold-leafed ceremonial weapons"
      - "Decorated helmets"
    method: "Partner with woodworker, lapidary"
    skill_required: "Master-level all skills"
    margin: "Highest, limited market"
```

---

## 7. Trade Mastery: The Engar (Farmer)

### 7.1 The Farmer's Reality

```yaml
farmer_overview:
  title: "Engar"
  description: "The backbone of society, feeding the city"
  social_status: "Commoner, but essential"
  learning_time: "Full seasonal cycle required (1 year minimum)"
  dependencies:
    - "Temple bureaucracy (land, seeds, water rights)"
    - "Weather and flood cycles"
    - "Draft animal availability"
    - "Labor for harvest"
```

### 7.2 The Farmer's Supply Chain

```yaml
farmer_supply_chain:
  land_and_water:
    acquisition:
      - "Contract with Temple Surveyor (Sa-gid)"
      - "Water time purchased at sluice gate"
    skill_needed: "Bureaucratic navigation, contract law"
    risk: "Water can be cut off upstream"

  seeds:
    source: "Temple Granary (loan system)"
    terms: "Receive 1 unit, return 2-3 after harvest"
    skill_needed: "Seed selection, storage"
    risk: "Bad seeds = failed crop = debt"

  draft_animals:
    requirement: "Team of 4 oxen to pull plow"
    acquisition: "Lease from Temple or wealthy farmer"
    cost: "~10 baskets barley/season"
    skill_needed: "Animal handling, scheduling"

  equipment:
    seeder_plow:
      description: "Sumerian innovation with seed funnel"
      function: "Opens furrow AND drops seed simultaneously"
      advantage: "Prevents bird predation, saves labor"
      skill_needed: "Operation and maintenance"
```

### 7.3 The Farmer's Skill Tree

```yaml
farmer_skill_tree:
  foundation_skills:
    soil_reading:
      tier_1: "Identify fertile vs poor soil"
      tier_2: "Predict crop success by soil"
      tier_3: "Soil amendment techniques"
      tier_4: "Optimal crop-soil matching"

    weather_reading:
      tier_1: "Basic weather prediction"
      tier_2: "Seasonal pattern recognition"
      tier_3: "Flood timing prediction"
      tier_4: "Microclimate management"

  water_management:
    basic_irrigation:
      requires: ["Soil reading (1)"]
      tier_1: "Operate sluice gates"
      tier_2: "Time irrigation correctly"
      tier_3: "Build secondary channels"
      tier_4: "Design canal systems"

    flood_control:
      requires: ["Basic irrigation (2)", "Weather reading (2)"]
      tier_1: "Build basic levees"
      tier_2: "Reinforce against flood"
      tier_3: "Controlled flooding (fertilization)"
      tier_4: "Major flood engineering"
      legal_note: "Your levee breaks = you pay for neighbor's crop"

    desalination:
      requires: ["Basic irrigation (3)"]
      tier_1: "Recognize salt damage"
      tier_2: "Fallow field rotation"
      tier_3: "Flush irrigation technique"
      tier_4: "Long-term salt prevention"
      key_knowledge: "Water evaporates, salt stays. Over-irrigation kills land."

  crop_production:
    grain_farming:
      requires: ["Basic irrigation (1)"]
      tier_1: "Plant and harvest barley"
      tier_2: "Optimize planting density"
      tier_3: "Multiple crop rotations"
      tier_4: "Maximum yield techniques"

    date_cultivation:
      requires: ["Grain farming (2)"]
      tier_1: "Maintain existing palms"
      tier_2: "Pollination techniques"
      tier_3: "New palm cultivation"
      tier_4: "Orchard design (microclimate)"
      note: "5-year investment before first harvest"

    vegetable_gardening:
      tier_1: "Basic onions, garlic"
      tier_2: "Diverse vegetables"
      tier_3: "Year-round production"
      tier_4: "Specialty/medicinal herbs"

  animal_husbandry:
    oxen_management:
      tier_1: "Basic care and feeding"
      tier_2: "Training for plow work"
      tier_3: "Breeding management"
      tier_4: "Veterinary skills"

    sheep_and_goats:
      tier_1: "Basic flock management"
      tier_2: "Wool production optimization"
      tier_3: "Breeding for quality"
      tier_4: "Large flock management"
```

### 7.4 The Farmer's Diversification

```yaml
farmer_diversification:
  date_palm_orchard:
    investment: "5+ years to maturity"
    return: "Massive once productive"
    bonus: "Shade enables second-tier crops below"
    products:
      - "Dates (high value)"
      - "Date wine/syrup"
      - "Palm wood"
      - "Shade vegetables"

  flock_management:
    use_fallow_fields: "Graze sheep on resting land"
    products:
      - "Wool (Sumerian 'oil')"
      - "Meat (occasional)"
      - "Milk (daily)"
      - "Manure (fertilizer)"

  brewing:
    description: "Value-add processing"
    process: "Convert barley → malt → bappir (beer-bread) → beer"
    advantage:
      - "Higher value than raw grain"
      - "Easier transport than grain"
      - "Constant demand"
    tradition: "Often female-led household operation"

  marsh_foraging:
    description: "Off-season income"
    products:
      - "Reeds (construction material)"
      - "Dried fish (preserved protein)"
      - "Wild fowl"
      - "Medicinal plants"
```

### 7.5 The Farmer's Economics

```yaml
farmer_economics:
  sample_yearly_budget:
    revenue:
      grain_harvest: "100 baskets barley"
      date_sales: "20 baskets equivalent (if orchard mature)"
      wool_sales: "10 baskets equivalent"
      total: "130 baskets"

    expenses:
      temple_tax: "-33 baskets (25%)"
      seed_loan_repayment: "-10 baskets"
      oxen_lease: "-10 baskets"
      equipment_maintenance: "-5 baskets"
      total: "-58 baskets"

    net_profit: "72 baskets"

    allocation:
      family_food: "-30 baskets"
      new_bronze_sickle: "-5 baskets"
      savings: "-20 baskets"
      market_purchases: "-17 baskets"
```

---

## 8. Trade Mastery: Other Professions

### 8.1 The Bahar (Potter)

```yaml
potter_skills:
  clay_preparation:
    tier_1: "Gather and clean clay"
    tier_2: "Temper clay properly"
    tier_3: "Store clay for optimal workability"
    tier_4: "Source specialty clays"

  wheel_throwing:
    tier_1: "Simple bowls"
    tier_2: "Consistent vessels"
    tier_3: "Large storage jars"
    tier_4: "Decorative/complex shapes"

  kiln_operation:
    tier_1: "Basic firing"
    tier_2: "Temperature control"
    tier_3: "Consistent results"
    tier_4: "Specialty firings (glazes later)"

  production_capacity:
    basic: "20 simple bowls/day"
    advanced: "5 large storage jars/day"
    specialty: "1 decorative piece/day"
```

### 8.2 The Ush-bar (Weaver)

```yaml
weaver_skills:
  fiber_preparation:
    tier_1: "Clean and card wool"
    tier_2: "Spin consistent thread"
    tier_3: "Dye fibers"
    tier_4: "Specialty fiber processing"

  loom_operation:
    tier_1: "Basic plain weave"
    tier_2: "Consistent fabric"
    tier_3: "Complex patterns"
    tier_4: "Masterwork textiles"

  production_notes:
    social_context: "Usually women, in temple workshops"
    output: "Major export product of Eridu"
    skill_transfer: "Mother to daughter traditionally"
```

### 8.3 The Lungaa (Brewer)

```yaml
brewer_skills:
  malt_production:
    tier_1: "Sprout barley"
    tier_2: "Consistent malting"
    tier_3: "Flavor variation"
    tier_4: "Specialty malts"

  brewing:
    tier_1: "Basic beer"
    tier_2: "Consistent quality"
    tier_3: "Multiple beer types"
    tier_4: "Strong/specialty beers"

  business_notes:
    social_context: "Often female profession"
    patron_goddess: "Ninkasi"
    importance: "Beer is safer than water, daily drink for all"
```

### 8.4 The Dub-sar (Scribe)

```yaml
scribe_skills:
  tablet_preparation:
    tier_1: "Make writing-ready tablets"
    tier_2: "Various tablet sizes"
    tier_3: "Tablet preservation"
    tier_4: "Archive management"

  cuneiform_writing:
    tier_1: "50 basic signs"
    tier_2: "200 signs (functional literacy)"
    tier_3: "400 signs (professional)"
    tier_4: "600+ signs (scholarly)"

  specialized_writing:
    accounting: "Numbers, quantities, contracts"
    legal: "Laws, judgments, property"
    religious: "Hymns, rituals, omens"
    literary: "Myths, stories, wisdom"

  power_of_literacy:
    note: "Literacy is RARE and powerful"
    advantages:
      - "Access to temple administration"
      - "Can read contracts (others can't)"
      - "Knowledge accumulation"
      - "Teaching earns significant SILA"
```

---

## 9. Supply Chain Knowledge

### 9.1 Trade Route Intelligence

```yaml
trade_knowledge:
  tier_1_local:
    description: "Know your immediate suppliers"
    examples:
      - "Which farmer sells best grain"
      - "When the potter fires his kiln"
      - "Who has leather in stock"
    acquisition: "Ask around, observation"

  tier_2_regional:
    description: "Know where goods come from"
    examples:
      - "Copper comes from Dilmun boats"
      - "Timber comes from upriver"
      - "Best wool from western herders"
    acquisition: "Talk to merchants, travel"

  tier_3_trade_routes:
    description: "Know the full supply chain"
    examples:
      - "Dilmun sources copper from Magan"
      - "Tin caravans cross Zagros passes"
      - "Lapis comes from beyond the mountains"
    acquisition: "Merchant relationships, travel, tablets"

  tier_4_strategic:
    description: "Know vulnerabilities and opportunities"
    examples:
      - "Mountain tribes can block tin routes"
      - "Flood affects upriver timber supply"
      - "War with Lagash cuts grain flow"
    acquisition: "Intelligence networks, experience"
```

### 9.2 Material Quality Assessment

```yaml
quality_assessment:
  copper:
    novice: "Can identify copper vs stone"
    journeyman: "Can assess purity by color"
    master: "Can predict alloy behavior"

  grain:
    novice: "Can identify spoiled grain"
    journeyman: "Can grade quality levels"
    master: "Can predict yield from seed"

  wool:
    novice: "Can identify wool vs other fiber"
    journeyman: "Can grade by fineness"
    master: "Can assess dye retention"

  wood:
    novice: "Can identify wood types"
    journeyman: "Can assess structural quality"
    master: "Can predict seasoning behavior"
```

---

## 10. The Tech Tree Structure

### 10.1 Master Tech Tree Overview

```
SKILLS & ABILITIES TECH TREE
════════════════════════════════════════════════════════════════

SURVIVAL (Everyone needs these)
├── Fire Starting ──────────► Cooking ──────────► Food Preservation
├── Water Finding ──────────► Basic Irrigation
├── Shelter Building ───────► Construction Basics
└── Foraging ───────────────► Herbalism ──────────► Medicine

AGRICULTURE (Food production)
├── Basic Farming
│   ├── Grain Production ──► Advanced Irrigation ──► Flood Control
│   ├── Date Cultivation ──► Orchard Management
│   └── Vegetable Gardening
└── Animal Husbandry
    ├── Oxen Management
    └── Sheep/Goat Management ──► Wool Production

CRAFTS (Making things)
├── Pottery
│   ├── Clay Preparation ──► Wheel Throwing ──► Kiln Operation
│   └── Decorative Pottery
├── Weaving
│   ├── Fiber Preparation ──► Spinning ──► Loom Operation
│   └── Dyeing
├── Metallurgy
│   ├── Fire Management ──► Copper Smelting ──► Alloying
│   ├── Bellows Operation
│   └── Mold Casting ──► Lost-Wax Casting ──► Socketed Tools
├── Carpentry
│   ├── Wood Working ──► Furniture ──► Boat Building
│   └── Tool Handles ──► Chariot Parts
└── Leather Working

KNOWLEDGE (Understanding)
├── Literacy
│   ├── Basic Cuneiform ──► Advanced Cuneiform ──► Scholarly Writing
│   └── Mathematics ──► Accounting ──► Architecture
├── Medicine
│   ├── Herbalism ──► Diagnosis ──► Treatment
│   └── Ritual Healing
└── Law & Administration
    ├── Contracts ──► Property Law ──► Temple Administration
    └── Judgment ──► Leadership

COMBAT (Fighting)
├── Melee
│   ├── Spear ──► Formation Fighting
│   ├── Axe
│   └── Mace
├── Ranged
│   ├── Bow ──► Composite Bow
│   └── Sling
└── Defense
    ├── Shield Use
    └── Armor Maintenance
```

### 10.2 Skill Interconnections

```yaml
skill_interconnections:
  metallurgy_requires:
    - "Fire management (from survival)"
    - "Trade negotiation (for materials)"
    - "Mathematics (for ratios)"

  advanced_farming_requires:
    - "Basic construction (for irrigation)"
    - "Water management"
    - "Weather reading"
    - "Bureaucratic skills (for Temple dealings)"

  scribal_work_requires:
    - "Formal education access"
    - "Mathematics"
    - "Tablet preparation"
    - "Extensive memorization"

  leadership_requires:
    - "Multiple trade skills OR combat skills"
    - "Literacy (helpful)"
    - "Reputation"
    - "Social network"
```

---

## 11. Skill Progression & Rewards

### 11.1 Learn the Ways Rewards

```yaml
learn_the_ways:
  philosophy: |
    Players who LEARN skills earn SILA.
    Players who BUY skills skip learning but get no reward.
    This incentivizes authentic skill development.

  reward_structure:
    first_time_learning:
      tier_1_achievement: "25 SILA"
      tier_2_achievement: "50 SILA"
      tier_3_achievement: "100 SILA"
      tier_4_achievement: "250 SILA"
      tier_5_achievement: "500 SILA"

    teaching_rewards:
      per_student_tier_gained: "50% of student's SILA reward"
      example: "Student reaches Tier 3 (100 SILA), teacher gets 50 SILA"

    innovation_rewards:
      discover_new_technique: "500 SILA + Codex credit"
      improve_existing_method: "100 SILA"

  purchased_skills:
    method: "Pay SILA to skip learning"
    cost: "2x the Learn reward"
    result: "Gain skill tier, but no SILA reward"
    trade_off: "Faster but more expensive"
```

### 11.2 Mastery Recognition

```yaml
mastery_recognition:
  titles:
    tier_3_journeyman: "Recognized competent"
    tier_4_master: "Can take apprentices, use title"
    tier_5_grandmaster: "Legendary status, unique privileges"

  privileges:
    masters:
      - "Can formally apprentice others"
      - "Higher prices for goods/services"
      - "Temple contract eligibility"
      - "Guild membership"

    grandmasters:
      - "Codex entries credited to name"
      - "Unique cosmetic recognition"
      - "NPC references to reputation"
      - "Special commissions available"
```

---

## 12. Training Data Value

### 12.1 Skill Learning Data

```yaml
skill_training_data:
  learning_curves:
    - "How quickly do different players learn?"
    - "What teaching methods work best?"
    - "Where do players get stuck?"
    - "How do failures affect motivation?"

  knowledge_transfer:
    - "How do players teach each other?"
    - "What knowledge do players trade?"
    - "How does information spread?"
    - "What creates knowledge monopolies?"

  specialization_patterns:
    - "Do players specialize or generalize?"
    - "What skill combinations emerge?"
    - "How do skills cluster socially?"
    - "What drives skill choice?"
```

### 12.2 Economic Decision Data

```yaml
economic_decision_data:
  supply_chain_decisions:
    - "How do players manage scarcity?"
    - "When do they stockpile vs just-in-time?"
    - "How do they respond to supply disruption?"

  business_decisions:
    - "How do players price goods?"
    - "When do they expand vs consolidate?"
    - "How do they manage employees?"
    - "What drives business failure?"

  investment_decisions:
    - "When do players invest in skills?"
    - "How do they evaluate ROI?"
    - "What makes them take risks?"
```

---

## 13. Implementation Notes

### 13.1 MVP Scope

```yaml
mvp_skills:
  included_skill_trees:
    survival:
      - "Fire starting (full)"
      - "Water finding (basic)"
      - "Shelter (basic)"

    crafts:
      - "Pottery (full)"
      - "Metallurgy (copper only, bronze basic)"

    agriculture:
      - "Grain farming (full)"
      - "Basic irrigation"

    knowledge:
      - "Literacy (basic cuneiform)"
      - "Mathematics (basic)"

    combat:
      - "Spear (full)"
      - "Shield (basic)"

  deferred:
    - "Full metallurgy tree (arsenical copper, advanced bronze)"
    - "Weaving"
    - "Carpentry"
    - "Animal husbandry"
    - "Advanced literacy"
    - "Medicine"
```

### 13.2 Data Structures

```yaml
skill_data:
  player_skill_record:
    skill_id: "metallurgy.bronze_casting"
    tier: 2
    experience: 35  # out of 50 for tier 3
    success_count: 28
    failure_count: 12
    last_practiced: "timestamp"
    learned_from: "npc_master_simug_01"

  skill_attempt_log:
    player_id: "xxx"
    skill_id: "metallurgy.bronze_casting"
    timestamp: "xxx"
    success: true
    quality: 0.85
    materials_used: ["copper_ingot", "tin_nugget"]
    materials_lost: []
    experience_gained: 1
    sila_earned: 0
```

---

## Appendix: Quick Reference Tables

### Skill Tier Summary

| Tier | Name | Success Rate | Time to Achieve | SILA Reward |
|------|------|--------------|-----------------|-------------|
| 0 | Awareness | Cannot attempt | Instant (exposure) | 0 |
| 1 | Novice | 50% | Hours | 25 |
| 2 | Apprentice | 75% | Days | 50 |
| 3 | Journeyman | 90% | Weeks | 100 |
| 4 | Master | 98% | Months | 250 |
| 5 | Grandmaster | 99%+ | Years | 500 |

### Key Supply Chains

| Trade | Critical Materials | Source | Risk Factor |
|-------|-------------------|--------|-------------|
| Smith | Copper, Tin, Fuel | Dilmun, Zagros, Imported | High (tin scarcity) |
| Farmer | Seeds, Water, Oxen | Temple, River, Lease | Medium (weather) |
| Potter | Clay, Fuel | Local, Imported | Low |
| Weaver | Wool, Dyes | Herders, Trade | Medium |
| Brewer | Grain, Water | Farmers, Wells | Low |

---

*"The master was once a disaster. Every expert was first an amateur. The only difference is they kept trying."*
