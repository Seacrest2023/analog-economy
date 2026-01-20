# Ancient Era Events: Director AI Playbook

> *"This document is the Director AI's instruction manual. Every event listed here has a trigger condition, a learning path, and consequences. Developers: if it's not in this spec, the Director doesn't know about it."*

## Overview

This specification defines **all scripted and dynamic events** for the Ancient Era (Eridu, 4500 BCE). Each event includes:
- **Trigger**: When the event activates
- **Codex Path**: How players learn to solve it
- **Failure State**: Consequences of not solving it
- **Success State**: Rewards and unlocks
- **Training Data**: What AI learns from player responses

---

## Event Schema Reference

```yaml
event_template:
  id: "unique_identifier"
  name: "Human-readable name"
  category: "onboarding|survival|innovation|social|economic|mystery"
  priority: "mvp|high|medium|low"

  trigger:
    type: "time|threshold|compound|random"
    conditions: []
    cooldown: "time before re-trigger"

  codex_path:
    prerequisite: "What player must know/have"
    discovery: "How player learns solution exists"
    unlock: "What becomes available"

  failure:
    deadline: "When failure locks in"
    consequence: "What happens"
    severity: "minor|moderate|severe|catastrophic"
    recovery: "Path back, if any"

  success:
    condition: "How to complete"
    sila_reward: integer
    karma_reward: integer
    unlocks: []

  training_data:
    category: "ambiguity|strategy|social|temporal|embodied"
    capture_schema: "sft|dpo|trajectory|cot"
```

---

## Part 1: Onboarding Events (First Hour)

### EVENT: First Awakening
```yaml
id: "onboard_001_awakening"
name: "First Awakening"
category: "onboarding"
priority: "mvp"

trigger:
  type: "time"
  conditions:
    - "game_time == 0:00"
    - "player_state == new_character"
  cooldown: "once_per_character"

codex_path:
  prerequisite: "None"
  discovery: "Automatic - UI tutorial overlay"
  unlock:
    - "Basic movement controls"
    - "Inventory access"
    - "Status bar understanding"

narrative:
  context: "Player awakens at dawn near the reed marshes outside Eridu"
  npc_prompt: "An elderly fisherman notices you stirring"

  dialogue_tree:
    fisherman: "You look lost, stranger. The city is that way. But first—you look hungry."
    options:
      - "Ask for food" → leads to THIRST_TUTORIAL
      - "Ask about the city" → leads to CITY_INTRO
      - "Ignore and explore" → no penalty, natural discovery

failure:
  deadline: "None - tutorial is patient"
  consequence: "None - player can take their time"
  severity: "none"
  recovery: "N/A"

success:
  condition: "Player moves 50 meters in any direction"
  sila_reward: 5
  karma_reward: 0
  unlocks: ["basic_navigation"]

training_data:
  category: "embodied"
  capture_schema: "trajectory"
  notes: "Capture first movement patterns, time-to-action metrics"
```

### EVENT: First Thirst
```yaml
id: "onboard_002_thirst"
name: "First Thirst"
category: "onboarding"
priority: "mvp"

trigger:
  type: "threshold"
  conditions:
    - "player.thirst < 70"
    - "tutorial_stage >= 1"
  cooldown: "once_per_character"

codex_path:
  prerequisite: "First Awakening complete"
  discovery:
    method: "status_bar_flash"
    hint: "Thirst icon pulses, tooltip appears"
  unlock:
    - "Codex entry: 'Finding Water'"
    - "Water source detection (highlighted)"

narrative:
  context: "Player's thirst drops, triggering survival instinct"

  visual_cues:
    - "Screen edges slightly yellow-tinted"
    - "Thirst icon pulses"
    - "Nearby canal/water source glows subtly"

failure:
  deadline: "thirst reaches 0"
  consequence: "Health begins draining (-5 HP/minute)"
  severity: "moderate"
  recovery: "Drink any water source"

success:
  condition: "player.thirst > 50 after drinking"
  sila_reward: 10
  karma_reward: 0
  unlocks: ["water_finding_skill_tier_0"]

training_data:
  category: "embodied"
  capture_schema: "trajectory"
  notes: "Time to respond, path to water, drinking behavior"
```

### EVENT: First Hunger
```yaml
id: "onboard_003_hunger"
name: "First Hunger"
category: "onboarding"
priority: "mvp"

trigger:
  type: "threshold"
  conditions:
    - "player.hunger < 60"
    - "tutorial_stage >= 2"
  cooldown: "once_per_character"

codex_path:
  prerequisite: "First Thirst complete"
  discovery:
    method: "npc_hint"
    hint: "NPC mentions fish in the canal, dates on palms"
  unlock:
    - "Codex entry: 'Foraging Basics'"
    - "Food source highlighting"
    - "Basic fishing interaction"

narrative:
  npc_prompt: "Fisherman returns if nearby"
  dialogue: "The canals are full of fish. Here—take this reed. Watch how I do it."

  if_no_npc:
    visual_cue: "Fish jumping in nearby canal"
    discovery: "Player can attempt to catch by hand (difficult) or find tool"

failure:
  deadline: "hunger reaches 0"
  consequence:
    - "Stamina regeneration stops"
    - "Movement speed -20%"
    - "At hunger 0 for 10 minutes: collapse"
  severity: "moderate"
  recovery: "Eat any food"

success:
  condition: "player.hunger > 50 after eating"
  sila_reward: 15
  karma_reward: 0
  unlocks:
    - "foraging_skill_tier_0"
    - "fishing_interaction_basic"

training_data:
  category: "embodied"
  capture_schema: "trajectory"
  notes: "Food source selection, gathering efficiency"
```

