# Food Production

> *"Bread is the gift of Nisaba, beer the blessing of Ninkasi. Together they sustain the city, feed the worker, and give strength to the soldier. Without the baker and brewer, Eridu would starve within a moon."*

## Overview

Food production in Eridu is a sophisticated industry dominated by two divine crafts: brewing and baking. The Lunga (brewer) transforms grain into beer—the daily drink of all classes—while the Muhaldim (baker/cook) creates the bread and prepared foods that sustain the population. This spec covers the complete food production chain from raw grain to tavern table.

---

## Design Philosophy

### Core Principles

1. **Essential Industry**: Everyone needs food and drink daily
2. **Temple Integration**: Major production happens in temple facilities
3. **Skill Progression**: From simple recipes to complex preparations
4. **Supply Chain Depth**: Raw materials → processing → finished goods
5. **Training Data Value**: Recipe following, quality control, business operations

### Economic Importance

```yaml
food_economy:
  beer_consumption:
    workers: "2-5 liters daily (ration)"
    all_classes: "Universal drink"
    reason: "Safer than water, nutritious"

  bread_consumption:
    staple: "Primary calorie source"
    types: "50+ varieties known"
    distribution: "Rations, market, taverns"

  tavern_role:
    social: "Community gathering point"
    economic: "Major food distribution"
    employment: "Significant sector"
```

---

## Brewing (Lunga)

### The Divine Art

```yaml
brewing_tradition:
  patron_deity: "Ninkasi (goddess of beer)"
  sacred_text: "Hymn to Ninkasi (brewing manual)"
  status: "Divine gift to humanity"

  cultural_importance:
    daily_drink: "All classes consume beer"
    safer: "Fermentation kills pathogens"
    nutrition: "Significant calorie source"
    ritual: "Temple offerings include beer"
```

### Beer Types

```yaml
beer_varieties:
  kas_ordinary:
    description: "Standard daily beer"
    strength: "Light to moderate"
    production: "Largest volume"
    consumers: "Workers, commoners"
    price: "1-2 SILA per jug"

  kas_sig:
    description: "Fine beer"
    strength: "Moderate"
    quality: "Better ingredients, longer process"
    consumers: "Middle class, celebrations"
    price: "3-5 SILA per jug"

  kas_gal:
    description: "Strong beer"
    strength: "High alcohol"
    process: "Extended fermentation"
    consumers: "Elite, special occasions"
    price: "5-10 SILA per jug"

  kas_kur:
    description: "Dark beer"
    character: "Rich, malty"
    process: "Roasted grain base"
    consumers: "Acquired taste, premium"
    price: "4-8 SILA per jug"

  date_beer:
    description: "Sweet date-infused beer"
    flavor: "Fruity, sweet"
    process: "Dates added during ferment"
    consumers: "Popular variety"
    price: "4-7 SILA per jug"
```

### Brewing Process

```yaml
brewing_steps:
  step_1_malting:
    process: "Sprout barley grains"
    duration: "3-5 days"
    skill: "Control moisture and temperature"
    sila_reward: 15

  step_2_bappir_creation:
    description: "Make beer bread (twice-baked)"
    process:
      - "Mix malted barley with water"
      - "Form into loaves"
      - "Bake partially"
      - "Dry for storage"
    storage: "Can keep for months"
    sila_reward: 20

  step_3_mashing:
    process: "Break bappir into vessel with water"
    vessel: "Large ceramic vat"
    action: "Stir to extract sugars"
    sila_reward: 15

  step_4_flavoring:
    additives:
      - "Dates (sweetness)"
      - "Honey (premium)"
      - "Herbs (variety)"
    timing: "Before or during ferment"
    sila_reward: 20

  step_5_fermentation:
    duration: "2-7 days"
    monitoring: "Check daily"
    vessel: "Covered vat"
    completion: "Bubbling stops"
    sila_reward: 25

  step_6_straining:
    method: "Pour through reed strainer"
    result: "Remove grain solids"
    sediment: "Some remains (normal)"
    sila_reward: 10

  step_7_serving:
    vessel: "Ceramic jugs"
    consumption: "Through reed straws"
    reason: "Strain remaining particles"
    freshness: "Best within days"
```

### Brewer Skill Tree

