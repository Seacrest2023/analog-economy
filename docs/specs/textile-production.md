# Textile Production

> *"Wool is silver that grows on legs. The weaver who masters thread masters wealth. The dyer who knows secrets holds power no king can take."*

## Overview

Textile production is the largest industry in Eridu after agriculture, employing more workers than any other craft. Wool accounts for 90% of fabric production and functions as currency itself. This spec covers the complete supply chain from raw fleece to finished garment, the skill progressions for spinning, weaving, and dyeing, and the economic opportunities within the temple workshop system.

---

## Design Philosophy

### Core Principles

1. **Industry Scale**: Textiles are massive—thousands work in this sector
2. **Women's Domain**: Historically female-dominated profession, reflected in gameplay
3. **Full Supply Chain**: From sheep to finished cloth, every step matters
4. **Quality Grades**: Output ranges from elite temple garments to worker rags
5. **Training Data Value**: Process mastery, quality control, production management

### Economic Significance

```yaml
textile_economy:
  scale: "Largest employer after agriculture"

  uses_of_wool:
    currency: "Wool bundles as trade medium"
    clothing: "All social classes"
    export: "Major trade good"
    temple: "Sacred garments for gods"
    taxation: "Measured in wool units"

  price_structure:
    raw_fleece: "Base value"
    spun_thread: "2x raw fleece"
    undyed_cloth: "3x raw fleece"
    dyed_cloth: "5-15x raw fleece"
    finished_garment: "10-50x raw fleece"
```

---

## The Production Chain

### Stage 1: Raw Materials

```yaml
raw_materials:
  wool_sources:
    temple_flocks:
      quality: "Highest (controlled breeding)"
      access: "Temple workers, approved purchasers"
      cost: "Set prices, reliable supply"

    private_shepherds:
      quality: "Variable"
      access: "Market purchase, contracts"
      cost: "Negotiable, seasonal variation"

    marsh_gatherers:
      quality: "Lower (wild sheep)"
      access: "Open (dangerous areas)"
      cost: "Time and risk"

  wool_grades:
    white_premium:
      description: "Purest white, takes any dye"
      value: "3x standard"
      use: "Elite garments, temple wear"

    standard_white:
      description: "Clean white wool"
      value: "Base unit"
      use: "General production"

    colored_natural:
      description: "Brown, black, grey natural"
      value: "0.8x standard"
      use: "Worker clothing, undyed goods"

    carpet_wool:
      description: "Coarse, long fibers"
      value: "0.5x standard"
      use: "Rugs, heavy blankets, bags"
```

### Stage 2: Fiber Preparation

```yaml
fiber_preparation:
  cleaning:
    process: "Remove dirt, debris, lanolin"
    method: "Washing in canal water, sun drying"
    skill: "Basic (anyone can learn)"
    time: "2-3 hours per fleece"
    sila_reward: 10

  sorting:
    process: "Separate grades within fleece"
    method: "Hand inspection, grouping"
    skill: "Requires training"
    importance: "Quality of final product"
    sila_reward: 15

  combing:
    process: "Align fibers for spinning"
    method: "Wooden or bone combs"
    skill: "Technique matters"
    output: "Roving (prepared fiber bundle)"
    sila_reward: 15
```

### Stage 3: Spinning

```yaml
spinning:
  tool: "Drop spindle with clay or stone whorl"

  process:
    step_1: "Attach roving to spindle"
    step_2: "Spin whorl to twist fibers"
    step_3: "Draw out and twist thread"
    step_4: "Wind onto spindle shaft"
    step_5: "Repeat until spindle full"

  skill_factors:
    tension: "Consistent = even thread"
    speed: "Faster = more output"
    fiber_management: "Smooth joins"

  thread_grades:
    fine:
      use: "Elite garments"
      difficulty: "High"
      value: "3x standard"
      sila_reward: 40

    standard:
      use: "General clothing"
      difficulty: "Medium"
      value: "Base"
      sila_reward: 25

    coarse:
      use: "Work clothes, rope"
      difficulty: "Low"
      value: "0.5x standard"
      sila_reward: 15

  production_rate:
    novice: "1 fleece/week"
    apprentice: "2 fleeces/week"
    journeyman: "3 fleeces/week"
    master: "4+ fleeces/week (supervising others)"
```

### Stage 4: Dyeing

