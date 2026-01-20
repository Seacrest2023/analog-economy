# Fishing & Sailing

> *"The marshes feed us. The gulf connects us. The man who knows the water knows life itself—where the fish hide, where the currents run, where the reeds grow thick enough to build a boat that won't sink."*

## Overview

Eridu sits at the edge of the Persian Gulf, making fishing and sailing central to its identity. The Shu-ku (fisherman) provides a primary protein source for all social classes, while the Ma-lah (boatman/sailor) enables the trade that makes Eridu wealthy. This spec covers fishing techniques, boat construction, harbor operations, and the maritime professions that define the city's relationship with water.

---

## Design Philosophy

### Core Principles

1. **Harbor City Identity**: Eridu's location defines its economy and culture
2. **Reed Boat Mastery**: World's earliest boat-building tradition
3. **Complete Supply Chain**: From catching fish to preserving and selling
4. **Maritime Trade Gateway**: Sailors connect Eridu to the world
5. **Training Data Value**: Navigation, construction techniques, resource management

### The Water Economy

```yaml
water_economy:
  fishing:
    importance: "Primary protein source after grain"
    accessibility: "Available to all social classes"
    preservation: "Enables trade and storage"

  sailing:
    trade_routes: "Dilmun, Magan, Meluhha"
    transport: "Goods, people, military"
    technology: "Among world's first sailing vessels"

  boat_building:
    materials: "Reed, bitumen, imported wood"
    innovation: "Shell-first construction"
    export: "Boats sold to other cities"
```

---

## The Fisherman (Shu-ku)

### Role and Status

```yaml
shuku_profession:
  title: "Shu-ku (Fisherman)"
  social_class: "Commoner (respected)"
  importance: "Vital food provider"

  daily_life:
    dawn: "Launch boats, set nets"
    morning: "Check traps, line fishing"
    midday: "Return with catch, sell fresh"
    afternoon: "Repair nets, prepare preservation"
    evening: "Prepare for next day"

  income_sources:
    fresh_sale: "Immediate market sales"
    preserved: "Dried, salted, smoked fish"
    specialty: "Live fish for temple ponds"
```

### Fishing Techniques

```yaml
fishing_methods:
  net_fishing:
    description: "Primary mass-catching method"
    equipment:
      nets: "Woven from plant fibers"
      weights: "Clay or stone sinkers"
      floats: "Reed bundles or gourds"
    technique:
      cast_net: "Thrown from shore or boat"
      seine_net: "Dragged between two boats"
      gill_net: "Set and left overnight"
    skill_requirements:
      novice: "Basic casting"
      apprentice: "Reading water for fish schools"
      journeyman: "Net construction and repair"
      master: "Large-scale operations"
    sila_rewards:
      learn_casting: 15
      first_catch: 20
      net_construction: 40

  hook_and_line:
    description: "Individual precision fishing"
    equipment:
      hooks:
        early: "Bone hooks with barbs"
        advanced: "Copper/bronze hooks"
        design: "Outward-facing barb, groove for line"
      line: "Plant fiber cord"
      lures: "Shell fragments, feathers"
    technique:
      still_fishing: "Patient waiting"
      active_fishing: "Moving lure to attract"
    skill_requirements:
      novice: "Basic baiting and waiting"
      apprentice: "Understanding fish behavior"
      journeyman: "Lure crafting"
      master: "Targeting specific species"
    sila_rewards:
      learn_basics: 15
      craft_lure: 25
      master_technique: 50

  spear_fishing:
    description: "Active hunting of larger fish"
    equipment:
      spears: "Wooden shaft, copper point"
      harpoons: "Barbed for sea turtles"
    technique: "Wading in shallows or from boat"
    targets: "Large fish, turtles, rays"
    skill: "High - requires patience and aim"
    sila_rewards:
      learn_basics: 20
      first_large_catch: 35

  trapping:
    description: "Passive fish collection"
    types:
      basket_traps: "Woven reed funnels"
      weirs: "Stone/reed barriers channeling fish"
      ponds: "Artificial holding pools"
    benefit: "Steady supply, less daily labor"
    skill: "Understanding fish movement patterns"
    sila_rewards:
      build_first_trap: 25
      design_weir: 50
```

### Fish Preservation

```yaml
preservation_methods:
  sun_drying:
    process: "Clean, salt lightly, dry in sun"
    duration: "2-4 days depending on size"
    result: "Stores for months"
    skill: "Low"
    sila_reward: 15

  salting:
    process: "Pack in salt/brine"
    material: "Sea salt or mineral salt"
    result: "Preserved for long trade journeys"
    skill: "Medium - proper ratios matter"
    sila_reward: 25

  smoking:
    process: "Hang over slow fire"
    fuel: "Reed, tamarisk wood"
    result: "Flavored and preserved"
    skill: "Medium - temperature control"
    sila_reward: 30

  live_holding:
    process: "Keep in temple fish ponds"
    purpose: "Fresh fish for sacred meals"
    skill: "High - maintaining water quality"
    temple_demand: "Steady income source"
    sila_reward: 40
```