```yaml
brewer_skills:
  tier_1_novice:
    skills:
      basic_brewing:
        description: "Make standard beer"
        sila_reward: 25
        quality: "Acceptable"

      malting:
        description: "Sprout grain properly"
        sila_reward: 20
        critical: "Foundation skill"

      bappir_making:
        description: "Create beer bread"
        sila_reward: 20

    role: "Assistant brewer"
    earnings: "Rations + small wage"

  tier_2_apprentice:
    requirements: "1 year training"
    skills:
      variety_brewing:
        description: "Multiple beer styles"
        sila_reward: 35
        types: "Light, dark, strong"

      flavor_control:
        description: "Consistent taste"
        sila_reward: 30
        importance: "Repeat customers"

      batch_scaling:
        description: "Large production runs"
        sila_reward: 30
        capacity: "Temple-scale brewing"

    role: "Working brewer"
    earnings: "Modest wage"

  tier_3_journeyman:
    requirements: "3 years + quality record"
    skills:
      recipe_development:
        description: "Create new varieties"
        sila_reward: 50
        value: "Unique offerings"

      quality_assessment:
        description: "Judge beer quality"
        sila_reward: 40
        role: "Inspector, buyer"

      fermentation_mastery:
        description: "Control complex ferments"
        sila_reward: 50
        result: "Premium products"

    role: "Senior brewer, supervisor"
    earnings: "Good wage + benefits"

  tier_4_master:
    requirements: "10 years + reputation"
    skills:
      temple_brewing:
        description: "Manage major operation"
        sila_reward: 100
        scale: "City-level production"

      sacred_brewing:
        description: "Ritual beer preparation"
        sila_reward: 100
        status: "Religious significance"

      training:
        description: "Teach brewing arts"
        sila_reward: 75
        legacy: "Pass on knowledge"

    role: "Master brewer, temple position"
    earnings: "Elite status"
```

---

## Baking & Cooking (Muhaldim)

### Bread Production

```yaml
bread_types:
  basic_bread:
    ingredients: "Barley flour, water, salt"
    form: "Flat rounds"
    baking: "Clay oven (tannur)"
    price: "0.5-1 SILA"
    consumption: "Daily staple"

  emmer_bread:
    ingredients: "Emmer wheat flour"
    quality: "Superior to barley"
    price: "1-2 SILA"
    consumers: "Middle class"

  fine_white:
    ingredients: "Sifted wheat flour"
    quality: "Highest grade"
    price: "3-5 SILA"
    consumers: "Elite, temple"

  sweetened:
    ingredients: "Flour, dates, honey"
    occasion: "Festivals, celebrations"
    price: "5-10 SILA"
    special: "Premium product"

  seed_bread:
    ingredients: "Flour + sesame, coriander"
    flavor: "Enhanced"
    price: "2-3 SILA"

  offerings_bread:
    description: "Temple ritual loaves"
    form: "Specific shapes required"
    production: "Temple bakeries"
    purpose: "Divine offerings"
```

### Baking Process

```yaml
baking_steps:
  step_1_flour_preparation:
    grinding:
      tool: "Saddle quern (stone grinder)"
      labor: "Intensive, often women's work"
      output: "Coarse to fine depending on skill"
    sifting:
      tool: "Reed sieves"
      purpose: "Remove bran for finer flour"
    sila_reward: 15

  step_2_dough_making:
    mixing: "Flour, water, salt"
    kneading: "Develop texture"
    leavening:
      method: "Saved dough from previous batch"
      alternative: "Beer foam (yeast source)"
    sila_reward: 20

  step_3_shaping:
    forms:
      - "Flat rounds"
      - "Loaves"
      - "Ritual shapes"
    decoration: "Some breads marked or stamped"
    sila_reward: 15

  step_4_baking:
    oven_types:
      tannur:
        description: "Cylindrical clay oven"
        method: "Stick dough on hot walls"
        heat: "Wood or dung fire"

      tabun:
        description: "Dome oven"
        method: "Place on floor"
        use: "Larger breads"

    monitoring: "Watch for proper browning"
    timing: "Minutes per bread"
    sila_reward: 25
```

### Prepared Foods

```yaml
prepared_foods:
  stews:
    barley_stew:
      ingredients: "Barley, onions, garlic, herbs"
      meat_optional: "When available"
      price: "2-4 SILA per portion"

    fish_stew:
      ingredients: "Fish, vegetables, spices"
      common: "Near canals and rivers"
      price: "3-5 SILA"

    meat_stew:
      ingredients: "Mutton or goat, vegetables"
      premium: "Meat is expensive"
      price: "5-10 SILA"

  grilled_foods:
    fish: "Fresh from canals"
    meat: "Skewered, grilled"
    vegetables: "Onions, leeks"

  dairy:
    fresh_milk: "Goat primarily"
    cheese: "Various aged types"
    ghee: "Clarified butter"
    yogurt: "Fermented milk"

  preserved:
    dried_fish: "Long storage"
    salted_meat: "Rare, expensive"
    pickled_vegetables: "Seasonal preservation"
```

