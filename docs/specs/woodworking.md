# Woodworking

> *"In a land without forests, the carpenter is worth his weight in copper. Every beam he shapes, every tool handle he crafts, every boat he builds—these are treasures carved from scarcity."*

## Overview

Woodworking in Eridu is a prestigious craft operating under severe material constraints. With no local forests, every piece of timber is precious—imported from distant mountains or salvaged from date palms. The Nagar (carpenter) transforms this scarce resource into essential goods: furniture, tools, boats, building components, and temple fittings. This spec covers wood supply, carpentry techniques, boat construction, and the economics of working in a timber-poor environment.

---

## Design Philosophy

### Core Principles

1. **Material Scarcity**: Wood is rare and valuable
2. **Skill Premium**: Craftsmen who minimize waste command respect
3. **Specialization**: Different carpentry branches (furniture, boats, construction)
4. **Import Dependence**: Trade relationships crucial for supply
5. **Training Data Value**: Resource optimization, precision craft, design decisions

### The Scarcity Challenge

```yaml
wood_scarcity:
  local_trees:
    date_palm:
      availability: "Common"
      quality: "Poor for carpentry"
      use: "Beams, rough construction"
      weakness: "Fibrous, splits easily"

    tamarisk:
      availability: "Some"
      quality: "Fair"
      use: "Small items, tools"

    willow:
      availability: "Canal banks"
      quality: "Soft, limited use"
      use: "Baskets, light items"

  imported_woods:
    cedar:
      source: "Lebanon mountains"
      quality: "Excellent"
      cost: "Very expensive"
      use: "Temple doors, elite furniture"

    pine:
      source: "Northern mountains"
      quality: "Good"
      cost: "Expensive"
      use: "Construction, boats"

    ebony:
      source: "Africa via trade"
      quality: "Premium"
      cost: "Luxury price"
      use: "Inlay, decoration"

  consequence:
    prices: "All wood products expensive"
    repair: "Repair preferred over replacement"
    alternatives: "Reed, clay used where possible"
```

---

## The Carpenter (Nagar)

### Role and Status

```yaml
nagar_profession:
  description: "Skilled wood craftsman"
  status: "Respected artisan"

  demand:
    constant: "Essential goods always needed"
    premium: "Skill with scarce material valued"

  specializations:
    general: "Various wood products"
    furniture: "Household items"
    construction: "Building carpentry"
    shipwright: "Boat construction"
    carriage: "Vehicles, carts"
```

### Core Skills

```yaml
carpentry_foundations:
  wood_selection:
    description: "Choose right wood for purpose"
    factors:
      - "Grain direction"
      - "Moisture content"
      - "Defects to avoid"
      - "Strength requirements"
    importance: "Wrong choice wastes precious material"
    sila_reward: 25

  measurement:
    description: "Precise dimensions"
    tools: "String, rods, body measures"
    tolerance: "Minimal waste margins"
    sila_reward: 20

  cutting:
    description: "Shape wood to purpose"
    tools:
      saw: "Copper or bronze blade"
      adze: "Curved cutting tool"
      chisel: "Detail work"
      axe: "Rough shaping"
    sila_reward: 25

  joining:
    description: "Connect wood pieces"
    methods:
      mortise_tenon: "Interlocking joints"
      pegs: "Wooden dowels"
      lashing: "Leather or fiber binding"
      bitumen: "Waterproof adhesive"
    sila_reward: 30

  finishing:
    description: "Smooth and protect surface"
    methods:
      sanding: "Abrasive stones"
      oiling: "Preserve wood"
      inlay: "Decorative additions"
    sila_reward: 25
```

### Carpenter Skill Tree