### Fisherman Skill Tree

```yaml
fisherman_skills:
  tier_1_novice:
    skills:
      basic_netting:
        description: "Cast and retrieve simple nets"
        sila_reward: 15

      fish_identification:
        description: "Know common species"
        sila_reward: 10

      boat_handling:
        description: "Basic reed boat operation"
        sila_reward: 20

    earnings: "20-50 SILA/day (variable)"
    status: "Entry-level fisherman"

  tier_2_apprentice:
    requirements: "30 days fishing"
    skills:
      net_construction:
        description: "Weave and repair nets"
        sila_reward: 35

      water_reading:
        description: "Find fish by water signs"
        sila_reward: 30

      basic_preservation:
        description: "Sun-dry and salt fish"
        sila_reward: 25

    earnings: "40-80 SILA/day"
    status: "Reliable fisherman"

  tier_3_journeyman:
    requirements: "1 year + reputation"
    skills:
      trap_construction:
        description: "Build basket traps and weirs"
        sila_reward: 50

      seasonal_mastery:
        description: "Know migration patterns"
        sila_reward: 60

      smoking_expertise:
        description: "Premium preservation"
        sila_reward: 45

    earnings: "80-150 SILA/day"
    status: "Respected provider"

  tier_4_master:
    requirements: "5 years + temple recognition"
    skills:
      fleet_management:
        description: "Coordinate multiple boats"
        sila_reward: 100

      temple_fish_keeper:
        description: "Manage sacred ponds"
        sila_reward: 100

      teaching:
        description: "Train apprentices"
        sila_reward: 75

    earnings: "150-300 SILA/day"
    status: "Master of the waters"
```

---

## Boats and Watercraft

### Boat Types

```yaml
boat_types:
  za_sha_reed_boat:
    description: "Bundled reed canoe with curved prow"
    construction:
      material: "Marsh reeds tightly bundled"
      technique: "Air trapped in stems provides buoyancy"
      sealing: "Bitumen coating for waterproofing"
    capacity: "1-4 people, light cargo"
    uses:
      - "Fishing in marshes"
      - "Short-distance transport"
      - "Personal travel"
    cost: "30-100 SILA"
    lifespan: "1-2 years with maintenance"
    sila_to_learn_building: 50

  guffa_coracle:
    description: "Perfectly round basket boat"
    construction:
      frame: "Pomegranate wood or willow branches"
      covering: "Animal hides"
      sealing: "Heavy bitumen coating"
    characteristics:
      shape: "Round - spins in current but can't sink"
      durability: "Extremely robust"
    capacity: "Heavy cargo, livestock"
    uses:
      - "River crossings"
      - "Grain transport"
      - "Livestock ferry"
    cost: "100-300 SILA"
    sila_to_learn_building: 75

  magan_boat_freighter:
    description: "Ocean-going cargo vessel"
    construction:
      hull: "Thick imported planks"
      joints: "Deep mortise-and-tenon"
      sealing: "Bitumen and fish oil"
      sail: "Single square sail (wool or linen)"
    capacity: "Up to 20 tons of cargo"
    range: "Persian Gulf to Indus Valley"
    uses:
      - "International trade"
      - "Bulk cargo"
      - "Military transport"
    cost: "2000-10000 SILA"
    crew: "5-15 sailors"
    sila_to_learn_building: 200

  skin_raft:
    description: "Inflated animal skins for flotation"
    construction:
      material: "Sheep or goat skins, inflated"
      frame: "Light wood platform"
    uses:
      - "River crossing"
      - "Military infiltration"
      - "Emergency flotation"
    cost: "20-50 SILA"
    sila_to_learn: 25
```

### Boat Construction Process