### EVENT: First Shelter
```yaml
id: "onboard_004_shelter"
name: "First Shelter"
category: "onboarding"
priority: "mvp"

trigger:
  type: "compound"
  conditions:
    - "game_time > 18:00 (first evening)"
    - "player has no shelter_claim"
    - "tutorial_stage >= 3"
  cooldown: "once_per_character"

codex_path:
  prerequisite: "First Hunger complete OR game_time > 18:00"
  discovery:
    method: "environmental"
    hint: "Temperature drops, screen darkens, stamina drain increases"
  unlock:
    - "Codex entry: 'Reed Shelter Construction'"
    - "Shelter blueprint (basic reed hut)"
    - "Material gathering interaction"

narrative:
  context: "Night approaches, temperature drops"

  environmental_pressure:
    - "Ambient temperature display drops"
    - "Stamina drain +50% outdoors at night"
    - "Predator sounds in distance"

  npc_hint_if_nearby:
    dialogue: "You'll want to find shelter before dark. The marshes have... things."

failure:
  deadline: "Spend night without shelter"
  consequence:
    - "Sanity -10"
    - "Health -20 (exposure)"
    - "Stamina starts at 50% next day"
  severity: "moderate"
  recovery: "Build or find shelter next night"

success:
  condition: "Player in shelter_zone when game_time > 22:00"
  sila_reward: 25
  karma_reward: 0
  unlocks:
    - "construction_skill_tier_0"
    - "territory_claim_basic"

training_data:
  category: "temporal"
  capture_schema: "trajectory"
  notes: "Time management, resource gathering sequence, construction choices"
```

### EVENT: First Social Contact
```yaml
id: "onboard_005_social"
name: "First Social Contact"
category: "onboarding"
priority: "mvp"

trigger:
  type: "compound"
  conditions:
    - "tutorial_stage >= 4"
    - "player enters Eridu city limits"
  cooldown: "once_per_character"

codex_path:
  prerequisite: "Shelter complete OR 2 hours game time"
  discovery:
    method: "automatic"
    hint: "Gate guard addresses player"
  unlock:
    - "Codex entry: 'Social Hierarchy of Eridu'"
    - "Reputation system visible"
    - "Basic trade interaction"

narrative:
  context: "Player approaches Eridu's outer settlements"

  gate_encounter:
    npc: "City watchman (Mashkim)"
    dialogue: "Another wanderer. You have the look of the marshes about you. Speak—what brings you to Eridu?"

  options:
    - "Seeking work" → directed to Labor Pool
    - "Seeking trade" → directed to Karum
    - "Seeking knowledge" → directed to Temple
    - "Just passing through" → suspicion +10, watched status

failure:
  deadline: "None - social is optional"
  consequence: "Limited access to city services if avoided"
  severity: "minor"
  recovery: "Can engage social system anytime"

success:
  condition: "Complete one social interaction in city"
  sila_reward: 20
  karma_reward: +3
  unlocks:
    - "social_skill_tier_0"
    - "reputation_system"
    - "npc_relationship_tracking"

training_data:
  category: "social"
  capture_schema: "sft"
  notes: "Dialogue choices, social approach preference"
```

---

## Part 2: Survival Events

### EVENT: The Annual Flood (MVP Critical)
```yaml
id: "survival_001_annual_flood"
name: "The Annual Flood"
category: "survival"
priority: "mvp"

trigger:
  type: "compound"
  conditions:
    - "calendar.season == 'spring'"
    - "calendar.day >= 7"
    - "player.shelter_exists == true"
    - "OR player.days_survived >= 30"
  cooldown: "annual (once per game year)"

warning_system:
  days_before: 7
  signs:
    day_7: "River level rising visibly"
    day_5: "NPCs discussing flood preparations"
    day_3: "Animals moving to high ground"
    day_1: "Water at canal banks, urgent NPC warnings"

codex_path:
  prerequisite: "player.shelter_exists OR player heard NPC flood warning"
  discovery:
    method: "observation"
    action: "Examine riverbank when water is rising"
    minigame: "Observation check - notice erosion patterns"
  unlock:
    - "Codex entry: 'Flood Patterns of the Euphrates'"
    - "Codex entry: 'Canal Irrigation Basics'"
    - "Canal construction blueprint"
    - "Levee repair interaction"

narrative:
  context: "Spring snowmelt from northern mountains reaches Eridu"

  escalation:
    warning_phase: "7 days of rising water, increasing NPC concern"
    crisis_phase: "3 days of flooding"
    aftermath: "Assessment of damage"

failure:
  deadline: "flood_peak (Day 10 of spring)"
  consequence:
    if_no_preparation:
      - "Shelter destroyed (if low ground)"
      - "Stored food ruined (granary flooded)"
      - "Crops destroyed"
      - "Health -30 from exposure"
      - "Sanity -20 from loss"
    if_partial_preparation:
      - "50% of stored goods lost"
      - "Shelter damaged but standing"
  severity: "severe"
  recovery:
    - "Rebuild shelter (materials + 3 days)"
    - "Replant crops (seeds + full growing season)"
    - "Temple may provide emergency rations (karma cost)"

success:
  condition:
    - "player.shelter.elevation >= flood_level"
    - "OR player.canal_built == true"
    - "OR player.goods in elevated_storage"
  sila_reward: 150
  karma_reward: +10 (if helped others prepare)
  unlocks:
    - "irrigation_skill_tier_1"
    - "flood_prediction_knowledge"
    - "levee_construction"

training_data:
  category: "temporal"
  capture_schema: "trajectory"
  notes: "Preparation timeline, resource allocation, risk assessment"
```