### Cook Skill Tree

```yaml
cook_skills:
  tier_1_novice:
    skills:
      basic_bread:
        description: "Simple flat bread"
        sila_reward: 20

      simple_stew:
        description: "Basic grain stew"
        sila_reward: 20

      fire_management:
        description: "Control oven heat"
        sila_reward: 15

    role: "Kitchen helper"
    earnings: "Rations"

  tier_2_apprentice:
    requirements: "1 year training"
    skills:
      variety_breads:
        description: "Multiple bread types"
        sila_reward: 35

      meat_preparation:
        description: "Butcher and cook meat"
        sila_reward: 30

      flavor_balancing:
        description: "Season properly"
        sila_reward: 30

    role: "Working cook"
    earnings: "Modest wage"

  tier_3_journeyman:
    requirements: "3 years + skill"
    skills:
      feast_preparation:
        description: "Large-scale cooking"
        sila_reward: 50

      specialty_dishes:
        description: "Complex recipes"
        sila_reward: 50

      preservation:
        description: "Store food safely"
        sila_reward: 40

    role: "Head cook"
    earnings: "Good wage"

  tier_4_master:
    requirements: "10 years + reputation"
    skills:
      royal_cuisine:
        description: "Elite meal preparation"
        sila_reward: 100

      temple_offerings:
        description: "Sacred food preparation"
        sila_reward: 100

      kitchen_management:
        description: "Oversee major operation"
        sila_reward: 100

    role: "Palace/temple chef"
    earnings: "Elite status"
```

---

## Butchering

### The Butcher's Trade

```yaml
butcher_role:
  description: "Process animals for meat"

  animals_processed:
    sheep: "Most common"
    goats: "Frequent"
    cattle: "Rare, premium"
    pigs: "Some areas"

  temple_connection:
    sacrifice: "Animals killed ritually first"
    meat_distribution: "Temple manages much"
    butcher_role: "Process after ritual"
```

### Butchering Skills

```yaml
butcher_skills:
  tier_1_novice:
    skills:
      basic_cuts:
        description: "Divide carcass"
        sila_reward: 20

      hide_removal:
        description: "Preserve hide intact"
        sila_reward: 15
        value: "Hide is valuable"

    role: "Assistant butcher"

  tier_2_apprentice:
    requirements: "1 year"
    skills:
      efficient_butchering:
        description: "Maximize usable meat"
        sila_reward: 35

      organ_processing:
        description: "Handle internal organs"
        sila_reward: 30

    role: "Working butcher"

  tier_3_journeyman:
    requirements: "3 years"
    skills:
      premium_cuts:
        description: "Elite portions"
        sila_reward: 50

      ritual_preparation:
        description: "Temple sacrifice support"
        sila_reward: 50

    role: "Senior butcher"

  tier_4_master:
    requirements: "10 years"
    skills:
      temple_butcher:
        description: "Official position"
        sila_reward: 100

      livestock_assessment:
        description: "Judge animal quality"
        sila_reward: 75

    role: "Master butcher"
```

---

## The Tavern (Eshdam)

### Tavern Operations

```yaml
tavern_system:
  description: "Public drinking and eating house"

  operator:
    title: "Kar-kid (tavern keeper)"
    typical: "Often women-owned"
    role: "Serve food, drink, manage business"

  services:
    beer: "Primary product"
    food: "Prepared dishes"
    social: "Gathering place"
    lodging: "Sometimes offered"

  clientele:
    workers: "After labor"
    travelers: "Passing through"
    merchants: "Business meetings"
    all_classes: "Mix of society"
```

### Tavern Keeper (Kar-kid)

```yaml
kar_kid_profession:
  gender: "Historically often female"
  status: "Independent business owner"

  responsibilities:
    procurement:
      - "Buy beer from brewers"
      - "Purchase food supplies"
      - "Manage inventory"

    service:
      - "Serve customers"
      - "Maintain order"
      - "Handle payment"

    business:
      - "Set prices"
      - "Manage credit (tab system)"
      - "Deal with authorities"

  legal_obligations:
    fair_measure: "Honest portions"
    reporting: "Report seditious talk"
    order: "Maintain peaceful house"

  penalties:
    watering_beer: "Death (historically severe)"
    price_gouging: "Fines, closure"
    harboring_criminals: "Severe punishment"

  skill_requirements:
    business_sense: "Profit management"
    people_skills: "Handle diverse clientele"
    physical: "Long hours on feet"
```