```yaml
carpenter_skills:
  tier_1_novice:
    skills:
      basic_cutting:
        description: "Shape wood with adze"
        sila_reward: 20
        challenge: "Minimize waste"

      simple_assembly:
        description: "Join pieces with pegs"
        sila_reward: 20
        products: "Basic items"

      tool_maintenance:
        description: "Care for tools"
        sila_reward: 15
        importance: "Tools are expensive"

    role: "Workshop helper"
    earnings: "Rations + small wage"
    products: "Simple handles, repairs"

  tier_2_apprentice:
    requirements: "2 years training"
    skills:
      joinery:
        description: "Complex joints"
        sila_reward: 35
        quality: "Strong, lasting connections"

      furniture_basics:
        description: "Stools, tables, chests"
        sila_reward: 35
        market: "Household goods"

      repair_work:
        description: "Fix existing items"
        sila_reward: 30
        value: "Extends precious wood life"

    role: "Working carpenter"
    earnings: "Modest wage"
    products: "Standard furniture, repairs"

  tier_3_journeyman:
    requirements: "5 years + demonstrated skill"
    skills:
      fine_furniture:
        description: "Quality pieces"
        sila_reward: 50
        clients: "Wealthy households"

      construction_carpentry:
        description: "Building components"
        sila_reward: 50
        products: "Doors, beams, frames"

      specialized_items:
        description: "Specific products"
        sila_reward: 50
        examples: "Looms, wheels, tools"

    role: "Senior carpenter"
    earnings: "Good wage"
    products: "Custom work, quality goods"

  tier_4_master:
    requirements: "10+ years + reputation"
    skills:
      temple_work:
        description: "Sacred furniture, doors"
        sila_reward: 100
        status: "Religious significance"

      design_innovation:
        description: "Create new forms"
        sila_reward: 100
        legacy: "Patterns copied"

      workshop_management:
        description: "Train apprentices, manage production"
        sila_reward: 75
        role: "Business owner"

    role: "Master carpenter"
    earnings: "Elite status"
    products: "Prestige commissions"
```

---

## Boat Construction

### The Shipwright's Art

```yaml
shipwright_specialization:
  description: "Boat and ship construction"
  status: "Elite carpentry branch"

  importance:
    trade: "Boats enable commerce"
    fishing: "Food supply"
    transport: "Move goods and people"
    military: "River warfare"
```

### Boat Types and Construction

```yaml
boat_construction:
  reed_boats:
    type: "Za-sha (bundle boat)"
    materials: "Reed bundles, bitumen"
    carpenter_role: "Limited (reed-worker primary)"
    use: "Fishing, light transport"

  coracle:
    type: "Guffa (round boat)"
    frame: "Willow withes"
    covering: "Hides, bitumen-sealed"
    carpenter_role: "Frame construction"
    use: "Ferry, river crossing"

  plank_boats:
    type: "Serious watercraft"
    construction:
      keel: "Backbone of boat"
      ribs: "Frame members"
      planks: "Hull covering"
      sealing: "Bitumen caulking"
    materials: "Imported timber essential"
    carpenter_role: "Primary builder"
    use: "Trade, transport"

  river_barges:
    type: "Ma-gur (cargo vessel)"
    construction: "Flat-bottomed, wide"
    capacity: "Heavy loads"
    materials: "Substantial timber"
    carpenter_role: "Specialist shipwright"
    use: "Bulk transport"

  magan_boat:
    type: "Sea-going freighter"
    construction: "Reinforced for ocean"
    materials: "Best imported timber"
    carpenter_role: "Master shipwright"
    use: "Long-distance trade (Dilmun, Magan)"
```

### Shipwright Skill Tree

```yaml
shipwright_skills:
  tier_1_boat_helper:
    skills:
      reed_boat_assist:
        description: "Help build reed boats"
        sila_reward: 20

      caulking:
        description: "Apply bitumen sealing"
        sila_reward: 20
        importance: "Waterproofing"

      basic_repairs:
        description: "Patch hull damage"
        sila_reward: 20

    role: "Shipyard helper"

  tier_2_boat_builder:
    requirements: "2 years in shipyard"
    skills:
      coracle_construction:
        description: "Build frame boats"
        sila_reward: 35

      plank_shaping:
        description: "Prepare hull planks"
        sila_reward: 35

      hull_assembly:
        description: "Join planks to frame"
        sila_reward: 40

    role: "Working boat builder"

  tier_3_shipwright:
    requirements: "5 years + boats completed"
    skills:
      river_boat_construction:
        description: "Build trade vessels"
        sila_reward: 60

      design_adaptation:
        description: "Modify plans for conditions"
        sila_reward: 50

      launching_management:
        description: "Coordinate completion"
        sila_reward: 50

    role: "Professional shipwright"

  tier_4_master_shipwright:
    requirements: "10 years + major vessels"
    skills:
      sea_vessel_construction:
        description: "Build ocean-worthy ships"
        sila_reward: 150

      shipyard_management:
        description: "Run boat-building operation"
        sila_reward: 100

      naval_consultation:
        description: "Advise on fleet needs"
        sila_reward: 100

    role: "Master shipwright"
    status: "Elite craftsman"
```

---

## Products and Markets

### Furniture