### EVENT: Drought Warning
```yaml
id: "survival_002_drought"
name: "Drought Warning"
category: "survival"
priority: "high"

trigger:
  type: "compound"
  conditions:
    - "calendar.season == 'summer'"
    - "random_chance(0.3) per summer"  # 30% chance each summer
    - "player.days_survived >= 60"
  cooldown: "seasonal"

warning_system:
  days_before: 14
  signs:
    day_14: "Less rain than usual"
    day_10: "Canal water levels dropping"
    day_7: "Crops showing stress"
    day_3: "Rationing begins in city"

codex_path:
  prerequisite: "Player noticed canal water dropping OR NPC mentioned drought"
  discovery:
    method: "npc_conversation"
    action: "Ask farmer or Gugallu about water levels"
  unlock:
    - "Codex entry: 'Water Conservation'"
    - "Codex entry: 'Drought-Resistant Crops'"
    - "Water storage construction"
    - "Crop rotation knowledge"

failure:
  deadline: "30 days without rain + no irrigation"
  consequence:
    - "Crops die (full harvest loss)"
    - "Water sources become contested"
    - "Food prices triple"
    - "Social unrest events trigger"
  severity: "severe"
  recovery:
    - "Buy food at inflated prices"
    - "Fish/forage for subsistence"
    - "Wait for rains (random 10-30 days)"

success:
  condition:
    - "player.water_storage >= 500L"
    - "OR player.irrigation_active == true"
    - "OR player.crops == drought_resistant"
  sila_reward: 100
  karma_reward: +5
  unlocks:
    - "water_management_tier_2"
    - "agricultural_planning"

training_data:
  category: "temporal"
  capture_schema: "cot"
  notes: "Long-term planning, resource management decisions"
```

### EVENT: Disease Outbreak
```yaml
id: "survival_003_disease"
name: "Disease Outbreak"
category: "survival"
priority: "high"

trigger:
  type: "compound"
  conditions:
    - "city.population_density > threshold"
    - "calendar.season IN ['summer', 'autumn']"
    - "random_chance(0.2) per season"
    - "player.days_survived >= 45"
  cooldown: "90 days"

warning_system:
  days_before: 5
  signs:
    day_5: "NPCs coughing, looking ill"
    day_3: "Temple announces sick being brought in"
    day_1: "Player's neighborhood has visible sick"

codex_path:
  prerequisite: "Player observed sick NPC OR visited healing house"
  discovery:
    method: "observation"
    action: "Examine sick person (with Asu or alone)"
  unlock:
    - "Codex entry: 'Common Ailments'"
    - "Codex entry: 'Hygiene Practices'"
    - "Basic medicine crafting"
    - "Quarantine mechanics"

failure:
  deadline: "exposure without precaution"
  consequence:
    if_infected:
      - "Health drains over 7 days"
      - "Cannot work while sick"
      - "May die if untreated (karma dependent)"
      - "Can infect others (karma penalty -5 per infection)"
  severity: "moderate to severe"
  recovery:
    - "Visit Asu (cost: 20-50 SILA)"
    - "Visit Ashipu if Asu fails (cost: 30-100 SILA)"
    - "Rest + herbal remedy (slow, 7-14 days)"

success:
  condition:
    - "player.health > 50 during outbreak"
    - "player avoided infection OR recovered"
  sila_reward: 50
  karma_reward: +15 (if helped treat others)
  unlocks:
    - "medicine_knowledge_tier_1"
    - "disease_resistance_passive"

training_data:
  category: "ambiguity"
  capture_schema: "dpo"
  notes: "Risk assessment, helping others vs self-preservation"
```

### EVENT: Predator Attack
```yaml
id: "survival_004_predator"
name: "Predator Attack"
category: "survival"
priority: "medium"

trigger:
  type: "compound"
  conditions:
    - "player.location == outside_city"
    - "game_time > 20:00 OR game_time < 06:00"
    - "random_chance(0.15) per night outside"
  cooldown: "24 hours"

warning_system:
  seconds_before: 30
  signs:
    - "Ambient animal sounds stop"
    - "Growling in distance"
    - "Movement in tall reeds"

codex_path:
  prerequisite: "None - reactive event"
  discovery:
    method: "survival"
    action: "Survive an attack OR find predator tracks"
  unlock:
    - "Codex entry: 'Predators of the Marshes'"
    - "Torch crafting (deters predators)"
    - "Weapon effectiveness knowledge"

failure:
  deadline: "immediate combat"
  consequence:
    if_killed:
      - "Death (karma-based reincarnation)"
    if_injured:
      - "Health -20 to -60"
      - "Possible infection"
      - "Equipment damage"
  severity: "moderate to catastrophic"
  recovery:
    - "Heal injuries"
    - "Repair/replace equipment"

success:
  condition:
    - "player survives encounter"
    - "player.health > 0"
  sila_reward: 30 (escape) / 75 (kill)
  karma_reward: 0 (neutral survival)
  unlocks:
    - "combat_experience"
    - "predator_awareness_passive"

training_data:
  category: "embodied"
  capture_schema: "trajectory"
  notes: "Combat decisions, fight vs flight, resource usage"
```