```yaml
boat_building:
  reed_boat_process:
    step_1_harvest:
      action: "Cut mature reeds from marshes"
      timing: "After dry season"
      skill: "Selecting proper reeds"

    step_2_drying:
      action: "Dry reeds in sun"
      duration: "1-2 weeks"
      purpose: "Prevent rot"

    step_3_bundling:
      action: "Tie reeds into tight bundles"
      technique: "Spiral binding with grass rope"
      skill: "Consistent tension"

    step_4_shaping:
      action: "Combine bundles into hull shape"
      technique: "Curved prow, flat bottom"
      skill: "Symmetry and balance"

    step_5_sealing:
      action: "Apply hot bitumen"
      material: "Natural asphalt from region"
      coverage: "Complete waterproofing"
      skill: "Proper temperature, even application"

    step_6_finishing:
      action: "Add seats, oar locks"
      customization: "Based on intended use"

  wooden_boat_process:
    technique: "Shell-first construction"
    description: "Build outer hull, then insert ribs"

    step_1_planking:
      action: "Shape planks with adze"
      skill: "Critical - determines hull shape"

    step_2_joining:
      method: "Mortise and tenon joints"
      alternative: "Lashing/sewing with palm fiber"
      benefit: "Allows flex without cracking"

    step_3_sealing:
      material: "Bitumen mortar"
      application: "All seams and joints"

    step_4_rigging:
      mast: "Single central mast"
      sail: "Square wool or linen"
      lines: "Palm fiber rope"
```

---

## The Sailor/Boatman (Ma-lah)

### Role and Status

```yaml
malah_profession:
  title: "Ma-lah (Sailor/Boatman)"
  social_class: "Commoner to respected professional"

  specializations:
    river_boatman:
      role: "Local transport on canals and rivers"
      income: "Steady, lower risk"

    gulf_sailor:
      role: "Coastal and gulf trading"
      income: "Higher, seasonal"

    ocean_mariner:
      role: "Long-distance trade voyages"
      income: "Highest, highest risk"
      prestige: "Significant"
```

### Sailor Skill Tree

```yaml
sailor_skills:
  tier_1_novice:
    skills:
      basic_rowing:
        description: "Propel small boats"
        sila_reward: 15

      knot_tying:
        description: "Essential sailing knots"
        sila_reward: 15

      cargo_handling:
        description: "Load and secure goods"
        sila_reward: 20

    earnings: "Crew wages (20-40 SILA/day)"
    status: "Deck hand"

  tier_2_apprentice:
    requirements: "3 months at sea"
    skills:
      navigation_basics:
        description: "Read stars, coastline"
        sila_reward: 40

      sail_handling:
        description: "Manage square sail"
        sila_reward: 35

      weather_reading:
        description: "Predict storms, winds"
        sila_reward: 40

    earnings: "40-70 SILA/day"
    status: "Experienced sailor"

  tier_3_journeyman:
    requirements: "2 years + gulf voyage"
    skills:
      monsoon_navigation:
        description: "Use seasonal winds for Meluhha route"
        sila_reward: 75

      ship_repair:
        description: "Emergency repairs at sea"
        sila_reward: 60

      crew_management:
        description: "Coordinate deck operations"
        sila_reward: 50

    earnings: "70-120 SILA/day"
    status: "Helmsman/First Mate"

  tier_4_master:
    requirements: "5 years + Meluhha voyage"
    skills:
      captain:
        description: "Command trading vessel"
        sila_reward: 150

      fleet_navigation:
        description: "Coordinate multiple ships"
        sila_reward: 150

      trade_negotiation:
        description: "Handle foreign port dealings"
        sila_reward: 100

    earnings: "Percentage of cargo profits"
    status: "Ship Captain"
```

### Maritime Navigation

```yaml
navigation_methods:
  coastal_piloting:
    technique: "Follow shoreline landmarks"
    tools: "Visual memory, oral tradition"
    range: "Gulf coastline"

  star_navigation:
    technique: "Use fixed stars for direction"
    key_stars: "Pole star for north"
    timing: "Night sailing"

  monsoon_timing:
    technique: "Use seasonal wind patterns"
    summer: "Southwest winds to Meluhha"
    winter: "Northeast winds return"
    voyage_planning: "Critical for Indian Ocean"

  dead_reckoning:
    technique: "Estimate position from speed/time"
    tools: "Experience, water depth"
    risk: "Accumulating error"
```

---

## Harbor Operations

### The Karum (Harbor District)

```yaml
karum_district:
  description: "Special economic zone for maritime trade"
  location: "Outside main city walls"

  functions:
    docking:
      facilities: "Wooden quays, mud-brick piers"
      services: "Mooring, unloading"

    warehousing:
      storage: "Goods awaiting sale or transport"
      security: "Guards, sealed rooms"

    market:
      trade: "Foreign and local goods"
      currency: "Silver, commodity exchange"

    foreign_quarter:
      residents: "Dilmun, Magan, Meluhha merchants"
      law: "International trade law applies"
      disputes: "Special merchant courts"

  player_opportunities:
    dock_worker:
      work: "Loading/unloading ships"
      income: "Daily wages (30-50 SILA)"

    warehouse_guard:
      work: "Protect stored goods"
      income: "Steady salary"

    harbor_pilot:
      work: "Guide ships into port"
      income: "Per-ship fees"
      skill: "Local water knowledge"
```

### Seasonal Rhythms

