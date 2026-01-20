# Pottery & Ceramics

> *"From the mud of the riverbank rises the vessel that holds the beer, the jar that stores the grain, the tablet that preserves the word. The potter's wheel is the axis upon which civilization turns."*

## Overview

Pottery is the foundation industry of Eridu. Unlike wood, clay is abundant—the gift of the Euphrates. Every household needs vessels for storage, cooking, and eating. The Bahar (potter) transforms river clay into the containers that hold civilization together: storage jars, cooking pots, drinking vessels, cult objects, and the clay tablets on which scribes write. This spec covers clay processing, wheel techniques, kiln operations, product specializations, and the economics of ceramic production.

---

## Design Philosophy

### Core Principles

1. **Material Abundance**: Clay is free and plentiful
2. **Skill Differentiation**: Quality separates potters
3. **Essential Products**: Everyone needs pottery daily
4. **Specialization Value**: Different vessels require different expertise
5. **Training Data Value**: Process mastery, quality control, kiln management

### Economic Context

```yaml
pottery_economy:
  material_advantage:
    clay: "Free from riverbanks"
    fuel: "Dung, reed, chaff available"
    tools: "Simple, homemade possible"

  market_reality:
    demand: "Constant, universal"
    competition: "Many potters"
    differentiation: "Quality and specialization"

  price_factors:
    size: "Larger = more expensive"
    quality: "Fine work commands premium"
    decoration: "Painted/incised adds value"
    specialty: "Specific uses cost more"
```

---

## Clay and Materials

### Clay Types

```yaml
clay_varieties:
  alluvial_clay:
    source: "River deposits"
    quality: "Variable"
    preparation: "Needs processing"
    use: "Common pottery"
    cost: "Free (labor to collect)"

  refined_clay:
    source: "Processed alluvial"
    quality: "Good"
    preparation: "Washed, levigated"
    use: "Quality vessels"

  fine_clay:
    source: "Specially selected and prepared"
    quality: "Excellent"
    preparation: "Extensive processing"
    use: "Tablets, fine ware"
    value: "Premium product"
```

### Clay Processing

```yaml
clay_preparation:
  step_1_collection:
    location: "Riverbank deposits"
    selection: "Choose clean clay beds"
    transport: "Baskets to workshop"
    sila_reward: 10

  step_2_cleaning:
    process: "Remove roots, stones, debris"
    method: "Manual picking, sieving"
    importance: "Contaminants cause failure"
    sila_reward: 15

  step_3_levigation:
    process: "Wash clay in water"
    method: "Settle, drain, repeat"
    result: "Fine particles separated"
    sila_reward: 20

  step_4_aging:
    process: "Store wet clay"
    duration: "Days to weeks"
    benefit: "Improves workability"
    science: "Bacterial action softens"
    sila_reward: 15

  step_5_wedging:
    process: "Knead to remove air"
    method: "Cut and slam repeatedly"
    critical: "Air bubbles explode in kiln"
    sila_reward: 20
```

### Temper and Additives

```yaml
temper_materials:
  purpose: "Reduce shrinkage and cracking"

  types:
    sand:
      source: "River sand"
      effect: "Opens clay body"
      use: "Large vessels, cooking pots"

    grog:
      source: "Ground fired pottery"
      effect: "Reduces shrinkage"
      use: "Structural ceramics"

    chaff:
      source: "Plant material"
      effect: "Burns out, creates pores"
      use: "Lightweight vessels"

    shell:
      source: "Crushed shells"
      effect: "Flux and temper"
      use: "Regional tradition"

  ratios:
    standard: "10-30% temper by volume"
    heavy: "More for large vessels"
    fine: "Less for thin walls"
```

---

## The Potter (Bahar)

### Profession Overview

```yaml
bahar_role:
  description: "Clay vessel maker"
  status: "Common artisan"

  workplace:
    home_workshop: "Family operation"
    commercial: "Market-oriented"
    temple: "Institutional production"

  income_sources:
    direct_sales: "Market, customers"
    commissions: "Specific orders"
    temple_contract: "Steady work"
```