```yaml
furniture_products:
  basic_items:
    stool:
      materials: "Palm wood or local"
      price: "5-15 SILA"
      market: "Common households"

    low_table:
      materials: "Local or imported"
      price: "10-30 SILA"
      market: "Standard homes"

    storage_chest:
      materials: "Mixed woods"
      price: "20-50 SILA"
      market: "All households"

  quality_items:
    bed_frame:
      materials: "Imported timber"
      price: "50-150 SILA"
      market: "Wealthy homes"

    chair_with_back:
      materials: "Quality wood"
      price: "30-100 SILA"
      market: "Status symbol"

    decorated_chest:
      materials: "Imported + inlay"
      price: "100-500 SILA"
      market: "Elite, temples"

  luxury_items:
    inlaid_furniture:
      materials: "Cedar, ebony, shell"
      price: "500+ SILA"
      market: "Palace, temple, wealthy"

    musical_instruments:
      materials: "Quality woods"
      price: "Varies widely"
      examples: "Lyre frames, drum bodies"
```

### Construction Components

```yaml
construction_products:
  structural:
    beams:
      use: "Roof support"
      materials: "Palm trunk or imported"
      price: "Based on length/quality"

    posts:
      use: "Vertical support"
      materials: "Solid wood"
      price: "Variable"

    lintels:
      use: "Door/window tops"
      materials: "Strong wood"
      price: "By size"

  finishing:
    doors:
      types: "Single, double, decorated"
      price: "20-200+ SILA"
      importance: "Security, status"

    window_frames:
      use: "Openings"
      price: "10-50 SILA"

    shutters:
      use: "Close windows"
      price: "15-40 SILA"

  temple_items:
    sacred_doors:
      materials: "Cedar, decorated"
      price: "Temple commission"
      status: "Highest prestige work"

    shrine_fittings:
      materials: "Quality woods"
      price: "Temple payment"
```

### Tools and Equipment

```yaml
tool_products:
  agricultural:
    plow_parts:
      components: "Handle, beam"
      price: "30-80 SILA"
      customer: "Farmers"

    tool_handles:
      types: "Hoe, sickle, axe"
      price: "2-10 SILA each"
      volume: "High demand"

    threshing_equipment:
      type: "Sledge components"
      price: "By complexity"

  craft_tools:
    loom_parts:
      customer: "Weavers"
      price: "Variable by type"
      importance: "Textile industry support"

    spindle_whorls:
      material: "Wood disc"
      price: "1-3 SILA"
      volume: "Common item"

  household:
    bowls_vessels:
      use: "Daily use"
      price: "2-15 SILA"
      note: "Compete with pottery"

    storage_items:
      types: "Boxes, containers"
      price: "Variable"
```

### Vehicles

```yaml
vehicle_products:
  carts:
    ox_cart:
      use: "Heavy transport"
      components: "Frame, wheels, axle"
      price: "100-300 SILA"
      customer: "Farmers, merchants"

    hand_cart:
      use: "Personal transport"
      price: "30-80 SILA"

  wheels:
    solid_wheel:
      construction: "Three-piece solid"
      materials: "Strong wood"
      price: "20-50 SILA each"
      specialty: "Wheelwright sub-trade"

  sledges:
    transport_sledge:
      use: "Move heavy loads"
      price: "40-100 SILA"
```

---

## Workshop Operations

### Tools of the Trade

```yaml
carpenter_tools:
  cutting:
    adze:
      description: "Curved blade for shaping"
      material: "Copper or bronze blade"
      cost: "15-30 SILA"
      use: "Primary shaping tool"

    saw:
      description: "Cutting blade"
      material: "Copper, bronze, or flint teeth"
      cost: "20-50 SILA"
      use: "Cutting planks"

    chisel:
      description: "Detail cutting"
      material: "Copper or bronze"
      cost: "5-15 SILA"
      set: "Multiple sizes needed"

    axe:
      description: "Rough cutting"
      material: "Stone or metal head"
      cost: "10-25 SILA"

  measuring:
    cubit_rod:
      description: "Standard length measure"
      use: "Consistent sizing"

    string_line:
      description: "Straight edge reference"
      use: "Layout, alignment"

    plumb:
      description: "Vertical reference"
      use: "Vertical alignment"

  finishing:
    abrasive_stones:
      description: "Smoothing surfaces"
      source: "Imported or local"
      use: "Final surface prep"

    bow_drill:
      description: "Make holes"
      use: "Peg holes, decoration"
```

### Workshop Economy

```yaml
workshop_structure:
  location:
    karum: "Market district"
    residential: "Home workshop"
    temple: "Institutional facility"

  personnel:
    master: "Owner/lead craftsman"
    journeymen: "Skilled workers"
    apprentices: "Learners"
    helpers: "Unskilled labor"

  materials:
    procurement:
      local: "Palm, tamarisk (limited)"
      imported: "Through merchants"
      cost: "Major expense"

    storage:
      dry: "Protect from moisture"
      secure: "Prevent theft"

  economics:
    pricing:
      materials: "40-60% of cost"
      labor: "30-40% of cost"
      profit: "10-20% margin"

    payment:
      commission: "Deposit + completion"
      stock: "Sale when finished"
      barter: "Often accepted"
```