```yaml
maritime_calendar:
  sailing_season:
    spring:
      activity: "Preparation, short voyages"
      winds: "Variable"

    summer:
      activity: "Peak Meluhha voyages"
      winds: "Southwest monsoon"
      duration: "Outbound to India"

    autumn:
      activity: "Return voyages, local trade"
      winds: "Shifting"

    winter:
      activity: "Return from east, boat repair"
      winds: "Northeast monsoon"
      harbor: "Full of goods"

  fishing_seasons:
    spring: "Spawning runs, abundant"
    summer: "Deep water fishing"
    autumn: "Migration catches"
    winter: "Marsh fishing, preservation"
```

---

## Water Warfare

### Naval Capabilities

```yaml
naval_warfare:
  note: "Land warfare predominates, but water has military uses"

  riverine_transport:
    purpose: "Move troops quickly"
    capacity: "Siege equipment, supplies"
    tactic: "Bypass marsh defenses"

  amphibious_raids:
    method: "Reed boats for stealth"
    target: "Settlements accessible by water"
    advantage: "Surprise attack capability"

  personal_flotation:
    device: "Inflated sheepskins"
    use: "Individual river crossing"
    military: "Infiltration, silent approach"

  water_as_weapon:
    tactical_flooding:
      method: "Dam then release"
      effect: "Wash away walls"

    dehydration_siege:
      method: "Divert canals upstream"
      effect: "Force surrender through thirst"

    infrastructure_destruction:
      target: "Levees, canals, wells"
      effect: "Long-term economic collapse"
```

### Eridu's Defensive Position

```yaml
eridu_defense:
  strategic_reality:
    role: "Sacred Temple-City, not military power"
    strategy: "Diplomacy over combat"

  vulnerabilities:
    elamite_raids: "Periodic devastation"
    water_dependency: "Upstream cities can cut supply"

  player_involvement:
    harbor_defense:
      role: "Guard against raiders"
      rewards: "Karma, loot from defeated enemies"

    emergency_response:
      role: "Repel barbarian incursions"
      rewards: "Sanity points, community standing"
```

---

## Economics

### Fishing Economy

```yaml
fishing_economics:
  daily_catch_value:
    small_catch: "30-50 SILA"
    average_catch: "50-100 SILA"
    good_catch: "100-200 SILA"
    exceptional: "200+ SILA"

  preserved_fish_value:
    dried: "1.5x fresh price"
    salted: "2x fresh price"
    smoked: "2.5x fresh price"

  costs:
    nets: "50-200 SILA"
    hooks: "5-20 SILA"
    small_boat: "50-150 SILA"
    large_boat: "500-2000 SILA"
    preservation_supplies: "10-30 SILA/batch"
```

### Maritime Trade Economy

```yaml
maritime_economics:
  crew_wages:
    deck_hand: "20-40 SILA/day"
    experienced_sailor: "40-70 SILA/day"
    helmsman: "70-120 SILA/day"
    captain: "Share of profits (5-15%)"

  voyage_profits:
    gulf_trade: "50-200% markup possible"
    meluhha_voyage: "200-500% on exotic goods"
    risk: "Ships lost, pirates, storms"

  harbor_fees:
    docking: "Per-day charge"
    warehouse: "Per-volume charge"
    pilot_services: "Per-ship fee"
```

---

## Training Data Value

### Knowledge Capture

```yaml
training_data:
  practical_skills:
    - "Fish behavior prediction"
    - "Weather and water reading"
    - "Navigation techniques"
    - "Construction methods"

  resource_management:
    - "Preservation decisions"
    - "Voyage planning"
    - "Crew coordination"

  risk_assessment:
    - "Storm avoidance"
    - "Route selection"
    - "Cargo decisions"
```

---

## Implementation Notes

### Database Schema

```yaml
maritime_records:
  fisherman_profile:
    player_id: uuid
    skill_level: integer
    catch_history: array
    boats_owned: array
    preservation_skills: array

  sailor_profile:
    player_id: uuid
    skill_level: integer
    voyages_completed: array
    navigation_skills: array
    current_vessel: uuid

  vessel_record:
    vessel_id: uuid
    type: enum
    owner_id: uuid
    condition: integer
    cargo_capacity: integer
    crew: array
```

---

## Appendix: Sumerian Maritime Terms

| Term | Meaning | Gameplay Role |
|------|---------|---------------|
| **Shu-ku** | Fisherman | Fishing profession |
| **Ma-lah** | Sailor/Boatman | Maritime profession |
| **Guffa** | Coracle (round boat) | River transport |
| **Za-sha** | Reed boat | Common vessel |
| **Karum** | Harbor district | Trade zone |

---

*"The fish do not care if you are rich or poor. The waves do not respect titles. On the water, only skill matters—and the blessing of Enki, lord of the deep."*