---

## Part 3: Innovation Events (MVP Critical)

### EVENT: The Heavy Burden (Wheel Discovery)
```yaml
id: "innovation_001_wheel"
name: "The Heavy Burden"
category: "innovation"
priority: "mvp"

trigger:
  type: "threshold"
  conditions:
    - "player.inventory_weight > 100kg"
    - "OR player attempts to move large_object"
    - "player.days_survived >= 20"
  cooldown: "once_per_character"

narrative:
  context: "Player needs to move something too heavy to carry"

  trigger_scenarios:
    - "Harvested grain needs transport to granary"
    - "Stone blocks for construction"
    - "Trade goods to/from Karum"

codex_path:
  prerequisite: "Player experienced weight limit frustration"
  discovery:
    method: "observation_minigame"
    action: "Observe rolling log (environmental, or NPC using)"
    minigame:
      type: "physics_observation"
      task: "Notice that round objects roll easier than flat"
      hint: "A log rolls past. Something clicks..."
  unlock:
    - "Codex entry: 'The Principle of the Wheel'"
    - "Roller blueprint (intermediate step)"
    - "Axle blueprint (after roller success)"
    - "Cart blueprint (after axle)"

progression:
  step_1_roller:
    discovery: "Observe rolling"
    craft: "Cut log sections"
    use: "Roll heavy objects on logs"
    sila_reward: 50

  step_2_axle:
    discovery: "Observe that fixed axle is better than loose logs"
    craft: "Woodworking tier 2 required"
    use: "Persistent rolling platform"
    sila_reward: 100

  step_3_wheel:
    discovery: "Realize solid disk is better than log section"
    craft: "Woodworking tier 3 required"
    use: "True wheeled cart"
    sila_reward: 200

failure:
  deadline: "None - innovation is optional"
  consequence:
    - "Must carry everything by hand"
    - "Limited to ~50kg transport"
    - "Trade efficiency severely limited"
    - "Cannot complete certain quests"
  severity: "moderate (progression gate)"
  recovery: "Can discover at any time"

success:
  condition: "Player crafts functional wheeled cart"
  sila_reward: 350 (total across steps)
  karma_reward: +20
  unlocks:
    - "vehicle_construction"
    - "trade_route_creation"
    - "heavy_material_transport"

training_data:
  category: "strategy"
  capture_schema: "cot"
  notes: "Problem-solving approach, observation-to-innovation chain"
```

### EVENT: The Counting Problem (Writing Discovery)
```yaml
id: "innovation_002_writing"
name: "The Counting Problem"
category: "innovation"
priority: "mvp"

trigger:
  type: "threshold"
  conditions:
    - "player.stored_goods_types >= 5"
    - "OR player.stored_grain > 500"
    - "OR player has trade_debt > 100 SILA"
  cooldown: "once_per_character"

narrative:
  context: "Player has too much to track mentally"

  trigger_scenarios:
    - "Grain storage exceeds easy counting"
    - "Multiple trade agreements to track"
    - "Temple asks for inventory count"

codex_path:
  prerequisite: "Player experienced counting/memory failure"
  discovery:
    method: "logic_minigame"
    action: "Visit temple scribe OR observe scribe working"
    minigame:
      type: "pattern_matching"
      task: "Associate symbols with quantities"
      progression:
        - "Tokens (physical counting objects)"
        - "Token impressions in clay"
        - "Abstract symbols representing tokens"
  unlock:
    - "Codex entry: 'From Tokens to Tablets'"
    - "Clay token crafting"
    - "Clay tablet crafting"
    - "Basic numeracy symbols"

progression:
  step_1_tokens:
    discovery: "Use physical objects to represent goods"
    craft: "Shape clay tokens"
    use: "1:1 counting system"
    sila_reward: 40

  step_2_impressions:
    discovery: "Press tokens into clay for record"
    craft: "Clay tablet + stylus"
    use: "Permanent count record"
    sila_reward: 75

  step_3_symbols:
    discovery: "Realize you can draw the token shape faster"
    craft: "Cuneiform basics"
    use: "Written numeracy"
    sila_reward: 150

  step_4_language:
    discovery: "Symbols can represent sounds, not just things"
    craft: "Word signs"
    use: "True writing"
    sila_reward: 300

failure:
  deadline: "None - but theft event triggers"
  consequence:
    if_no_records:
      - "Theft event: 10-20% of untracked goods stolen"
      - "Cannot prove ownership in disputes"
      - "Cannot access Edubba or scribe profession"
      - "Trade limited to simple barter"
  severity: "moderate (economic penalty)"
  recovery: "Learn writing at any time"

success:
  condition: "Player creates valid inventory record on clay tablet"
  sila_reward: 565 (total across steps)
  karma_reward: +15
  unlocks:
    - "scribe_profession_access"
    - "contract_creation"
    - "edubba_enrollment"
    - "advanced_trade"

training_data:
  category: "strategy"
  capture_schema: "cot"
  notes: "Abstraction development, symbol-meaning association"
```

