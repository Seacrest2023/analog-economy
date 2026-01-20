# Eridu: The First City

> "Before Ur was great, before Uruk was built, before there was a king in Kish—there was Eridu, where Enki raised the first temple from the waters."

## Table of Contents

1. [Overview](#1-overview)
2. [Visual Identity](#2-visual-identity)
3. [City Layout](#3-city-layout)
4. [The Zones](#4-the-zones)
5. [Major Landmarks](#5-major-landmarks)
6. [Institutions & Services](#6-institutions--services)
7. [Currency & Commerce](#7-currency--commerce)
8. [Streets & Infrastructure](#8-streets--infrastructure)
9. [The Harbor](#9-the-harbor)
10. [Daily Life & Atmosphere](#10-daily-life--atmosphere)
11. [Sounds & Ambiance](#11-sounds--ambiance)
12. [Weather & Environment](#12-weather--environment)
13. [NPC Population](#13-npc-population)
14. [Player Starting Experience](#14-player-starting-experience)
15. [Implementation Notes](#15-implementation-notes)

---

## 1. Overview

### 1.1 Historical Context

```yaml
eridu_facts:
  founded: "~5400 BCE (oldest continuously inhabited city)"
  peak_period: "5400-4900 BCE"
  game_start: "4500 BCE (still prominent, pre-Uruk dominance)"
  location: "Southern Mesopotamia, edge of Persian Gulf"
  patron_deity: "Enki (God of Water, Wisdom, Creation)"
  primary_temple: "E-Abzu (House of the Aquifer)"
  population_at_start: "~2,000-4,000 inhabitants"
  significance: "First temple, first city, birthplace of civilization"
```

### 1.2 Modern Parallels

To help visualize Eridu, we draw from surviving examples:

```yaml
visual_references:
  architecture:
    ma'dan_villages:
      description: "Marsh Arab communities in southern Iraq"
      relevance: "Reed construction techniques (mudhifs) nearly identical"
      use_for: "Fisher folk homes, marsh-edge structures"

    yazd_iran:
      description: "Ancient mud-brick city with wind towers"
      relevance: "Earth-toned urban density, adobe construction"
      use_for: "Upper-class homes, temple complex walls"

  landscape:
    basra_marshes:
      description: "Iraqi wetlands, 130km from Eridu ruins"
      relevance: "Same alluvial floodplain, reed beds, waterways"
      use_for: "Surrounding terrain, marsh areas"

  conceptual:
    venice:
      description: "Canal-integrated city"
      relevance: "Water as transportation, life built around channels"
      use_for: "Understanding how canals function in daily life"
```

### 1.3 The Temple-City Concept

Eridu was not a modern city with separate zones. It was a **temple-city**:

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  MODERN CITY                          ERIDU (TEMPLE-CITY)           │
│  ───────────                          ───────────────────           │
│                                                                     │
│  City Hall ───┐                       ┌───────────────────┐         │
│               │                       │                   │         │
│  Bank ────────┼── Separate            │    THE TEMPLE     │         │
│               │   Buildings           │                   │         │
│  Warehouse ───┤                       │  = Government     │         │
│               │                       │  = Bank           │         │
│  Factory ─────┤                       │  = Warehouse      │         │
│               │                       │  = Factory        │         │
│  Church ──────┘                       │  = Church         │         │
│                                       │  = School         │         │
│                                       │  = Hospital       │         │
│                                       └───────────────────┘         │
│                                                                     │
│  Religion, government, and commerce were INDISTINGUISHABLE.         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2. Visual Identity

### 2.1 Color Palette

```yaml
color_palette:
  primary_earth_tones:
    sun_dried_brick: "#C4A882"  # Dominant wall color
    wet_mud: "#8B7355"          # Fresh construction, streets
    dried_clay: "#D2B48C"       # Pottery, tablets
    whitewash: "#F5F5DC"        # Temple and wealthy homes

  water_tones:
    euphrates_blue: "#4A7C8C"   # River water
    marsh_green: "#5D7A5D"      # Reed beds, standing water
    canal_murky: "#6B7B5F"      # Irrigation channels

  vegetation:
    date_palm_trunk: "#5D4E37"  # Palm trees throughout
    reed_yellow: "#C9B896"      # Dried reeds, construction
    reed_green: "#7D8C5C"       # Living reeds at water edge

  accent_colors:
    lapis_blue: "#1E4D8C"       # Rare, precious, temple decoration
    copper_red: "#B87333"       # Metal goods, wealthy decoration
    bitumen_black: "#2C2C2C"    # Waterproofing, road material

  sky_and_light:
    dawn: "#FFB366"             # Orange-gold sunrise
    midday: "#87CEEB"           # Harsh bright blue
    dusk: "#FF6B6B"             # Dusty red sunset
    night: "#1A1A2E"            # Deep blue-black
```

### 2.2 Architectural Style

```yaml
architectural_elements:
  construction_materials:
    primary:
      - "Sun-dried mud brick (adobe) - 90% of structures"
      - "Bundled reeds (for marsh-edge and poor housing)"
      - "Kiln-fired brick (rare, sacred structures only)"

    secondary:
      - "Date palm wood (beams, doors, furniture)"
      - "Reed matting (roofing, walls, floors)"
      - "Bitumen/asphalt (waterproofing, mortar)"

    decorative:
      - "Whitewash (temple, wealthy homes)"
      - "Clay cone mosaics (temple facade)"
      - "Copper fittings (temple doors)"

  building_heights:
    common_homes: "Single story, 2-3 meters"
    wealthy_homes: "Two stories, 4-5 meters"
    temple_platform: "Stepped, 8-12 meters"
    city_walls: "5-7 meters"

  roof_styles:
    flat: "Most common, used for sleeping in summer"
    vaulted: "Reed bundle arches for larger spans"
    reed_thatch: "Poorer structures, needs frequent replacement"

  characteristic_features:
    - "No windows on ground floor (privacy, security)"
    - "Small high windows or open roofs for ventilation"
    - "Narrow doorways (defense, heat management)"
    - "Courtyard layouts (private outdoor space)"
    - "Thick walls (thermal mass for cooling)"
```

### 2.3 Visual Landmarks (What You See First)

```yaml
first_impressions:
  from_river_approach:
    - "Brown-gold city rising from reed marshes"
    - "The ziggurat platform visible above walls"
    - "Smoke rising from hundreds of cooking fires"
    - "Palm trees lining the canal entrances"
    - "Harbor with reed boats and wooden quays"

  from_desert_approach:
    - "Walls emerging from heat shimmer"
    - "Green ribbon of vegetation along water"
    - "White-topped temple gleaming in sun"
    - "Dust rising from the gate roads"

  from_inside_walls:
    - "Narrow winding streets, always visible sky"
    - "Whitewashed temple towering over all"
    - "Date palms in courtyards"
    - "Constant presence of water (canals, wells)"
```

---

## 3. City Layout

### 3.1 Overall Map

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  ═══════════════════════════════════════════════════════════════   │
│                          EUPHRATES RIVER                            │
│  ═══════════════════════════════════════════════════════════════   │
│              │                                                      │
│              │ Main Canal                                           │
│              ▼                                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │          ╔═══════════════════════════════════════╗           │  │
│  │          ║            HARBOR DISTRICT            ║           │  │
│  │          ║  • Quays and docks                    ║           │  │
│  │          ║  • Fish market                        ║           │  │
│  │          ║  • Boat builders                      ║           │  │
│  │          ║  • Foreign merchants                  ║           │  │
│  │          ╚═══════════════════════════════════════╝           │  │
│  │                           │                                   │  │
│  │    ┌──────────────────────┴──────────────────────┐           │  │
│  │    │              PROCESSIONAL WAY               │           │  │
│  │    │         (Paved with fired brick)            │           │  │
│  │    └──────────────────────┬──────────────────────┘           │  │
│  │                           │                                   │  │
│  │  ┌─────────────┐    ╔═════╧═════╗    ┌─────────────┐         │  │
│  │  │   ELITE     │    ║           ║    │   ELITE     │         │  │
│  │  │  QUARTER    │    ║  E-ABZU   ║    │  QUARTER    │         │  │
│  │  │             │    ║  TEMPLE   ║    │             │         │  │
│  │  │ • Priests   │    ║  COMPLEX  ║    │ • Merchants │         │  │
│  │  │ • Officials │    ║           ║    │ • Scribes   │         │  │
│  │  │ • Scribes   │    ║ ┌───────┐ ║    │ • Officials │         │  │
│  │  └─────────────┘    ║ │ZIGGU- │ ║    └─────────────┘         │  │
│  │                     ║ │ RAT   │ ║                             │  │
│  │  ╔═══════════╗      ║ │       │ ║      ╔═══════════╗         │  │
│  │  ║ ARTISAN   ║      ║ └───────┘ ║      ║ ARTISAN   ║         │  │
│  │  ║ QUARTER   ║      ║           ║      ║ QUARTER   ║         │  │
│  │  ║ • Potters ║      ║• Treasury ║      ║ • Weavers ║         │  │
│  │  ║ • Smiths  ║      ║• Granary  ║      ║ • Tanners ║         │  │
│  │  ║ • Carvers ║      ║• Workshops║      ║ • Brewers ║         │  │
│  │  ╚═══════════╝      ╚═══════════╝      ╚═══════════╝         │  │
│  │                                                               │  │
│  │  ┌───────────────────────────────────────────────────────┐   │  │
│  │  │                  COMMONER QUARTER                      │   │  │
│  │  │  • Farmers  • Laborers  • Servants  • Fishermen       │   │  │
│  │  │  • Simple mud-brick homes  • Shared courtyards        │   │  │
│  │  └───────────────────────────────────────────────────────┘   │  │
│  │                                                               │  │
│  │  ════════════════════════════════════════════════════════    │  │
│  │                        CITY WALLS                             │  │
│  │  ════════════════════════════════════════════════════════    │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                │                    │                    │          │
│           GATE (NORTH)         GATE (EAST)         GATE (SOUTH)    │
│                                                                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐     │
│  │ EXTRA-MURAL     │  │    IRRIGATION   │  │   MARSH/REED    │     │
│  │ SETTLEMENTS     │  │     FIELDS      │  │     BEDS        │     │
│  │ • Herders       │  │ • Grain fields  │  │ • Fisher folk   │     │
│  │ • Seasonal      │  │ • Date palms    │  │ • Reed cutters  │     │
│  │   workers       │  │ • Canal network │  │ • Hunters       │     │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.2 Distances & Scale

```yaml
city_dimensions:
  walled_area: "~400m x 300m (approximately 12 hectares)"
  wall_circumference: "~1.4 km"

  walking_times:
    gate_to_temple: "5-8 minutes"
    temple_to_harbor: "3-5 minutes"
    across_entire_city: "10-15 minutes"
    city_to_nearest_field: "5-10 minutes"
    city_to_marsh_edge: "10-15 minutes"

  building_density:
    temple_area: "Large open courtyards"
    elite_quarters: "Medium density, private courtyards"
    artisan_quarters: "Dense, workshop/home combos"
    commoner_quarters: "Very dense, shared spaces"
```

---

## 4. The Zones

### 4.1 Temple Complex (Center)

```yaml
temple_complex:
  size: "~80m x 60m (largest structure in the city)"

  components:
    ziggurat:
      description: "Stepped platform, 3 levels"
      height: "~8-10 meters"
      access: "Priests and officials only"
      visual: "Whitewashed, visible from anywhere in city"

    e_abzu:
      description: "Temple proper atop platform"
      features:
        - "Inner sanctum (statue of Enki)"
        - "Offering hall"
        - "Ritual bathing pool"
        - "Sacred date palm grove"

    administrative_wings:
      description: "Buildings surrounding platform"
      functions:
        - "Granary (grain storage, the 'bank')"
        - "Treasury (silver, copper, precious goods)"
        - "Scribe school"
        - "Priest quarters"
        - "Workshop complex"

    courtyard:
      description: "Open area before temple steps"
      functions:
        - "Public rituals and announcements"
        - "Market on festival days"
        - "Justice dispensed"
        - "Player spawn area"

  access_rules:
    outer_courtyard: "Anyone during day"
    administrative_wings: "Business or appointment"
    temple_base: "Offering or prayer (favor 10+)"
    upper_levels: "Priests and high favor only (50+)"
    inner_sanctum: "Special permission (100+ favor)"
```

### 4.2 Elite Quarter

```yaml
elite_quarter:
  location: "Immediately surrounding temple"
  residents: "Priests, officials, wealthy merchants, scribes"

  housing_style:
    size: "100-200 sq meters"
    stories: "Two floors common"
    features:
      - "Private courtyard with well"
      - "Whitewashed exterior"
      - "Servant quarters"
      - "Storage rooms for trade goods"
      - "Reception room for business"

  typical_layout:
    ground_floor:
      - "Entry vestibule (no direct view inside)"
      - "Courtyard (open to sky)"
      - "Kitchen"
      - "Storage"
      - "Servant room"
    upper_floor:
      - "Family sleeping quarters"
      - "Private shrine"
      - "Roof access (summer sleeping)"

  notable_residents:
    - "High Priest of Enki"
    - "Temple administrator (EN)"
    - "Chief scribe"
    - "Harbor master"
    - "Master craftsmen guild leaders"

  player_access:
    - "Can walk streets freely"
    - "Entry to homes requires invitation or quest"
    - "Higher prices in shops"
    - "Better quality goods available"
```

### 4.3 Artisan Quarters

```yaml
artisan_quarters:
  location: "Ring around elite quarter, both sides"
  residents: "Craftsmen, skilled workers, their families"

  craft_specializations:
    east_quarter:
      - "Potters (clay source nearby)"
      - "Brick makers"
      - "Sculptors"
      - "Reed workers"

    west_quarter:
      - "Weavers (large looms need space)"
      - "Metalworkers (fire hazard, edge of city)"
      - "Leather workers (smell)"
      - "Brewers (grain access)"

  workshop_homes:
    size: "50-100 sq meters"
    layout:
      ground_floor: "Workshop, open to street"
      upper_floor_or_back: "Family living space"
    features:
      - "Display area facing street"
      - "Work area visible to passersby"
      - "Small courtyard or shared yard"
      - "Kiln or forge (where applicable)"

  atmosphere:
    - "Constant activity, noise of work"
    - "Smoke from kilns and forges"
    - "Smell of leather, beer, fired clay"
    - "Apprentices running errands"
    - "Haggling over prices"

  player_opportunities:
    - "Learn crafts (apprenticeship quests)"
    - "Purchase goods at better prices"
    - "Find innovation clues"
    - "Employment for currency"
```

### 4.4 Commoner Quarter

```yaml
commoner_quarter:
  location: "Inner edge of city walls"
  residents: "Farmers, laborers, servants, fishermen, new arrivals"

  housing_style:
    size: "20-40 sq meters"
    stories: "Single floor"
    features:
      - "Shared courtyard (3-5 families)"
      - "Mud brick or reed construction"
      - "Minimal furniture"
      - "Sleeping mats, few possessions"
      - "Shared cooking area"

  living_conditions:
    density: "High, little privacy"
    sanitation: "Waste in streets, periodic cleaning"
    water: "Shared wells or canal access"
    light: "Open doors during day, oil lamps (precious)"

  community_features:
    - "Communal ovens"
    - "Shared wells"
    - "Street vendors"
    - "Informal markets"
    - "Gossip networks"

  player_relevance:
    - "Cheapest lodging"
    - "Day labor opportunities"
    - "Information from working class"
    - "Starting point for most players"
    - "Crime more common"
```

### 4.5 Harbor District

```yaml
harbor_district:
  location: "North edge of city, canal entrance"
  function: "Trade, fishing, boat building, foreign contact"

  physical_features:
    main_quay:
      description: "Wooden and brick dock extending into canal"
      capacity: "20-30 boats at once"
      activities: "Loading, unloading, merchant negotiation"

    boat_yard:
      description: "Reed boat construction area"
      crafts: "Coracles, reed rafts, wooden cargo boats"
      smell: "Bitumen (waterproofing), wet reeds"

    fish_market:
      description: "Daily morning market"
      goods: "Fresh fish, dried fish, shellfish"
      timing: "Dawn to mid-morning"

    foreign_quarter:
      description: "Area for non-local merchants"
      residents: "Traders from Dilmun, Magan, possibly Indus"
      features: "Different language, exotic goods, inn/lodging"

  trade_goods:
    imports:
      - "Copper (from Magan/Oman)"
      - "Timber (from mountains via river)"
      - "Stone (absent in alluvial plain)"
      - "Lapis lazuli (from Afghanistan)"
      - "Carnelian (from Indus)"

    exports:
      - "Grain (barley, wheat)"
      - "Textiles (wool, linen)"
      - "Dates and date products"
      - "Dried fish"
      - "Bitumen"

  player_opportunities:
    - "Trade with foreign merchants"
    - "Learn sailing/navigation"
    - "Hear tales of distant lands"
    - "Employment as dock worker"
    - "Acquire exotic goods"
```

### 4.6 Extra-Mural Areas

```yaml
extra_mural:
  outside_walls:
    herder_camps:
      location: "North, dry side"
      residents: "Semi-nomadic herders"
      animals: "Sheep, goats, some cattle"
      relationship: "Trade wool, meat; buy grain, goods"

    irrigation_fields:
      location: "East and West, along canals"
      crops: "Barley, wheat, vegetables, flax"
      features: "Canal network, shaduf (water lifting)"
      residents: "Farmers (live in commoner quarter, work here)"

    marsh_settlements:
      location: "South, toward standing water"
      residents: "Fisher folk, reed cutters, fowlers"
      housing: "Reed huts on platforms, some on artificial islands"
      culture: "Distinct from city-dwellers, older traditions"

    cemetery:
      location: "Beyond east fields"
      features: "Simple graves, some brick tombs for wealthy"
      significance: "Offerings to ancestors, connection to underworld"

  travel_times_from_gate:
    nearest_field: "5 minutes"
    main_agricultural_zone: "15-30 minutes"
    marsh_edge: "20-30 minutes"
    true_wilderness: "1+ hours"
```

---

## 5. Major Landmarks

### 5.1 The E-Abzu (Temple of Enki)

```yaml
e_abzu:
  name_meaning: "House of the Aquifer / House of the Cosmic Waters"

  physical_description:
    base: "Mud-brick platform, 40m x 30m"
    levels: "Three stepped tiers"
    height: "8-10 meters total"
    temple_building: "Atop platform, mudbrick with whitewash"
    stairs: "Single monumental staircase, east-facing"

  visual_details:
    exterior:
      - "Walls covered in white lime plaster"
      - "Niches and buttresses create shadow patterns"
      - "Copper-sheathed doors at entrance"
      - "Clay cone mosaics (colored patterns)"
    interior:
      - "Dim, lit by oil lamps"
      - "Walls painted with ritual scenes"
      - "Statue of Enki in rear niche"
      - "Offering tables before statue"
      - "Incense smoke constantly rising"

  the_abzu_pool:
    description: "Sacred freshwater pool within complex"
    significance: "Represents primordial waters, Enki's domain"
    features:
      - "Fed by underground spring"
      - "Fish kept as sacred animals"
      - "Ritual bathing for purification"
      - "Visions possible (Witness cost)"

  functions:
    religious:
      - "Daily offerings to Enki"
      - "Festival rituals"
      - "Divination and omens"
      - "Purification rites"
    economic:
      - "Grain storage and loans"
      - "Craft workshop management"
      - "Trade oversight"
      - "Weight/measure standards"
    administrative:
      - "Record keeping"
      - "Justice administration"
      - "Land allocation"
      - "Labor organization"

  gameplay_significance:
    - "Central hub for quests"
    - "Enki communion possible"
    - "Innovation clues from priests"
    - "Economic transactions"
    - "Hidden areas below (Anunnaki content)"
```

### 5.2 The City Gates

```yaml
city_gates:
  north_gate_water_gate:
    faces: "Harbor, canal"
    traffic: "Merchants, fishermen, boats"
    features:
      - "Massive wooden doors"
      - "Guard chamber"
      - "Customs inspection area"
      - "Ramp to water level"
    atmosphere: "Busiest gate, constant activity"

  east_gate_field_gate:
    faces: "Agricultural lands"
    traffic: "Farmers, laborers, grain carts"
    features:
      - "Wide for cart access"
      - "Morning/evening rush"
      - "Grain inspection"
    atmosphere: "Dawn departure, dusk return"

  south_gate_marsh_gate:
    faces: "Marshlands"
    traffic: "Fisher folk, reed cutters, hunters"
    features:
      - "Smaller, less fortified"
      - "Near commoner quarter"
      - "Less monitored"
    atmosphere: "Quieter, more informal"

  gate_mechanics:
    hours:
      open: "Dawn to dusk"
      closed: "Night (emergency only)"
    guards:
      - "Check incoming goods"
      - "Collect tolls on trade goods"
      - "Question strangers"
    player_experience:
      - "Entry requires stating business"
      - "Known residents pass freely"
      - "Strangers may need vouching"
```

### 5.3 The Processional Way

```yaml
processional_way:
  description: "Paved road from harbor to temple"
  length: "~150 meters"
  width: "4-5 meters"

  construction:
    surface: "Kiln-fired brick set in bitumen"
    drainage: "Slight crown, channels to sides"
    significance: "First intentional 'road' in history"

  usage:
    daily: "Main thoroughfare, market activity"
    festivals: "Ritual processions, statue parades"
    special: "Judgment announcements, public events"

  atmosphere:
    - "Most crowded area of city"
    - "Vendors lining both sides"
    - "Priests walking in formal procession"
    - "Animals being led to sacrifice"
    - "Scribes recording transactions"

  player_relevance:
    - "Best place to find traders"
    - "Hear news and rumors"
    - "Observe daily life"
    - "Meet quest-givers"
    - "Pickpocket risk area"
```

### 5.4 The Granary

```yaml
granary:
  location: "Temple complex, west wing"

  physical_structure:
    building: "Large, thick-walled for temperature control"
    storage: "Multiple sealed chambers"
    capacity: "Enough to feed city for months"

  functions:
    storage:
      - "Temple receives portion of all harvests"
      - "Surplus stored for lean times"
      - "Seed grain protected"

    banking:
      - "Farmers deposit grain, receive 'credit'"
      - "Loans for planting season"
      - "Interest paid in grain"

    payment:
      - "Workers paid in grain rations"
      - "Standardized measures"
      - "Exchange for other goods possible"

  gameplay_mechanics:
    - "Store grain safely"
    - "Take loans (with obligation)"
    - "Exchange grain for credit"
    - "Employment: granary worker"
    - "Quest location: theft investigation"
```

---

## 6. Institutions & Services

### 6.1 The Temple as Institution

```yaml
temple_institution:
  governance:
    leader: "EN (High Priest/ess)"
    council: "Senior priests, temple administrators"
    authority: "Religious, economic, judicial combined"

  services_provided:
    religious:
      - "Daily rituals maintaining cosmic order"
      - "Personal blessings and purification"
      - "Divination and omens"
      - "Funeral rites"

    economic:
      - "Grain storage and loans"
      - "Standard weights and measures"
      - "Trade arbitration"
      - "Employment in workshops"

    social:
      - "Orphan and widow support"
      - "Dispute resolution"
      - "Education (scribal school)"
      - "Healing (limited, ritual-based)"

    administrative:
      - "Land records"
      - "Census of population"
      - "Labor corvée organization"
      - "Military coordination"

  player_interactions:
    - "Pray and make offerings"
    - "Seek loans or store grain"
    - "Report crimes"
    - "Learn to read/write (scribal school)"
    - "Find employment"
    - "Gain quest assignments"
```

### 6.2 The Scribal School (E-Dubba)

```yaml
scribal_school:
  location: "Temple complex, east wing"
  name_meaning: "House of Tablets"

  function:
    primary: "Train scribes for temple administration"
    secondary: "Preserve and copy important texts"

  students:
    typical: "Sons of officials and merchants"
    age: "Beginning around 7-8 years old"
    duration: "10+ years for full training"

  curriculum:
    basic:
      - "Clay tablet preparation"
      - "Stylus use"
      - "Cuneiform sign memorization (600+ signs)"
      - "Copying exercises"
    advanced:
      - "Mathematics (base-60 system)"
      - "Accounting and record-keeping"
      - "Literature and myths"
      - "Divination texts"

  player_relevance:
    - "Learn writing innovation here"
    - "Access historical texts"
    - "Find innovation clues in old tablets"
    - "Employment as scribe (after training)"
    - "Quest: Find missing tablet"
```

### 6.3 The Workshop Complex

```yaml
temple_workshops:
  location: "Temple complex, surrounding main structure"

  crafts_housed:
    textile_workshop:
      workers: "100+ weavers (mostly women)"
      products: "Wool and linen cloth, garments"
      organization: "Temple-employed, paid in rations"

    pottery_workshop:
      workers: "20-30 potters"
      products: "Storage vessels, bowls, ritual objects"
      features: "Kilns behind building"

    metallurgy_workshop:
      workers: "10-15 smiths"
      products: "Copper tools, weapons, ritual objects"
      note: "Bronze not yet common (4500 BCE)"

    carpentry_workshop:
      workers: "15-20 woodworkers"
      products: "Furniture, doors, tool handles, boats"
      materials: "Imported timber, local palm wood"

  employment_for_players:
    requirements: "Demonstrate basic skill"
    payment: "Grain rations, occasional goods"
    advancement: "Better work, more pay, specialization"
    benefit: "Learning toward innovations"
```

### 6.4 Informal Institutions

```yaml
informal_institutions:
  the_beer_houses:
    description: "Taverns/bars run by women (sabitum)"
    function:
      - "Social gathering"
      - "Information exchange"
      - "Informal deals"
      - "Entertainment"
    player_relevance:
      - "Hear rumors"
      - "Meet contacts"
      - "Drink and eat cheaply"
      - "Find work (less formal)"

  the_market_areas:
    harbor_market:
      goods: "Imports, exotic items"
      timing: "All day, busiest morning"
    temple_courtyard:
      goods: "Festival days only, special items"
      timing: "Festival calendars"
    street_vendors:
      goods: "Food, basic necessities"
      timing: "Throughout day"

  the_elders_bench:
    description: "Informal council of respected old men"
    location: "Temple courtyard, shade area"
    function:
      - "Memory of old ways"
      - "Dispute mediation"
      - "Wisdom and advice"
    player_relevance:
      - "Innovation clues from memories"
      - "Reputation in community"
      - "Learn traditions"
```

---

## 7. Currency & Commerce

### 7.1 The Monetary System

```yaml
currency_system:
  principle: "No coins (invented ~600 BCE). Commodity money and credit."

  units_of_account:
    shekel:
      definition: "Unit of weight (~8.3 grams)"
      precious_metal: "Silver shekel = 8.3g silver"
      grain_equivalent: "1 silver shekel = ~300 liters barley"
      usage: "Large transactions, record keeping"
      note: "Rarely physically exchanged"

    mina:
      definition: "60 shekels"
      usage: "Very large transactions, temple accounts"

    smaller_units:
      se: "1/180 shekel (single barley grain weight)"
      gin: "1/60 shekel"

  daily_currency:
    barley:
      form: "Physical grain"
      usage: "Daily purchases, wages"
      rate: "1 sila (liter) = basic daily food"
      worker_wage: "~2 sila/day for unskilled labor"

    dates:
      usage: "Secondary food currency"

    oil:
      form: "Sesame or fish oil"
      usage: "Lighting, cooking, medicine"

    wool:
      usage: "Clothing production, trade"
```

### 7.2 Credit & Contracts

```yaml
credit_system:
  clay_tokens:
    description: "Small shaped clay pieces representing goods"
    types:
      - "Cone = small measure of grain"
      - "Sphere = large measure of grain"
      - "Disk = animal (sheep/goat)"
      - "Cylinder = labor day"
    usage: "Counting, contracts, debts"

  bullae:
    description: "Hollow clay balls containing tokens"
    function: "Sealed contracts"
    process:
      1: "Tokens placed inside wet clay ball"
      2: "Ball sealed with cylinder seal impressions"
      3: "Breaking ball reveals true count"
    significance: "Proto-writing (led to cuneiform)"

  temple_credit:
    loans:
      agricultural: "Seed grain loaned, repaid with harvest + 33%"
      commercial: "Silver loaned, repaid with 20% interest"
      emergency: "Food loans during shortage"

    deposits:
      function: "Store grain safely in temple"
      benefit: "Protection from theft, pests"
      cost: "Small percentage to temple"

  player_wallet:
    display:
      - "Barley: 45 sila"
      - "Silver: 0.3 shekels"
      - "Dates: 12 sila"
      - "Temple Credit: 100 sila (owed to you)"
    note: "Physical items vs temple-recorded credit"
```

### 7.3 Prices & Wages

```yaml
price_list:
  # All in sila of barley unless noted

  food:
    barley_1_sila: "1 (base unit)"
    bread_loaf: "0.5"
    fish_fresh: "2"
    fish_dried: "1"
    dates_1_sila: "1.5"
    meat_portion: "5"
    beer_jug: "2"
    onions_bundle: "0.3"

  basic_goods:
    reed_mat: "3"
    clay_pot_small: "5"
    clay_pot_large: "15"
    rope_length: "2"
    oil_lamp: "8"
    oil_for_lamp: "3"

  tools:
    wooden_hoe: "20"
    copper_knife: "50"
    copper_axe: "100"
    fishing_net: "30"

  clothing:
    simple_garment: "30"
    quality_garment: "100"
    sandals: "15"

  services:
    ferryman: "0.5"
    porter: "2/load"
    scribe_letter: "5"
    healer_visit: "10-50"

wages:
  unskilled_laborer: "2 sila/day"
  skilled_craftsman: "5 sila/day"
  scribe: "8 sila/day"
  master_craftsman: "10+ sila/day"

  temple_rations:
    male_worker: "60 sila/month"
    female_worker: "30 sila/month"
    child: "15 sila/month"
```

---

## 8. Streets & Infrastructure

### 8.1 Street System

```yaml
street_types:
  processional_way:
    width: "4-5 meters"
    surface: "Fired brick in bitumen"
    drainage: "Channels to sides"
    lighting: "None (daytime use)"
    maintenance: "Temple responsibility"

  main_streets:
    width: "2-3 meters"
    surface: "Packed earth, sometimes gravel"
    drainage: "Central depression, runoff to canals"
    encroachment: "Constant battle with building expansion"

  residential_lanes:
    width: "1-2 meters (sometimes less)"
    surface: "Packed earth and debris"
    drainage: "Poor, water collects"
    waste: "Often used as dump"

  dead_ends:
    description: "Common, organic growth pattern"
    function: "Semi-private neighborhood spaces"
    note: "Can be confusing for newcomers"

  no_grid:
    description: "Streets follow no planned pattern"
    reason: "Organic growth over centuries"
    navigation: "Landmarks, not street names"
```

### 8.2 Water Systems

```yaml
water_infrastructure:
  canals:
    main_canal:
      source: "Euphrates River"
      width: "10-15 meters"
      function: "Navigation, irrigation supply"

    secondary_canals:
      width: "3-5 meters"
      function: "Distribution to fields"

    city_channels:
      width: "1-2 meters"
      function: "Bring water inside walls"
      maintenance: "Constant dredging needed"

  wells:
    public_wells:
      location: "Temple courtyard, major intersections"
      access: "Free, communal"
      quality: "Variable, deeper = cleaner"

    private_wells:
      location: "Elite home courtyards"
      access: "Owner only"
      prestige: "Sign of wealth"

  water_lifting:
    method: "Bucket on rope"
    innovation_coming: "Shaduf (counterweight lever)"
    canal_access: "Steps down to water level"
```

### 8.3 Sanitation

```yaml
sanitation:
  waste_disposal:
    human_waste:
      - "Pots/jars in home"
      - "Emptied into streets or pits"
      - "Gradual accumulation raises street level"

    household_waste:
      - "Ash, broken pottery, food scraps"
      - "Dumped in streets"
      - "Pigs and dogs as cleaners"

    industrial_waste:
      - "Pottery kilns: ash, broken pieces"
      - "Metalworking: slag, charcoal"
      - "Tanning: extremely smelly waste"

  periodic_cleaning:
    - "Temple-organized cleanups before festivals"
    - "Individual home-front maintenance expected"
    - "Debris gradually compacted into floor"

  health_consequences:
    - "Disease common (player health risk)"
    - "Flies and pests constant"
    - "Smell varies by neighborhood"

  gameplay_note: |
    The sanitation system creates organic gameplay:
    - Disease events
    - Innovation opportunity (sewage system later)
    - Class distinction visible in cleanliness
```

---

## 9. The Harbor

### 9.1 Physical Layout

```yaml
harbor_layout:
  main_quay:
    construction: "Mud-brick base, wooden deck"
    length: "~100 meters"
    features:
      - "Mooring posts"
      - "Steps to water"
      - "Crane/hoist for heavy cargo"
      - "Harbor master's station"

  boat_yard:
    location: "West of main quay"
    activities:
      - "Reed boat construction"
      - "Boat repair"
      - "Bitumen application"
    smells: "Hot bitumen, wet reeds"

  fish_market:
    location: "East of main quay"
    timing: "Dawn to mid-morning"
    features:
      - "Stone/brick slabs for display"
      - "Scales for weighing"
      - "Constant haggling"

  foreign_quarter:
    location: "Behind fish market"
    features:
      - "Traveler lodgings"
      - "Exotic goods storage"
      - "Different cooking smells"
      - "Foreign languages heard"
```

### 9.2 Boats & Vessels

```yaml
boat_types:
  guffa:
    description: "Round coracle, reed frame, hide cover"
    size: "1-2 person"
    use: "River crossing, fishing"
    construction: "Simple, player can learn"

  reed_raft:
    description: "Bundled reeds, flat platform"
    size: "Variable"
    use: "Cargo, short distances"
    construction: "Basic, player can learn"

  reed_boat:
    description: "Shaped reed bundle hull"
    size: "4-10 people or equivalent cargo"
    use: "River travel, fishing"
    construction: "Skilled, apprenticeship needed"

  wooden_cargo_boat:
    description: "Plank construction, rare"
    size: "Large cargo capacity"
    use: "Long-distance trade"
    construction: "Master shipwright only"
    note: "Wood is imported, expensive"
```

### 9.3 Trade Connections

```yaml
trade_routes:
  river_routes:
    upstream:
      destinations: "Sippar, Kish, Akkad region"
      goods_out: "Fish, reeds, marshland products"
      goods_in: "Timber, stone, mountain products"
      travel_time: "Days to weeks"

    downstream:
      destinations: "Persian Gulf, open sea"
      goods_out: "Grain, textiles, dates"
      goods_in: "Copper, stone, exotics"

  sea_routes:
    dilmun:
      modern_location: "Bahrain"
      goods: "Copper, pearls, exotic woods"
      merchants: "Regular visitors"
      significance: "Major trade partner"

    magan:
      modern_location: "Oman"
      goods: "Copper, diorite stone"
      merchants: "Occasional"

    meluhha:
      modern_location: "Indus Valley"
      goods: "Carnelian, ivory, exotic items"
      merchants: "Rare, prestigious"
      significance: "Source of mystery and rumors"
```

---

## 10. Daily Life & Atmosphere

### 10.1 The Daily Cycle

```yaml
daily_cycle:
  dawn:
    sky: "Orange-pink, cool air"
    activities:
      - "Temple rituals begin"
      - "Farmers leave for fields"
      - "Fishermen return from night fishing"
      - "Markets open"
    sounds: "Temple drums, animal noises, waking voices"
    atmosphere: "Energetic, fresh"

  morning:
    sky: "Bright, warming rapidly"
    activities:
      - "Peak market activity"
      - "Crafts workshops busy"
      - "Harbor loading/unloading"
      - "Scribes at work"
    sounds: "Haggling, hammering, loom clacking"
    atmosphere: "Busy, productive"

  midday:
    sky: "Harsh, white-hot"
    activities:
      - "Shade-seeking"
      - "Light meal"
      - "Indoor work continues"
      - "Outdoor activity slows"
    sounds: "Quieter, insects buzzing"
    atmosphere: "Oppressive heat, slower pace"

  afternoon:
    sky: "Still bright, slightly less intense"
    activities:
      - "Work resumes"
      - "Farmers begin return"
      - "Beer houses fill"
      - "Social visits"
    sounds: "Activity returning"
    atmosphere: "Second wind, anticipation of evening"

  dusk:
    sky: "Red-orange, cooling"
    activities:
      - "Farmers return through gates"
      - "Evening meal preparation"
      - "Markets close"
      - "Temple evening rituals"
    sounds: "Cooking fires, evening prayers, children playing"
    atmosphere: "Relief, domesticity"

  night:
    sky: "Deep blue to black, stars brilliant"
    activities:
      - "Eating main meal"
      - "Storytelling"
      - "Sleep (roof in summer, inside in winter)"
      - "Night fishermen depart"
    sounds: "Distant voices, dogs, nocturnal animals"
    atmosphere: "Dark, mostly quiet, some danger"
    note: "Few venture out, streets very dark"
```

### 10.2 The Seasonal Cycle

```yaml
seasonal_cycle:
  spring:
    months: "March-May"
    weather: "Warming, pleasant"
    activities:
      - "Barley harvest"
      - "Major agricultural work"
      - "Trade season begins"
    events:
      - "New Year Festival (Akitu)"
      - "Harvest celebrations"
    player_note: "Best time for outdoor activities"

  summer:
    months: "June-August"
    weather: "Extremely hot, 40-50°C"
    activities:
      - "Minimal outdoor work midday"
      - "Night activity increases"
      - "River level lowest"
    challenges:
      - "Heat exhaustion risk"
      - "Water scarcity"
      - "Stored grain pest risk"
    player_note: "Plan around heat, carry water"

  autumn:
    months: "September-November"
    weather: "Cooling, pleasant"
    activities:
      - "Date harvest"
      - "Plowing and planting"
      - "Trade season continues"
    events:
      - "Date festival"
    player_note: "Second good season"

  winter:
    months: "December-February"
    weather: "Cool, occasional rain"
    activities:
      - "Wheat planting"
      - "Indoor crafts"
      - "Repair work"
    challenges:
      - "Mud streets difficult"
      - "Cold nights (no heating except fire)"
    player_note: "Rain affects travel"

  flood_season:
    timing: "Late spring (variable)"
    cause: "Snowmelt from northern mountains"
    effects:
      - "River rises dramatically"
      - "Can flood fields and city"
      - "Irrigation canals fill"
    gameplay: "Major event, innovation opportunity"
```

### 10.3 Food & Meals

```yaml
food_culture:
  staples:
    grains:
      - "Barley (primary, makes bread and beer)"
      - "Wheat (secondary, finer bread)"
    vegetables:
      - "Onions"
      - "Garlic"
      - "Leeks"
      - "Lentils"
      - "Chickpeas"
    fruits:
      - "Dates (extremely important)"
      - "Figs"
      - "Pomegranates"
    protein:
      - "Fish (common, dried or fresh)"
      - "Mutton (occasional)"
      - "Beef (rare, usually sacrifice)"
      - "Fowl (ducks, geese)"
    fats:
      - "Sesame oil"
      - "Fish oil"
      - "Animal fat (rare)"

  meals:
    breakfast: "Light, bread and dates"
    midday: "Light, bread, onions, beer"
    evening: "Main meal, stew or fish, bread, beer"

  beer:
    description: "Not modern beer - thick, nutritious"
    consumption: "Daily, all ages, safer than water"
    production: "Important craft, often by women"
    varieties: "Multiple types, some quite strong"

  player_mechanics:
    hunger: "Depletes over time"
    thirst: "Depletes faster in heat"
    nutrition: "Variety improves health"
    cooking: "Skill can be developed"
```

---

## 11. Sounds & Ambiance

### 11.1 Soundscape by Location

```yaml
soundscape:
  temple_area:
    constant:
      - "Distant chanting from temple"
      - "Bells or clappers at ritual times"
      - "Footsteps on brick"
    occasional:
      - "Priests intoning prayers"
      - "Animal bleating (sacrifice)"
      - "Drums during ceremonies"

  harbor:
    constant:
      - "Water lapping"
      - "Creaking of boats"
      - "Seabirds calling"
    occasional:
      - "Shouting commands"
      - "Cargo being loaded"
      - "Foreign languages"

  artisan_quarter:
    constant:
      - "Hammering (metal, wood)"
      - "Loom clacking"
      - "Potter's wheel spinning"
    occasional:
      - "Fire roaring (kiln, forge)"
      - "Apprentices being scolded"
      - "Haggling over prices"

  commoner_quarter:
    constant:
      - "Children playing"
      - "Dogs barking"
      - "Cooking sounds"
    occasional:
      - "Arguments"
      - "Babies crying"
      - "Street vendor calls"

  markets:
    constant:
      - "Haggling voices"
      - "Animals (donkeys, goats)"
      - "Coins/weights clinking"
    occasional:
      - "Announcements"
      - "Disputes"

  outside_walls:
    fields:
      - "Wind in grain"
      - "Irrigation water"
      - "Oxen/workers"
    marshes:
      - "Reeds rustling"
      - "Water birds"
      - "Frogs at night"
      - "Insects constantly"
```

### 11.2 Music & Entertainment

```yaml
music:
  instruments:
    lyres: "Stringed, for formal occasions"
    drums: "Various sizes, ritual and entertainment"
    flutes: "Reed, common"
    clappers: "Wood or bone, rhythm"

  occasions:
    temple_rituals: "Formal music, hymns"
    festivals: "Loud, celebratory"
    beer_houses: "Informal singing, stories"
    funerals: "Laments, wailing"

  stories_and_tales:
    epic_tales:
      - "Stories of the gods"
      - "Creation myths"
      - "Flood story"
    entertainment:
      - "Trickster tales"
      - "Animal fables"
      - "Local legends"

  player_experience:
    - "Hear fragments of myths (lore clues)"
    - "Learn songs (social bonding)"
    - "Attend performances"
```

---

## 12. Weather & Environment

### 12.1 Climate

```yaml
climate:
  classification: "Hot desert (BWh), but wetter 7000 years ago"

  temperature:
    summer_high: "40-50°C (104-122°F)"
    summer_low: "25-30°C"
    winter_high: "15-20°C"
    winter_low: "5-10°C"
    note: "Game exaggerates extremes for gameplay"

  precipitation:
    annual: "~150mm (in ancient times, possibly more)"
    pattern: "Winter rains, dry summer"
    flooding: "Spring river flood from mountain snowmelt"

  humidity:
    summer: "Low in city, high near marshes"
    winter: "Moderate"
    morning: "Fog possible near water"
```

### 12.2 Weather Events

```yaml
weather_events:
  dust_storm:
    frequency: "Occasional, more in spring/autumn"
    effects:
      - "Visibility reduced drastically"
      - "Outdoor activity impossible"
      - "Health effect if exposed"
      - "Some damage to structures"
    gameplay: "Shelter required, time passes, thief opportunity"

  heat_wave:
    frequency: "Summer"
    effects:
      - "Faster thirst depletion"
      - "Stamina reduced"
      - "NPCs seek shade"
      - "Night activity increases"
    gameplay: "Water critical, timing matters"

  flood:
    frequency: "Annual, variable intensity"
    warning: "River rising over days"
    effects:
      - "Fields flooded (good or bad)"
      - "City can flood if severe"
      - "Death risk if caught"
    gameplay: "Major event, innovation trigger"

  rain:
    frequency: "Winter months"
    effects:
      - "Streets become muddy"
      - "Travel difficult"
      - "Crops benefit"
      - "Mud brick erosion"
    gameplay: "Movement penalty, indoor work favored"
```

### 12.3 Flora & Fauna

```yaml
flora:
  cultivated:
    date_palm: "Ubiquitous, food/construction/shade"
    barley: "Primary crop"
    wheat: "Secondary crop"
    vegetables: "Gardens near water"
    flax: "For linen"

  wild:
    reeds: "Massive reed beds, construction material"
    papyrus: "In marshes"
    tamarisk: "Shade tree"
    willow: "Along water"

fauna:
  domestic:
    sheep: "Wool, meat, milk"
    goats: "Milk, meat, hardy"
    cattle: "Draft animals, prestige, sacrifice"
    pigs: "Meat, scavengers"
    donkeys: "Transport"
    dogs: "Guarding, hunting, scavenging"

  wild:
    fish: "Carp, catfish, many species"
    birds: "Ducks, geese, herons, pelicans"
    gazelle: "Hunted for meat"
    wild_boar: "In marshes, dangerous"
    lions: "Rare, in outlying areas, dangerous"
    snakes: "Various, some venomous"
    scorpions: "Common, dangerous"
    insects: "Flies, mosquitoes, locusts"

  mythological_hints:
    "strange_fish": "In the Abzu... different"
    "marsh_lights": "Not always explained"
    "large_shadows": "In deep water..."
```

---

## 13. NPC Population

### 13.1 Population Distribution

```yaml
population:
  total: "~3,000-4,000 at game start"

  by_class:
    elite: "5% (~150-200)"
    artisan: "20% (~600-800)"
    commoner: "60% (~1,800-2,400)"
    servant_slave: "15% (~450-600)"

  by_gender:
    male: "~50%"
    female: "~50%"
    note: "Women visible in most roles"

  by_age:
    children: "30% (high birth rate, high mortality)"
    adult: "60%"
    elderly: "10% (rare to reach old age)"
```

### 13.2 Key NPC Types

```yaml
npc_types:
  authority_figures:
    en_priest:
      role: "High priest, city leader"
      location: "Temple"
      player_interaction: "Rare, quest-giver"

    temple_administrators:
      role: "Run daily temple operations"
      location: "Temple complex"
      player_interaction: "Loans, employment, disputes"

    harbor_master:
      role: "Oversee trade, customs"
      location: "Harbor"
      player_interaction: "Trade permits, information"

  knowledge_holders:
    senior_scribes:
      role: "Record keepers, teachers"
      location: "Scribal school"
      player_interaction: "Writing instruction, innovation clues"

    elder_craftsmen:
      role: "Master artisans"
      location: "Workshops"
      player_interaction: "Apprenticeship, innovation clues"

    temple_diviners:
      role: "Interpret omens, contact divine"
      location: "Temple"
      player_interaction: "Prophecies, communion assistance"

  daily_life:
    merchants:
      local: "Shop owners, market vendors"
      foreign: "Traders from Dilmun, distant lands"
      player_interaction: "Buy/sell, rumors, quests"

    craftsmen:
      types: "Potter, weaver, smith, carpenter, etc."
      player_interaction: "Employment, apprenticeship, purchase"

    farmers:
      location: "Fields by day, commoner quarter by night"
      player_interaction: "Information, labor exchange"

    fishermen:
      location: "Harbor, marshes"
      player_interaction: "Boat access, marsh knowledge"

  special:
    beer_house_keeper:
      role: "Runs tavern (usually women)"
      player_interaction: "Rumors, social hub, lodging"

    healer:
      role: "Treat illness (ritual + practical)"
      player_interaction: "Health restoration, rare knowledge"

    traveler:
      role: "Visitors from other cities/lands"
      player_interaction: "News, exotic goods, map information"

    the_elders:
      role: "Old men with memories"
      player_interaction: "Innovation clues, history, warnings"
```

### 13.3 NPC Schedules

```yaml
npc_schedules:
  farmer:
    dawn: "Leave through east gate"
    morning: "Work in fields"
    midday: "Rest in field shade"
    afternoon: "Continue work"
    dusk: "Return through gate"
    evening: "Home, meal, beer house"
    night: "Sleep"

  craftsman:
    dawn: "Open workshop"
    morning: "Primary production"
    midday: "Light meal, rest"
    afternoon: "Production, sales"
    dusk: "Close workshop"
    evening: "Family, beer house"
    night: "Sleep"

  merchant:
    dawn: "Open shop or travel to market"
    morning: "Peak selling"
    midday: "Slower"
    afternoon: "Continued trade"
    dusk: "Close, count earnings"
    evening: "Business meetings, beer house"
    night: "Sleep"

  priest:
    dawn: "Morning rituals"
    morning: "Temple duties"
    midday: "Midday rituals"
    afternoon: "Administrative work"
    dusk: "Evening rituals"
    evening: "Study, rest"
    night: "Some maintain night vigil"
```

---

## 14. Player Starting Experience

### 14.1 The Drop

```yaml
player_drop:
  location: "Temple courtyard, edge of crowd"
  time: "Dawn, cool air"
  context: "Morning gathering, daily announcements"

  first_sensations:
    visual:
      - "White temple rising before you"
      - "Mud-brick buildings surrounding"
      - "Crowd of people in simple garments"
      - "Smoke rising from cooking fires"

    audio:
      - "Priest's voice echoing"
      - "Crowd murmuring"
      - "Distant animal sounds"
      - "Water somewhere nearby"

    physical:
      - "Hunger beginning (85%)"
      - "Thirst (90%)"
      - "Morning chill fading"

  immediate_situation:
    - "Elder approaches (tutorial NPC)"
    - "Water level mentioned (flood coming)"
    - "Opportunity to establish yourself"
```

### 14.2 First Decisions

```yaml
first_decisions:
  identity:
    question: "Who are you?"
    options:
      - "Local recently come of age"
      - "Refugee from failed settlement"
      - "Trader's assistant, separated"
    impact: "Starting relationships, knowledge"

  skills:
    question: "What do you know?"
    options:
      - "Farming basics"
      - "Fishing basics"
      - "Craft basics"
    impact: "Starting skills, quest opportunities"

  residence:
    question: "Where will you sleep tonight?"
    options:
      - "Temple courtyard (free, exposed)"
      - "Commoner quarter (cheap, crowded)"
      - "Work for lodging (task required)"
    impact: "Starting resources, social position"
```

### 14.3 Tutorial Flow

```yaml
tutorial_elements:
  survival_basics:
    trigger: "Hunger/thirst meters"
    lesson: "Find food, find water"
    location: "Market, well"

  social_basics:
    trigger: "NPC interaction"
    lesson: "Talk to people, learn things"
    location: "Elder NPC, beer house"

  economic_basics:
    trigger: "Need to purchase something"
    lesson: "Barter, work for pay"
    location: "Workshop, harbor"

  threat_introduction:
    trigger: "Elder mentions rising water"
    lesson: "The world has dangers, time pressure"
    countdown: "Flood timer begins (14 days)"

  innovation_teaser:
    trigger: "Observe failed attempt by NPC"
    lesson: "Things can be improved, but how?"
    hook: "Canal mentioned but not working"
```

---

## 15. Implementation Notes

### 15.1 MVP Scope

```yaml
mvp_eridu:
  included:
    zones:
      - "Temple complex (simplified)"
      - "Harbor district"
      - "One artisan quarter"
      - "Commoner quarter"
      - "Fields (simplified)"

    npcs:
      - "20-30 unique NPCs with schedules"
      - "Background crowd NPCs (non-interactive)"

    buildings:
      - "Temple (exterior + courtyard)"
      - "3-5 enterable buildings per zone"

    features:
      - "Day/night cycle"
      - "Basic weather (heat, occasional rain)"
      - "Market system"
      - "Basic crime/guards"

  deferred:
    - "Full marsh settlement"
    - "All buildings enterable"
    - "Complete NPC population"
    - "Full seasonal cycle"
    - "All weather events"
```

### 15.2 Performance Considerations

```yaml
performance:
  npc_simulation:
    active: "NPCs in player's zone"
    simulated: "NPCs in other zones (simplified schedules)"
    spawned: "Background NPCs as needed"

  building_interiors:
    loaded: "Only when entered"
    persistent: "State saved when left"

  crowd_density:
    market_morning: "High (performance test)"
    night: "Low"
    adaptive: "Based on player hardware"
```

### 15.3 Art Direction Notes

```yaml
art_direction:
  style: "Realistic but stylized"
  palette: "Earth tones with accent colors"
  lighting: "Dramatic, time-of-day dependent"

  reference_images:
    - "Ma'dan reed villages (architecture)"
    - "Yazd, Iran (urban density)"
    - "Museum reconstructions of Sumerian buildings"
    - "Archaeological site photos (Tell Abu Shahrain)"

  atmosphere_keywords:
    - "Ancient"
    - "Alive"
    - "Harsh but beautiful"
    - "Water-touched"
    - "Mystery beneath surface"
```

---

## Appendix: Quick Reference

### Zone Summary

| Zone | Population | Wealth | Safety | Innovation Relevance |
|------|------------|--------|--------|---------------------|
| Temple Complex | Priests, officials | High | Very Safe | Knowledge, quests |
| Elite Quarter | Wealthy | High | Safe | Patrons, resources |
| Artisan Quarter | Craftsmen | Medium | Moderate | Skills, tools |
| Commoner Quarter | Workers | Low | Less Safe | Labor, rumors |
| Harbor | Mixed | Varied | Moderate | Trade, travel |
| Fields | Farmers | Low | Moderate | Agriculture |
| Marshes | Fisher folk | Low | Variable | Old knowledge |

### Daily Schedule Quick Reference

| Time | Where to Find People | Best Activities |
|------|---------------------|-----------------|
| Dawn | Gates, temple, harbor | Meet NPCs, buy fish |
| Morning | Markets, workshops | Trade, learn, work |
| Midday | Shade, indoors | Rest, temple visits |
| Afternoon | Workshops, fields | Work, travel |
| Dusk | Gates, beer houses | Social, rumors |
| Night | Indoors, temple | Sleep, night quests |

---

*"The first city was not built. It grew, like reeds from the water, like knowledge from ignorance. And at its heart was the temple, where the god who loved us most kept watch over the waters."*