### Forming Techniques

```yaml
forming_methods:
  hand_building:
    coiling:
      description: "Build with clay ropes"
      process: "Stack and smooth coils"
      use: "Large vessels"
      skill: "Basic but time-consuming"
      sila_reward: 20

    pinching:
      description: "Shape from ball"
      process: "Pinch out walls"
      use: "Small items"
      skill: "Simple technique"
      sila_reward: 15

    slab_building:
      description: "Flat clay sheets"
      process: "Cut and join slabs"
      use: "Angular forms, boxes"
      skill: "Moderate"
      sila_reward: 25

  wheel_throwing:
    slow_wheel:
      description: "Tournette (hand-turned)"
      process: "Rotate while shaping"
      use: "Symmetrical vessels"
      skill: "Intermediate"
      sila_reward: 30

    fast_wheel:
      description: "Kick wheel"
      process: "Continuous rotation"
      use: "Mass production, fine work"
      skill: "Advanced"
      sila_reward: 50
      advantage: "Speed and precision"

  mold_forming:
    press_mold:
      description: "Press clay into form"
      process: "Reusable molds"
      use: "Repeated shapes, tablets"
      skill: "Moderate"
      sila_reward: 25
```

### Potter Skill Tree

```yaml
potter_skills:
  tier_1_novice:
    skills:
      clay_preparation:
        description: "Process raw clay"
        sila_reward: 20
        foundation: "Essential starting skill"

      basic_coiling:
        description: "Build simple vessels"
        sila_reward: 20
        products: "Bowls, small jars"

      drying_management:
        description: "Prevent cracking"
        sila_reward: 15
        critical: "Rushed drying ruins work"

    role: "Workshop helper"
    earnings: "Rations"
    products: "Simple utilitarian ware"

  tier_2_apprentice:
    requirements: "1 year training"
    skills:
      wheel_basics:
        description: "Slow wheel forming"
        sila_reward: 35
        products: "Symmetrical vessels"

      slip_decoration:
        description: "Colored clay coating"
        sila_reward: 30
        effect: "Visual enhancement"

      kiln_loading:
        description: "Stack for firing"
        sila_reward: 30
        skill: "Maximize capacity, prevent damage"

    role: "Working potter"
    earnings: "Modest wage"
    products: "Standard household ware"

  tier_3_journeyman:
    requirements: "3 years + skill demonstration"
    skills:
      fast_wheel_mastery:
        description: "Kick wheel expertise"
        sila_reward: 50
        advantage: "Speed, precision, thin walls"

      kiln_management:
        description: "Control firing process"
        sila_reward: 50
        critical: "Temperature determines quality"

      decoration_arts:
        description: "Painted, incised designs"
        sila_reward: 50
        value: "Premium pricing"

    role: "Senior potter"
    earnings: "Good income"
    products: "Quality decorated ware"

  tier_4_master:
    requirements: "10 years + reputation"
    skills:
      fine_ware:
        description: "Exceptional thin-wall vessels"
        sila_reward: 100
        market: "Elite customers"

      specialty_forms:
        description: "Complex shapes"
        sila_reward: 100
        examples: "Ritual vessels, figurines"

      kiln_construction:
        description: "Build efficient kilns"
        sila_reward: 100
        value: "Improved production"

    role: "Master potter"
    earnings: "Premium prices"
    products: "Prestige ceramics"
```

---

## Kiln Technology

### Kiln Types