### EVENT: The Thirsty Fields (Irrigation Discovery)
```yaml
id: "innovation_003_irrigation"
name: "The Thirsty Fields"
category: "innovation"
priority: "mvp"

trigger:
  type: "compound"
  conditions:
    - "player.has_farm == true"
    - "player.crops_water_stress > 3 days"
    - "OR drought_event_active"
  cooldown: "once_per_character"

narrative:
  context: "Crops are dying from lack of water despite nearby canal"

  problem: "River floods AFTER planting, is LOW when crops need water"

codex_path:
  prerequisite: "Player has farm AND observed crop stress"
  discovery:
    method: "environmental_observation"
    action: "Study riverbank and canal system"
    minigame:
      type: "spatial_reasoning"
      task: "Trace water flow, identify gravity principles"
      hint: "The canal is higher than your field..."
  unlock:
    - "Codex entry: 'Water Flows Downhill'"
    - "Codex entry: 'Canal Irrigation'"
    - "Ditch digging tool"
    - "Sluice gate construction"

progression:
  step_1_ditch:
    discovery: "Dig channel from canal to field"
    craft: "Digging (labor)"
    problem: "Water flows uncontrolled"
    sila_reward: 50

  step_2_sluice:
    discovery: "Need to control water flow"
    craft: "Reed/mud gate"
    use: "Open/close water access"
    sila_reward: 100

  step_3_levee:
    discovery: "Need to prevent flooding"
    craft: "Earthwork construction"
    use: "Channel control"
    sila_reward: 150

failure:
  deadline: "crop_death (7 days without water)"
  consequence:
    - "Crops die (full harvest loss)"
    - "Replanting costs seeds + full season"
    - "May trigger food shortage"
  severity: "severe"
  recovery: "Replant next season with irrigation"

success:
  condition: "Crops survive to harvest with irrigation"
  sila_reward: 300 (total)
  karma_reward: +10
  unlocks:
    - "gugallu_profession_access"
    - "water_rights_system"
    - "agricultural_scaling"

training_data:
  category: "temporal"
  capture_schema: "trajectory"
  notes: "Engineering problem-solving, cause-effect reasoning"
```

### EVENT: The Soft Metal (Metallurgy Discovery)
```yaml
id: "innovation_004_metallurgy"
name: "The Soft Metal"
category: "innovation"
priority: "high"

trigger:
  type: "compound"
  conditions:
    - "player.days_survived >= 45"
    - "player has stone_tools"
    - "player encounters copper_ore OR copper_object"
  cooldown: "once_per_character"

narrative:
  context: "Player finds strange green-tinged rocks or sees metal object"

  discovery_paths:
    - "Find native copper nugget"
    - "See merchant's copper tool"
    - "Observe temple's ritual objects"

codex_path:
  prerequisite: "Player has seen copper in any form"
  discovery:
    method: "experimentation"
    action: "Heat copper ore in fire"
    minigame:
      type: "temperature_observation"
      task: "Notice copper melts, can be shaped"
  unlock:
    - "Codex entry: 'The Art of the Smith'"
    - "Crucible construction"
    - "Basic casting"

progression:
  step_1_native_copper:
    discovery: "Hammer soft native copper"
    craft: "Cold working"
    product: "Simple copper tools"
    sila_reward: 75

  step_2_smelting:
    discovery: "Heat ore to extract copper"
    craft: "Build furnace"
    product: "Refined copper"
    sila_reward: 150

  step_3_casting:
    discovery: "Pour molten copper into mold"
    craft: "Mold making"
    product: "Cast copper objects"
    sila_reward: 200

  step_4_bronze:
    discovery: "Add tin to copper"
    craft: "Alloy production"
    product: "Bronze tools/weapons"
    sila_reward: 400

failure:
  deadline: "None - optional progression"
  consequence:
    - "Stuck with stone tools"
    - "Cannot craft advanced items"
    - "Limited combat effectiveness"
    - "Cannot access smith profession"
  severity: "moderate (progression gate)"
  recovery: "Discover at any time"

success:
  condition: "Player successfully smelts copper"
  sila_reward: 825 (total across steps)
  karma_reward: +15
  unlocks:
    - "simug_profession_access"
    - "tool_upgrade_path"
    - "weapon_crafting"

training_data:
  category: "strategy"
  capture_schema: "cot"
  notes: "Experimental methodology, material science discovery"
```

---

## Part 4: Economic Events

### EVENT: First Trade
```yaml
id: "economic_001_first_trade"
name: "First Trade"
category: "economic"
priority: "high"

trigger:
  type: "compound"
  conditions:
    - "player.inventory contains tradeable_goods"
    - "player.location == karum OR player near merchant_npc"
    - "player.days_survived >= 10"
  cooldown: "once_per_character"

codex_path:
  prerequisite: "Player has surplus goods"
  discovery:
    method: "npc_interaction"
    action: "Speak with merchant in Karum"
  unlock:
    - "Codex entry: 'Trade and Barter'"
    - "Codex entry: 'Standard Weights and Measures'"
    - "Trade interface"
    - "Price awareness"

narrative:
  merchant_dialogue: "Ah, you have fish! Fresh, I see. I could offer you... hmm... two measures of barley?"

  teaching_moment:
    - "Shows exchange rate concept"
    - "Introduces negotiation"
    - "Demonstrates SILA equivalence"

failure:
  deadline: "None"
  consequence: "Goods may spoil if not traded or consumed"
  severity: "minor"
  recovery: "N/A"

success:
  condition: "Complete one barter transaction"
  sila_reward: 25
  karma_reward: +3 (fair dealing)
  unlocks:
    - "trade_skill_tier_0"
    - "price_memory"
    - "merchant_relationships"

training_data:
  category: "social"
  capture_schema: "sft"
  notes: "Negotiation patterns, value assessment"
```