```yaml
dyeing:
  timing: "Dye thread BEFORE weaving (not after)"

  mordants:
    purpose: "Fix color permanently to fiber"
    types:
      alum: "Most common, bright colors"
      iron: "Darkens colors, greys"
      ash: "Alkali, affects hue"
    importance: "Wrong mordant = color fades"

  color_sources:
    red:
      source: "Madder root"
      availability: "Common"
      meaning: "Life, vitality"
      value: "2x undyed"
      sila_reward: 35

    blue:
      source: "Woad (local) or Indigo (imported)"
      availability: "Woad common, indigo rare"
      meaning: "Divine, heavenly"
      value: "3x undyed (woad), 5x (indigo)"
      sila_reward: 50

    yellow:
      source: "Saffron, pomegranate rind, safflower"
      availability: "Moderate"
      meaning: "Abundance, priestly"
      value: "2-4x undyed"
      sila_reward: 40

    purple:
      source: "Murex shellfish (imported)"
      availability: "Rare, expensive"
      meaning: "Royal, ultimate prestige"
      value: "10x+ undyed"
      sila_reward: 100
      note: "Trade route dependent"

    brown:
      source: "Walnut hulls"
      availability: "Common"
      meaning: "Earth, humble"
      value: "1.5x undyed"
      sila_reward: 25

    black:
      source: "Iron + tannins"
      availability: "Moderate"
      meaning: "Authority, mystery"
      value: "2x undyed"
      sila_reward: 35

  process:
    step_1: "Prepare mordant bath"
    step_2: "Soak thread in mordant"
    step_3: "Prepare dye bath"
    step_4: "Submerge thread in dye"
    step_5: "Monitor time for depth"
    step_6: "Rinse and dry"

  secrets:
    description: "Master dyers guard their recipes"
    competitive_advantage: "Unique colors = premium prices"
    learning: "Apprenticeship or experimentation"
    training_data: "Recipe development, color theory"
```

### Stage 5: Weaving

```yaml
weaving:
  loom_types:
    vertical_loom:
      description: "Warp-weighted, standing loom"
      use: "Standard cloth production"
      cost: "50-150 SILA"
      footprint: "Modest space"
      output: "2-3 cubits/day"

    horizontal_loom:
      description: "Ground loom, wider fabrics"
      use: "Large textiles, special patterns"
      cost: "100-300 SILA"
      footprint: "More space required"
      output: "3-4 cubits/day"

    tablet_loom:
      description: "Portable, for bands and straps"
      use: "Decorative borders, belts"
      cost: "10-30 SILA"
      portability: "Carry anywhere"

  process:
    warping: "Set up vertical threads (critical)"
    heddles: "Organize threads for pattern"
    weaving: "Pass weft through warp"
    beating: "Compact each row"
    finishing: "Cut off, process edges"

  patterns:
    plain_weave:
      difficulty: "Low"
      use: "Basic cloth"
      sila_reward: 25

    twill:
      difficulty: "Medium"
      use: "Stronger fabric, diagonal lines"
      sila_reward: 40

    patterned:
      difficulty: "High"
      use: "Decorative, elite garments"
      sila_reward: 75

    tapestry:
      difficulty: "Very high"
      use: "Wall hangings, temple decoration"
      sila_reward: 100

  cloth_grades:
    sumptuous:
      description: "Finest thread, complex pattern"
      use: "Gods' garments, royal wear"
      price: "500-2000 SILA"

    first_grade:
      description: "Quality thread, good weave"
      use: "Elite citizens"
      price: "100-500 SILA"

    second_grade:
      description: "Standard quality"
      use: "Middle class"
      price: "30-100 SILA"

    third_grade:
      description: "Coarse but functional"
      use: "Common workers"
      price: "10-30 SILA"

    fourth_grade:
      description: "Rough, utilitarian"
      use: "Slaves, laborers"
      price: "5-10 SILA"
```

### Stage 6: Finishing

```yaml
finishing:
  processes:
    fulling:
      description: "Thicken and soften cloth"
      method: "Beating, treading in water"
      result: "Denser, warmer fabric"

    napping:
      description: "Raise fuzzy surface"
      method: "Brush with teasels"
      result: "Softer hand feel"

    cutting:
      description: "Shape into garments"
      method: "Bronze shears"
      skill: "Critical for fit"

    sewing:
      description: "Join pieces"
      method: "Bone needles, thread"
      skill: "Fine work for seams"

  garment_types:
    kaunakes:
      description: "Fleece skirt with tufts"
      use: "Traditional formal wear"
      production: "Specialized skill"

    tunic:
      description: "Basic body covering"
      use: "Universal wear"
      production: "Standard skill"

    shawl:
      description: "Draped outer garment"
      use: "All classes"
      production: "Simple construction"

    priestly_robes:
      description: "Elaborate ritual garments"
      use: "Temple ceremonies"
      production: "Master craftwork"
```

---

## Skill Trees

### Spinner Skill Tree