```yaml
kiln_varieties:
  open_fire:
    description: "Bonfire firing"
    temperature: "600-800°C"
    fuel: "Dung, wood, reed"
    quality: "Low, uneven"
    use: "Simple pottery"
    skill: "Basic"

  pit_kiln:
    description: "Fire in ground pit"
    temperature: "700-900°C"
    fuel: "Mixed fuels"
    quality: "Better than open"
    use: "Household production"
    skill: "Moderate"

  updraft_kiln:
    description: "Enclosed chamber"
    temperature: "900-1100°C"
    structure:
      firebox: "Lower chamber for fuel"
      floor: "Perforated for heat"
      chamber: "Upper stacking area"
      vent: "Top opening"
    quality: "Good, controllable"
    use: "Professional production"
    skill: "Advanced"

  two_chamber:
    description: "Separate fire and ware"
    temperature: "Higher, more even"
    quality: "Excellent"
    use: "Fine ceramics"
    skill: "Expert"
```

### Firing Process

```yaml
firing_stages:
  preparation:
    loading:
      process: "Stack vessels in kiln"
      skill: "Maximize capacity safely"
      separation: "Prevent sticking"
      sila_reward: 25

    fuel:
      types: "Dung cakes, reed, chaff, wood"
      preparation: "Dry, sized for burning"
      quantity: "Enough for full cycle"

  water_smoking:
    temperature: "20-150°C"
    duration: "Slow rise"
    purpose: "Drive out moisture"
    danger: "Too fast = explosion"
    sila_reward: 20

  oxidation:
    temperature: "300-600°C"
    process: "Burn out organics"
    atmosphere: "Plenty of air"
    color: "Clay lightens"

  sintering:
    temperature: "600-1000°C+"
    process: "Clay particles fuse"
    result: "Hardened ceramic"
    critical: "Target temperature for type"
    sila_reward: 40

  cooling:
    process: "Slow cool in kiln"
    danger: "Thermal shock cracks"
    duration: "Hours to overnight"
    sila_reward: 20

  unloading:
    timing: "When cool enough to touch"
    inspection: "Check for defects"
    sorting: "Quality grades"
```

### Kiln Management Skills

```yaml
kiln_expertise:
  temperature_reading:
    method: "Visual (color of flame/clay)"
    indicators:
      red_glow: "~700°C"
      bright_red: "~900°C"
      orange: "~1000°C+"
    skill: "Experience-based judgment"
    sila_reward: 40

  atmosphere_control:
    oxidation:
      method: "Open vents, air flow"
      result: "Light-colored pottery"

    reduction:
      method: "Restrict air"
      result: "Dark colors, special effects"

  fuel_management:
    rate: "Steady feeding"
    type: "Match to stage"
    efficiency: "Minimize waste"
    sila_reward: 30

  problem_solving:
    cracks: "Adjust drying/firing speed"
    color_issues: "Modify atmosphere"
    breakage: "Review loading/clay prep"
    sila_reward: 35
```

---

## Product Lines

### Storage Vessels

```yaml
storage_pottery:
  grain_jars:
    sizes:
      small: "5-10 liters (3-8 SILA)"
      medium: "20-50 liters (10-20 SILA)"
      large: "100+ liters (30-60 SILA)"
    features: "Wide mouth, stable base"
    market: "Every household"

  oil_jars:
    design: "Narrow neck, sealed"
    sizes: "Various"
    price: "5-25 SILA"
    use: "Sesame oil, fats"

  beer_vessels:
    types:
      brewing_vat: "Large, open"
      storage_jar: "Sealed for keeping"
      serving_jug: "Pour spout"
    market: "Brewers, taverns, households"
    price: "10-50 SILA"

  water_jars:
    features: "Porous (evaporative cooling)"
    sizes: "Daily use to large storage"
    price: "5-20 SILA"
```

### Cooking Vessels

```yaml
cooking_pottery:
  cooking_pots:
    features: "Thick walls, tempered clay"
    design: "Rounded bottom for fire"
    sizes: "1-20 liter capacity"
    price: "3-15 SILA"

  braziers:
    purpose: "Hold burning fuel"
    design: "Open top, vented"
    use: "Indoor cooking, heating"
    price: "5-20 SILA"

  baking_trays:
    purpose: "Flat bread preparation"
    design: "Shallow, wide"
    price: "2-8 SILA"
```