### EVENT: Tappu Partnership Opportunity
```yaml
id: "economic_002_tappu"
name: "Tappu Partnership Opportunity"
category: "economic"
priority: "high"

trigger:
  type: "compound"
  conditions:
    - "player.wealth >= 500 SILA"
    - "player.reputation_merchant >= 20"
    - "player.days_survived >= 60"
  cooldown: "30 days"

codex_path:
  prerequisite: "Player has traded successfully multiple times"
  discovery:
    method: "npc_approach"
    action: "Merchant approaches with investment opportunity"
  unlock:
    - "Codex entry: 'The Tappu Partnership'"
    - "Investment interface"
    - "Risk assessment tools"

narrative:
  context: "Successful merchant seeks investment partner"

  merchant_pitch: "I have a connection in Dilmun. Copper, my friend—the temples can't get enough. But I need capital for the voyage. You provide the silver, I provide the ship and the risk. We split 60-40."

  player_choices:
    - "Invest (specify amount)"
    - "Negotiate terms"
    - "Decline"
    - "Ask for more information"

failure:
  deadline: "Decision required in 3 days"
  consequence:
    if_declined: "Opportunity passes, no penalty"
    if_invested_and_fails:
      - "Lose invested capital"
      - "No karma penalty (honest loss)"
  severity: "moderate (economic risk)"
  recovery: "Wait for next opportunity"

success:
  condition: "Investment returns profit"
  sila_reward: "30-300% of investment (variable)"
  karma_reward: +5 (successful partnership)
  unlocks:
    - "damgar_profession_access"
    - "long_distance_trade_knowledge"
    - "investment_mechanics"

training_data:
  category: "ambiguity"
  capture_schema: "dpo"
  notes: "Risk assessment, trust evaluation, negotiation"
```

### EVENT: Market Crash
```yaml
id: "economic_003_crash"
name: "Market Crash"
category: "economic"
priority: "medium"

trigger:
  type: "compound"
  conditions:
    - "global.trade_volume > threshold"
    - "random_event_seed matches"
    - "player.days_survived >= 90"
  cooldown: "180 days"

warning_system:
  days_before: 7
  signs:
    - "Merchants seem nervous"
    - "Prices fluctuating wildly"
    - "Rumors of caravan losses"

codex_path:
  prerequisite: "Player engaged in trade economy"
  discovery:
    method: "observation"
    action: "Notice price instability"
  unlock:
    - "Codex entry: 'Economic Cycles'"
    - "Price history tracking"

failure:
  deadline: "crash_event"
  consequence:
    - "All goods lose 50% value temporarily"
    - "Outstanding contracts may default"
    - "Some merchants disappear"
  severity: "moderate to severe"
  recovery: "Wait 30 days for stabilization"

success:
  condition: "Player maintains solvency OR profits from crash"
  sila_reward: 100 (survival) / 500+ (profiting)
  karma_reward: +10 (if helped others) / -20 (if exploited)
  unlocks:
    - "economic_resilience"
    - "market_timing_knowledge"

training_data:
  category: "temporal"
  capture_schema: "cot"
  notes: "Economic reasoning, crisis response"
```

---

## Part 5: Social Events

### EVENT: Temple Tithe Demand
```yaml
id: "social_001_tithe"
name: "Temple Tithe Demand"
category: "social"
priority: "high"

trigger:
  type: "time"
  conditions:
    - "calendar.day == 1 of month"
    - "player.wealth > 0"
    - "player.days_survived >= 30"
  cooldown: "monthly"

narrative:
  context: "Temple priest arrives to collect monthly offering"

  priest_dialogue: "The gods have blessed you with another month of life. Enki's temple requires its due. The tithe is one-tenth of your increase."

codex_path:
  prerequisite: "None - mandatory event"
  discovery:
    method: "automatic"
  unlock:
    - "Codex entry: 'Temple Obligations'"
    - "Tithe tracking"

player_options:
  - "Pay full tithe" → karma +3, temple_favor +5
  - "Pay partial" → karma 0, temple_favor -5
  - "Refuse" → karma -10, temple_favor -20
  - "Claim poverty (if true)" → karma 0, temple_favor 0
  - "Claim poverty (if false)" → karma -15, temple_favor -10 when discovered

failure:
  deadline: "3 days after demand"
  consequence:
    if_refused:
      - "Temple disfavor"
      - "Sanity drain +2/day"
      - "NPC reactions worsen"
      - "Cannot access temple services"
  severity: "moderate"
  recovery: "Pay double next month + apology"

success:
  condition: "Pay tithe"
  sila_reward: 0 (cost, not reward)
  karma_reward: +3
  unlocks:
    - "temple_favor_benefits"
    - "priestly_interactions"

training_data:
  category: "ambiguity"
  capture_schema: "dpo"
  notes: "Religious obligation vs economic self-interest"
```

