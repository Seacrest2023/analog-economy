# Housing & Building System: Foundations of Civilization

> "First shelter. Then storage. Then workshop. Then temple. This is how cities are born."

## Table of Contents

1. [Overview](#1-overview)
2. [Design Philosophy](#2-design-philosophy)
3. [Land Acquisition](#3-land-acquisition)
4. [Building Types](#4-building-types)
5. [Construction Process](#5-construction-process)
6. [Materials & Resources](#6-materials--resources)
7. [Maintenance & Decay](#7-maintenance--decay)
8. [Upgrades & Expansion](#8-upgrades--expansion)
9. [Special Structures](#9-special-structures)
10. [Training Data Value](#10-training-data-value)
11. [Implementation Notes](#11-implementation-notes)

---

## 1. Overview

Buildings in The Analog Economy are not decorative placements—they are functional investments that require materials, labor, time, and ongoing maintenance. Construction is a skill tree, ownership carries obligations, and every structure serves a purpose.

### Core Principles

| Principle | Implementation |
|-----------|----------------|
| **Function over form** | Buildings exist for gameplay purposes |
| **Construction is a skill** | Players learn building techniques |
| **Maintenance is ongoing** | Buildings decay without care |
| **Land has tiers** | Location and ownership type matter |
| **Community infrastructure** | Some buildings require cooperation |

---

## 2. Design Philosophy

### 2.1 Buildings as Investments

```yaml
investment_philosophy:
  principle: |
    A building is not a one-time purchase. It is an ongoing commitment
    that generates value (production, storage, shelter) but requires
    continued investment (maintenance, taxes, labor).

  cost_types:
    initial:
      - "Materials (significant)"
      - "Labor (yours or hired)"
      - "Time (construction duration)"
      - "Land (rent or purchase)"

    ongoing:
      - "Maintenance (materials, labor)"
      - "Taxes (to Temple/settlement)"
      - "Staffing (NPCs if delegating)"
      - "Upgrades (as needs grow)"

  value_generation:
    - "Shelter (survival)"
    - "Production (income)"
    - "Storage (security)"
    - "Status (reputation)"
```

### 2.2 Historical Authenticity

```yaml
historical_building:
  materials:
    primary: "Mud-brick (abundant, local)"
    scarce: "Wood (imported, expensive)"
    special: "Stone (very rare in Eridu region)"

  techniques:
    foundation: "Packed earth, bitumen waterproofing"
    walls: "Mud-brick, sun-dried or kiln-fired"
    roof: "Reed bundles, palm fronds, mud layer"
    maintenance: "Annual replastering essential"

  limitations:
    - "Multi-story limited by materials"
    - "Flat roofs (no rain to shed)"
    - "Small windows (heat management)"
    - "Thick walls (insulation)"
```

### 2.3 Training Data Goals

```yaml
building_training_data:
  economic_decisions:
    - "How do players allocate resources to construction?"
    - "When do they invest vs save?"
    - "How do they balance maintenance vs expansion?"

  planning_behaviors:
    - "How do players plan building projects?"
    - "How do they handle setbacks?"
    - "How do they prioritize features?"

  cooperation_patterns:
    - "How do players coordinate large projects?"
    - "How are resources pooled?"
    - "How is labor distributed?"
```

---

## 3. Land Acquisition

### 3.1 Land Tier System

```yaml
land_tiers:
  tier_0_squatter:
    name: "Squatter"
    cost: "Free"
    location: "Marsh edge, outside walls, unclaimed"
    legal_status: "No rights—can be displaced"
    building_allowed: "Reed hut only"
    tax: "None"
    risk: "High (eviction, flooding, raids)"

  tier_1_tenant:
    name: "Tenant"
    cost: "Labor or rent (grain/month)"
    location: "Commoner quarter, designated areas"
    legal_status: "Use rights, not ownership"
    building_allowed: "Small mud-brick home"
    tax: "Rent to owner"
    risk: "Medium (eviction if rent unpaid)"

  tier_2_leaseholder:
    name: "Leaseholder"
    cost: "SILA + Temple favor"
    location: "Artisan quarter, agricultural plots"
    legal_status: "Multi-year lease, transferable"
    building_allowed: "Workshop-home, small farm"
    tax: "10-15% to Temple"
    risk: "Low (lease renewal needed)"

  tier_3_deed_owner:
    name: "Deed Owner"
    cost: "ANALOG (NFT) + significant SILA"
    location: "Prime locations, large plots"
    legal_status: "Permanent ownership, hereditary"
    building_allowed: "Large estate, multiple structures"
    tax: "15-25% to Temple"
    risk: "Minimal (but high tax obligations)"
```

### 3.2 Land Acquisition Process

```yaml
acquisition_process:
  squatting:
    process:
      1: "Find unclaimed land"
      2: "Build shelter"
      3: "Hope no one claims it"
    risks:
      - "Temple may reclaim"
      - "Other squatters may dispute"
      - "Flooding in marginal areas"

  renting:
    process:
      1: "Find landlord NPC or player"
      2: "Negotiate terms"
      3: "Pay first month's rent"
      4: "Move in"
    requirements:
      - "Reputation check (some landlords)"
      - "Consistent rent payment"

  leasing:
    process:
      1: "Apply to Temple administration"
      2: "Pay lease fee (SILA)"
      3: "Survey marks boundaries (Sa-gid)"
      4: "Contract recorded on clay tablet"
      5: "Begin use"
    requirements:
      - "Minimum Temple favor"
      - "Purpose stated (farming, craft, etc.)"
      - "Annual tax commitment"

  purchasing:
    process:
      1: "Check available deed parcels"
      2: "Pay ANALOG (blockchain transaction)"
      3: "NFT minted representing deed"
      4: "Survey and registration"
      5: "Full ownership rights"
    requirements:
      - "ANALOG tokens"
      - "Willingness to pay ongoing taxes"
      - "Accept maintenance obligations"
```

### 3.3 Location Value Factors

```yaml
location_factors:
  proximity_to_water:
    value: "Very High"
    reason: "Irrigation, transport, drinking"
    premium: "+50-100% land cost"

  proximity_to_temple:
    value: "High"
    reason: "Status, access to services"
    premium: "+30-50% land cost"

  proximity_to_market:
    value: "High (commercial)"
    reason: "Customer access"
    premium: "+25-40% land cost"

  soil_quality:
    value: "High (agricultural)"
    reason: "Crop yields"
    premium: "+20-40% land cost"

  elevation:
    value: "Medium-High"
    reason: "Flood protection"
    premium: "+15-30% land cost"

  defensibility:
    value: "Medium"
    reason: "Raid protection"
    premium: "+10-20% land cost"
```

---

## 4. Building Types

### 4.1 Residential Buildings

```yaml
residential_buildings:
  reed_hut:
    description: "Simplest shelter, traditional marsh dwelling"
    materials: ["Reeds", "Rope", "Palm fronds"]
    construction_time: "2-4 hours"
    capacity: "1-2 people"
    durability: "Low (1-2 years)"
    features:
      - "Basic shelter from sun/rain"
      - "Minimal storage"
      - "No security"
    tier_required: "None (squatter)"

  mud_brick_house:
    description: "Standard commoner dwelling"
    materials: ["Mud bricks (500-1000)", "Wood beams", "Reed roofing", "Bitumen"]
    construction_time: "1-2 weeks"
    capacity: "4-6 people"
    durability: "Medium (10-20 years with maintenance)"
    features:
      - "Solid walls"
      - "Storage room"
      - "Cooking area"
      - "Basic security (door)"
    tier_required: "Tenant or higher"

  courtyard_house:
    description: "Prosperous family home"
    materials: ["Mud bricks (2000-3000)", "Quality wood", "Bitumen", "Plastering"]
    construction_time: "3-5 weeks"
    capacity: "6-10 people + servants"
    durability: "High (30+ years with maintenance)"
    features:
      - "Central courtyard"
      - "Multiple rooms"
      - "Private storage"
      - "Servant quarters"
      - "Guest room"
    tier_required: "Leaseholder or higher"

  estate_complex:
    description: "Elite residence compound"
    materials: ["Mud bricks (5000+)", "Premium wood", "Decorative elements"]
    construction_time: "2-3 months"
    capacity: "10-20 people + staff"
    durability: "Very high with maintenance"
    features:
      - "Multiple buildings"
      - "Gardens"
      - "Private temple/shrine"
      - "Staff housing"
      - "Secure storage"
      - "Reception hall"
    tier_required: "Deed owner"
```

### 4.2 Production Buildings

```yaml
production_buildings:
  pottery_workshop:
    description: "Clay vessel production"
    materials: ["Mud bricks (800)", "Kiln materials", "Wood storage"]
    construction_time: "2 weeks"
    equipment_needed: ["Potter's wheel", "Kiln"]
    production_capacity: "20-50 items/day"
    requirements:
      - "Pottery skill (Tier 2+)"
      - "Clay source access"
      - "Fuel supply"

  smithy:
    description: "Metalworking facility"
    materials: ["Mud bricks (1000)", "Fire-resistant lining", "Ventilation"]
    construction_time: "3 weeks"
    equipment_needed: ["Smelting furnace", "Bellows", "Anvil", "Tools"]
    production_capacity: "5-20 items/day (varies by complexity)"
    requirements:
      - "Metallurgy skill (Tier 2+)"
      - "Metal source (trade)"
      - "Charcoal supply"

  weaving_workshop:
    description: "Textile production"
    materials: ["Mud bricks (600)", "Covered work area"]
    construction_time: "1-2 weeks"
    equipment_needed: ["Looms (1-4)", "Spindles", "Dye vats"]
    production_capacity: "2-8 cloth lengths/day"
    requirements:
      - "Weaving skill (Tier 2+)"
      - "Wool/fiber supply"

  brewery:
    description: "Beer production"
    materials: ["Mud bricks (500)", "Vat space", "Storage"]
    construction_time: "1-2 weeks"
    equipment_needed: ["Brewing vats", "Storage vessels", "Straining equipment"]
    production_capacity: "50-200 liters/batch"
    requirements:
      - "Brewing skill (Tier 2+)"
      - "Grain supply"
      - "Water access"
```

### 4.3 Agricultural Buildings

```yaml
agricultural_buildings:
  granary:
    description: "Grain storage facility"
    materials: ["Mud bricks (1000)", "Raised floor", "Ventilation"]
    construction_time: "2-3 weeks"
    capacity: "500-2000 baskets"
    features:
      - "Pest protection"
      - "Moisture control"
      - "Easy counting"
    requirements:
      - "Farm or trading operation"

  animal_pen:
    description: "Livestock enclosure"
    materials: ["Mud bricks (300)", "Wood fencing", "Shade structure"]
    construction_time: "1 week"
    capacity: "10-50 animals (varies)"
    features:
      - "Water trough"
      - "Feeding area"
      - "Shade"
    requirements:
      - "Animal husbandry skill"

  irrigation_structures:
    shaduf:
      description: "Water-lifting device"
      materials: ["Wood beam", "Counterweight", "Bucket"]
      construction_time: "1-2 days"
      capacity: "Manual water lifting"

    canal_gate:
      description: "Water flow control"
      materials: ["Mud bricks", "Wood gate", "Sealing"]
      construction_time: "1 week"
      capacity: "Controls water to fields"
```

### 4.4 Commercial Buildings

```yaml
commercial_buildings:
  market_stall:
    description: "Simple sales point"
    materials: ["Wood frame", "Shade cloth", "Counter"]
    construction_time: "1 day"
    location: "Market area (rent required)"
    capacity: "Display goods, conduct sales"

  warehouse:
    description: "Bulk storage for trade"
    materials: ["Mud bricks (1500)", "Secure doors", "Inventory system"]
    construction_time: "3-4 weeks"
    capacity: "Large quantity storage"
    features:
      - "Security"
      - "Organization"
      - "Can rent space to others"

  tavern:
    description: "Drinking establishment"
    materials: ["Mud bricks (800)", "Serving area", "Seating"]
    construction_time: "2-3 weeks"
    capacity: "10-30 customers"
    features:
      - "Beer sales"
      - "Information hub"
      - "Social gathering"
    requirements:
      - "Brewing connection"
      - "License (Temple approval)"
```

---

## 5. Construction Process

### 5.1 Construction Phases

```yaml
construction_phases:
  phase_1_planning:
    activities:
      - "Choose location"
      - "Design building (or use standard plan)"
      - "Calculate materials needed"
      - "Estimate labor and time"
    output: "Construction plan"
    skills_used: ["Architecture (if custom)", "Mathematics"]

  phase_2_preparation:
    activities:
      - "Clear and level site"
      - "Gather materials"
      - "Prepare foundation"
      - "Stage materials"
    output: "Ready construction site"
    skills_used: ["Construction basics"]

  phase_3_foundation:
    activities:
      - "Dig foundation trenches"
      - "Lay base layer (packed earth)"
      - "Apply waterproofing (bitumen)"
      - "Set corner markers"
    output: "Stable foundation"
    skills_used: ["Construction (Tier 2)"]

  phase_4_walls:
    activities:
      - "Lay brick courses"
      - "Set doorways and windows"
      - "Embed support beams"
      - "Build to full height"
    output: "Structural walls"
    skills_used: ["Construction (Tier 2-3)"]

  phase_5_roofing:
    activities:
      - "Install main beams"
      - "Lay reed matting"
      - "Apply mud layer"
      - "Seal and waterproof"
    output: "Completed roof"
    skills_used: ["Construction (Tier 2)"]

  phase_6_finishing:
    activities:
      - "Plaster walls (inside and out)"
      - "Install doors"
      - "Build interior features"
      - "Final cleanup"
    output: "Completed building"
    skills_used: ["Construction (Tier 2)", "Carpentry"]
```

### 5.2 Labor Requirements

```yaml
labor_requirements:
  solo_construction:
    description: "One player building alone"
    speed: "Slowest"
    suitable_for: ["Reed hut", "Small structures"]
    challenges:
      - "Heavy lifting difficult"
      - "Multi-person tasks impossible"
      - "Very time-consuming"

  hired_npcs:
    description: "Pay NPCs to assist"
    speed: "Moderate"
    suitable_for: ["Any building"]
    costs:
      unskilled_labor: "20 SILA/day"
      skilled_labor: "50 SILA/day"
    benefits:
      - "Reliable labor"
      - "Can work while you're offline"
      - "Developer takes 10% of wages"

  community_help:
    description: "Other players assist"
    speed: "Fastest"
    suitable_for: ["Large projects"]
    costs: "Social capital, reciprocity expected"
    benefits:
      - "Free labor"
      - "Faster completion"
      - "Community bonding"
    challenges:
      - "Must coordinate schedules"
      - "Owe favors in return"
```

### 5.3 Time Requirements

```yaml
construction_times:
  reed_hut: "2-4 hours"
  mud_brick_house: "1-2 weeks"
  workshop: "2-3 weeks"
  courtyard_house: "3-5 weeks"
  warehouse: "3-4 weeks"
  estate_complex: "2-3 months"

  time_factors:
    solo_work: "1.0x (baseline)"
    with_1_npc: "0.7x"
    with_3_npcs: "0.4x"
    with_community: "0.3x"
    unskilled_builder: "1.5x"
    master_builder: "0.8x"
```

---

## 6. Materials & Resources

### 6.1 Primary Materials

```yaml
primary_materials:
  mud_bricks:
    source: "Made from local mud + straw"
    production: "10-50 bricks/day (depending on setup)"
    drying_time: "3-7 days in sun"
    cost: "Labor intensive, materials cheap"
    storage: "Keep dry"

  reeds:
    source: "Marsh harvesting"
    uses: ["Roofing", "Matting", "Hut walls"]
    cost: "Labor to harvest"
    storage: "Keep dry"

  wood:
    source: "Imported (expensive)"
    uses: ["Beams", "Doors", "Furniture"]
    cost: "High (trade goods)"
    storage: "Protected from weather"
    note: "Scarce in Eridu region"

  bitumen:
    source: "Natural seeps, traded"
    uses: ["Waterproofing", "Sealing"]
    cost: "Moderate"
    storage: "Won't spoil"

  palm_fronds:
    source: "Date palms"
    uses: ["Roofing", "Shade"]
    cost: "Low if you have palms"
```

### 6.2 Material Quantities

```yaml
material_quantities:
  reed_hut:
    reeds: "100-200 bundles"
    rope: "50 lengths"
    total_cost: "~50 SILA equivalent"

  mud_brick_house:
    bricks: "500-1000"
    wood_beams: "5-10"
    reeds: "50 bundles"
    bitumen: "10 containers"
    total_cost: "~500 SILA equivalent"

  workshop:
    bricks: "800-1200"
    wood_beams: "10-15"
    special_materials: "Varies by type"
    total_cost: "~1000 SILA equivalent"

  courtyard_house:
    bricks: "2000-3000"
    wood_beams: "20-30"
    wood_doors: "3-5"
    plaster: "Large quantity"
    total_cost: "~3000 SILA equivalent"
```

---

## 7. Maintenance & Decay

### 7.1 Decay Mechanics

```yaml
decay_mechanics:
  principle: |
    Buildings in Mesopotamia required constant maintenance.
    Mud-brick erodes, roofs leak, foundations shift.
    Neglect leads to collapse.

  decay_factors:
    weather:
      rain: "Erodes mud-brick walls"
      sun: "Cracks plaster"
      flooding: "Undermines foundations"

    use:
      heavy_use: "Floors wear, doors weaken"
      production: "Equipment area degrades faster"

    time:
      annual_decay: "5-10% condition loss/year"
      critical_events: "Flood, earthquake = major damage"

  condition_levels:
    excellent: "100-80% - Full function"
    good: "79-60% - Minor issues"
    fair: "59-40% - Reduced function"
    poor: "39-20% - Major problems"
    critical: "19-1% - Barely standing"
    collapsed: "0% - Ruins"
```

### 7.2 Maintenance Activities

```yaml
maintenance_activities:
  annual_replastering:
    frequency: "Once per year (before rainy season)"
    materials: "Mud plaster, whitewash"
    labor: "1-3 days depending on size"
    effect: "Restores 10-20% condition"
    neglect_consequence: "Walls erode, leak"

  roof_maintenance:
    frequency: "Twice per year"
    materials: "Reeds, mud"
    labor: "1-2 days"
    effect: "Restores 5-10% condition"
    neglect_consequence: "Leaks, collapse risk"

  foundation_check:
    frequency: "After floods, annually"
    materials: "Bitumen, packed earth"
    labor: "1-2 days"
    effect: "Prevents catastrophic failure"
    neglect_consequence: "Wall collapse"

  door_and_fixture_repair:
    frequency: "As needed"
    materials: "Wood, leather, metal"
    labor: "Hours to days"
    effect: "Maintains security and function"
```

### 7.3 NPC Maintenance Delegation

```yaml
maintenance_delegation:
  caretaker_npc:
    cost: "30-50 SILA/month"
    capabilities:
      - "Routine maintenance"
      - "Alert to problems"
      - "Minor repairs"
    limitations:
      - "Cannot handle major repairs"
      - "Requires materials supplied"
      - "Quality varies by NPC tier"

  skilled_maintenance:
    cost: "100+ SILA/month"
    capabilities:
      - "All maintenance tasks"
      - "Quality repairs"
      - "Proactive prevention"
    value: "Building condition stays high"
```

---

## 8. Upgrades & Expansion

### 8.1 Building Upgrades

```yaml
upgrade_paths:
  reed_hut_upgrades:
    to_semi_permanent:
      description: "Add mud-brick base"
      cost: "200 bricks, 1 week"
      benefit: "Lasts longer, more secure"

  mud_brick_house_upgrades:
    storage_expansion:
      description: "Add dedicated storage room"
      cost: "300 bricks, 1 week"
      benefit: "Increased storage capacity"

    workshop_addition:
      description: "Add production space"
      cost: "500 bricks, equipment"
      benefit: "Home + work combined"

    second_story:
      description: "Build up (limited)"
      cost: "500 bricks, heavy beams"
      benefit: "More space, same footprint"
      note: "Requires strong foundation"

  workshop_upgrades:
    capacity_expansion:
      description: "More production stations"
      cost: "Materials for stations"
      benefit: "Higher output"

    quality_improvement:
      description: "Better equipment"
      cost: "Premium materials"
      benefit: "Higher quality products"

    storage_addition:
      description: "Materials storage"
      cost: "400 bricks"
      benefit: "Hold more inventory"
```

### 8.2 Property Expansion

```yaml
property_expansion:
  acquiring_adjacent_land:
    process:
      1: "Check if available"
      2: "Negotiate with owner/Temple"
      3: "Pay acquisition cost"
      4: "Merge parcels"
    benefits:
      - "Larger operation"
      - "More building space"
      - "Unified property"

  building_additional_structures:
    requirements:
      - "Land space available"
      - "Materials and labor"
      - "Skills for construction"
    examples:
      - "Add granary to farm"
      - "Add storage to workshop"
      - "Add servant quarters to estate"

  vertical_expansion:
    limitations:
      - "Mud-brick limits height (2 stories max)"
      - "Foundation must support"
      - "Skills required for safe construction"
```

---

## 9. Special Structures

### 9.1 Community Buildings

```yaml
community_buildings:
  settlement_walls:
    requirements:
      - "Settlement cooperation"
      - "Massive labor (months)"
      - "Huge material quantities"
    benefits:
      - "Raid protection"
      - "Controlled access"
      - "Status symbol"
    maintenance: "Shared responsibility"

  settlement_granary:
    requirements:
      - "Community investment"
      - "Large construction"
    benefits:
      - "Emergency food reserve"
      - "Communal storage option"
    management: "Settlement governance decides"

  local_shrine:
    requirements:
      - "Temple approval"
      - "Community donations"
    benefits:
      - "Local Temple favor access"
      - "Ritual space"
    maintenance: "Community offerings"

  canal_systems:
    requirements:
      - "Multi-property cooperation"
      - "Engineering skill"
      - "Major labor investment"
    benefits:
      - "Shared irrigation"
      - "Transport route"
    maintenance: "All users contribute"
```

### 9.2 Defensive Structures

```yaml
defensive_structures:
  watchtower:
    description: "Elevated observation point"
    materials: ["Heavy bricks", "Platform", "Shade"]
    construction: "1-2 weeks"
    benefit: "Early warning of threats"
    requirements: "Must be manned"

  wall_section:
    description: "Defensive barrier"
    materials: ["5000+ bricks per 50m section"]
    construction: "Weeks per section"
    benefit: "Physical barrier to attackers"
    requirements: "Community effort usually"

  gate_complex:
    description: "Controlled entrance"
    materials: ["Heavy construction", "Wood gates", "Metal fittings"]
    construction: "3-4 weeks"
    benefit: "Secure access point"
    vulnerability: "Primary siege target"
```

---

## 10. Training Data Value

### 10.1 Construction Decision Data

```yaml
construction_training_data:
  planning_decisions:
    - "How do players plan construction projects?"
    - "What factors drive building choices?"
    - "How do they prioritize features?"
    - "How do they handle resource constraints?"

  investment_decisions:
    - "When do players build vs buy?"
    - "How do they value different building types?"
    - "How do they balance quality vs cost?"
    - "How do they finance construction?"

  maintenance_decisions:
    - "How do players approach maintenance?"
    - "When do they repair vs rebuild?"
    - "How do they delegate maintenance?"
    - "What happens when they neglect buildings?"
```

### 10.2 Property Management Data

```yaml
property_training_data:
  acquisition_patterns:
    - "How do players choose locations?"
    - "What drives tier progression?"
    - "How do they value different land features?"

  expansion_patterns:
    - "When do players expand?"
    - "How do they plan growth?"
    - "What triggers upgrades?"

  failure_patterns:
    - "What causes building failure?"
    - "How do players respond to decay?"
    - "What leads to abandonment?"
```

---

## 11. Implementation Notes

### 11.1 MVP Scope

```yaml
mvp_building:
  included_structures:
    residential:
      - "Reed hut"
      - "Mud-brick house"

    production:
      - "Basic workshop (generic)"
      - "Storage shed"

    agricultural:
      - "Animal pen"
      - "Granary (small)"

  included_systems:
    - "Basic construction (gather materials, build)"
    - "Simple decay (annual maintenance needed)"
    - "Land tiers (squatter, tenant, lease)"

  deferred:
    - "Complex multi-room structures"
    - "Community buildings (walls, canals)"
    - "Detailed construction skill tree"
    - "NFT deed purchases"
    - "Sophisticated upgrade paths"
```

### 11.2 Technical Considerations

```yaml
technical:
  building_placement:
    - "Grid-based placement"
    - "Collision detection"
    - "Terrain compatibility check"

  persistence:
    - "Building state saved to database"
    - "Condition updated periodically"
    - "Decay calculated on login or batch"

  visualization:
    - "Condition affects appearance"
    - "Construction shows progress"
    - "Damage visible"
```

---

## Appendix: Quick Reference

### Building Cost Summary

| Building | Bricks | Wood | Time | SILA Est. |
|----------|--------|------|------|-----------|
| Reed Hut | 0 | 0 | 2-4h | 50 |
| Mud-Brick House | 500-1000 | 5-10 | 1-2w | 500 |
| Workshop | 800-1200 | 10-15 | 2-3w | 1000 |
| Courtyard House | 2000-3000 | 20-30 | 3-5w | 3000 |
| Warehouse | 1500 | 15 | 3-4w | 2000 |

### Land Tier Summary

| Tier | Entry Cost | Tax | Building Limit | Security |
|------|------------|-----|----------------|----------|
| Squatter | Free | None | Reed hut | None |
| Tenant | Rent | Rent | Small house | Low |
| Leaseholder | SILA | 10-15% | Workshop/farm | Medium |
| Deed Owner | ANALOG | 15-25% | Estate | High |

### Maintenance Schedule

| Building Type | Replaster | Roof | Foundation | Annual Cost |
|---------------|-----------|------|------------|-------------|
| Reed Hut | N/A | Monthly | N/A | ~20 SILA |
| Mud-Brick | Annual | 2x/year | Annual | ~100 SILA |
| Workshop | Annual | 2x/year | Annual | ~150 SILA |
| Courtyard | Annual | 2x/year | Annual | ~300 SILA |

---

*"The first shelter you build is survival. The tenth is a home. The hundredth is a legacy."*