### Tableware

```yaml
tableware:
  bowls:
    types:
      eating_bowl: "Individual portions"
      serving_bowl: "Larger, communal"
      drinking_bowl: "Beverage vessel"
    price: "1-10 SILA"
    decoration: "Plain to painted"

  cups:
    design: "Hand-held drinking"
    sizes: "Small to standard"
    price: "1-5 SILA"

  plates:
    less_common: "Bread often serves as plate"
    use: "Formal dining"
    price: "2-8 SILA"

  beer_strainers:
    purpose: "Filter sediment while drinking"
    design: "Perforated bottom cup"
    use: "With drinking straws"
    price: "3-8 SILA"
```

### Specialty Items

```yaml
specialty_pottery:
  cult_objects:
    incense_burners:
      design: "Open top, often decorated"
      price: "5-30 SILA"
      customer: "Temples, households"

    offering_bowls:
      design: "Specific ritual forms"
      price: "5-20 SILA"
      customer: "Temples"

    figurines:
      types: "Gods, animals, humans"
      price: "5-50 SILA"
      skill: "Sculpture ability"

  tablets:
    clay_tablets:
      preparation: "Fine, smooth clay"
      forms: "Various sizes"
      market: "Scribes, schools, temples"
      price: "1-5 SILA per tablet"
      note: "Different from vessel potters"

  architectural:
    baked_bricks:
      production: "Specialized kilns"
      use: "Important structures"
      scale: "Industrial volume"
      price: "Bulk pricing"

    decorative_cones:
      use: "Wall decoration"
      technique: "Push into mud walls"
      price: "By quantity"

    drain_pipes:
      use: "Water management"
      design: "Interlocking tubes"
      price: "By length"
```

---

## Decoration Techniques

### Surface Treatments

```yaml
decoration_methods:
  slip:
    description: "Liquid clay coating"
    colors: "Red, white, black"
    application: "Dip, brush, pour"
    timing: "Before firing"
    sila_reward: 25

  burnishing:
    description: "Polish surface smooth"
    tool: "Smooth stone"
    timing: "Leather-hard stage"
    effect: "Shiny surface"
    sila_reward: 20

  painting:
    description: "Colored designs"
    materials: "Mineral pigments in slip"
    timing: "Before or after firing"
    complexity: "Simple to elaborate"
    sila_reward: 30-50

  incising:
    description: "Cut designs into surface"
    tool: "Sharp stick, stylus"
    timing: "Leather-hard"
    effect: "Lines, patterns"
    sila_reward: 25

  impressed:
    description: "Press patterns"
    tools: "Rope, shells, stamps"
    timing: "Wet clay"
    effect: "Textured surface"
    sila_reward: 20

  applied:
    description: "Add clay decorations"
    types: "Coils, pellets, figures"
    timing: "Wet to leather-hard"
    effect: "3D decoration"
    sila_reward: 35
```

### Design Traditions

```yaml
design_vocabulary:
  geometric:
    patterns: "Lines, zigzags, crosshatch"
    meaning: "Traditional motifs"
    use: "Common decoration"

  naturalistic:
    subjects: "Animals, plants, water"
    skill: "Higher artistic ability"
    use: "Premium ware"

  symbolic:
    elements: "Divine symbols, cult marks"
    meaning: "Religious significance"
    use: "Temple ware, offerings"

  pictorial:
    scenes: "Activities, stories"
    skill: "Advanced artistic"
    use: "Elite commissions"
```

---

## Workshop Economics

### Business Models

```yaml
pottery_business:
  family_workshop:
    structure: "Family members work together"
    scale: "Small to moderate"
    market: "Local customers"
    advantage: "Low overhead"

  commercial_workshop:
    structure: "Master with employees"
    scale: "Higher volume"
    market: "Broader reach"
    advantage: "Specialization possible"

  temple_pottery:
    structure: "Institutional operation"
    scale: "Large"
    market: "Temple needs, distribution"
    advantage: "Steady demand"
```