### EVENT: Neighbor Dispute
```yaml
id: "social_002_dispute"
name: "Neighbor Dispute"
category: "social"
priority: "medium"

trigger:
  type: "compound"
  conditions:
    - "player.has_property == true"
    - "random_chance(0.1) per week"
    - "player.days_survived >= 45"
  cooldown: "30 days"

narrative:
  context: "Neighbor accuses player of boundary violation or damage"

  dispute_types:
    - "Your irrigation flooded my field!"
    - "Your wall is on my land!"
    - "Your animals ate my crops!"

codex_path:
  prerequisite: "None - reactive event"
  discovery:
    method: "automatic"
  unlock:
    - "Codex entry: 'Property Law in Eridu'"
    - "Legal system interface"

player_options:
  - "Apologize and compensate"
  - "Deny and argue"
  - "Propose compromise"
  - "Demand court hearing"
  - "Threaten neighbor"

failure:
  deadline: "7 days to resolve"
  consequence:
    if_unresolved:
      - "Neighbor takes to court"
      - "May lose case + pay damages"
      - "Reputation damage"
      - "Ongoing hostility"
  severity: "moderate"
  recovery: "Court settlement"

success:
  condition: "Dispute resolved peacefully"
  sila_reward: 20 (negotiation success)
  karma_reward: +5 (fair resolution) / -10 (bullying)
  unlocks:
    - "negotiation_skill"
    - "legal_awareness"

training_data:
  category: "social"
  capture_schema: "sft"
  notes: "Conflict resolution, social negotiation"
```

### EVENT: Labor Corvée Call
```yaml
id: "social_003_corvee"
name: "Labor Corvée Call"
category: "social"
priority: "high"

trigger:
  type: "time"
  conditions:
    - "calendar.season == 'dry_season'"
    - "player.land_owner == true"
    - "player.days_survived >= 60"
  cooldown: "annual"

narrative:
  context: "City calls all landowners for mandatory canal maintenance"

  herald_announcement: "By order of the Ensi! All holders of irrigated land must report to the canal head for silt removal. Three days' labor is required."

codex_path:
  prerequisite: "Player owns land"
  discovery:
    method: "automatic"
  unlock:
    - "Codex entry: 'Corvée Labor System'"
    - "Water rights understanding"

player_options:
  - "Attend and work" → karma +5, community standing +10
  - "Send substitute (if available)" → karma 0, cost: wages
  - "Claim exemption (medical)" → karma 0 if true, -10 if false
  - "Refuse" → karma -15, water rights revoked

failure:
  deadline: "Corvée period (3 days)"
  consequence:
    if_refused:
      - "Water rights suspended"
      - "Community shunning"
      - "Legal fines"
      - "Crops may die"
  severity: "severe"
  recovery: "Pay fine + double labor next season"

success:
  condition: "Complete corvée labor"
  sila_reward: 45 (15/day)
  karma_reward: +5
  unlocks:
    - "community_standing"
    - "water_allocation_rights"
    - "infrastructure_knowledge"

training_data:
  category: "ambiguity"
  capture_schema: "dpo"
  notes: "Civic duty vs personal interest, community obligations"
```

---

## Part 6: Mystery Events (Anunnaki Layer)

### EVENT: Strange Metal Fragment
```yaml
id: "mystery_001_fragment"
name: "Strange Metal Fragment"
category: "mystery"
priority: "low"

trigger:
  type: "compound"
  conditions:
    - "player.location == deep_mine OR player.location == ancient_ruins"
    - "random_chance(0.05) per visit"
    - "player.anunnaki_fragments < 7"
  cooldown: "7 days"

narrative:
  context: "Player finds metal that shouldn't exist"

  discovery: "Among the rocks, something glints. It's metal, but... wrong. Too light. Too smooth. It hums faintly when you touch it."

codex_path:
  prerequisite: "None - discovery event"
  discovery:
    method: "found_object"
  unlock:
    - "Codex entry: 'Unknown Artifacts' (partial)"
    - "Fragment added to inventory"
    - "If fragment #7: Anunnaki quest unlocks"

narrative_hints:
  fragment_1: "The metal is impossibly pure."
  fragment_3: "You've seen this material before..."
  fragment_5: "The fragments seem to... resonate together."
  fragment_7: "A vision flashes—mountains, a dark entrance, something waiting."

failure:
  deadline: "None"
  consequence: "None - optional content"
  severity: "none"
  recovery: "N/A"

success:
  condition: "Fragment collected"
  sila_reward: 50
  karma_reward: 0
  unlocks:
    - "anunnaki_awareness +1"
    - "If all 7: anunnaki_quest_available"

training_data:
  category: "temporal"
  capture_schema: "trajectory"
  notes: "Exploration patterns, mystery engagement"
```

### EVENT: Sailor's Tale (Anunnaki Clue)
```yaml
id: "mystery_002_sailor"
name: "Sailor's Tale"
category: "mystery"
priority: "low"

trigger:
  type: "compound"
  conditions:
    - "player.location == tavern near karum"
    - "game_time > 20:00"
    - "random_chance(0.1) per tavern visit"
    - "player.anunnaki_clues.sailor == false"
  cooldown: "once_per_character"

narrative:
  context: "Drunk sailor tells strange story"

  sailor_dialogue: "You want to hear something? Something no one believes? I was off Dilmun, five years back. Middle of the night. The sky... the sky lit up. Not lightning—something moving. Too fast, too bright. And the old trader I was with, he just nodded. Said his grandfather told him about the 'sky chariots.' Said they came from a place called... Nibiru? I don't know. Pass me that beer."

codex_path:
  prerequisite: "Player in tavern at night"
  discovery:
    method: "npc_conversation"
  unlock:
    - "Codex entry: 'Strange Tales from the Sea'"
    - "Anunnaki clue #2"

failure:
  deadline: "None"
  consequence: "Miss clue, can potentially find elsewhere"
  severity: "none"
  recovery: "Other clue sources exist"

success:
  condition: "Listen to full tale"
  sila_reward: 10
  karma_reward: 0
  unlocks:
    - "anunnaki_clue_sailor"

training_data:
  category: "social"
  capture_schema: "sft"
  notes: "Information gathering, NPC interaction"
```

