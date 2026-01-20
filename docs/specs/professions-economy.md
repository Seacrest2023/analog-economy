# Professions & Economy: How Players Earn

> "Before you can build a legacy, you must survive. Before you can survive, you must work."

## Table of Contents

1. [Design Philosophy](#1-design-philosophy)
2. [The Opportunity Map](#2-the-opportunity-map)
3. [Starting Classes](#3-starting-classes)
4. [Profession Paths](#4-profession-paths)
5. [Starting Equipment](#5-starting-equipment)
6. [Earning Mechanics](#6-earning-mechanics)
7. [The Job Board System](#7-the-job-board-system)
8. [Business Ownership](#8-business-ownership)
9. [Social Mobility](#9-social-mobility)
10. [The First Hour](#10-the-first-hour)
11. [Innovation Integration](#11-innovation-integration)
12. [Training Data Value](#12-training-data-value)
13. [Implementation Notes](#13-implementation-notes)

---

## 1. Design Philosophy

### 1.1 The Core Loop

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│                    THE ANALOG ECONOMY LOOP                          │
│                                                                     │
│     ┌──────────┐                                                    │
│     │  WORK    │ ─────► Earn currency (barley, credit)             │
│     └────┬─────┘                                                    │
│          │                                                          │
│          ▼                                                          │
│     ┌──────────┐                                                    │
│     │ SURVIVE  │ ─────► Food, water, shelter, health               │
│     └────┬─────┘                                                    │
│          │                                                          │
│          ▼                                                          │
│     ┌──────────┐                                                    │
│     │  LEARN   │ ─────► Skills, innovations, knowledge             │
│     └────┬─────┘                                                    │
│          │                                                          │
│          ▼                                                          │
│     ┌──────────┐                                                    │
│     │ ADVANCE  │ ─────► Better work, higher class, more options    │
│     └────┬─────┘                                                    │
│          │                                                          │
│          └──────────────────► (Return to WORK, but better)         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.2 Immediate Purpose

Players must understand within **5 minutes** of spawning:
1. **I need to eat** (survival meter visible)
2. **I can work to earn food** (jobs visible on map)
3. **There are things to discover** (innovation hints)
4. **Something big is coming** (flood timer)

### 1.3 Work Should Feel Meaningful

```yaml
work_philosophy:
  not_grinding:
    description: "Work is not click-to-collect. It's doing."
    example: "Farming involves actually guiding the plow, reading soil"

  skill_based:
    description: "Better technique = better results"
    example: "An experienced fisher catches more than a beginner"

  socially_embedded:
    description: "Work connects you to NPCs and players"
    example: "Your employer remembers you, gives better jobs"

  pathway_to_innovation:
    description: "Work exposes you to problems worth solving"
    example: "A frustrated farmer is motivated to improve tools"
```

---

## 2. The Opportunity Map

### 2.1 The Zoom-Out View

When players press the map key, they zoom out to see Eridu from above:

```
┌─────────────────────────────────────────────────────────────────────┐
│  [MAP VIEW]                               [FILTERS: ▼]              │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                                                               │ │
│  │              ═══════════════════════════════                  │ │
│  │                    EUPHRATES RIVER                            │ │
│  │              ═══════════════════════════════                  │ │
│  │                      │                                        │ │
│  │                 ┌────┴────┐                                   │ │
│  │                 │ HARBOR  │ 🟡 3 jobs                         │ │
│  │                 │  ⚓🐟   │                                   │ │
│  │                 └────┬────┘                                   │ │
│  │    ┌─────────┐  ┌────┴────┐  ┌─────────┐                     │ │
│  │    │ ARTISAN │  │ TEMPLE  │  │ ARTISAN │                     │ │
│  │    │ 🟡 5    │  │  ⛪     │  │ 🟢 12   │                     │ │
│  │    │ 🔴 2    │  │ 🟡 2    │  │ 🔴 1    │                     │ │
│  │    └─────────┘  └─────────┘  └─────────┘                     │ │
│  │         ┌─────────────────────────┐                          │ │
│  │         │     COMMONER QUARTER    │                          │ │
│  │         │        🟡 8 jobs        │                          │ │
│  │         └─────────────────────────┘                          │ │
│  │    ══════════════════════════════════════                    │ │
│  │                  CITY WALLS                                   │ │
│  │    ══════════════════════════════════════                    │ │
│  │                                                               │ │
│  │    ┌─────────┐  ┌─────────┐  ┌─────────┐                     │ │
│  │    │ HERDERS │  │ FIELDS  │  │ MARSHES │                     │ │
│  │    │ 🟡 2    │  │ 🟢 25   │  │ 🟡 4    │                     │ │
│  │    └─────────┘  └─────────┘  └─────────┘                     │ │
│  │                                                               │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  LEGEND:                                                            │
│  🟢 High demand (many jobs, good pay)                              │
│  🟡 Moderate demand (some jobs available)                          │
│  🔴 Innovation opportunity (problem needs solving)                 │
│  ⭐ Business for sale/rent                                         │
│                                                                     │
│  YOUR STATUS:                                                       │
│  Class: Laborer | Barley: 12 sila | Tools: Basic hoe              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.2 Map Layers

```yaml
map_layers:
  jobs_layer:
    description: "Shows where work is available"
    icons:
      green_dot: "High demand (5+ jobs)"
      yellow_dot: "Moderate demand (1-4 jobs)"
      gray: "No current openings"
    details_on_hover:
      - "Job type"
      - "Pay rate"
      - "Skill requirements"
      - "Employer reputation"

  innovation_layer:
    description: "Shows where problems exist that innovations could solve"
    icons:
      red_dot: "Active problem (frustrated NPCs, failed attempts)"
      orange_dot: "Latent problem (inefficiency, not yet critical)"
    details_on_hover:
      - "What's failing"
      - "Who's affected"
      - "Potential reward"

  business_layer:
    description: "Shows economic opportunities"
    icons:
      star: "Business/land for sale"
      diamond: "Business seeking partner"
      house: "Residence available"
    details_on_hover:
      - "Type of business"
      - "Price/rent"
      - "Income potential"
      - "Requirements"

  resource_layer:
    description: "Shows resource flows"
    display:
      - "Trade routes (animated lines)"
      - "Resource concentrations"
      - "Shortages (pulsing areas)"

  social_layer:
    description: "Shows your connections"
    display:
      - "NPCs you know (by name)"
      - "Reputation zones (friendly/neutral/hostile)"
      - "Player activity areas"
```

### 2.3 The Radar Pulse

A key feature: the map "pulses" to show opportunity:

```yaml
opportunity_radar:
  description: "Visual heartbeat showing where the economy needs you"

  pulse_types:
    urgent_need:
      color: "Red pulse"
      meaning: "Critical shortage or problem"
      example: "Fields need harvest NOW, crops will rot"

    good_opportunity:
      color: "Gold pulse"
      meaning: "High-paying work available"
      example: "Merchant needs porters for caravan"

    innovation_hint:
      color: "Blue pulse"
      meaning: "Something could be improved here"
      example: "Irrigation failing, farmers frustrated"

  frequency:
    update_rate: "Every game hour"
    major_events: "Immediate pulse on new opportunity"
```

---

## 3. Starting Classes

### 3.1 Class Selection

Players don't choose from a menu. They answer questions that determine starting position:

```yaml
class_selection:
  method: "Narrative questions, not menu"

  question_1:
    prompt: "How did you come to Eridu?"
    options:
      refugee:
        text: "My village was destroyed by flood"
        effect: "Start with nothing, commoner quarter"
        class: "Displaced (Laborer)"

      coming_of_age:
        text: "I've just come of age in my family"
        effect: "Start with family trade, some tools"
        class: "Apprentice (based on family)"

      trader_assistant:
        text: "I arrived with a merchant caravan"
        effect: "Start with some goods, harbor area"
        class: "Trader's Hand"

      temple_dedication:
        text: "My family dedicated me to the temple"
        effect: "Start with temple access, literacy path"
        class: "Temple Initiate"

  question_2:
    prompt: "What skills did you learn before coming here?"
    options:
      hands:
        text: "I worked the land"
        effect: "+Agriculture skills"
        tools: "Basic farming tools"

      craft:
        text: "I learned a craft"
        effect: "+Crafting skills"
        tools: "Basic craft tools"
        followup: "Which craft?" (pottery, weaving, etc.)

      water:
        text: "I lived by the water"
        effect: "+Fishing, swimming"
        tools: "Net, fishing gear"

      none:
        text: "I have only my strength"
        effect: "No bonuses, but no constraints"
        tools: "Nothing but clothes"
```

### 3.2 Starting Class Distribution

```yaml
starting_classes:
  laborer:
    description: "Unskilled worker, sells physical labor"
    starting_resources:
      barley: 5
      tools: "None or very basic"
      clothing: "Simple garment"
      shelter: "None (must find)"
    advantages:
      - "No obligations"
      - "Can try anything"
      - "Accepted everywhere"
    disadvantages:
      - "Lowest pay"
      - "No specialized skills"
      - "Must build from nothing"
    typical_first_job: "Field work, hauling, digging"

  farmer_apprentice:
    description: "Learning agriculture from family or patron"
    starting_resources:
      barley: 10
      tools: "Wooden hoe, sickle"
      clothing: "Work garment"
      shelter: "Shared quarters"
    advantages:
      - "Known skill path"
      - "Mentor relationship"
      - "Tool access"
    disadvantages:
      - "Obligations to patron"
      - "Less freedom"
    typical_first_job: "Assist with plowing, planting, harvest"

  fisher:
    description: "Works the marshes and river"
    starting_resources:
      barley: 8
      tools: "Net, fish spear, small coracle"
      clothing: "Light garment"
      shelter: "Marsh settlement access"
    advantages:
      - "Independent work"
      - "Daily food source"
      - "Water knowledge"
    disadvantages:
      - "Dangerous work"
      - "Socially marginal"
    typical_first_job: "Fishing, reed cutting, fowling"

  craft_apprentice:
    description: "Learning a specific trade"
    starting_resources:
      barley: 8
      tools: "Basic craft tools (varies by craft)"
      clothing: "Work garment"
      shelter: "Workshop sleeping area"
    craft_options:
      - "Potter (clay tools, kiln access)"
      - "Weaver (spindle, loom access)"
      - "Reed worker (cutting tools)"
      - "Carpenter (basic woodworking)"
    advantages:
      - "Clear skill progression"
      - "Workshop community"
      - "Can produce goods to sell"
    disadvantages:
      - "Bound to master for period"
      - "Limited freedom initially"
    typical_first_job: "Assist master, simple tasks"

  traders_hand:
    description: "Works with merchants, knows trade"
    starting_resources:
      barley: 15
      tools: "Carrying equipment, perhaps small goods"
      clothing: "Better garment"
      shelter: "Harbor quarter lodging"
    advantages:
      - "Economic knowledge"
      - "Foreign contact potential"
      - "Better starting resources"
    disadvantages:
      - "Expected to maintain merchant relationship"
      - "Focused on commerce, not production"
    typical_first_job: "Porter, trade assistant, inventory keeper"

  temple_initiate:
    description: "Dedicated to temple service"
    starting_resources:
      barley: 10
      tools: "None (temple provides)"
      clothing: "Temple garment"
      shelter: "Temple dormitory"
    advantages:
      - "Literacy path available"
      - "Temple protection"
      - "Regular meals"
      - "Knowledge access"
    disadvantages:
      - "Bound to temple duties"
      - "Less personal freedom"
      - "Religious obligations"
    typical_first_job: "Temple cleaning, ritual assistance, record copying"
```

---

## 4. Profession Paths

### 4.1 The Profession Tree

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│                    PROFESSION PROGRESSION                           │
│                                                                     │
│  AGRICULTURE PATH                                                   │
│  ────────────────                                                   │
│  Laborer ──► Field Hand ──► Farmer ──► Master Farmer               │
│                    │                        │                       │
│                    └──► Shepherd ──► Herd Master                   │
│                    │                                                │
│                    └──► Irrigation Worker ──► Canal Supervisor     │
│                                                                     │
│  CRAFTS PATH                                                        │
│  ────────────                                                       │
│  Apprentice ──► Journeyman ──► Craftsman ──► Master Craftsman     │
│       │                              │                              │
│       ├── Potter                     └──► Guild Leader             │
│       ├── Weaver                                                    │
│       ├── Smith                                                     │
│       ├── Carpenter                                                 │
│       └── Reed Worker                                               │
│                                                                     │
│  TRADE PATH                                                         │
│  ──────────                                                         │
│  Porter ──► Trader's Hand ──► Merchant ──► Trade Master           │
│                    │                 │                              │
│                    └──► Boatman ──► Ship Captain                   │
│                                                                     │
│  TEMPLE PATH                                                        │
│  ────────────                                                       │
│  Initiate ──► Acolyte ──► Priest ──► High Priest                  │
│       │           │                                                 │
│       │           └──► Scribe ──► Chief Scribe                     │
│       │                                                             │
│       └──► Temple Worker ──► Temple Administrator                  │
│                                                                     │
│  SERVICE PATH                                                       │
│  ────────────                                                       │
│  Servant ──► Skilled Servant ──► House Manager                     │
│       │                                                             │
│       └──► Brewer ──► Tavern Keeper ──► Tavern Owner              │
│                                                                     │
│  SPECIAL PATHS (Require specific achievements)                      │
│  ─────────────                                                      │
│  Any ──► Innovator (Solve major problem)                           │
│  Any ──► Elder (Survive to old age, share wisdom)                  │
│  Any ──► Leader (Gain followers, political path)                   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 4.2 Progression Requirements

```yaml
progression_requirements:
  laborer_to_field_hand:
    time: "7 game days of farm work"
    skill: "Basic agriculture 10+"
    reputation: "Known to a farmer"

  field_hand_to_farmer:
    time: "30 game days"
    skill: "Agriculture 30+"
    assets: "Own tools OR patron sponsorship"
    knowledge: "Understand seasonal cycles"

  farmer_to_master_farmer:
    time: "Multiple seasons"
    skill: "Agriculture 70+"
    assets: "Own or lease land"
    achievement: "Survive a bad year, help others"
    teaching: "Train at least one field hand"

  apprentice_to_journeyman:
    time: "30 game days with master"
    skill: "Craft skill 30+"
    product: "Produce acceptable goods independently"

  journeyman_to_craftsman:
    time: "Multiple months"
    skill: "Craft skill 60+"
    product: "Produce high-quality goods"
    reputation: "Known for quality work"

  craftsman_to_master:
    skill: "Craft skill 90+"
    innovation: "Create improvement or new technique"
    teaching: "Train at least one journeyman"
    recognition: "Temple or guild acknowledgment"
```

### 4.3 Profession Benefits

```yaml
profession_benefits:
  field_hand:
    income: "3 sila/day base"
    access: "Farm tool borrowing"
    knowledge: "Seasonal planting info"

  farmer:
    income: "Variable (crop dependent)"
    access: "Land lease eligibility"
    knowledge: "Advanced agriculture"
    status: "Respected community member"

  master_farmer:
    income: "High (surplus sales)"
    access: "Own land, hire workers"
    knowledge: "Innovation opportunities"
    status: "Community leader potential"

  journeyman_craftsman:
    income: "5 sila/day"
    access: "Workshop access anywhere"
    knowledge: "Trade secrets"
    freedom: "Can work independently"

  master_craftsman:
    income: "10+ sila/day"
    access: "Own workshop"
    knowledge: "Innovation priority"
    status: "Guild council eligibility"
    special: "Can create heirloom items"

  merchant:
    income: "Variable (trade dependent)"
    access: "Foreign contacts"
    knowledge: "Market information"
    mobility: "Travel privileges"

  priest:
    income: "Temple salary (comfortable)"
    access: "Temple inner areas"
    knowledge: "Divine lore, literacy"
    status: "High social standing"
    special: "Communion with gods possible"

  scribe:
    income: "8+ sila/day"
    access: "Archives, records"
    knowledge: "Literacy (rare, powerful)"
    status: "Essential to administration"
    special: "Can create permanent records"
```

---

## 5. Starting Equipment

### 5.1 Equipment by Class

```yaml
starting_equipment:
  laborer:
    clothing:
      - "Simple linen kilt"
      - "Sandals (worn)"
    tools: []
    consumables:
      - "5 sila barley"
    total_value: "~8 sila equivalent"

  farmer_apprentice:
    clothing:
      - "Work tunic"
      - "Sandals"
      - "Head wrap (sun protection)"
    tools:
      - "Wooden hoe (basic quality)"
      - "Sickle (shared with master)"
      - "Seed pouch"
    consumables:
      - "10 sila barley"
      - "Small oil flask"
    total_value: "~35 sila equivalent"

  fisher:
    clothing:
      - "Light kilt"
      - "No sandals (barefoot in water)"
    tools:
      - "Fishing net (basic)"
      - "Fish spear"
      - "Coracle access (shared)"
      - "Gutting knife"
    consumables:
      - "8 sila barley"
      - "String for repairs"
    total_value: "~40 sila equivalent"

  potter_apprentice:
    clothing:
      - "Work tunic (clay-stained)"
      - "Sandals"
    tools:
      - "Clay shaping tools (set)"
      - "Water bowl"
      - "Kiln access (master's)"
    consumables:
      - "8 sila barley"
      - "Clay allocation (weekly)"
    total_value: "~30 sila equivalent"

  weaver_apprentice:
    clothing:
      - "Simple garment"
      - "Sandals"
    tools:
      - "Spindle (personal)"
      - "Loom access (master's)"
      - "Wool allocation (weekly)"
    consumables:
      - "8 sila barley"
    total_value: "~25 sila equivalent"

  traders_hand:
    clothing:
      - "Better quality tunic"
      - "Good sandals"
      - "Carrying bag"
    tools:
      - "Counting tokens"
      - "Small scale"
      - "Trade goods (5 sila value)"
    consumables:
      - "15 sila barley"
    total_value: "~50 sila equivalent"

  temple_initiate:
    clothing:
      - "Temple garment (white)"
      - "Sandals"
    tools:
      - "Cleaning implements"
      - "Practice stylus"
      - "Wax tablet (for learning)"
    consumables:
      - "10 sila barley (temple allocation)"
    total_value: "~30 sila equivalent"
    special: "Temple provides meals if duties completed"
```

### 5.2 Tool Quality System

```yaml
tool_quality:
  tiers:
    makeshift:
      description: "Improvised, temporary"
      durability: "25% of standard"
      effectiveness: "60% of standard"
      cost: "Free or very cheap"

    basic:
      description: "Simple but functional"
      durability: "100% (baseline)"
      effectiveness: "100% (baseline)"
      cost: "Standard price"

    quality:
      description: "Well-made, better materials"
      durability: "150%"
      effectiveness: "120%"
      cost: "2x standard"

    superior:
      description: "Expert craftsmanship"
      durability: "200%"
      effectiveness: "140%"
      cost: "5x standard"

    masterwork:
      description: "Exceptional, named items"
      durability: "300%"
      effectiveness: "160%"
      cost: "10x+ standard"
      special: "Can become heirloom"

  durability_system:
    description: "Tools wear with use"
    repair: "Can be repaired (cost, time)"
    breaking: "Broken tool = major setback"
    maintenance: "Regular care extends life"
```

---

## 6. Earning Mechanics

### 6.1 Work Types

```yaml
work_types:
  wage_labor:
    description: "Work for someone else, paid by time"
    payment: "Daily in barley"
    examples:
      - "Field hand (3 sila/day)"
      - "Porter (4 sila/day)"
      - "Digger (3 sila/day)"
    pros: "Reliable income, no investment"
    cons: "Low pay, no ownership, limited advancement"

  piece_work:
    description: "Paid per item or task"
    payment: "Per completion"
    examples:
      - "Harvest baskets (0.5 sila/basket)"
      - "Bricks made (0.3 sila/brick)"
      - "Fish caught (market rate)"
    pros: "Skill rewards more earnings"
    cons: "Variable income, quality matters"

  crafting:
    description: "Create goods to sell"
    payment: "Sale price minus materials"
    examples:
      - "Pots (10-30 sila depending on quality)"
      - "Cloth (15-50 sila depending on quality)"
      - "Tools (variable)"
    pros: "Higher potential income, ownership"
    cons: "Need skills, tools, materials, market"

  trading:
    description: "Buy low, sell high"
    payment: "Profit margin"
    examples:
      - "Bring fish to city (markup)"
      - "Bring city goods to farms (markup)"
      - "Import/export with travelers"
    pros: "Can scale, leverage knowledge"
    cons: "Requires capital, risk of loss"

  service:
    description: "Provide a service"
    payment: "Fee or tips"
    examples:
      - "Guide (negotiated)"
      - "Translator (high value)"
      - "Healer (variable)"
      - "Entertainer (tips)"
    pros: "No material investment"
    cons: "Reputation dependent, variable demand"

  temple_work:
    description: "Work for temple in exchange for rations"
    payment: "Monthly rations + meals"
    examples:
      - "Temple cleaning"
      - "Ritual assistance"
      - "Record copying"
    pros: "Stable, food included, advancement path"
    cons: "Lower flexibility, obligations"
```

### 6.2 Income Levels

```yaml
income_levels:
  daily_needs:
    food: "2 sila barley equivalent"
    water: "Free from wells"
    basic_shelter: "1 sila (shared room)"
    total_survival: "~3 sila/day"

  comfortable_living:
    food: "3-4 sila (variety)"
    shelter: "3-5 sila (private room)"
    clothing: "10 sila/month"
    misc: "2 sila/day"
    total: "~8-10 sila/day"

  prosperous_living:
    food: "5+ sila (quality)"
    shelter: "10+ sila (good house)"
    servants: "5 sila/day"
    status_goods: "Variable"
    total: "~20+ sila/day"

  income_by_profession:
    # Daily averages
    unskilled_laborer: "2-3 sila"
    skilled_laborer: "4-5 sila"
    craftsman: "5-8 sila"
    merchant: "Variable (5-50+)"
    scribe: "8-12 sila"
    priest: "10-15 sila (plus benefits)"
```

### 6.3 Payment Methods

```yaml
payment_methods:
  daily_rations:
    form: "Barley, sometimes dates, oil"
    typical_for: "Laborers, temple workers"
    timing: "End of day or weekly"

  piece_payment:
    form: "Barley per item/task"
    typical_for: "Craftsmen, contractors"
    timing: "On completion"

  temple_credit:
    form: "Recorded in temple accounts"
    typical_for: "Regular workers, merchants"
    timing: "Ongoing balance"
    benefit: "Safer than carrying grain"

  goods_in_kind:
    form: "Products instead of grain"
    typical_for: "Barter arrangements"
    example: "Weave cloth, receive pots"

  silver:
    form: "Weighed silver pieces"
    typical_for: "Large transactions only"
    rarity: "Uncommon for daily work"
    note: "Usually temple-backed credit instead"
```

---

## 7. The Job Board System

### 7.1 How Jobs Appear

```yaml
job_sources:
  temple_board:
    location: "Temple courtyard"
    job_types:
      - "Temple positions (regular)"
      - "Public works (corvée)"
      - "Emergency needs"
    how_posted:
      - "Scribe announces"
      - "Physical board with tokens"
    reliability: "High pay, good conditions"

  harbor_board:
    location: "Harbor master's station"
    job_types:
      - "Loading/unloading"
      - "Boat work"
      - "Trade assistance"
    how_posted:
      - "Harbor master announces"
      - "Ship captains directly"
    reliability: "Variable, immediate payment"

  workshop_recruiting:
    location: "Artisan quarters"
    job_types:
      - "Apprenticeships"
      - "Temporary help"
      - "Specific commissions"
    how_posted:
      - "Master craftsmen directly"
      - "Word of mouth"
    reliability: "Depends on master"

  farm_work:
    location: "East gate, fields"
    job_types:
      - "Seasonal harvest"
      - "Plowing, planting"
      - "Irrigation maintenance"
    how_posted:
      - "Farmers at gate at dawn"
      - "Overseer assignments"
    reliability: "Seasonal, hard work"

  word_of_mouth:
    location: "Anywhere"
    job_types:
      - "Odd jobs"
      - "Personal service"
      - "Opportunities"
    how_found:
      - "Talk to NPCs"
      - "Reputation brings offers"
    reliability: "Variable"
```

### 7.2 Job Listing UI

```
┌─────────────────────────────────────────────────────────────────────┐
│  AVAILABLE WORK - TEMPLE DISTRICT                                   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ 🌾 HARVEST WORKERS NEEDED                                   │   │
│  │ Employer: Temple Granary                                    │   │
│  │ Pay: 4 sila/day + midday meal                              │   │
│  │ Duration: 10 days                                           │   │
│  │ Requirements: None (strength preferred)                     │   │
│  │ Status: 15 of 20 positions filled                          │   │
│  │ [APPLY] [DETAILS]                                          │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ 🏺 POTTER'S ASSISTANT                                       │   │
│  │ Employer: Master Ur-Nanshe                                  │   │
│  │ Pay: 3 sila/day                                            │   │
│  │ Duration: Ongoing (trial period)                           │   │
│  │ Requirements: Craft skill 5+                                │   │
│  │ Status: Seeking 1 person                                    │   │
│  │ Note: Could lead to apprenticeship                         │   │
│  │ [APPLY] [DETAILS]                                          │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ ⚠️ CANAL REPAIR - URGENT                                    │   │
│  │ Employer: Temple Administration                             │   │
│  │ Pay: 5 sila/day                                            │   │
│  │ Duration: Until complete                                    │   │
│  │ Requirements: None                                          │   │
│  │ Status: Needs 30 workers immediately                       │   │
│  │ Warning: Flood season approaching                          │   │
│  │ [APPLY] [DETAILS]                                          │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  [< Previous]  Page 1 of 3  [Next >]                               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 7.3 Dynamic Job Generation

```yaml
job_generation:
  factors:
    seasonal:
      - "Harvest season = many farm jobs"
      - "Flood season = construction/repair jobs"
      - "Festival = service jobs"

    economic:
      - "Trade ship arrival = porter jobs"
      - "Successful harvest = craft demand"
      - "Shortage = high-pay urgent jobs"

    story:
      - "Quest-related positions"
      - "Innovation-related needs"
      - "Player actions create jobs"

    player_driven:
      - "Players can post jobs (if they can pay)"
      - "Player businesses create NPC/player jobs"

  balance:
    always_available:
      - "Basic labor (low pay but reliable)"
      - "Temple positions (if favor sufficient)"
    sometimes_available:
      - "Skilled work (depends on need)"
      - "Good pay work (competitive)"
    rare:
      - "High-status positions"
      - "Special opportunities"
```

---

## 8. Business Ownership

### 8.1 Types of Businesses

```yaml
business_types:
  agricultural:
    farm:
      startup_cost: "100-500 sila (land lease)"
      requirements: "Agriculture skill 50+, tools"
      income_potential: "Variable (seasonal)"
      employees: "2-10 depending on size"

    orchard:
      startup_cost: "200-800 sila"
      requirements: "Agriculture skill 40+, patience (trees take time)"
      income_potential: "High once established"
      employees: "1-5"

    fishing_operation:
      startup_cost: "50-200 sila (boats, nets)"
      requirements: "Fishing skill 40+"
      income_potential: "Steady, moderate"
      employees: "2-6"

  craft:
    pottery_workshop:
      startup_cost: "100-300 sila (kiln, tools, space)"
      requirements: "Pottery skill 60+, master status"
      income_potential: "Moderate to high"
      employees: "2-8 (apprentices count)"

    weaving_house:
      startup_cost: "150-400 sila (looms, materials)"
      requirements: "Weaving skill 60+"
      income_potential: "Steady, scalable"
      employees: "3-20"

    smithy:
      startup_cost: "200-500 sila (forge, tools, materials)"
      requirements: "Metalworking skill 60+"
      income_potential: "High (specialized)"
      employees: "2-5"

  service:
    tavern:
      startup_cost: "100-300 sila (space, brewing equipment)"
      requirements: "Brewing skill 30+, social standing"
      income_potential: "Steady, information hub"
      employees: "2-6"

    lodging_house:
      startup_cost: "150-400 sila (building)"
      requirements: "Capital, location"
      income_potential: "Steady"
      employees: "1-4"

  trade:
    merchant_stall:
      startup_cost: "50-150 sila (goods, location)"
      requirements: "Trading skill 30+"
      income_potential: "Variable"
      employees: "1-3"

    trading_company:
      startup_cost: "500+ sila (capital, boats, contacts)"
      requirements: "Trading skill 60+, foreign contacts"
      income_potential: "High risk, high reward"
      employees: "5-20"
```

### 8.2 Business on the Map

Businesses for sale appear on the opportunity map:

```yaml
business_listings:
  display:
    icon: "Star (⭐)"
    color: "Gold for sale, silver for rent, bronze for partnership"

  listing_info:
    - "Business type"
    - "Location"
    - "Price/terms"
    - "Current income (if existing business)"
    - "Reputation/history"
    - "Requirements to purchase"

  acquisition_methods:
    purchase:
      description: "Buy outright"
      cost: "Full price"
      result: "Full ownership"

    lease:
      description: "Rent for period"
      cost: "Monthly payment"
      result: "Temporary control"

    partnership:
      description: "Share with another"
      cost: "Partial investment"
      result: "Shared profits and responsibilities"

    inheritance:
      description: "Receive from family/legacy"
      cost: "None (death of previous owner)"
      result: "Full or partial ownership"
```

### 8.3 Running a Business

```yaml
business_management:
  owner_tasks:
    daily:
      - "Check inventory"
      - "Manage employees"
      - "Handle customers"
      - "Quality control"

    periodic:
      - "Restock materials"
      - "Pay workers"
      - "Maintain equipment"
      - "Handle disputes"

  delegation:
    description: "Can hire manager to run day-to-day"
    cost: "Higher wages"
    benefit: "Freedom to do other things"
    risk: "Theft, incompetence possible"

  automation_level:
    active_management: "Player handles everything"
    supervised: "Player checks in daily"
    delegated: "Manager runs it, player reviews weekly"
    passive: "Just collect income (reduced efficiency)"

  failure_risks:
    - "Material shortage"
    - "Employee issues"
    - "Competition"
    - "Disaster (fire, flood)"
    - "Theft"
    - "Reputation damage"
```

---

## 9. Social Mobility

### 9.1 The Class Ladder

```yaml
social_classes:
  # Historical accuracy with gameplay mobility

  slave:
    description: "Bound to owner, few rights"
    how_to_enter: "Debt, crime, war (NPC mostly)"
    how_to_exit:
      - "Owner frees you"
      - "Buy freedom (save earnings)"
      - "Heroic act"
    player_note: "Players don't start as slaves but could fall into debt slavery"

  commoner:
    description: "Free but poor"
    typical_roles: "Laborer, farmer, fisher, basic worker"
    income_range: "2-5 sila/day"
    mobility: "Can rise through skill, luck, innovation"

  artisan:
    description: "Skilled, respected"
    typical_roles: "Craftsman, skilled worker, minor merchant"
    income_range: "5-10 sila/day"
    requirements: "Skill 50+ in a craft"
    mobility: "Can rise through mastery, business success"

  merchant_class:
    description: "Wealth but not birth"
    typical_roles: "Trader, business owner, wealthy craftsman"
    income_range: "10-50+ sila/day"
    requirements: "Significant capital, reputation"
    mobility: "Can approach elite through wealth"

  professional:
    description: "Essential specialized skills"
    typical_roles: "Scribe, priest, administrator"
    income_range: "10-20 sila/day"
    requirements: "Literacy or temple training"
    mobility: "Respected, can influence elites"

  elite:
    description: "Ruling class"
    typical_roles: "High priest, official, noble"
    how_to_reach:
      - "Major innovation (rare)"
      - "Political success"
      - "Exceptional service"
      - "Marry into"
    player_note: "Very difficult for first-generation player"
```

### 9.2 Mobility Mechanisms

```yaml
mobility_paths:
  skill_mastery:
    description: "Become the best at something"
    example: "Master potter → guild leader → temple recognition"
    timeline: "Multiple lifetimes potentially"

  innovation:
    description: "Solve a major problem"
    example: "Invent better irrigation → recognized → elevated"
    timeline: "Can be rapid if successful"
    reward: "Immediate class jump possible"

  wealth_accumulation:
    description: "Get rich through trade/business"
    example: "Successful merchant → buy land → become landed"
    timeline: "Gradual, one lifetime possible"

  temple_path:
    description: "Rise through religious hierarchy"
    example: "Initiate → scribe → priest → high priest"
    timeline: "Long, requires dedication"
    benefit: "Stable path with clear steps"

  political:
    description: "Gain influence and power"
    example: "Organize workers → lead community → recognized"
    timeline: "Variable, risky"
    requirement: "Charisma, followers"

  marriage:
    description: "Marry above your station"
    example: "Craftsman's daughter marries merchant's son"
    limitation: "More about children's status than yours"

  legacy:
    description: "Children inherit your progress"
    mechanism: "Bloodline system carries forward"
    benefit: "Next generation starts higher"
```

---

## 10. The First Hour

### 10.1 Immediate Onboarding

```yaml
first_hour_flow:
  minute_0_5:
    event: "Timeline zoom, drop into Eridu"
    player_state: "Confused, awed, hungry"
    ui_shows:
      - "Survival meters (Hunger 85%, Thirst 90%)"
      - "No inventory"
      - "Map hint"

  minute_5_10:
    event: "Elder NPC approaches"
    dialogue: |
      "You look lost, friend. New to Eridu?
      The temple gives water freely, and
      there's always work for willing hands.
      But hurry - the river rises soon."
    ui_shows:
      - "Quest marker: Temple courtyard"
      - "Timer hint: Flood in 14 days"

  minute_10_15:
    event: "Reach temple courtyard"
    available_actions:
      - "Drink from public well (thirst restored)"
      - "Talk to job announcer"
      - "Observe activity"
    ui_shows:
      - "Job board icon glows"
      - "Multiple NPCs highlighted (interactable)"

  minute_15_25:
    event: "First job taken"
    typical_job: "Help carry grain to granary (1 hour)"
    experience:
      - "Learn work mechanics"
      - "Earn first pay (2 sila)"
      - "Meet other workers"
      - "Hear rumors"
    ui_shows:
      - "Work progress bar"
      - "Payment received notification"

  minute_25_35:
    event: "First purchase"
    need: "Hungry, need food"
    options:
      - "Buy bread from vendor (0.5 sila)"
      - "Buy fish (2 sila, better)"
      - "Find free food (scraps, luck)"
    learning: "Currency system, prices"

  minute_35_45:
    event: "Shelter decision"
    options:
      - "Temple courtyard (free, uncomfortable)"
      - "Commoner quarter room (1 sila)"
      - "Work for lodging"
    introduces: "Housing mechanics"

  minute_45_60:
    event: "Introduction to innovation"
    trigger: "Overhear frustrated farmer"
    dialogue: |
      "The water won't reach the far field!
      Every year the same problem...
      If only there was a way..."
    effect:
      - "Innovation opportunity noted on map"
      - "Quest hint: Maybe you could help?"
    ui_shows:
      - "Innovation radar pulse"
      - "Problem area highlighted"
```

### 10.2 First Day Goals

```yaml
first_day_goals:
  survival:
    - "Find food (achieved through first job)"
    - "Find water (temple well)"
    - "Find shelter (any option)"

  economic:
    - "Complete first job"
    - "Earn first payment"
    - "Understand currency"

  social:
    - "Meet at least 3 NPCs"
    - "Learn one person's name"
    - "Hear one rumor"

  world:
    - "See map overview"
    - "Understand flood is coming"
    - "Notice innovation opportunity"

  optional_achievements:
    - "Find better paying job"
    - "Make a friend"
    - "Explore outside walls"
    - "Visit different district"
```

### 10.3 First Week Arc

```yaml
first_week_arc:
  day_1_2:
    focus: "Survival"
    activities: "Basic work, establish routine"
    goal: "Stable food and shelter"

  day_3_4:
    focus: "Integration"
    activities: "Better job, relationships"
    goal: "Known to some NPCs, regular income"

  day_5_6:
    focus: "Preparation"
    activities: "Flood preparation visible"
    goal: "Understand the threat, find role"
    event: "Canal work opportunity"

  day_7:
    focus: "Investment"
    decision_point: "What path to pursue?"
    options:
      - "Double down on current work"
      - "Seek apprenticeship"
      - "Investigate innovation"
      - "Build relationships"

  flood_countdown:
    day_7: "7 days until flood"
    urgency: "NPCs talking about it"
    opportunity: "High-pay emergency work"
    innovation_hook: "Canal system clearly inadequate"
```

---

## 11. Innovation Integration

### 11.1 Work Reveals Problems

```yaml
innovation_through_work:
  principle: "Working exposes you to inefficiencies"

  examples:
    farmer:
      work: "Manually carrying water"
      frustration: "Back aches, takes forever"
      innovation_hint: "Shaduf (lever system)"
      discovery_path: "Work → observe → think → try"

    potter:
      work: "Hand-shaping clay"
      frustration: "Inconsistent shapes, slow"
      innovation_hint: "Potter's wheel improvement"
      discovery_path: "Practice → frustration → experiment"

    fisher:
      work: "Paddling upstream"
      frustration: "Exhausting, can't reach good spots"
      innovation_hint: "Sail"
      discovery_path: "Observe wind → experiment → succeed"

    laborer:
      work: "Carrying heavy loads short distance"
      frustration: "Too heavy, too slow"
      innovation_hint: "Wheel, lever, ramp"
      discovery_path: "Necessity → observation → testing"

  mechanic:
    description: "Time spent working increases innovation insight"
    formula: "Hours worked + frustration events = discovery chance"
    benefit: "Workers have natural path to innovation"
```

### 11.2 Innovation Map Markers

```yaml
innovation_markers:
  problem_sites:
    icon: "Red pulse"
    info_shown:
      - "What's failing"
      - "Who's frustrated"
      - "Potential impact if solved"
    example:
      location: "East irrigation canal"
      problem: "Water not reaching far fields"
      affected: "12 farming families"
      potential: "Solve = major reputation + possible reward"

  hint_sources:
    icon: "Blue glow"
    info_shown:
      - "NPC who knows something"
      - "Artifact or text location"
      - "Observation opportunity"
    example:
      location: "Elder by the harbor"
      hint_type: "Memory of old technique"
      requirement: "Build relationship first"

  experiment_sites:
    icon: "Yellow area"
    info_shown:
      - "Safe to try things"
      - "Materials available"
      - "Previous attempts"
    example:
      location: "Abandoned field east of city"
      features: "Water access, privacy, discarded materials"
      history: "Others have tried here before"
```

### 11.3 Work-Innovation Synergy

```yaml
work_innovation_synergy:
  time_invested:
    description: "More work in area = more innovation potential"
    mechanic:
      - "10 hours farm work = +5% canal innovation chance"
      - "20 hours pottery = +10% wheel innovation chance"
      - "Cumulative, capped"

  skill_level:
    description: "Higher skill = see deeper problems"
    mechanic:
      - "Skill 0-20: See obvious problems"
      - "Skill 20-50: See subtle inefficiencies"
      - "Skill 50+: See potential improvements"

  relationship_bonus:
    description: "Known workers get told secrets"
    mechanic:
      - "Employer reputation 50+ = hints shared"
      - "Community standing = elders share memories"

  example_path:
    day_1_10: "Work as field hand, learn irrigation"
    day_11_20: "Notice canal problems, hear complaints"
    day_21_30: "Earn trust, elder shares old story"
    day_31_40: "Experiment with improvements"
    day_41_50: "Achieve breakthrough or fail and learn"
```

---

## 12. Training Data Value

### 12.1 Economic Behavior Data

```yaml
economic_training_data:
  questions_studied:
    - "How do humans make economic decisions under scarcity?"
    - "What motivates risk-taking vs. safety?"
    - "How do people evaluate opportunity cost?"
    - "What causes market behaviors to emerge?"

  data_captured:
    job_selection:
      - "Why did player choose this job over that?"
      - "How does pay vs. interest balance?"
      - "Risk tolerance in job choice"

    resource_allocation:
      - "Save vs. spend decisions"
      - "Investment timing"
      - "Response to shortage"

    business_decisions:
      - "When do players start businesses?"
      - "How do they price goods?"
      - "How do they handle competition?"

    class_mobility:
      - "What paths do players choose?"
      - "How do they balance advancement vs. security?"
      - "Long-term vs. short-term thinking"
```

### 12.2 Work Behavior Data

```yaml
work_training_data:
  questions_studied:
    - "How do humans approach repetitive tasks?"
    - "What makes work feel meaningful vs. grinding?"
    - "How does skill acquisition change behavior?"
    - "What triggers innovation thinking?"

  data_captured:
    task_approach:
      - "Optimization strategies"
      - "Efficiency improvements"
      - "Social vs. solo work preference"

    skill_development:
      - "Learning curves"
      - "Practice patterns"
      - "Knowledge transfer methods"

    innovation_triggers:
      - "Frustration threshold"
      - "Creative problem identification"
      - "Solution testing approaches"
```

---

## 13. Implementation Notes

### 13.1 MVP Scope

```yaml
mvp_professions:
  starting_classes:
    - "Laborer (simplest)"
    - "Farmer apprentice"
    - "Fisher"
    - "Temple initiate"

  profession_paths:
    - "Laborer → Field Hand → Farmer"
    - "Initiate → Temple Worker"
    - "Fisher path (complete)"

  job_system:
    - "Temple job board"
    - "Farm work (seasonal)"
    - "Basic harbor jobs"
    - "10-15 unique job types"

  business:
    - "Deferred to post-MVP"
    - "Focus on employment first"

  map_features:
    - "Job layer (green/yellow dots)"
    - "Innovation layer (red dots)"
    - "Basic zoom functionality"
```

### 13.2 Economy Balancing

```yaml
economy_balance:
  principles:
    - "Survival should be achievable but not trivial"
    - "Advancement should feel earned"
    - "Innovation should be attractive alternative to grinding"
    - "No single dominant strategy"

  tuning_variables:
    - "Job pay rates"
    - "Food/shelter costs"
    - "Tool durability"
    - "Skill progression speed"
    - "Innovation discovery rates"

  anti_exploit:
    - "Diminishing returns on repeated tasks"
    - "Market prices respond to supply/demand"
    - "NPCs remember player behavior"
```

### 13.3 UI Requirements

```yaml
ui_requirements:
  opportunity_map:
    - "Zoom in/out smoothly"
    - "Layer toggles"
    - "Pulse animations"
    - "Details on hover/click"

  job_board:
    - "Filterable list"
    - "Clear requirements/pay"
    - "Application tracking"

  economy_hud:
    - "Current resources"
    - "Active job status"
    - "Skill progress"
    - "Relevant meters"
```

---

## Appendix: Quick Reference

### Starting Class Comparison

| Class | Barley | Tools | Shelter | Best For |
|-------|--------|-------|---------|----------|
| Laborer | 5 | None | Find own | Freedom, blank slate |
| Farmer Apprentice | 10 | Hoe, sickle | Shared | Agriculture path |
| Fisher | 8 | Net, spear, boat | Marsh | Independence |
| Potter Apprentice | 8 | Clay tools | Workshop | Craft path |
| Weaver Apprentice | 8 | Spindle | Workshop | Craft path |
| Trader's Hand | 15 | Trade goods | Harbor | Commerce path |
| Temple Initiate | 10 | Stylus | Temple | Knowledge path |

### Income Quick Reference

| Work Type | Daily Income | Skill Required | Notes |
|-----------|-------------|----------------|-------|
| Unskilled labor | 2-3 sila | None | Always available |
| Farm hand | 3-4 sila | Basic | Seasonal peaks |
| Porter | 4 sila | Strength | Variable demand |
| Skilled craft | 5-8 sila | Craft 30+ | Need tools |
| Fishing | Variable | Fishing 20+ | Keep what you catch |
| Merchant assist | 5-6 sila | Trade 20+ | Better opportunities |
| Scribe work | 8-12 sila | Literacy | Rare, prestigious |

### Daily Budget (Survival)

| Expense | Cost | Notes |
|---------|------|-------|
| Food (minimum) | 2 sila | Bread and water |
| Food (comfortable) | 3-4 sila | Variety, beer |
| Shelter (shared) | 1 sila | Commoner quarter |
| Shelter (private) | 3-5 sila | Own room |
| **Total (survival)** | **3 sila** | Bare minimum |
| **Total (comfortable)** | **8-10 sila** | Decent living |

---

*"Every king was once a farmer's son. Every merchant was once a porter. The only difference is what they did with their days."*