### Pricing Factors

```yaml
price_determinants:
  size:
    impact: "Larger = more expensive"
    reason: "More material, skill, risk"

  quality:
    factors:
      - "Wall thickness"
      - "Symmetry"
      - "Surface finish"
      - "Firing quality"
    premium: "30-100% over standard"

  decoration:
    plain: "Base price"
    simple_slip: "+20%"
    painted: "+50-100%"
    elaborate: "+100-200%"

  specialty:
    standard_forms: "Base price"
    unusual_shapes: "+30-50%"
    custom_orders: "+50-100%"

  volume:
    single_pieces: "Full price"
    bulk_orders: "Discount 10-20%"
```

### Competition

```yaml
market_competition:
  differentiation:
    quality: "Finer work"
    price: "Lower costs"
    specialty: "Unique products"
    service: "Custom orders"
    reputation: "Known reliability"

  challenges:
    oversupply: "Many potters"
    low_margins: "Common ware"
    fuel_costs: "Firing expenses"
    seasonal: "Market fluctuations"

  success_factors:
    skill: "Quality work"
    efficiency: "Minimize waste, maximize output"
    location: "Good market access"
    relationships: "Regular customers"
```

---

## Supply Chain

### Material Flow

```yaml
pottery_supply_chain:
  clay_acquisition:
    source: "River deposits"
    labor: "Collection, transport"
    cost: "Time, not money"

  fuel_supply:
    sources:
      dung: "Collect from animals"
      reed: "Marshes, canals"
      chaff: "Agricultural waste"
      wood: "Expensive, limited"
    cost: "Collection labor or purchase"

  tool_needs:
    wheel: "Made or purchased"
    forming_tools: "Simple, homemade"
    decoration_tools: "Various"

  distribution:
    market_stall: "Direct sales"
    wholesale: "To merchants"
    commissions: "Custom orders"
    barter: "Grain, goods exchange"
```

---

## Training Data Value

### Knowledge Capture

```yaml
training_data:
  process_mastery:
    - "Multi-stage manufacturing"
    - "Quality control at each step"
    - "Problem diagnosis"

  material_knowledge:
    - "Clay properties"
    - "Firing behavior"
    - "Decoration materials"

  business_decisions:
    - "Product mix optimization"
    - "Pricing strategies"
    - "Customer relationships"

  artistic_judgment:
    - "Design choices"
    - "Aesthetic evaluation"
    - "Cultural preferences"
```

---

## Implementation Notes

### Database Schema

```yaml
pottery_records:
  potter_profile:
    player_id: uuid
    skill_level: integer
    specializations: array
    kiln_owned: boolean
    workshop_id: uuid
    reputation: integer
    products_made: integer

  product_record:
    product_id: uuid
    maker_id: uuid
    type: string
    size: string
    quality: integer
    decoration: string
    price: integer
    status: enum

  kiln_record:
    kiln_id: uuid
    owner_id: uuid
    type: enum
    condition: integer
    capacity: integer
    fuel_type: string
    location: string

  firing_record:
    firing_id: uuid
    kiln_id: uuid
    potter_id: uuid
    pieces_loaded: integer
    pieces_survived: integer
    quality_result: object
    fuel_used: integer
    timestamp: datetime
```

---

## Appendix: Sumerian Pottery Terms

| Term | Meaning | Gameplay Role |
|------|---------|---------------|
| **Bahar** | Potter | Primary profession |
| **Im** | Clay | Raw material |
| **Dug** | Pot/Vessel | Generic container |
| **Gir-tab** | Kiln | Firing structure |
| **Udun** | Oven/Kiln | Firing chamber |
| **Lagab** | Clay lump | Prepared material |

---

*"The potter sits at the wheel, and beneath her hands the formless becomes form, the common becomes essential. She shapes the vessels that hold the grain, the beer, the oil, the water of life. Without her art, there would be no storing, no cooking, no drinking—no civilization."*