```yaml
spinner_skills:
  tier_1_novice:
    skills:
      basic_spinning:
        description: "Produce coarse thread"
        sila_reward: 15
        output: "Usable but low value"

      fiber_recognition:
        description: "Identify wool grades"
        sila_reward: 10
        importance: "Quality control"

    earnings: "Temple rations or 5-15 SILA/day"
    employment: "Workshop laborer"

  tier_2_apprentice:
    requirements: "50 spindles spun"
    skills:
      even_tension:
        description: "Consistent thread thickness"
        sila_reward: 25
        unlocks: "Standard grade output"

      speed_spinning:
        description: "Faster production rate"
        sila_reward: 20
        benefit: "More output = more income"

    earnings: "15-30 SILA/day"
    employment: "Valued workshop worker"

  tier_3_journeyman:
    requirements: "200 spindles + quality test"
    skills:
      fine_spinning:
        description: "Produce fine thread"
        sila_reward: 40
        unlocks: "Premium product access"

      teaching:
        description: "Train novice spinners"
        sila_reward: 30
        income: "Supervisor bonus"

    earnings: "30-60 SILA/day"
    employment: "Workshop supervisor"

  tier_4_master:
    requirements: "500 spindles + reputation"
    skills:
      ultra_fine:
        description: "Produce thread for gods' garments"
        sila_reward: 75
        prestige: "Elite recognition"

      workshop_management:
        description: "Run spinning operation"
        sila_reward: 100
        path: "Business ownership"

    earnings: "60-150 SILA/day"
    employment: "Independent or temple lead"
```

### Weaver Skill Tree

```yaml
weaver_skills:
  tier_1_novice:
    skills:
      loom_setup:
        description: "Warp a basic loom"
        sila_reward: 20
        critical: "Foundation for all weaving"

      plain_weave:
        description: "Basic over-under pattern"
        sila_reward: 20
        output: "Functional cloth"

    earnings: "Temple rations or 10-20 SILA/day"

  tier_2_apprentice:
    requirements: "20 lengths woven"
    skills:
      twill_patterns:
        description: "Diagonal weave patterns"
        sila_reward: 35
        output: "Stronger, more attractive"

      edge_finishing:
        description: "Clean selvedges"
        sila_reward: 25
        quality: "Professional appearance"

    earnings: "20-40 SILA/day"

  tier_3_journeyman:
    requirements: "100 lengths + pattern mastery"
    skills:
      complex_patterns:
        description: "Geometric, representational"
        sila_reward: 60
        prestige: "Artistic recognition"

      tapestry_basics:
        description: "Pictorial weaving"
        sila_reward: 75
        market: "Temple, elite commissions"

    earnings: "40-80 SILA/day"

  tier_4_master:
    requirements: "300 lengths + temple approval"
    skills:
      sacred_textiles:
        description: "Weave for gods' garments"
        sila_reward: 100
        honor: "Highest textile calling"

      design_creation:
        description: "Create original patterns"
        sila_reward: 100
        legacy: "Designs may outlive you"

    earnings: "80-200 SILA/day"
```

### Dyer Skill Tree

```yaml
dyer_skills:
  tier_1_novice:
    skills:
      mordant_preparation:
        description: "Prepare fixing baths"
        sila_reward: 20
        foundation: "All dyeing starts here"

      basic_colors:
        description: "Brown, simple yellow"
        sila_reward: 25
        output: "Common, functional"

    earnings: "Temple rations or 10-25 SILA/day"

  tier_2_apprentice:
    requirements: "50 dye batches"
    skills:
      red_mastery:
        description: "Consistent madder red"
        sila_reward: 35
        demand: "Popular color"

      color_depth:
        description: "Control light to dark"
        sila_reward: 30
        skill: "Timing mastery"

    earnings: "25-50 SILA/day"

  tier_3_journeyman:
    requirements: "200 batches + color range"
    skills:
      blue_mastery:
        description: "Woad/indigo techniques"
        sila_reward: 60
        prestige: "Divine color"

      compound_colors:
        description: "Green, orange, purple tones"
        sila_reward: 75
        skill: "Overdyeing techniques"

    earnings: "50-100 SILA/day"

  tier_4_master:
    requirements: "Secret recipes + reputation"
    skills:
      proprietary_recipes:
        description: "Unique colors only you can make"
        sila_reward: 150
        competitive: "Market advantage"

      purple_mastery:
        description: "Murex purple techniques"
        sila_reward: 200
        prestige: "Ultimate dyer status"

    earnings: "100-300 SILA/day"
```

---

## Employment Systems

### Temple Workshop

