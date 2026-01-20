# Art Direction & Graphics Specification

> "The first city must feel alive—not as a game, but as a world that existed."

## Table of Contents

1. [Vision](#1-vision)
2. [Technical Foundation](#2-technical-foundation)
3. [Camera System](#3-camera-system)
4. [Visual Style](#4-visual-style)
5. [Character Design](#5-character-design)
6. [Environment Design](#6-environment-design)
7. [Lighting & Atmosphere](#7-lighting--atmosphere)
8. [Animation](#8-animation)
9. [UI/UX Design](#9-uiux-design)
10. [Audio Direction](#10-audio-direction)
11. [AI Asset Pipeline](#11-ai-asset-pipeline)
12. [Performance Targets](#12-performance-targets)
13. [Development Phases](#13-development-phases)

---

## 1. Vision

### 1.1 Core Aesthetic

```yaml
visual_philosophy:
  primary_goal: "Historical authenticity that feels lived-in"

  inspiration:
    films:
      - "Apocalypto (visceral, grounded)"
      - "Gladiator (scale, atmosphere)"
      - "The Northman (ritual, texture)"
    games:
      - "Red Dead Redemption 2 (world detail, third-person)"
      - "Assassin's Creed Origins (ancient world)"
      - "Kingdom Come Deliverance (historical grounding)"

  NOT_this:
    - "Stylized/cartoonish (Fortnite)"
    - "Over-clean fantasy (most MMOs)"
    - "Grimdark desaturated (Dark Souls)"

  keywords:
    - "Warm"
    - "Dusty"
    - "Textured"
    - "Human-scale"
    - "Lived-in"
```

### 1.2 The Feel

```yaml
emotional_targets:
  entering_eridu:
    feeling: "Awe at humanity's first city"
    visual_cues:
      - "Ziggurat visible from distance"
      - "Smoke from cooking fires"
      - "Sound of activity before you see it"
      - "Dogs barking, people calling"

  daily_life:
    feeling: "Routine, community, purpose"
    visual_cues:
      - "NPCs with visible tasks"
      - "Time-of-day lighting changes"
      - "Weather affecting behavior"

  wilderness:
    feeling: "Danger, isolation, vulnerability"
    visual_cues:
      - "Tall grass obscuring vision"
      - "Animal sounds"
      - "Distance from safety visible"

  temple_interior:
    feeling: "Sacred, mysterious, powerful"
    visual_cues:
      - "Dramatic lighting from openings"
      - "Incense haze"
      - "Gleaming cult statue"
```

---

## 2. Technical Foundation

### 2.1 Engine Choice

```yaml
engine: "Unreal Engine 5"

rationale:
  rendering:
    nanite: "Allows detailed environments without LOD management"
    lumen: "Real-time global illumination (critical for ancient interiors)"
    virtual_shadow_maps: "Soft, realistic shadows"

  development_efficiency:
    marketplace: "Thousands of assets adaptable to ancient setting"
    blueprints: "Visual scripting reduces code complexity"
    documentation: "Extensive, AI can assist effectively"
    community: "Large, active, problem-solving resources"

  business:
    cost: "Free until $1M gross revenue"
    future: "Industry standard, hireable talent pool"

  alternatives_considered:
    unity:
      rejected_because: "Weaker realistic rendering, recent trust issues"
    godot:
      rejected_because: "Not mature enough for realistic 3D at this scale"
    custom:
      rejected_because: "Solo dev—need proven tools"
```

### 2.2 Target Specifications

```yaml
minimum_spec:
  gpu: "GTX 1060 / RX 580"
  cpu: "Intel i5-8400 / Ryzen 5 2600"
  ram: "16 GB"
  storage: "50 GB SSD"
  resolution: "1080p @ 30fps (medium settings)"

recommended_spec:
  gpu: "RTX 3060 / RX 6600 XT"
  cpu: "Intel i7-10700 / Ryzen 7 3700X"
  ram: "32 GB"
  storage: "100 GB NVMe SSD"
  resolution: "1440p @ 60fps (high settings)"

ultra_spec:
  gpu: "RTX 4080 / RX 7900 XT"
  cpu: "Intel i9-13900K / Ryzen 9 7950X"
  ram: "64 GB"
  storage: "NVMe SSD"
  resolution: "4K @ 60fps (ultra settings)"
```

---

## 3. Camera System

### 3.1 Primary Camera (Third-Person)

```yaml
third_person_camera:
  style: "Over-shoulder, similar to RDR2/Witcher 3"

  default_distance:
    exploration: "2.5-3 meters behind character"
    combat: "3-4 meters (wider view)"
    conversation: "Closer, slight angle"

  field_of_view:
    default: "75 degrees"
    sprint: "80 degrees (slight widening)"
    aim: "65 degrees (zoom in)"

  camera_collision:
    method: "Soft push-in when near walls"
    priority: "Never clip through geometry"

  shoulder_swap:
    enabled: true
    default: "Right shoulder"
    toggle: "Player preference"
```

### 3.2 Camera Modes

```yaml
camera_modes:
  exploration:
    description: "Default wandering mode"
    distance: "Medium"
    rotation_speed: "Player controlled"
    auto_center: "Gentle, after 3 seconds"

  work_mode:
    description: "When performing tasks (farming, crafting)"
    distance: "Pulled back slightly"
    angle: "Higher, see work area"
    lock: "Soft lock on work station"

  conversation:
    description: "Talking to NPCs"
    distance: "Close"
    angle: "Over shoulder toward NPC"
    cuts: "Subtle angle changes, not hard cuts"

  detail_view:
    description: "Examining objects, reading tablets"
    transition: "Smooth zoom to first-person"
    use: "Clay tablets, artifacts, innovations"

  combat:
    description: "When threats detected"
    distance: "Pulled back"
    tracking: "Soft lock on primary threat"
    awareness: "Show peripheral enemies"

  building:
    description: "Construction, farming layout"
    distance: "Far pulled back"
    angle: "Higher overhead"
    grid: "Optional alignment overlay"
```

### 3.3 Cinematic Camera

```yaml
cinematic_triggers:
  first_time_events:
    - "Entering Eridu first time"
    - "First view of ziggurat"
    - "Witnessing major ritual"
    - "Birth of child"
    - "Death of character"

  implementation:
    style: "Brief (3-5 second) cinematic angle"
    control: "Player can skip"
    frequency: "Rare—preserve impact"
```

---

## 4. Visual Style

### 4.1 Color Palette

```yaml
color_palette:
  primary_colors:
    mud_brick:
      hex: "#C4A77D"
      use: "Buildings, walls, most structures"

    river_blue:
      hex: "#4A7C9B"
      use: "Water, sky accents"

    date_palm_green:
      hex: "#5D7F4A"
      use: "Vegetation, oases"

    barley_gold:
      hex: "#D4A84B"
      use: "Fields, harvest, grain"

    desert_sand:
      hex: "#E8D4B8"
      use: "Ground, dust, paths"

  accent_colors:
    lapis_blue:
      hex: "#1E4D8C"
      use: "Jewelry, temple decoration, status"

    carnelian_red:
      hex: "#B44B3A"
      use: "Jewelry, pottery decoration"

    temple_white:
      hex: "#F5F0E6"
      use: "Whitewashed walls, linen"

    copper_orange:
      hex: "#B87333"
      use: "Tools, weapons, metal objects"

  atmospheric_colors:
    dawn:
      sky: "#FFD4A3"
      light: "Warm, golden"

    midday:
      sky: "#87CEEB"
      light: "Harsh, bright, shadows sharp"

    dusk:
      sky: "#FF7F50"
      light: "Orange, dramatic, long shadows"

    night:
      sky: "#1A1A2E"
      light: "Blue moonlight, warm fire spots"
```

### 4.2 Material Philosophy

```yaml
material_approach:
  principle: "Everything has texture, wear, and history"

  categories:
    organic:
      - "Reed bundles (visible individual reeds)"
      - "Woven textiles (thread patterns)"
      - "Wood (grain, weathering)"
      - "Leather (creases, patina)"

    mineral:
      - "Mud brick (fingerprints visible, cracks)"
      - "Fired clay (kiln marks, glaze variation)"
      - "Stone (chisel marks, weathering)"
      - "Metal (hammer marks, tarnish)"

    liquid:
      - "Water (river sediment, reflections)"
      - "Beer (amber, foam)"
      - "Blood (realistic but not gratuitous)"

  wear_and_tear:
    principle: "Nothing is perfectly new"
    implementation:
      - "Vertex dirt in corners and edges"
      - "Wear patterns on high-contact areas"
      - "Repairs visible on old items"
      - "Status items better maintained"
```

---

## 5. Character Design

### 5.1 Body Types

```yaml
character_bodies:
  variation_principle: "Historical body diversity, not modern idealization"

  male_types:
    laborer:
      build: "Lean, muscular from work"
      distinguishing: "Callused hands, sun-darkened skin"

    craftsman:
      build: "Upper body development from trade"
      distinguishing: "Trade-specific marks (potter's fingers, smith burns)"

    priest:
      build: "Well-fed, softer"
      distinguishing: "Shaved head, cleaner skin"

    farmer:
      build: "Strong back, weathered"
      distinguishing: "Bent posture from fieldwork"

  female_types:
    worker:
      build: "Strong, practical"
      distinguishing: "Working hands"

    household:
      build: "Variable"
      distinguishing: "Depends on class"

    temple:
      build: "Well-maintained"
      distinguishing: "Religious jewelry/marks"

  age_representation:
    children: "Properly proportioned, not mini-adults"
    young_adult: "Peak physical condition"
    middle_age: "Wear showing"
    elder: "Rare (respected), visible age"
```

### 5.2 Clothing System

```yaml
clothing:
  base_garments:
    male_common:
      kilt:
        description: "Wool or linen wrap at waist"
        variations: "Length, fringe, belt"
        class_markers: "Quality of fabric, decoration"

    female_common:
      tunic:
        description: "Draped dress, one or both shoulders"
        variations: "Length, layers, pins"
        class_markers: "Fabric quality, embroidery"

    priestly:
      kaunakes:
        description: "Tiered wool skirt (tufted appearance)"
        unique_to: "Temple personnel"
        status: "High—instantly recognizable"

  accessories:
    belts: "Leather or woven, class-variable"
    sandals: "Most go barefoot; sandals = status"
    headwear: "Rarely worn except priests/royalty"

  material_quality_tiers:
    poor: "Rough wool, undyed, patched"
    common: "Decent wool, natural colors"
    prosperous: "Fine wool, some dye"
    wealthy: "Linen, rich dyes, embroidery"
    elite: "Finest linen, gold thread, luxury materials"
```

### 5.3 Jewelry & Adornment

```yaml
jewelry_visuals:
  importance: "Primary status display—MUST be visible and detailed"

  items:
    collar_necklaces:
      visual: "Wide, multi-strand, catches light"
      lod_priority: "High—visible at distance"

    earrings:
      visual: "Heavy hoops or pendants"
      animation: "Subtle sway with movement"

    cylinder_seals:
      visual: "Worn on chest pin or wrist cord"
      detail: "Carved pattern visible on inspection"

    bracelets:
      visual: "Stacked, various materials"
      animation: "Clink sound, subtle movement"

  material_rendering:
    gold: "Warm reflections, never too shiny"
    silver: "Cooler, slightly tarnished"
    lapis: "Deep blue, gold flecks in texture"
    carnelian: "Translucent red-orange, polished"
    shell: "Iridescent, carved patterns"
```

### 5.4 Hair & Grooming

```yaml
hair_styles:
  historical_accuracy: "Based on archaeological evidence"

  male_hair:
    common: "Shoulder-length, sometimes tied"
    priest: "Shaved head (required)"
    elite: "Well-groomed, oiled"

  female_hair:
    common: "Long, braided, decorated with beads/pins"
    married: "Specific styles indicate status"
    elite: "Elaborate arrangements, gold ornaments"

  beards:
    common: "Full beards, moderately groomed"
    priest: "Often shaved"
    elite: "Carefully shaped, oiled"

  technical:
    hair_system: "Unreal Groom or optimized cards"
    jewelry_attachment: "Hair ornaments as separate mesh"
    physics: "Subtle movement, braids sway"
```

---

## 6. Environment Design

### 6.1 City of Eridu

```yaml
eridu_layout:
  reference: "Aerial reference image—canals, ziggurat center, organic streets"

  zones:
    temple_complex:
      visuals:
        - "Ziggurat dominates skyline (3 tiers)"
        - "Whitewashed walls (brighter than surroundings)"
        - "Blue and gold decorations at top"
        - "Processional stairs with reliefs"
      atmosphere: "Awe, sacred, incense visible"

    craftsmen_district:
      visuals:
        - "Workshops with tools visible"
        - "Smoke from kilns and forges"
        - "Goods displayed outside"
        - "Narrow streets, busy"
      atmosphere: "Industry, activity, noise"

    residential_poor:
      visuals:
        - "Reed huts mixed with mud brick"
        - "Narrow, winding alleys"
        - "Visible wear, patches"
        - "Animals roaming"
      atmosphere: "Crowded, alive, organic"

    residential_wealthy:
      visuals:
        - "Larger houses with courtyards"
        - "Whitewashed exteriors"
        - "Gardens visible"
        - "Servants, guards"
      atmosphere: "Ordered, prosperous"

    harbor:
      visuals:
        - "Reed boats of various sizes"
        - "Fish drying racks"
        - "Trade goods stacked"
        - "Travelers from foreign lands"
      atmosphere: "Commerce, diversity, movement"

    marketplace:
      visuals:
        - "Temporary stalls, awnings"
        - "Goods on ground cloths"
        - "Crowd of NPCs"
        - "Colors from textiles"
      atmosphere: "Chaotic, vibrant, loud"
```

### 6.2 Architecture

```yaml
architecture:
  mud_brick_buildings:
    construction_visible:
      - "Brick courses visible"
      - "Mortar (mud or bitumen) between"
      - "Timber beams at doors/windows"
      - "Reed matting on roofs"

    weathering:
      - "Rain erosion on upper edges"
      - "Salt efflorescence at base"
      - "Repairs with different colored mud"
      - "Cracks from settling"

  reed_construction:
    technique: "Bundled reeds bent into arches"
    use: "Poor housing, storage, marsh buildings"
    visual: "Golden color, visible bundle patterns"

  ziggurat:
    scale: "Dominates city—visible from everywhere"
    tiers: "3 levels, each smaller"
    surface: "Baked brick face, mud brick core"
    top: "Small temple, blue glazed brick"
    stairs: "Central staircase, side stairs"
```

### 6.3 Natural Environment

```yaml
landscape:
  river_and_canals:
    water:
      color: "Silty brown-green, not crystal clear"
      movement: "Visible current, debris"
      edges: "Reeds, mud banks, birds"

    canals:
      construction: "Cut into earth, reinforced edges"
      maintenance: "Some sections pristine, others silted"
      features: "Sluice gates, bridges, water lifts"

  vegetation:
    date_palms:
      density: "Clustered near water"
      detail: "Individual fronds, dates visible in season"
      scale: "Tall—provide shade, landmarks"

    reeds:
      location: "Along water, marshes"
      use: "Building material, hiding places"
      animation: "Sway in wind"

    crops:
      barley: "Golden when ripe, green when young"
      wheat: "Similar, taller"
      visible_growth: "Seasonal change"

    gardens:
      wealthy_homes: "Vegetables, fruit trees, flowers"
      temple: "Sacred gardens, medicinal plants"

  terrain:
    fertile_land:
      color: "Dark, rich near river"
      texture: "Plowed rows visible"

    desert_edge:
      color: "Pale sand and gravel"
      texture: "Cracked, sparse vegetation"

    marshes:
      water: "Shallow, reeds everywhere"
      visibility: "Limited—danger"
      wildlife: "Birds, fish jumping, crocodile eyes"
```

---

## 7. Lighting & Atmosphere

### 7.1 Day/Night Cycle

```yaml
day_night_cycle:
  duration: "1 hour real time = 1 day game time (adjustable)"

  phases:
    pre_dawn:
      time: "4:00-5:00"
      sky: "Deep blue to pink at horizon"
      light: "Dim, cool"
      activity: "City waking"

    dawn:
      time: "5:00-6:00"
      sky: "Orange and pink, dramatic"
      light: "Warm, long shadows"
      activity: "Workers heading to fields"

    morning:
      time: "6:00-10:00"
      sky: "Blue, some clouds"
      light: "Pleasant, moderate shadows"
      activity: "Peak activity"

    midday:
      time: "10:00-14:00"
      sky: "Harsh blue, blazing sun"
      light: "Bright, short sharp shadows"
      activity: "Slowdown, seek shade"

    afternoon:
      time: "14:00-18:00"
      sky: "Blue, warming"
      light: "Golden hour approaching"
      activity: "Work resumes"

    dusk:
      time: "18:00-19:00"
      sky: "Orange, red, purple"
      light: "Dramatic, long shadows"
      activity: "Return to city"

    evening:
      time: "19:00-22:00"
      sky: "Deep blue to black"
      light: "Firelight, oil lamps"
      activity: "Social, domestic"

    night:
      time: "22:00-4:00"
      sky: "Black, stars VERY visible (no light pollution)"
      light: "Moonlight (phase matters), fire only"
      activity: "Sleep, danger in wilderness"
```

### 7.2 Weather System

```yaml
weather:
  clear:
    frequency: "Most common"
    visual: "Blue sky, dust in air"
    gameplay: "Normal"

  dust_haze:
    frequency: "Common"
    visual: "Reduced visibility, orange tint"
    gameplay: "Harder to spot threats"

  sandstorm:
    frequency: "Rare but dramatic"
    visual: "Severe visibility reduction, sand particles"
    gameplay: "Must seek shelter, damage possible"

  rain:
    frequency: "Seasonal (winter)"
    visual: "Gray sky, puddles form, mud"
    gameplay: "Some work impossible, disease risk"

  flood:
    frequency: "Annual event"
    visual: "River rising, fields submerged"
    gameplay: "Major event, preparation required"
```

### 7.3 Interior Lighting

```yaml
interior_lighting:
  principle: "Dramatic contrast between bright exterior and dim interior"

  sources:
    doorways: "Primary light source, dramatic shafts"
    windows: "Small, high—limited light"
    oil_lamps: "Warm, flickering, smoky"
    fires: "Cooking hearths, warm pools"

  temple_interiors:
    outer_rooms: "Dim, lamp-lit"
    inner_sanctum: "Very dark, dramatic cult statue lighting"
    smoke: "Incense creating volumetric effects"

  homes:
    poor: "Single room, fire pit, door light"
    wealthy: "Courtyard brings light, multiple lamps"
```

---

## 8. Animation

### 8.1 Character Animation

```yaml
animation_priorities:
  locomotion:
    walk: "Relaxed, natural gait"
    run: "Purposeful, not athletic sprint"
    sprint: "Emergency only, exhausting"
    variations: "Carrying loads, injured, tired"

  work_animations:
    farming:
      - "Sowing (scattering motion)"
      - "Harvesting (sickle sweep, gather)"
      - "Threshing (beating grain)"
      - "Grinding (stone against stone)"

    crafting:
      - "Potter's wheel (continuous, meditative)"
      - "Weaving (rhythmic shuttle movement)"
      - "Smithing (hammer blows, bellows)"
      - "Brickmaking (forming, stacking)"

    domestic:
      - "Cooking (stirring, kneading)"
      - "Carrying water (jug on head/hip)"
      - "Sweeping (reed broom)"
      - "Childcare (holding, feeding)"

  social:
    greeting: "Bow, hand gestures"
    conversation: "Hand movements, head tilts"
    prayer: "Hands raised, kneeling"
    trading: "Examining goods, weighing"

  combat:
    spear: "Thrusting, defensive stance"
    bow: "Draw, aim, release"
    knife: "Close quarters, grappling"
    unarmed: "Wrestling, pushing"
```

### 8.2 NPC Behavior Animation

```yaml
npc_animations:
  idle_behaviors:
    - "Adjusting clothing"
    - "Wiping sweat"
    - "Looking around"
    - "Stretching"
    - "Scratching"
    - "Yawning"

  contextual:
    marketplace: "Examining goods, haggling gestures"
    temple: "Reverent posture, quiet movement"
    beer_house: "Relaxed, drinking, laughing"
    work: "Focused, repetitive task motion"

  reactions:
    player_approach: "Notice, assess, respond"
    important_person: "Defer, bow"
    danger: "Alert, flee or fight"
```

### 8.3 Animal Animation

```yaml
animal_animations:
  dogs:
    idle: "Sitting, lying, scratching"
    alert: "Ears up, tail still"
    friendly: "Tail wag, approach"
    aggressive: "Hackles, growl, bark"

  livestock:
    sheep: "Grazing, clustering, fleeing"
    goats: "Climbing, browsing, stubborn stops"
    cattle: "Slow movement, chewing, plowing"

  predators:
    lion: "Stalking crouch, explosive pounce"
    wolves: "Pack coordination, circling"
    crocodile: "Still... then explosive lunge"

  wildlife:
    birds: "Flocking, startled flight"
    fish: "Jumping, swimming schools"
    gazelles: "Grazing, fleeing in herds"
```

---

## 9. UI/UX Design

### 9.1 UI Philosophy

```yaml
ui_philosophy:
  principle: "Minimal, diegetic where possible"

  approach:
    hud: "Minimalist—only essential info"
    menus: "Clay tablet aesthetic"
    notifications: "Subtle, in-world when possible"

  diegetic_elements:
    health: "No bar—visual cues (limping, blood, pale)"
    hunger: "Stomach sounds, visual exhaustion"
    time: "Sun position, shadow length"
    reputation: "NPC reactions"
```

### 9.2 HUD Elements

```yaml
hud:
  always_visible:
    nothing: "Clean screen by default"

  on_demand:
    status: "Hold key to see vitals"
    map: "Open as inventory item"
    inventory: "Open as carried bag"

  contextual:
    interaction_prompt: "Small icon when near interactable"
    danger_indicator: "Subtle edge vignette when threatened"
    quest_marker: "Optional, off by default"

  combat:
    health_indicator: "Screen effects (red edge, blur)"
    stamina: "Breathing sounds, posture"
    enemy_health: "Visual damage, behavior"
```

### 9.3 Menu Design

```yaml
menu_aesthetic:
  theme: "Clay tablet / cylinder seal"

  elements:
    background: "Warm tan, textured like clay"
    text: "Impressed marks (stylized cuneiform-inspired)"
    icons: "Simple pictographs"
    borders: "Cylinder seal patterns"

  inventory:
    visual: "Items laid out on cloth or in basket"
    interaction: "Pick up, examine, use"
    categories: "Physical organization, not tabs"

  dialogue:
    style: "Subtitles with speaker name"
    choices: "Listed options, not wheel"
    voice: "Key lines voiced, rest text"
```

---

## 10. Audio Direction

### 10.1 Music

```yaml
music:
  principle: "Sparse, meaningful, period-appropriate"

  instrumentation:
    primary:
      - "Lyre (stringed, plucked)"
      - "Drums (clay, skin)"
      - "Flute (reed)"
      - "Vocal chanting"

    avoid:
      - "Modern orchestra"
      - "Electronic elements"
      - "Western harmonies"

  usage:
    exploration: "Minimal or none—ambient sounds"
    temple: "Sacred chanting, lyre"
    danger: "Drums, tension"
    triumph: "Full instrumentation, rare"
    death: "Mournful, sparse"
```

### 10.2 Ambient Sound

```yaml
ambient_audio:
  city:
    constant:
      - "Distant voices"
      - "Dogs barking"
      - "Footsteps on packed earth"
      - "Wind"

    location_specific:
      marketplace: "Haggling, animal sounds, goods being moved"
      temple: "Chanting, bells, incense crackling"
      harbor: "Water, boats, foreign languages"
      craftsmen: "Hammering, wheel spinning, kiln roar"

  wilderness:
    constant:
      - "Wind"
      - "Insects"
      - "Bird calls"

    danger_cues:
      - "Silence (predator near)"
      - "Distant howls"
      - "Rustling grass"

  time_of_day:
    dawn: "Birds waking"
    midday: "Insects, heat shimmer"
    dusk: "Evening insects, cooking sounds"
    night: "Owls, dogs, distant sounds carry"
```

---

## 11. AI Asset Pipeline

### 11.1 Image Generation

```yaml
ai_image_generation:
  tool: "Nano Banana (current)"

  workflow:
    concept_art:
      1: "Generate reference images for major elements"
      2: "Curate best results"
      3: "Use as reference for 3D modeling"

    texture_generation:
      1: "Generate tileable textures"
      2: "Process for game use (normal maps, etc.)"
      3: "Validate in engine"

    ui_elements:
      1: "Generate icons and decorative elements"
      2: "Clean up and vectorize"
      3: "Implement in UI system"

  style_consistency:
    method: "Maintain reference library"
    prompt_templates: "Document working prompts"
    color_grading: "Post-process to match palette"
```

### 11.2 3D Asset Strategy

```yaml
3d_assets:
  sources:
    marketplace:
      priority: "High—fastest path to visual quality"
      adaptation: "Retexture and modify for period accuracy"
      examples:
        - "Base human characters (customize)"
        - "Vegetation (palm trees, crops)"
        - "Animals (dogs, sheep, wildlife)"
        - "Basic architecture (adapt style)"

    ai_assisted_generation:
      tools: "Meshy, Tripo3D, Point-E (evolving)"
      use_cases:
        - "Unique props (specific tools, vessels)"
        - "Decorative elements"
        - "Blocked-out buildings"
      post_processing: "Manual cleanup required"

    custom_creation:
      priority: "Hero assets only"
      examples:
        - "Main character customization"
        - "Ziggurat (unique landmark)"
        - "Key story items"
```

### 11.3 Animation Strategy

```yaml
animation_sources:
  mocap_libraries:
    - "Mixamo (free, extensive)"
    - "Marketplace packs"
    - "Retarget to characters"

  procedural:
    - "Locomotion blending"
    - "IK for interactions"
    - "Ragdoll for death"

  custom:
    - "Key emotional moments"
    - "Unique work animations"
    - "Combat specials"
```

---

## 12. Performance Targets

### 12.1 Optimization Strategy

```yaml
optimization:
  geometry:
    nanite: "Use for complex static meshes"
    lods: "Still needed for non-nanite (characters, etc.)"
    culling: "Aggressive distance culling"

  lighting:
    lumen: "Use for GI, but budget carefully"
    baked: "Supplement with baked where static"
    shadows: "Virtual shadow maps, cascade optimization"

  streaming:
    world_partition: "Use UE5 world partition"
    level_streaming: "Load areas as needed"
    texture_streaming: "Aggressive VRAM management"

  npc_count:
    target: "50-100 visible NPCs in city"
    lod: "Reduce animation detail at distance"
    culling: "Off-screen NPCs simplified"
```

### 12.2 Scalability

```yaml
scalability_settings:
  low:
    nanite: "Reduced detail"
    lumen: "Screen-space GI"
    shadows: "Reduced resolution"
    npcs: "Reduced count and detail"

  medium:
    nanite: "Standard"
    lumen: "Software ray tracing"
    shadows: "Standard VSM"
    npcs: "Full count, reduced animation"

  high:
    nanite: "Full detail"
    lumen: "Hardware ray tracing (if available)"
    shadows: "High resolution"
    npcs: "Full detail"

  ultra:
    nanite: "Maximum"
    lumen: "Maximum quality"
    shadows: "Maximum"
    npcs: "Maximum crowd density"
```

---

## 13. Development Phases

### 13.1 Phase 1: Proof of Concept

```yaml
phase_1:
  goal: "Playable vertical slice of Eridu"
  duration: "3-6 months"

  deliverables:
    environment:
      - "Temple complex (exterior)"
      - "Market area"
      - "One residential zone"
      - "Surrounding fields"

    characters:
      - "Player character (basic customization)"
      - "10-20 NPC types"
      - "Basic animals (dogs, sheep)"

    systems:
      - "Third-person camera"
      - "Basic locomotion"
      - "Day/night cycle"
      - "One work activity (farming)"

    art_quality:
      - "Final lighting"
      - "Representative materials"
      - "Placeholder animations"
```

### 13.2 Phase 2: Core Experience

```yaml
phase_2:
  goal: "Complete Ancient Era playable"
  duration: "6-12 months"

  additions:
    - "Full city of Eridu"
    - "Surrounding wilderness"
    - "All professions playable"
    - "Innovation system"
    - "NPC routines"
    - "Combat"
    - "Full audio"
```

### 13.3 Phase 3: Polish & Release

```yaml
phase_3:
  goal: "Release-ready Ancient Era"
  duration: "3-6 months"

  focus:
    - "Performance optimization"
    - "Bug fixing"
    - "Tutorial refinement"
    - "Multiplayer testing"
    - "Platform requirements"
```

---

## Appendix: Reference Image Library

```yaml
reference_library:
  location: "docs/reference/"

  categories:
    characters:
      - "farmers-reference.jpg"
      - "woman-reference.jpg"
      - "priest-reference.jpg"

    animals:
      - "mastiff-reference.jpg"

    architecture:
      - "eridu-aerial-reference.jpg"
      - "ziggurat-reference.jpg"

    landscape:
      - "marshes-reference.jpg"
      - "fields-reference.jpg"

  usage:
    for_ai: "Use as reference in prompts"
    for_3d: "Model to match aesthetic"
    for_review: "Compare work against reference"
```

---

*"Build the world they lived in, not the museum we put them in."*