---

## Wood Supply Chain

### Import Process

```yaml
wood_importing:
  sources:
    lebanon_cedar:
      route: "Overland or coast"
      intermediaries: "Multiple traders"
      premium: "Highest prices"

    northern_pine:
      route: "River from mountains"
      form: "Logs floated downstream"
      availability: "More accessible"

    various:
      route: "Trade networks"
      timing: "Seasonal availability"

  local_procurement:
    date_palm:
      source: "Orchards, dead trees"
      permission: "Owner negotiation"
      quality: "Limited use"

    driftwood:
      source: "River deposits"
      rights: "First finder"
      quality: "Variable"

  merchant_role:
    damgar: "Import wood"
    markup: "Significant profit"
    credit: "May extend to carpenters"
```

### Wood Market

```yaml
wood_trading:
  pricing:
    by_piece: "Individual items"
    by_volume: "Bulk purchases"
    by_quality: "Grade-based"

  factors:
    species: "Cedar > pine > palm"
    condition: "Seasoned > green"
    size: "Larger pieces premium"
    grain: "Straight > crooked"

  seasons:
    flush: "After trade caravans"
    scarce: "Between arrivals"
    price_swing: "Significant variation"

  preservation:
    challenge: "Insects, rot"
    methods: "Oil, storage conditions"
    loss: "Material deterioration"
```

---

## Temple and Palace Work

### Prestigious Commissions

```yaml
temple_commissions:
  sacred_doors:
    description: "Main temple entrance"
    materials: "Cedar, precious metals"
    decoration: "Carved, inlaid"
    carpenter_role: "Wood components"
    status: "Career-defining work"
    sila_reward: 200

  furniture:
    altars: "Offering tables"
    thrones: "Divine seats"
    storage: "Sacred object containers"
    sila_reward: 100-150

  structural:
    roof_beams: "Temple construction"
    doorframes: "Monumental scale"
    sila_reward: 100

  payment:
    type: "Temple resources"
    benefits: "Steady work, prestige"
    relationship: "Long-term if quality"
```

### Palace Work

```yaml
palace_commissions:
  royal_furniture:
    beds: "Elaborate construction"
    thrones: "Ceremonial seating"
    storage: "Official documents"

  administrative:
    shelving: "Archive storage"
    desks: "Scribe furniture"

  status:
    appointment: "Royal craftsman"
    benefits: "Salary, rations, housing"
    prestige: "Highest secular status"
```

---

## Training Data Value

### Knowledge Capture

```yaml
training_data:
  design_decisions:
    - "Material selection reasoning"
    - "Joint type selection"
    - "Design for purpose"

  resource_optimization:
    - "Minimizing waste"
    - "Substitution choices"
    - "Repair vs. replace decisions"

  quality_judgment:
    - "Wood evaluation"
    - "Work assessment"
    - "Customer requirements"

  business_reasoning:
    - "Pricing decisions"
    - "Material procurement"
    - "Commission negotiation"
```

---

## Implementation Notes

### Database Schema

```yaml
woodworking_records:
  carpenter_profile:
    player_id: uuid
    specialization: enum  # general, furniture, shipwright, construction
    skill_level: integer
    tools_owned: array
    workshop_id: uuid
    reputation: integer
    major_works: array

  project_record:
    project_id: uuid
    carpenter_id: uuid
    type: string
    materials_used: array
    commission_value: integer
    client_id: uuid
    status: enum
    quality_rating: integer

  wood_inventory:
    inventory_id: uuid
    owner_id: uuid
    wood_type: string
    quantity: float
    quality: integer
    source: string
    acquisition_date: datetime
```

---

## Appendix: Sumerian Woodworking Terms

| Term | Meaning | Gameplay Role |
|------|---------|---------------|
| **Nagar** | Carpenter | Primary profession |
| **Gish** | Wood/Tree | Material |
| **Ma** | Boat | Watercraft |
| **Gish-kiri** | Orchard | Wood source |
| **Eren** | Cedar | Premium import |
| **Gish-apin** | Plow | Agricultural tool |

---

*"The carpenter shapes not just wood, but possibility. In his hands, a foreign log becomes a door that guards a home, a beam that holds a roof, a hull that carries dreams across the water. He transforms scarcity into sufficiency."*