### Tavern Skill Tree

```yaml
tavern_skills:
  tier_1_novice:
    skills:
      serving:
        description: "Bring food and drink"
        sila_reward: 15

      basic_accounts:
        description: "Track tabs"
        sila_reward: 20

      customer_service:
        description: "Handle patrons"
        sila_reward: 15

    role: "Tavern server"
    earnings: "Tips + wage"

  tier_2_apprentice:
    requirements: "1 year experience"
    skills:
      procurement:
        description: "Source supplies"
        sila_reward: 30

      quality_judgment:
        description: "Judge beer/food quality"
        sila_reward: 30

      crowd_management:
        description: "Handle busy nights"
        sila_reward: 30

    role: "Senior server"
    earnings: "Better wage"

  tier_3_journeyman:
    requirements: "3 years + capital"
    skills:
      business_management:
        description: "Run profitable tavern"
        sila_reward: 50

      supplier_relationships:
        description: "Negotiate good prices"
        sila_reward: 40

      reputation_building:
        description: "Attract regular customers"
        sila_reward: 50

    role: "Tavern manager/owner"
    earnings: "Business profits"

  tier_4_master:
    requirements: "10 years + success"
    skills:
      establishment_fame:
        description: "Known across city"
        sila_reward: 100

      multiple_locations:
        description: "Expand business"
        sila_reward: 100

      community_influence:
        description: "Social hub operator"
        sila_reward: 75

    role: "Prominent tavern owner"
    earnings: "Significant wealth"
```

---

## Temple Food Production

### Institutional Scale

```yaml
temple_food_system:
  scale: "Feeds hundreds to thousands daily"

  facilities:
    brewery:
      size: "Large vat capacity"
      staff: "Multiple brewers"
      output: "City-scale production"

    bakery:
      ovens: "Multiple large ovens"
      staff: "Baker teams"
      output: "Thousands of loaves"

    kitchen:
      purpose: "Offerings, staff meals"
      staff: "Professional cooks"

  distribution:
    rations:
      recipients: "Temple workers"
      content: "Bread, beer, sometimes meat"
      schedule: "Daily or periodic"

    offerings:
      purpose: "Divine service"
      quality: "Best products"
      handling: "Special preparation"

    surplus:
      destination: "Market sale"
      benefit: "Temple revenue"
```

### Employment Opportunities

```yaml
temple_food_employment:
  positions:
    brewer:
      type: "Full-time staff"
      benefits: "Rations, housing, stability"
      path: "Progress to master brewer"

    baker:
      type: "Full-time staff"
      benefits: "Same as brewer"
      specialization: "Offering breads"

    cook:
      type: "Staff position"
      duties: "Prepare temple meals"
      status: "Respectable"

    ration_distributor:
      duties: "Manage handouts"
      requires: "Counting, organization"

  player_paths:
    entry: "Start as assistant"
    progress: "Skill determines advancement"
    ceiling: "Department head"
```

---

## Supply Chains

### Grain to Beer

```yaml
beer_supply_chain:
  step_1_farming:
    source: "Barley fields"
    provider: "Farmers (Engar)"
    form: "Whole grain"

  step_2_malting:
    location: "Brewery or malt house"
    processor: "Brewer or specialist"
    product: "Malted grain"

  step_3_bappir:
    location: "Bakery/brewery"
    product: "Beer bread"
    storage: "Can stockpile"

  step_4_brewing:
    location: "Brewery"
    labor: "Brewers (Lunga)"
    product: "Fresh beer"

  step_5_distribution:
    channels:
      - "Taverns (wholesale)"
      - "Direct sale (market)"
      - "Temple rations"
      - "Private orders"
```

### Grain to Bread

```yaml
bread_supply_chain:
  step_1_farming:
    source: "Barley or wheat fields"
    provider: "Farmers"
    form: "Whole grain"

  step_2_milling:
    location: "Home or commercial mill"
    labor: "Miller or household"
    product: "Flour"

  step_3_baking:
    location: "Bakery or home"
    labor: "Bakers (Muhaldim)"
    product: "Bread"

  step_4_distribution:
    channels:
      - "Market sale"
      - "Temple rations"
      - "Tavern supply"
      - "Direct orders"
```

### Meat Supply Chain