---

## Part 7: Ascension Events

### EVENT: Pillar Complete Notification
```yaml
id: "ascension_001_pillar"
name: "Pillar Complete"
category: "ascension"
priority: "high"

trigger:
  type: "threshold"
  conditions:
    - "player completes any of the 5 pillars"
  cooldown: "once per pillar"

narrative:
  context: "Player achieves major milestone"

  notification: "A sense of completion washes over you. The [PILLAR_NAME] is fulfilled. [4/3/2/1/0] pillars remain."

  if_pillar_5:
    special_dialogue: "The Temple of Enki pulses with light only you can see. A priest approaches—there is knowing in his eyes."

codex_path:
  prerequisite: "N/A"
  discovery:
    method: "automatic"
  unlock:
    - "Ascension progress tracking visible"
    - "If all 5: ascension_ceremony_available"

failure:
  deadline: "None"
  consequence: "Cannot ascend until complete"
  severity: "progression_gate"
  recovery: "Complete remaining pillars"

success:
  condition: "Pillar requirements met"
  sila_reward: "Pillar-specific (see ascension-karma.md)"
  karma_reward: "Pillar-specific"
  unlocks:
    - "Pillar-specific rewards"

training_data:
  category: "temporal"
  capture_schema: "cot"
  notes: "Goal progress, milestone achievement patterns"
```

### EVENT: Ascension Ceremony
```yaml
id: "ascension_002_ceremony"
name: "Ascension Ceremony"
category: "ascension"
priority: "high"

trigger:
  type: "threshold"
  conditions:
    - "all 5 pillars complete"
    - "player initiates ceremony at temple"
  cooldown: "once_per_era"

narrative:
  context: "Player ready to leave Ancient Era"

  ceremony_sequence:
    1: "Temple priests gather"
    2: "Player's achievements recited"
    3: "Legacy transfer confirmed"
    4: "Ritual of passage"
    5: "Vision of next era"
    6: "Transition"

codex_path:
  prerequisite: "All 5 pillars"
  discovery:
    method: "automatic"
  unlock:
    - "Next era access"
    - "Ascension NFT"

failure:
  deadline: "None - optional"
  consequence: "Remain in Ancient Era (valid choice)"
  severity: "none"
  recovery: "Can ascend whenever ready"

success:
  condition: "Complete ceremony"
  sila_reward: 1000
  karma_reward: +50
  unlocks:
    - "Next era character creation"
    - "Legacy bonuses active"
    - "Era-specific title"

training_data:
  category: "temporal"
  capture_schema: "trajectory"
  notes: "Era completion, long-term goal achievement"
```

---

## Implementation Notes

### Director AI Integration

```yaml
director_integration:
  event_queue:
    priority_order: ["mvp", "high", "medium", "low"]
    concurrent_limit: 3  # Max active events

  trigger_evaluation:
    frequency: "every 60 game-seconds"
    batch_check: true  # Check all triggers at once

  difficulty_scaling:
    player_skill_factor: true
    karma_factor: true
    time_pressure_factor: true

  training_data_tagging:
    auto_tag: true  # Tag all captured data with event_id
    quality_threshold: 0.7  # Minimum quality score to keep
```

### Database Schema Additions

```yaml
event_schema:
  event_instance:
    instance_id: uuid
    event_id: string  # Reference to this spec
    player_id: uuid
    trigger_time: datetime
    status: enum  # triggered, active, success, failure, expired
    player_response: jsonb
    outcome: object
    training_data_id: uuid
```

---

## Appendix: Event ID Quick Reference

| ID | Name | Category | Priority |
|----|------|----------|----------|
| onboard_001 | First Awakening | onboarding | mvp |
| onboard_002 | First Thirst | onboarding | mvp |
| onboard_003 | First Hunger | onboarding | mvp |
| onboard_004 | First Shelter | onboarding | mvp |
| onboard_005 | First Social | onboarding | mvp |
| survival_001 | Annual Flood | survival | mvp |
| survival_002 | Drought | survival | high |
| survival_003 | Disease | survival | high |
| survival_004 | Predator | survival | medium |
| innovation_001 | Wheel | innovation | mvp |
| innovation_002 | Writing | innovation | mvp |
| innovation_003 | Irrigation | innovation | mvp |
| innovation_004 | Metallurgy | innovation | high |
| economic_001 | First Trade | economic | high |
| economic_002 | Tappu | economic | high |
| economic_003 | Market Crash | economic | medium |
| social_001 | Temple Tithe | social | high |
| social_002 | Neighbor Dispute | social | medium |
| social_003 | Corvée | social | high |
| mystery_001 | Strange Fragment | mystery | low |
| mystery_002 | Sailor's Tale | mystery | low |
| ascension_001 | Pillar Complete | ascension | high |
| ascension_002 | Ceremony | ascension | high |

---

*"This is the Director's script. Every event, every trigger, every consequence—documented and ready for implementation. The narrative is no longer just story; it is now code."*