```yaml
temple_workshop:
  description: "Large-scale production facility"

  organization:
    lukur:
      role: "High-ranking priestess manager"
      duties: "Quotas, recipes, cycles"
      authority: "Absolute within workshop"

    sakintu:
      role: "Female administrator"
      duties: "Shipments, trade coordination"
      scope: "International commerce"

    overseers:
      role: "Floor supervisors"
      duties: "Quality control, discipline"
      ratio: "1 per 10-20 workers"

    workers:
      composition: "Local citizens, indentured, war captives"
      duties: "Production labor"
      compensation: "Rations, small wages"

  production_cycles:
    lunar_based: "Work organized around moon phases"
    quotas: "Specific output requirements"
    quality_checks: "Regular inspections"

  player_paths:
    worker:
      entry: "Available to any female character"
      compensation: "Rations + 5-15 SILA/day"
      advancement: "Skill demonstration"

    supervisor:
      requirements: "Journeyman skill + reputation"
      compensation: "Better rations + 30-60 SILA/day"
      responsibility: "Quality, discipline"

    administrator:
      requirements: "Literacy + high skill + connections"
      compensation: "Elite status + 80-150 SILA/day"
      responsibility: "Trade, logistics"
```

### Independent Production

```yaml
independent_production:
  requirements:
    equipment: "Own loom (50-300 SILA)"
    space: "Workshop area in home"
    materials: "Purchase wool, dyes"
    customers: "Build client base"

  advantages:
    flexibility: "Set own hours"
    profit: "Keep all margins"
    creativity: "Choose products"

  challenges:
    capital: "Must own equipment"
    materials: "Source everything"
    marketing: "Find customers"
    competition: "Temple undercuts prices"

  income_potential:
    novice: "15-30 SILA/day (slim margins)"
    established: "40-80 SILA/day"
    master: "100-300 SILA/day (specialty goods)"
```

---

## Quality and Trade

### Quality Grades

```yaml
quality_system:
  sumptuous:
    thread: "Ultra-fine, even"
    weave: "Complex patterns, perfect"
    dye: "Rare colors, vibrant"
    market: "Temple, royalty"
    price_multiplier: "10-20x base"

  first_grade:
    thread: "Fine, consistent"
    weave: "Good patterns"
    dye: "Quality colors"
    market: "Elite citizens"
    price_multiplier: "5-10x base"

  second_grade:
    thread: "Standard"
    weave: "Plain or simple twill"
    dye: "Common colors"
    market: "Middle class"
    price_multiplier: "2-4x base"

  third_grade:
    thread: "Coarse but usable"
    weave: "Plain only"
    dye: "Often undyed"
    market: "Common workers"
    price_multiplier: "1x base"

  fourth_grade:
    thread: "Rough"
    weave: "Basic"
    dye: "None"
    market: "Poorest"
    price_multiplier: "0.5x base"
```

### Trade Networks

```yaml
textile_trade:
  exports:
    destinations: "Elam, Dilmun, Egypt (eventually)"
    products: "Finished cloth, dyed thread"
    value: "Major trade surplus"

  imports:
    sources: "India (indigo), Mediterranean (murex)"
    products: "Rare dyes, exotic fibers"
    cost: "Premium prices"

  caravan_opportunities:
    player_role: "Supply trader with goods"
    profit: "Buy low, sell high"
    risk: "Caravan dangers"
```

---

## Training Data Value

### Knowledge Capture

```yaml
training_data:
  process_mastery:
    - "Step-by-step craft procedures"
    - "Quality control decisions"
    - "Problem-solving (broken thread, uneven dye)"

  production_management:
    - "Resource allocation"
    - "Quota optimization"
    - "Worker coordination"

  market_decisions:
    - "Pricing strategies"
    - "Customer identification"
    - "Competition response"

  recipe_development:
    - "Dye experimentation"
    - "Color matching"
    - "Mordant selection"
```

---

## Implementation Notes

### Database Schema

```yaml
textile_records:
  producer_profile:
    player_id: uuid
    specializations: array  # spinner, weaver, dyer
    skill_levels: object
    recipes_known: array  # dye formulas
    equipment_owned: array
    production_history: array

  product_record:
    product_id: uuid
    producer_id: uuid
    material_grade: enum
    thread_quality: enum
    dye_color: string
    weave_pattern: string
    final_grade: enum
    price: integer
```

---

## Appendix: Sumerian Textile Terms

| Term | Meaning | Gameplay Role |
|------|---------|---------------|
| **Lukur** | High priestess/textile manager | Workshop authority |
| **Sakintu** | Female administrator | Trade coordinator |
| **Udu** | Sheep | Wool source |
| **Sig** | Wool | Raw material |
| **Tug** | Cloth/garment | Finished product |
| **Kaunakes** | Fleece skirt | Traditional garment |

---

*"Thread by thread, the weaver builds a world. Each pass of the shuttle is a choice. Each color is a statement. In Eridu, we wear our wealth, our status, our devotion—all in the cloth that covers us."*