```yaml
meat_supply_chain:
  step_1_husbandry:
    source: "Flocks and herds"
    provider: "Shepherds (Sipa)"
    selection: "Surplus males, old animals"

  step_2_ritual:
    location: "Temple (often)"
    process: "Proper slaughter"
    purpose: "Religious requirement"

  step_3_butchering:
    location: "Butcher shop or temple"
    labor: "Butcher"
    product: "Meat cuts, organs, hide"

  step_4_distribution:
    channels:
      - "Market sale (fresh)"
      - "Tavern supply"
      - "Temple distribution"
      - "Elite households"

  timing: "Meat must be consumed quickly"
```

---

## Quality Control

### Standards

```yaml
quality_standards:
  beer:
    measures:
      - "Color consistency"
      - "Flavor profile"
      - "Alcohol strength"
      - "Clarity"
    enforcement: "Customer complaints, reputation"
    penalty_for_fraud: "Severe (historical: death for watering)"

  bread:
    measures:
      - "Weight (standard sizes)"
      - "Texture"
      - "Freshness"
    enforcement: "Market inspectors"
    penalty: "Fines, market exclusion"

  meat:
    measures:
      - "Freshness"
      - "Proper handling"
      - "Honest weight"
    enforcement: "Inspection, complaints"
    penalty: "Fines, closure"
```

### Hygiene

```yaml
hygiene_practices:
  brewing:
    vessel_cleaning: "Rinse between batches"
    ingredient_quality: "Fresh grain, clean water"
    storage: "Cool, covered"

  baking:
    flour_storage: "Keep dry, pest-free"
    dough_handling: "Clean hands and surfaces"
    oven_maintenance: "Regular cleaning"

  meat:
    freshness: "Same-day processing"
    cooling: "Shade, quick sale"
    waste: "Proper disposal"
```

---

## Gameplay Integration

### Starting Paths

```yaml
entry_options:
  brewer_apprentice:
    requirements: "None (willingness to learn)"
    employer: "Tavern or temple"
    path: "Learn brewing skills"

  baker_helper:
    requirements: "Physical stamina"
    employer: "Bakery or temple"
    path: "Grinding, kneading, baking"

  kitchen_worker:
    requirements: "None"
    employer: "Temple, wealthy household"
    path: "Learn cooking skills"

  tavern_server:
    requirements: "Social skills"
    employer: "Tavern keeper"
    path: "Learn business, become owner"
```

### Economic Opportunities

```yaml
business_opportunities:
  tavern_ownership:
    capital_required: "Moderate (lease building)"
    profit_potential: "Good with location"
    risks: "Competition, regulation"

  mobile_food_vendor:
    capital_required: "Low"
    product: "Prepared foods, bread"
    location: "Markets, worksites"
    profit: "Modest but steady"

  temple_contract:
    opportunity: "Supply beer or bread"
    requirements: "Quality and quantity"
    benefit: "Guaranteed orders"
    competition: "Other producers"
```

---

## Training Data Value

### Knowledge Capture

```yaml
training_data:
  recipe_execution:
    - "Following multi-step procedures"
    - "Timing and temperature judgment"
    - "Quality assessment"

  business_reasoning:
    - "Pricing decisions"
    - "Supply chain management"
    - "Customer relationship"

  quality_control:
    - "Ingredient selection"
    - "Process monitoring"
    - "Problem diagnosis"

  cultural_knowledge:
    - "Food preferences and traditions"
    - "Ritual requirements"
    - "Social customs around eating and drinking"
```

---

## Implementation Notes

### Database Schema

```yaml
food_records:
  product_record:
    product_id: uuid
    type: enum  # beer, bread, stew, meat
    variety: string
    producer_id: uuid
    quality: integer
    quantity: integer
    production_date: datetime
    expiration: datetime

  tavern_record:
    tavern_id: uuid
    owner_id: uuid
    location: string
    reputation: integer
    inventory: array
    employees: array

  recipe_record:
    recipe_id: uuid
    product_type: string
    ingredients: array
    steps: array
    skill_required: integer
    known_by: array  # player_ids
```

---

## Appendix: Sumerian Food Terms

| Term | Meaning | Gameplay Role |
|------|---------|---------------|
| **Lunga** | Brewer | Beer production |
| **Muhaldim** | Baker/Cook | Food preparation |
| **Kas** | Beer | Main beverage |
| **Ninda** | Bread | Staple food |
| **Eshdam** | Tavern | Social/business venue |
| **Kar-kid** | Tavern keeper | Tavern operator |
| **Bappir** | Beer bread | Brewing ingredient |
| **Ninkasi** | Beer goddess | Divine patron |

---

*"The brewer who knows her art transforms humble grain into liquid joy. The baker who masters fire feeds multitudes. The tavern keeper who serves with honesty builds community. These are the pillars upon which the city's daily life rests."*
