# World Lore: Mesopotamia & The Anunnaki Mystery

> "The gods did not create us to worship them. They created us to remember."

## Table of Contents

1. [Design Philosophy](#1-design-philosophy)
2. [The Map System](#2-the-map-system)
3. [The City-States](#3-the-city-states)
4. [Fog of War & Discovery](#4-fog-of-war--discovery)
5. [The Sumerian Pantheon](#5-the-sumerian-pantheon)
6. [The Anunnaki Mystery Layer](#6-the-anunnaki-mystery-layer)
7. [The Seven Sages (Apkallu)](#7-the-seven-sages-apkallu)
8. [The Divine ME](#8-the-divine-me)
9. [Sacred Sites & Hidden Locations](#9-sacred-sites--hidden-locations)
10. [The Witness System Integration](#10-the-witness-system-integration)
11. [Training Data Value](#11-training-data-value)
12. [Implementation Notes](#12-implementation-notes)

---

## 1. Design Philosophy

### 1.1 Layers of Truth

The world of The Analog Economy operates on multiple layers of understanding:

```
LAYER 1: SURFACE (What everyone knows)
├── "The gods live in the temples"
├── "The priests speak for the gods"
├── "The flood comes when Enlil is angry"
└── Common knowledge, safe, expected

LAYER 2: LEARNED (What scholars discover)
├── "The gods came from the heavens"
├── "They brought the ME (divine knowledge)"
├── "The Apkallu taught the first arts"
└── Requires study, relationships, effort

LAYER 3: HIDDEN (What seekers find)
├── "The gods are not what they seem"
├── "There are places older than Eridu"
├── "The tablets speak of other worlds"
└── Dangerous knowledge, Witness cost

LAYER 4: FORBIDDEN (What changes everything)
├── [REDACTED - discovered through play]
├── [REDACTED - discovered through play]
├── [REDACTED - discovered through play]
└── True nature of the Anunnaki
```

### 1.2 The Sitchin Inspiration

We draw from Zecharia Sitchin's interpretations not as literal truth, but as **narrative fuel**:

- The Anunnaki as "those who from heaven came"
- Nibiru as a mystery, not a certainty
- The creation of humanity as labor force
- The "me" as technological/knowledge packages
- The Apkallu as hybrid teacher-beings

**Key Principle:** The game never confirms or denies. It presents mysteries. Players interpret.

### 1.3 Why This Matters

```yaml
design_goals:
  immersion:
    - "Ancient people believed the gods were real"
    - "Players should feel that weight"
    - "The unexplained should feel unexplainable"

  discovery_reward:
    - "Curious players find more"
    - "Deep lore rewards exploration"
    - "Secrets feel earned, not given"

  training_data:
    - "How do humans respond to mystery?"
    - "What drives investigation vs acceptance?"
    - "How does belief affect behavior?"
```

---

## 2. The Map System

### 2.1 The World Map

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│                              CASPIAN                                │
│                                SEA                                  │
│                                                                     │
│    ════╗                                                            │
│        ║ HABOR                                                      │
│  ╔═════╝     ┌───────────────────────────────────────────┐         │
│  ║           │  MOUNTAIN REGIONS (unexplored at start)   │         │
│  ║  MARI     └───────────────────────────────────────────┘         │
│  ║    ●                                                             │
│  ║         ● ASSUR                                                  │
│  ╚══════════════════════════════════════════╗                      │
│          EUPHRATES                          ║ TIGRIS               │
│                    ● ESHNUNNA              ║                       │
│              ● SIPPAR                      ║                       │
│                         ● KISH            ║  ● SUSA               │
│           ● BABYLON          ● NIPPUR    ║                        │
│                    ● MARAD              ║                          │
│                           ● URUK    ● LAGASH                       │
│                              ● LARSA                               │
│                                  ● UR                              │
│                                      ● ERIDU  ←── [YOU START HERE] │
│                                                                     │
│  ═══════════════════════════════════════════════════════════════   │
│                        PERSIAN GULF                                 │
│                                                                     │
│  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │
│                           DESERT                                    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.2 Scale & Travel

```yaml
world_scale:
  map_size: "Approximately 800km x 600km"

  travel_times:
    walking:
      speed: "4 km/hour (game time)"
      eridu_to_ur: "~2 hours"
      eridu_to_uruk: "~6 hours"
      eridu_to_babylon: "~12 hours"

    boat_river:
      speed: "8 km/hour downstream, 3 km/hour upstream"
      primary_routes: ["Euphrates", "Tigris"]

    donkey_cart:
      speed: "6 km/hour"
      requires: "Wheel innovation or purchase"

    ox_cart:
      speed: "4 km/hour"
      capacity: "Heavy loads"

  time_compression:
    ratio: "1 real hour = 4 game hours"
    day_cycle: "6 real hours = 1 game day"
```

---

## 3. The City-States

### 3.1 City Timeline & Peaks

Each city rises and falls. The game reflects this dynamically:

```yaml
city_states:
  eridu:
    peak: "5400-4900 BCE"
    status_at_4500: "Established, modest"
    patron_deity: "Enki"
    specialty: "Water wisdom, first temple"
    starting_city: true

  ur:
    peak: "3500-3000 BCE"
    status_at_4500: "Small settlement"
    patron_deity: "Nanna (Moon)"
    specialty: "Trade, ziggurat"
    unlocks_when: "Population 500+"

  uruk:
    peak: "3500-3000 BCE"
    status_at_4500: "Growing village"
    patron_deity: "Inanna"
    specialty: "Writing, administration"
    unlocks_when: "Writing innovation achieved"

  nippur:
    peak: "2100-1763 BCE"
    status_at_4500: "Sacred site only"
    patron_deity: "Enlil"
    specialty: "Religious center, scribal schools"
    unlocks_when: "Temple reputation 50+"

  babylon:
    peak: "1792-1750 BCE (Hammurabi)"
    status_at_4500: "Does not exist"
    patron_deity: "Marduk"
    specialty: "Law, empire"
    unlocks_when: "Era progression (later timeline)"

  lagash:
    peak: "2500-2300 BCE"
    status_at_4500: "Tribal territory"
    patron_deity: "Ningirsu"
    specialty: "Military, agriculture"
    unlocks_when: "Conflict resolution (war or diplomacy)"

  susa:
    peak: "3400-639 BCE"
    status_at_4500: "Independent Elamite settlement"
    patron_deity: "Inshushinak"
    specialty: "Foreign trade, different culture"
    unlocks_when: "Trade route established"
    note: "Non-Sumerian, different customs"
```

### 3.2 City Discovery

Cities are not visible on the map until discovered:

```yaml
discovery_methods:
  eridu:
    method: "Starting location"
    visibility: "Full"

  nearby_cities:  # Ur, Larsa
    method: "Automatic after 3 game days"
    visibility: "Name and direction only"
    full_reveal: "Visit or detailed traveler info"

  distant_cities:  # Uruk, Nippur, Kish
    method: "Traveler tales, merchant routes"
    visibility: "Rumor (approximate location)"
    full_reveal: "Visit personally"

  far_cities:  # Assur, Mari, Susa
    method: "Rare travelers, expedition"
    visibility: "Legend only"
    full_reveal: "Major expedition or quest"

  hidden_locations:  # Anunnaki sites
    method: "Specific clues, artifacts, visions"
    visibility: "Never on normal map"
    full_reveal: "Only through discovery"
```

---

## 4. Fog of War & Discovery

### 4.1 The Fog System

```yaml
fog_of_war:
  initial_state:
    visible: "Eridu and immediate surroundings (5km radius)"
    fog: "Everything else"
    hints: "River directions, general terrain"

  revelation_methods:
    exploration:
      trigger: "Player physically visits"
      radius: "500m around player"
      permanence: "Permanent"

    observation:
      trigger: "Climb height, use observation point"
      radius: "2km in direction viewed"
      permanence: "Permanent"

    traveler_tales:
      trigger: "NPC shares information"
      effect: "Adds marker (uncertain location)"
      permanence: "Marker only, not terrain"
      accuracy: "80% accurate placement"

    maps_purchased:
      trigger: "Buy map from merchant"
      effect: "Reveals trade routes"
      permanence: "Permanent for owned map"
      note: "Maps can be wrong or outdated"

    divine_vision:
      trigger: "Temple ritual, Apkallu encounter"
      effect: "Reveals specific location"
      permanence: "Permanent"
      cost: "Witness points or offering"

  fog_types:
    unknown: "Black - never seen"
    rumored: "Dark gray with ? marker"
    mapped: "Gray - seen on map, not visited"
    explored: "Full visibility"
    changed: "Area has changed since last visit"
```

### 4.2 Map Interface

```
┌─────────────────────────────────────────────────────────────────────┐
│  [ZOOM: Regional]  [FILTER: Cities | Routes | Shrines | Resources]  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│                    ░░░░░░░░░░░░░░░░░░░░░░░                          │
│                 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                       │
│              ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                     │
│           ░░░░░░░░░░░░░░?░░░░░░░░░░░░░░░░░░░░░░░                    │
│           ░░░░░░░░░░(Uruk?)░░░░░░░░░░░░░░░░░░░░░                    │
│              ░░░░░░░░░░░░░░░░░▓▓▓▓▓░░░░░░░░░░░                      │
│                 ░░░░░░░░░░░▓▓▓▓▓▓▓▓▓░░░░░░░░                        │
│                    ░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░                          │
│                       ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                             │
│                     ▓▓▓▓▓●▓▓▓▓▓▓▓▓▓▓▓▓▓▓                            │
│                    ▓▓▓▓ Ur ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                           │
│                   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                          │
│                  ████████████████████████████                       │
│                 ████████●█████████████████████                      │
│                █████ ERIDU ██████████████████                       │
│               █████(You are here)█████████████                      │
│                ═══════════════════════════════                      │
│                        PERSIAN GULF                                 │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│  Legend: █ Explored  ▓ Mapped  ░ Unknown  ● City  ? Rumored        │
│  Distance to Ur: ~15km (3-4 hours walk)                            │
└─────────────────────────────────────────────────────────────────────┘
```

### 4.3 Discovery Rewards

```yaml
discovery_rewards:
  first_to_discover:
    new_city:
      reward: "25 Legacy Points + permanent Codex credit"
      title: "Discovered [City Name]"

    hidden_site:
      reward: "50 Legacy Points + unique knowledge"
      title: "Seeker of [Site Name]"

    anunnaki_location:
      reward: "100 Legacy Points + ??? (varies)"
      title: "Witness to [REDACTED]"

  personal_discovery:
    any_new_location:
      reward: "Map permanently updated"
      bonus: "5 Legacy Points first visit"
```

---

## 5. The Sumerian Pantheon

### 5.1 The Major Gods

```yaml
pantheon:
  anu:
    title: "Sky Father, King of the Gods"
    domain: "Heavens, kingship, authority"
    symbol: "Horned crown, winged disc"
    presence: "Rarely appears - too important"
    player_interaction:
      direct: "Almost never"
      indirect: "Through priests, visions, omens"
    mystery_layer: "The absent king - why doesn't he intervene?"

  enlil:
    title: "Lord of the Wind, Chief of Earth"
    domain: "Air, storms, earth, civilization"
    symbol: "Horned crown, mountain"
    presence: "Active through storms, disasters"
    player_interaction:
      direct: "Temple visions (rare)"
      indirect: "Priests of Nippur, weather events"
    mystery_layer: "Sent the flood - why destroy what was created?"
    temple_city: "Nippur"

  enki:
    title: "Lord of the Earth, God of Wisdom"
    domain: "Water, wisdom, creation, crafts"
    symbol: "Goatfish, flowing water"
    presence: "Active through knowledge, water"
    player_interaction:
      direct: "Possible at Eridu temple"
      indirect: "The Apkallu serve him"
    mystery_layer: "The creator who warns - whose side is he on?"
    temple_city: "Eridu"
    innovation_link: "Patron of all innovation quests"

  inanna:
    title: "Queen of Heaven, Goddess of Love and War"
    domain: "Love, war, fertility, Venus"
    symbol: "Eight-pointed star, lion"
    presence: "Active - loves attention"
    player_interaction:
      direct: "Temple rituals, battlefield"
      indirect: "Love/war events"
    mystery_layer: "Descended to underworld - what did she learn?"
    temple_city: "Uruk"

  utu_shamash:
    title: "Sun God, Lord of Justice"
    domain: "Sun, justice, truth, law"
    symbol: "Sun disc, saw-toothed blade"
    presence: "Daily cycle, judgment"
    player_interaction:
      direct: "Oaths, trials, moral crossroads"
      indirect: "Day/night cycle, truth revelation"
    mystery_layer: "Sees all - but tells only some"

  marduk:
    title: "Supreme God (later period)"
    domain: "Creation, order, Babylon"
    symbol: "Dragon, spade"
    presence: "Not yet risen at 4500 BCE"
    player_interaction:
      direct: "Only in later eras"
      indirect: "Prophecies of future greatness"
    mystery_layer: "The god who will replace the old ones"
```

### 5.2 Temple Mechanics

```yaml
temple_system:
  structure:
    - "Every major city has a central temple"
    - "Temple dedicated to patron deity"
    - "Ziggurat (raised platform) in larger cities"

  player_interactions:
    offerings:
      grain: "+5 favor per 10 units"
      livestock: "+15 favor per animal"
      craft_goods: "+10 favor per quality item"
      time_service: "+2 favor per hour worked"

    rituals:
      daily_prayer: "+1 favor (once per day)"
      festival_participation: "+20 favor (rare events)"
      major_sacrifice: "+50 favor (significant cost)"

    benefits_by_favor:
      0-25: "Can enter temple, basic blessings"
      25-50: "Can consult priests, minor divination"
      50-75: "Access to temple library, healing"
      75-100: "Private rituals, advanced divination"
      100+: "Direct communion attempts, inner sanctum"

  divine_communion:
    description: "Attempt to directly experience the god"
    requirement: "100+ favor, major offering, ritual preparation"
    outcomes:
      - "Vision (information about world/self)"
      - "Blessing (temporary stat boost)"
      - "Quest (divine mission with major reward)"
      - "Silence (nothing happens - try again)"
      - "Wrath (Witness damage, favor loss)"
    witness_cost: "10-30 Witness points regardless of outcome"
```

### 5.3 Divine Favor Consequences

```yaml
divine_favor:
  high_favor_effects:
    Enki:
      - "Innovation clues come easier"
      - "Apkallu more likely to appear"
      - "Water-related tasks easier"

    Enlil:
      - "Weather warnings"
      - "Authority over NPCs (leadership)"
      - "Storm protection"

    Inanna:
      - "Combat bonuses"
      - "Social/charm bonuses"
      - "Love/relationship luck"

    Utu:
      - "Truth detection (limited)"
      - "Legal disputes favor you"
      - "Hidden things revealed"

  low_favor_effects:
    - "Priests refuse service"
    - "Bad omens affect NPC behavior toward you"
    - "Divine 'tests' (random challenges)"

  opposing_favors:
    - "High Enki + Low Enlil = dangerous"
    - "Gods have their conflicts"
    - "Players can be caught between"
```

---

## 6. The Anunnaki Mystery Layer

### 6.1 The Core Mystery

```yaml
anunnaki_mystery:
  surface_narrative:
    - "The Anunnaki are the gods"
    - "They created humanity to serve them"
    - "They gave us civilization"

  discovered_narrative:
    - "The Anunnaki 'came from' somewhere"
    - "They needed workers for some task"
    - "They have... disagreements"
    - "Some wanted to destroy us, some to save us"

  deep_narrative:
    - "They are not what 'god' means to us"
    - "Their 'heaven' may be a place"
    - "Their 'creation' may be... modification"
    - "They may not be gone"

  forbidden_narrative:
    - "[DISCOVERED THROUGH PLAY]"
    - "[REQUIRES SIGNIFICANT WITNESS COST]"
    - "[CHANGES UNDERSTANDING OF THE GAME]"
```

### 6.2 Clue Types

```yaml
anunnaki_clues:
  tier_1_common:
    - "NPC mentions gods 'descending'"
    - "Temple art shows beings in strange craft"
    - "Creation myths speak of 'mixing'"
    - "The flood was deliberate"
    prevalence: "Available to anyone who asks"
    witness_cost: 0

  tier_2_uncommon:
    - "Tablets describing Nibiru (the crossing)"
    - "References to the Igigi (lesser gods/workers)"
    - "Descriptions of the Abzu (Enki's domain)"
    - "The Anunnaki had children with humans"
    prevalence: "Requires temple access, scholar NPCs"
    witness_cost: 0-5

  tier_3_rare:
    - "Artifacts that shouldn't exist"
    - "Structures with impossible precision"
    - "Apkallu direct testimony"
    - "Visions during communion"
    prevalence: "Dedicated search, high favor"
    witness_cost: 10-20

  tier_4_forbidden:
    - "Locations that predate Eridu"
    - "Devices that function without explanation"
    - "Direct witness to... something"
    prevalence: "Hidden sites, extreme dedication"
    witness_cost: 30-50+
```

### 6.3 The Central Questions

The game presents but never definitively answers:

```yaml
open_questions:
  origin:
    question: "Where did the Anunnaki come from?"
    hints:
      - "Heaven (AN = sky)"
      - "Nibiru (a crossing, a place)"
      - "Before the flood, before memory"
    answer: "[PLAYER INTERPRETATION]"

  nature:
    question: "What are the Anunnaki?"
    hints:
      - "Gods (divine beings)"
      - "Ancestors (advanced humans)"
      - "Others (non-human intelligence)"
    answer: "[PLAYER INTERPRETATION]"

  purpose:
    question: "Why did they create us?"
    hints:
      - "To serve (labor)"
      - "To replace (they were dying)"
      - "By accident (experiment gone right)"
    answer: "[PLAYER INTERPRETATION]"

  presence:
    question: "Are they still here?"
    hints:
      - "They left (after the flood)"
      - "They hide (in temples, in dreams)"
      - "They watch (from Nibiru, from heaven)"
    answer: "[PLAYER INTERPRETATION]"
```

---

## 7. The Seven Sages (Apkallu)

### 7.1 Who They Are

```yaml
apkallu:
  description: |
    The Apkallu are the Seven Sages sent by Enki to teach humanity
    the arts of civilization. They appeared before the flood and
    taught the antediluvian kings.

    In game terms: They are rare NPC encounters that can accelerate
    innovation learning - but at a cost.

  appearance:
    - "Part fish, part human (some depictions)"
    - "Winged beings with buckets and cones"
    - "Robed figures with inhuman features"
    - "Sometimes appear fully human"

  names_and_domains:
    uanna_adapa:
      domain: "All knowledge, the first sage"
      teaches: "Any Phase 1 innovation"
      rarity: "Extremely rare"

    uanduga:
      domain: "Water and channels"
      teaches: "Canal Irrigation, Sewage"
      rarity: "Rare near rivers"

    enmeduga:
      domain: "Good fortune, governance"
      teaches: "Coinage, Calendar"
      rarity: "Rare in temples"

    enmegalamma:
      domain: "Crafts and building"
      teaches: "Brick, Arch, Wheel"
      rarity: "Rare at construction sites"

    enmebulugga:
      domain: "Metallurgy"
      teaches: "Bronze, Iron, Steel"
      rarity: "Rare near forges"

    anenlilda:
      domain: "Writing and records"
      teaches: "Cuneiform, Alphabet"
      rarity: "Rare in scribal houses"

    utuabzu:
      domain: "The final sage, transformation"
      teaches: "[UNKNOWN]"
      rarity: "Almost never appears"
```

### 7.2 Encounter Mechanics

```yaml
apkallu_encounters:
  trigger_conditions:
    base_chance: "0.1% per game day in relevant location"
    modifiers:
      high_enki_favor: "+0.5%"
      innovation_struggle: "+0.3% (3+ failed attempts)"
      night_time: "+0.2%"
      near_water: "+0.2%"
      carrying_artifact: "+0.5%"
      witnessed_forbidden: "+1.0%"

    forced_encounters:
      - "Temple communion critical success"
      - "Specific quest completion"
      - "Hidden site discovery"

  encounter_flow:
    1_appearance:
      description: "Strange figure appears, reality feels... bent"
      player_choice: ["Approach", "Observe", "Flee"]

    2_test:
      description: "The Apkallu tests your worthiness"
      methods:
        - "Question about your struggles"
        - "Request for offering (knowledge, not goods)"
        - "Challenge (moral or practical)"

    3_teaching:
      if_passed:
        - "Rapid innovation progress (skip 50% of discovery)"
        - "Specific clue about innovation mechanics"
        - "One 'ah-ha' insight that crystalizes understanding"
      if_failed:
        - "Apkallu departs"
        - "Small Witness cost (5 points)"
        - "Cannot encounter same Apkallu for 30 days"

  witness_cost:
    encounter: "5 Witness points (unavoidable)"
    teaching_received: "+10 Witness points"
    deep_knowledge: "+20 Witness points"

  the_trade:
    description: |
      Apkallu teaching is a shortcut, but it costs sanity.
      Learning the normal way is slower but Witness-free.
      This creates a meaningful choice: speed vs. mental health.
```

### 7.3 Apkallu Dialogue Style

```yaml
dialogue_style:
  characteristics:
    - "Speaks in questions"
    - "References things you haven't mentioned"
    - "Knows your failures"
    - "Time seems to slow"

  example_encounter:
    context: "Player has failed at wheel-building 3 times"

    apkallu_appears: |
      The fisherman on the riverbank was not there a moment ago.
      His robe drips, but he is not wet. His eyes have too many years.

    apkallu_speaks: |
      "Three times the wood has cracked. Three times the center
      was not center. Do you know why a circle has no beginning?"

    player_responds: "[PLAYER CHOICE]"

    apkallu_teaches: |
      "The fish knows the river, but the river does not know the fish.
      Your wheel knows only what your hands tell it.
      Your hands know only what your eyes see.
      But your eyes see the edge. The center is what the edge is not."

      [PLAYER RECEIVES: "Center-Finding" technique - geometric method
      for finding circle center using intersecting lines]
```

---

## 8. The Divine ME

### 8.1 What the ME Are

```yaml
me_concept:
  description: |
    In Sumerian mythology, the ME (pronounced "may") are the divine
    decrees or fundamental concepts that make civilization possible.
    They include everything from kingship to truth to the art of
    lovemaking to the descent to the underworld.

    In the game, ME are rare artifacts that grant significant bonuses
    or unlock abilities - but they come with responsibilities.

  canonical_me:
    # From historical Sumerian lists
    - "The ME of kingship"
    - "The ME of godship"
    - "The ME of the exalted crown"
    - "The ME of the throne"
    - "The ME of shepherding"
    - "The ME of truth"
    - "The ME of descent to the underworld"
    - "The ME of the craft of the smith"
    - "The ME of the craft of the builder"
    - "The ME of wisdom"
    - "The ME of the scribal art"
    # ... there are traditionally 100+
```

### 8.2 ME in Gameplay

```yaml
me_gameplay:
  acquisition:
    methods:
      - "Extremely rare temple rewards (100+ favor)"
      - "Hidden site discovery"
      - "Apkallu gift (rarest)"
      - "Player-to-player transfer (can be stolen via conquest)"

    types_available_in_ancient_era:
      me_of_the_smith:
        effect: "+25% metallurgy success rate"
        responsibility: "Must teach 3 players per era"

      me_of_the_builder:
        effect: "+25% construction quality"
        responsibility: "Must contribute to public works"

      me_of_the_scribe:
        effect: "+25% writing/record speed"
        responsibility: "Must contribute 5 Codex entries per era"

      me_of_irrigation:
        effect: "+25% water control efficiency"
        responsibility: "Must maintain public canals"

  mechanics:
    carrying:
      - "Only ONE ME can be active at a time"
      - "ME is soul-bound (cannot be stolen)"
      - "ME can be voluntarily transferred"

    responsibility:
      - "Each ME has a duty"
      - "Failing duty = ME becomes dormant (no bonus)"
      - "Dormant ME can be reactivated by fulfilling duty"

    conquest:
      - "If you conquer someone's city, their ME goes dormant"
      - "Their ME can't be stolen, but it stops working"
      - "Creates incentive to protect ME holders"

  mystery_aspect:
    - "ME artifacts are physically strange"
    - "They don't quite fit the technology level"
    - "Examining them too closely = Witness cost"
    - "What ARE they, really?"
```

---

## 9. Sacred Sites & Hidden Locations

### 9.1 Known Sacred Sites

```yaml
known_sacred_sites:
  temples:
    e_abzu:  # Eridu
      description: "Temple of Enki, the first temple"
      features:
        - "Fresh water pool (the Abzu)"
        - "Ancient foundations (older than the city)"
        - "Inner sanctum with strange acoustics"
      access: "Temple favor 25+"
      secrets: "Contains entrance to deeper level"  # pragma: allowlist secret

    e_kur:  # Nippur
      description: "Mountain House, Temple of Enlil"
      features:
        - "Raised platform (proto-ziggurat)"
        - "Storm observation chamber"
        - "The Tablet of Destinies (legendary)"
      access: "Temple favor 50+"
      secrets: "Records of the flood"  # pragma: allowlist secret

    e_anna:  # Uruk
      description: "House of Heaven, Temple of Inanna"
      features:
        - "Massive precinct"
        - "Sacred marriage chamber"
        - "Administrative archives"
      access: "Temple favor 25+"
      secrets: "Inanna's descent to the underworld"

  natural_sites:
    confluence:
      location: "Where Tigris and Euphrates meet"
      significance: "Site of earliest settlements"
      features:
        - "Strange ruins beneath the water"
        - "Fish that aren't quite fish"
      access: "Boat + diving ability"

    the_marshes:
      location: "South of Eridu"
      significance: "Where the Apkallu emerged"
      features:
        - "Reed structures that move"
        - "Lights at night"
        - "Time feels wrong"
      access: "Guide + high Enki favor"
```

### 9.2 Hidden Locations

```yaml
hidden_locations:
  # These never appear on maps - must be discovered

  the_abzu_depths:
    discovery:
      clues: ["Temple of Enki inner sanctum", "Apkallu reference", "Dream vision"]
      requirement: "100+ Enki favor, specific artifact"
    nature:
      description: "Chambers beneath the temple, submerged or not"
      contents:
        - "Carvings that predate Eridu"
        - "Pools that show... elsewhere"
        - "The 'boat' of Enki (what is it?)"
      witness_cost: "30+ per visit"

  the_mountain_before:
    discovery:
      clues: ["Enlil communion vision", "Ancient map fragment", "Dying elder's story"]
      requirement: "Major expedition, survival gear"
    nature:
      description: "Site in the northern mountains, before civilization"
      contents:
        - "Structures that shouldn't exist"
        - "Writings in no known language"
        - "Views of the sky that feel important"
      witness_cost: "40+ per visit"

  the_garden:
    discovery:
      clues: ["References in multiple traditions", "Apkallu riddle", "Near-death vision"]
      requirement: "Unknown - changes per player"
    nature:
      description: "A place that was, or will be, or is"
      contents:
        - "Trees that bear knowledge"
        - "The presence of... someone"
        - "Answers that raise questions"
      witness_cost: "50+ per visit"
      note: "The game's most hidden secret"
```

### 9.3 Discovery Flow

```yaml
hidden_site_discovery:
  phase_1_rumor:
    trigger: "Random NPC dialogue, temple scroll, player rumor"
    effect: "Player learns site exists (no location)"
    example: "An old priest speaks of chambers below the temple..."

  phase_2_clues:
    trigger: "Active investigation, multiple sources"
    effect: "Player gets general area or requirement hints"
    example: "The fisherman, the merchant, and the dream all point to the marshes..."

  phase_3_trail:
    trigger: "Significant effort, possible Apkallu hint"
    effect: "Player knows how to find it"
    example: "When the moon is dark, follow the light that has no source..."

  phase_4_discovery:
    trigger: "Player physically arrives at hidden site"
    effect: "Site revealed permanently to that player"
    reward: "Major Legacy Points, unique knowledge"
    warning: "What is seen cannot be unseen (Witness cost begins)"
```

---

## 10. The Witness System Integration

### 10.1 Divine Knowledge & Sanity

```yaml
witness_divine_cost:
  principle: |
    The Witness system represents sanity/trauma. Divine/forbidden
    knowledge strains the mind. The more you know, the more it costs.

  cumulative_effect:
    baseline: "Normal gameplay has no Witness cost"
    divine_contact: "Adds Witness vulnerability"
    forbidden_knowledge: "Permanent Witness modifier"

  example_progression:
    stage_1:
      knowledge: "The gods exist and influence the world"
      witness_cost: 0
      effect: "Normal Sumerian worldview"

    stage_2:
      knowledge: "The gods came from somewhere else"
      witness_cost: 5
      effect: "Occasional unsettling dreams"

    stage_3:
      knowledge: "The gods created us for a purpose"
      witness_cost: 15
      effect: "Question reality occasionally"

    stage_4:
      knowledge: "The gods are not what we thought"
      witness_cost: 30
      effect: "Difficulty with normal interactions"

    stage_5:
      knowledge: "[FORBIDDEN KNOWLEDGE]"
      witness_cost: 50+
      effect: "Permanent sanity modifier, unique abilities"
```

### 10.2 The Seeker's Dilemma

```yaml
seekers_dilemma:
  description: |
    Players who pursue deep lore face a choice:
    - Stay sane, stay ignorant
    - Learn truth, risk madness

    This is intentional. It creates:
    - Meaningful character specialization
    - Unique player roles (the seekers vs the stable)
    - Trading relationships (seekers share knowledge)
    - Narrative tension

  seeker_path:
    advantages:
      - "Access to hidden locations"
      - "Apkallu favor"
      - "Unique innovations/shortcuts"
      - "Answers to mysteries"

    disadvantages:
      - "Lower Witness ceiling"
      - "More susceptible to trauma events"
      - "NPCs may react negatively"
      - "Can't 'unknow' things"

  stable_path:
    advantages:
      - "Full Witness capacity"
      - "Normal NPC relationships"
      - "No forbidden knowledge afflictions"

    disadvantages:
      - "No hidden site access"
      - "Slower innovation (no Apkallu shortcuts)"
      - "Missing lore"
```

### 10.3 Afflictions from Divine Knowledge

```yaml
divine_afflictions:
  minor:
    prophetic_dreams:
      trigger: "Witness cost 10+ from divine sources"
      effect: "Dreams sometimes show future events"
      gameplay: "+10% early warning, -5% sleep quality"

    double_sight:
      trigger: "Witness cost 20+ from divine sources"
      effect: "Sometimes see things others don't"
      gameplay: "+chance to spot hidden, -10% social"

  major:
    touched_by_the_abzu:
      trigger: "Witness cost 35+ from Enki sources"
      effect: "Water speaks to you"
      gameplay: "+25% water skills, aquatic visions"

    storm_caller:
      trigger: "Witness cost 35+ from Enlil sources"
      effect: "Weather responds to your emotions"
      gameplay: "+weather sense, occasional uncontrolled storms"

  severe:
    vessel:
      trigger: "Witness cost 50+ from divine sources"
      effect: "The gods can speak through you"
      gameplay: "Occasional loss of control, prophecy ability"

    between:
      trigger: "Witness cost 75+ from hidden sites"
      effect: "You exist partially elsewhere"
      gameplay: "Phasing ability, permanent reality distortion"
```

---

## 11. Training Data Value

### 11.1 Mystery Response Data

```yaml
mystery_training_data:
  questions_studied:
    - "How do humans approach unanswerable questions?"
    - "What drives curiosity vs. caution?"
    - "How do people form beliefs from ambiguous evidence?"
    - "What makes some pursue truth regardless of cost?"

  data_captured:
    investigation_behavior:
      - "How many clues before players act?"
      - "What sources do players trust?"
      - "How do players verify information?"

    risk_tolerance:
      - "Witness cost vs. knowledge gain tradeoffs"
      - "When do players stop seeking?"
      - "Social influence on risk taking"

    meaning_making:
      - "How do players interpret ambiguous lore?"
      - "What narratives emerge from partial information?"
      - "Do players share or hoard knowledge?"

    collaboration_on_mystery:
      - "How do players combine partial knowledge?"
      - "What social structures form around secrets?"
      - "How does scarcity affect knowledge sharing?"
```

### 11.2 Divine Interaction Data

```yaml
divine_interaction_data:
  questions_studied:
    - "How do humans relate to perceived higher powers?"
    - "What motivates offerings, service, worship?"
    - "How do people respond to silence from the divine?"
    - "What happens when faith is tested?"

  data_captured:
    relationship_patterns:
      - "Transactional vs. devotional approaches"
      - "Consistency of practice over time"
      - "Response to unanswered prayers"

    moral_reasoning:
      - "Divine command vs. personal ethics"
      - "Justification of actions via divine will"
      - "Response to contradictory divine demands"
```

---

## 12. Implementation Notes

### 12.1 MVP Scope

```yaml
mvp_lore:
  included:
    fog_of_war:
      - "Basic system (explored/unexplored)"
      - "Traveler tales revealing locations"
      - "3 discoverable cities beyond Eridu"

    pantheon:
      - "Enki (Eridu) fully implemented"
      - "Temple favor system"
      - "Basic communion mechanic"

    anunnaki_layer:
      - "Tier 1 clues (common)"
      - "Tier 2 clues (uncommon)"
      - "1 hidden location (The Abzu Depths)"

    apkallu:
      - "1-2 Apkallu implemented"
      - "Basic encounter system"
      - "Teaching mechanic"

  deferred:
    - "Full city-state system"
    - "All seven Apkallu"
    - "ME artifacts"
    - "Deep hidden locations (Mountain, Garden)"
    - "Multiple pantheon members fully implemented"
```

### 12.2 Content Gating

```yaml
content_gates:
  prevent_early_access:
    - "Hidden locations require specific triggers"
    - "Apkallu encounters have prerequisites"
    - "Forbidden knowledge requires progression"

  ensure_earned_discovery:
    - "No UI hints for hidden content"
    - "Clues must be found organically"
    - "Player knowledge ≠ character knowledge"

  maintain_mystery:
    - "Never confirm Anunnaki nature"
    - "Multiple valid interpretations"
    - "Some questions stay open"
```

### 12.3 Lore Consistency Checks

```yaml
consistency:
  all_npcs:
    - "Speak from in-world perspective"
    - "Never break fourth wall"
    - "Reflect their knowledge level"

  all_artifacts:
    - "Have plausible in-world explanation"
    - "Leave room for mystery"
    - "Don't confirm extraterrestrial origin"

  all_events:
    - "Could be divine or coincidence"
    - "Player interprets meaning"
    - "Game does not editorialize"
```

---

## Appendix: Quick Reference

### Sumerian Terms

| Term | Meaning | Game Usage |
|------|---------|------------|
| Anunnaki | "Those of royal blood" / "Those from heaven came" | The gods / mystery beings |
| Apkallu | "Sages" / "Wise ones" | Seven teacher-beings |
| ME | "Divine decrees" | Power artifacts |
| Abzu | "The deep" / "Freshwater abyss" | Enki's domain, hidden depths |
| Nibiru | "Crossing point" | Mystery location / the 12th planet |
| Igigi | "The watchers" | Lesser divine beings |
| E-[name] | "House of [name]" | Temple designation |
| An | "Heaven" / "Sky" | The realm above |
| Ki | "Earth" | The realm below |
| Kur | "Mountain" / "Underworld" | The land of the dead |

### God Quick Reference

| God | Domain | City | Player Benefit | Mystery Aspect |
|-----|--------|------|----------------|----------------|
| Anu | Sky/Authority | - | Leadership buffs | The absent king |
| Enlil | Wind/Earth | Nippur | Weather control | Destroyer |
| Enki | Water/Wisdom | Eridu | Innovation help | Creator/Rebel |
| Inanna | Love/War | Uruk | Combat/Social | Underworld secrets |
| Utu | Sun/Justice | Sippar | Truth/Law | The watcher |
| Nanna | Moon | Ur | Time/Cycles | Hidden calendar |
| Marduk | Order | Babylon | (Later era) | The successor |

---

*"In the beginning, there was the water. And from the water came the word. And the word was not ours."*
