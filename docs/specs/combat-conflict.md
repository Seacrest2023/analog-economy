# Combat & Conflict: The Art of War in Eridu

> "War is the continuation of water rights by other means."

## Table of Contents

1. [Overview](#1-overview)
2. [Design Philosophy](#2-design-philosophy)
3. [Causes of Conflict](#3-causes-of-conflict)
4. [Combat Scenarios](#4-combat-scenarios)
5. [Battle Mechanics](#5-battle-mechanics)
6. [Weapons & Equipment](#6-weapons--equipment)
7. [Siege Warfare](#7-siege-warfare)
8. [Personal Combat](#8-personal-combat)
9. [Consequences of Violence](#9-consequences-of-violence)
10. [Defense & Protection](#10-defense--protection)
11. [The Warfare Calendar](#11-the-warfare-calendar)
12. [Training Data Value](#12-training-data-value)
13. [Implementation Notes](#13-implementation-notes)

---

## 1. Overview

Combat in The Analog Economy reflects historical reality: organized warfare between city-states, not individual murder simulators. Violence has severe consequences, battles are seasonal and strategic, and most conflicts are resolved through economics, not bloodshed.

### Core Principles

| Principle | Implementation |
|-----------|----------------|
| **Organized over chaotic** | Wars are declared between settlements, not random PvP |
| **Seasonal warfare** | Combat happens in spring, after planting/before harvest |
| **Economic roots** | Most wars are about water, land, or trade routes |
| **Phalanx over dueling** | Group tactics matter more than individual skill |
| **Consequences are real** | Violence triggers karma, NPC response, and legal penalties |

---

## 2. Design Philosophy

### 2.1 The "Dueling" Myth - Debunked

While myths like the Epic of Gilgamesh depict heroes in single combat, historical records tell a different story:

```yaml
myth_vs_reality:
  the_myth:
    - "Heroes fight one-on-one duels"
    - "Individual skill decides battles"
    - "Champions determine fate of armies"
    - "Combat is glorious and honorable"

  the_reality:
    - "Armies fought in tight phalanx formations"
    - "Individual soldiers who broke ranks died quickly"
    - "Battles were won by mass, discipline, and momentum"
    - "Combat was brutal, short, and decisive"
    - "Most casualties occurred during the rout"

  gameplay_implication: |
    A lone player challenging a phalanx will be swarmed and killed.
    Combat rewards cooperation, formation, and strategy—not
    "main character" heroics.
```

### 2.2 Violence Has Weight

The game does not glorify violence. It presents it as:

- **Costly** - Equipment, time, health, karma
- **Consequential** - Legal, social, and spiritual penalties
- **Strategic** - A tool for achieving goals, not entertainment
- **Rare** - Most gameplay is economic and social

```yaml
violence_weight:
  every_kill_costs:
    - "Karma penalty (affects reincarnation)"
    - "Witness strain (trauma accumulates)"
    - "Potential legal consequences"
    - "Reputation effects (positive or negative)"
    - "Equipment wear and damage"

  exception_warfare:
    - "Declared wars have reduced karma penalty"
    - "Defending your settlement is karma-neutral"
    - "Temple-sanctioned wars have divine blessing"
```

### 2.3 Training Data Goals

```yaml
training_data_from_combat:
  questions_studied:
    - "How do humans coordinate in violent conflict?"
    - "What causes escalation vs de-escalation?"
    - "How do groups form defensive alliances?"
    - "What makes some players choose violence, others diplomacy?"
    - "How do consequences affect future behavior?"

  valuable_scenarios:
    - "Resource scarcity driving conflict decisions"
    - "Alliance formation under threat"
    - "Leadership emergence in crisis"
    - "Moral reasoning about violence"
    - "Post-conflict reconciliation"
```

---

## 3. Causes of Conflict

### 3.1 Primary Causes (Historical)

```yaml
conflict_causes:
  water_rights:
    frequency: "Most common"
    description: |
      Upriver cities (like Umma) block canals or build new ones to
      "starve" downriver cities (like Lagash or Eridu) of water.
    escalation_path:
      1: "Diplomatic complaint to Temple"
      2: "Economic sanctions (trade embargo)"
      3: "Sabotage (canal destruction at night)"
      4: "Declared war"
    gameplay: |
      Players controlling water sources have enormous power.
      Water theft is a legitimate casus belli.

  border_disputes:
    frequency: "Common"
    description: |
      Conflicts over fertile "no-man's land" between settlements,
      marked by boundary stones that are frequently moved or destroyed.
    escalation_path:
      1: "Surveyors dispute (Sa-gid investigation)"
      2: "Temple arbitration"
      3: "Tit-for-tat harassment"
      4: "Armed conflict"
    gameplay: |
      Moving boundary stones is a crime that can trigger war.
      Land disputes require witnesses and documentation.

  divine_will:
    frequency: "Occasional"
    description: |
      War as a struggle between patron deities. A city's defeat means
      their god has temporarily abandoned them.
    trigger:
      - "Priests declare enemy city has offended the gods"
      - "Omens interpreted as call to war"
      - "Temple demands conquest of rival shrine"
    gameplay: |
      High Temple favor can trigger or prevent "holy wars."
      Defeating an enemy can capture their divine statues.

  trade_disruption:
    frequency: "Occasional"
    description: |
      Cutting off trade routes, piracy on the rivers, or caravan raids.
    escalation_path:
      1: "Complaints to merchants guild"
      2: "Armed escorts for caravans"
      3: "Retaliatory raids"
      4: "Full trade war"
    gameplay: |
      Merchants may hire players as guards or raiders.
      Trade wars affect prices throughout the region.

  succession_crisis:
    frequency: "Rare but dramatic"
    description: |
      When a Lugal dies without clear heir, rival factions fight
      for control of the city.
    trigger:
      - "Ruler death without designated successor"
      - "Rival claimants with military backing"
      - "External powers supporting different factions"
    gameplay: |
      Players can back different claimants.
      Civil wars are the most destructive conflicts.
```

### 3.2 Conflict Escalation Ladder

```
TENSION LEVEL          ACTIONS AVAILABLE
─────────────────────────────────────────────────────────

[1] PEACEFUL           Normal trade, movement, interaction
     │
     ▼
[2] DISPUTE            Diplomatic complaints, trade restrictions
     │                 No violence, legal channels only
     ▼
[3] HOSTILE            Embargoes, sabotage, spying
     │                 Covert action, no open combat
     ▼
[4] SKIRMISH           Border raids, caravan attacks
     │                 Limited violence, deniable
     ▼
[5] DECLARED WAR       Open battle, siege, conquest
     │                 Full military engagement
     ▼
[6] TOTAL WAR          City destruction, enslavement
                       Rare, catastrophic, divine punishment risk
```

---

## 4. Combat Scenarios

### 4.1 Organized Warfare (Primary)

```yaml
organized_warfare:
  description: |
    The primary form of combat in the game. Wars are declared between
    settlements (player-run or NPC city-states) and follow rules.

  declaration_requirements:
    - "Settlement leader (Lugal) must declare"
    - "Reason (casus belli) must be stated publicly"
    - "3-day warning period before hostilities begin"
    - "Temple must be notified (record keeping)"

  battle_types:
    open_field:
      description: "Phalanx vs phalanx in agreed location"
      typical_size: "50-500 combatants per side"
      duration: "1-4 hours real-time"
      outcome: "Determined by formation breaks, not kills"

    siege:
      description: "Attacking a fortified settlement"
      typical_duration: "Days to weeks"
      methods: ["Assault", "Starvation", "Negotiated surrender"]
      outcome: "Walls breached, supplies exhausted, or terms accepted"

    raid:
      description: "Quick strike on vulnerable target"
      typical_size: "5-50 raiders"
      targets: ["Farms", "Caravans", "Outlying structures"]
      outcome: "Loot acquired, damage done, withdrawal"

  who_fights:
    professional_soldiers: "NPCs maintained by settlements"
    militia: "Players and NPCs called up for defense/offense"
    mercenaries: "Hired fighters (NPCs or players)"
```

### 4.2 Personal Combat (Secondary)

```yaml
personal_combat:
  description: |
    Individual violence outside organized warfare. Rare, dangerous,
    and heavily penalized by karma and law.

  legal_scenarios:
    self_defense:
      trigger: "Another player/NPC attacks you first"
      karma_impact: "None if proportional response"
      legal_status: "Protected, attacker faces consequences"

    property_defense:
      trigger: "Thief or raider on your land"
      karma_impact: "None for non-lethal, minor for lethal"
      legal_status: "Protected within your property"

    ritual_duel:
      trigger: "Both parties formally agree to combat"
      karma_impact: "Reduced (sanctioned violence)"
      legal_status: "Legal if witnessed and agreed"
      purpose: "Settle disputes, prove honor"

  illegal_scenarios:
    murder:
      definition: "Killing without legal justification"
      karma_impact: "Severe (-50 to -100 karma)"
      legal_status: "Hunted by authorities, blood price owed"
      consequence: "NPCs turn hostile, exile, or execution"

    assault:
      definition: "Attacking without killing"
      karma_impact: "Moderate (-10 to -30 karma)"
      legal_status: "Fined, possible imprisonment"

    banditry:
      definition: "Robbery with violence"
      karma_impact: "Severe (-30 to -60 karma)"
      legal_status: "Outlawed, kill on sight"
```

---

## 5. Battle Mechanics

### 5.1 The Phalanx System

```yaml
phalanx_formation:
  description: |
    The dominant military formation of the era. Soldiers form tight
    ranks with overlapping shields, presenting a wall of spears.

  structure:
    depth: "6 ranks deep"
    width: "Variable based on army size"
    spacing: "Shoulder to shoulder, shields overlapping"

  roles:
    front_rank:
      name: "The Face"
      equipment: "Heavy shield, short spear"
      role: "Absorb impact, hold the line"
      danger: "Highest casualties"

    middle_ranks:
      name: "The Push"
      equipment: "Shield, long spear"
      role: "Add mass, push forward, stab over shoulders"
      danger: "Moderate"

    rear_ranks:
      name: "The Reserve"
      equipment: "Variable"
      role: "Replace fallen, prevent flank attacks"
      danger: "Lower until formation breaks"

  gameplay_mechanics:
    formation_integrity:
      description: "Health bar for the entire formation"
      factors:
        - "Number of soldiers"
        - "Training level"
        - "Morale"
        - "Terrain"
      when_breaks: "Formation scatters, soldiers become vulnerable"

    the_push:
      description: "Phalanxes 'shove' each other"
      mechanic: "Combined strength vs combined strength"
      outcome: "Weaker side pushed back, eventually breaks"

    flanking:
      description: "Attacking the phalanx from side or rear"
      effect: "Massive damage to formation integrity"
      counter: "Reserve troops, wider formation, refused flank"
```

### 5.2 Battle Flow

```yaml
battle_phases:
  phase_1_skirmish:
    duration: "10-20 minutes"
    actions:
      - "Armies deploy at distance (~300 feet)"
      - "Archers and slingers exchange missiles"
      - "Light troops probe for weakness"
      - "Commanders observe and adjust"
    casualties: "Light (5-10%)"
    decision_point: "Commit to engagement or withdraw?"

  phase_2_advance:
    duration: "5-10 minutes"
    actions:
      - "Phalanxes advance toward each other"
      - "War wagons move to flanks (if available)"
      - "Missile fire intensifies"
      - "Morale checks begin"
    casualties: "Moderate (10-15%)"
    decision_point: "Which flank to weight? Where to strike?"

  phase_3_clash:
    duration: "15-45 minutes"
    actions:
      - "Shield walls collide"
      - "The 'push' begins"
      - "Casualties mount in front ranks"
      - "Flanking attempts"
    casualties: "Heavy (20-40%)"
    decision_point: "Hold the line or commit reserves?"

  phase_4_break:
    duration: "Variable"
    trigger: "One side's formation integrity fails"
    actions:
      - "Broken formation scatters"
      - "Victors pursue"
      - "Massacre of the routing"
    casualties: "Most deaths occur here (50-80% of total)"
    decision_point: "How far to pursue? Take prisoners?"

  phase_5_aftermath:
    duration: "Hours to days"
    actions:
      - "Collect wounded"
      - "Strip the dead (equipment)"
      - "Count casualties"
      - "Negotiate terms (if siege avoided)"
    outcomes:
      - "Victor claims disputed territory"
      - "Loser pays tribute or surrenders"
      - "Prisoners ransomed or enslaved"
```

### 5.3 Individual Roles in Battle

```yaml
battle_roles:
  commander:
    requirements: "High reputation, leadership experience"
    abilities:
      - "Issue formation commands"
      - "Boost morale (aura effect)"
      - "Call strategic retreats"
    position: "Behind lines or on war wagon"
    death_effect: "Massive morale penalty to army"

  line_soldier:
    requirements: "Basic training, equipment"
    abilities:
      - "Hold position in formation"
      - "Follow commands"
      - "Individual combat if formation breaks"
    position: "In the phalanx"
    death_effect: "Weakens formation"

  skirmisher:
    requirements: "Bow/sling skill, mobility"
    abilities:
      - "Ranged attacks before/during battle"
      - "Harass flanks"
      - "Scout enemy positions"
    position: "Loose formation, flanks, front (early)"
    death_effect: "Minor tactical loss"

  support:
    requirements: "Medical, logistics skills"
    abilities:
      - "Drag wounded to safety"
      - "Provide water/supplies"
      - "Treat injuries during lulls"
    position: "Behind lines"
    death_effect: "Reduced army sustainability"
```

---

## 6. Weapons & Equipment

### 6.1 Infantry Weapons

```yaml
infantry_weapons:
  spear:
    types:
      short_spear:
        length: "1.5-2 meters"
        use: "Front rank, close combat"
        skill_required: "Basic"
        damage: "Moderate piercing"

      long_spear:
        length: "2.5-3 meters"
        use: "Middle ranks, over-shoulder attacks"
        skill_required: "Intermediate"
        damage: "High piercing"

    advantages: "Reach, formation synergy"
    disadvantages: "Useless if enemy closes inside reach"

  axe:
    types:
      copper_axe:
        weight: "1-2 kg"
        use: "Chopping, shield breaking"
        skill_required: "Basic"
        damage: "High slashing"

      bronze_socketed_axe:
        weight: "1.5-2.5 kg"
        use: "Premium weapon, unbreakable"
        skill_required: "Intermediate"
        damage: "Very high slashing"

    advantages: "Devastating against unarmored, breaks shields"
    disadvantages: "Short reach, tiring to use"

  mace:
    types:
      stone_mace:
        weight: "1-1.5 kg"
        use: "Crushing helmets, stunning"
        skill_required: "Basic"
        damage: "High blunt"

      copper_mace:
        weight: "1.5-2 kg"
        use: "Premium crushing weapon"
        skill_required: "Intermediate"
        damage: "Very high blunt"

    advantages: "Effective against helmets, intimidating"
    disadvantages: "Heavy, slow"

  dagger:
    use: "Last resort, finishing wounded"
    skill_required: "Basic"
    damage: "Low piercing"
    note: "Every soldier carries one"
```

### 6.2 Ranged Weapons

```yaml
ranged_weapons:
  composite_bow:
    range: "100-150 meters effective"
    damage: "Moderate piercing"
    rate_of_fire: "6-10 arrows/minute"
    skill_required: "High (years of training)"
    materials: "Wood, horn, sinew, glue"
    cost: "Expensive (imported materials)"
    role: "Elite skirmishers, chariot troops"

  simple_bow:
    range: "50-80 meters effective"
    damage: "Low piercing"
    rate_of_fire: "8-12 arrows/minute"
    skill_required: "Intermediate"
    materials: "Wood"
    cost: "Moderate"
    role: "Common skirmishers, hunters"

  sling:
    range: "50-100 meters effective"
    damage: "Moderate blunt"
    rate_of_fire: "4-6 stones/minute"
    skill_required: "Intermediate (but common)"
    materials: "Leather, cord"
    cost: "Cheap"
    role: "Mass skirmishers, shepherds turned soldiers"
    note: "Surprisingly deadly—stones can crack skulls"

  javelin:
    range: "20-40 meters"
    damage: "High piercing"
    rate_of_fire: "1-2 throws then melee"
    skill_required: "Basic"
    materials: "Wood, copper/bronze tip"
    cost: "Moderate"
    role: "Opening volley before charge"
```

### 6.3 Defensive Equipment

```yaml
defensive_equipment:
  shields:
    rectangular_shield:
      description: "The phalanx shield"
      size: "Covers torso to knees"
      material: "Wicker frame, leather cover"
      weight: "3-5 kg"
      protection: "Excellent frontal coverage"
      mobility: "Reduced (meant for formation)"

    round_shield:
      description: "Skirmisher/individual shield"
      size: "60-80 cm diameter"
      material: "Wood, leather"
      weight: "2-3 kg"
      protection: "Good all-around"
      mobility: "Better than rectangular"

  helmets:
    copper_helmet:
      protection: "Head, partial face"
      weight: "1-1.5 kg"
      cost: "Expensive"
      availability: "Officers, elite troops"

    leather_cap:
      protection: "Head (padding only)"
      weight: "0.3-0.5 kg"
      cost: "Cheap"
      availability: "Common soldiers"

  body_armor:
    note: "Full body armor is rare in this era"
    options:
      leather_vest: "Basic protection, common"
      copper_scales: "Good protection, expensive, elite only"
      felt_padding: "Minimal protection, better than nothing"
```

---

## 7. Siege Warfare

### 7.1 Fortifications

```yaml
fortifications:
  city_walls:
    construction: "Mud-brick, 5-7 meters high"
    thickness: "2-3 meters at base"
    features:
      - "Towers at intervals for archer coverage"
      - "Battlements for defender protection"
      - "Narrow gates (chokepoints)"
      - "Moat or ditch in front (some cities)"

  defensive_advantages:
    - "Attackers exposed during approach"
    - "Defenders have height advantage"
    - "Walls absorb arrows and stones"
    - "Gates create fatal funnels"

  weaknesses:
    - "Mud-brick can be undermined"
    - "Walls crumble if not maintained"
    - "Prolonged siege exhausts food/water"
    - "Treachery from within"
```

### 7.2 Siege Tactics

```yaml
siege_tactics:
  assault:
    methods:
      scaling_ladders:
        description: "Rush walls with ladders"
        risk: "Very high casualties"
        speed: "Fast if successful"
        counter: "Push ladders off, drop stones"

      battering_ram:
        description: "Break down gates"
        construction: "Large log, wheeled frame, roof"
        risk: "Moderate (protected crew)"
        speed: "Slow but reliable"
        counter: "Fire, stones, sorties"

      sapping:
        description: "Tunnel under walls to collapse"
        construction: "Dig tunnel, burn supports"
        risk: "Low (underground)"
        speed: "Very slow (weeks)"
        counter: "Counter-tunnels, flooding"

  blockade:
    description: "Surround and starve"
    requirements:
      - "Larger army than defenders"
      - "Control of water sources"
      - "Time (weeks to months)"
    outcome: "Defenders eventually surrender or die"
    counter: "Stored supplies, relief army, breakout"

  negotiation:
    description: "Offer terms to avoid bloodshed"
    common_terms:
      - "Tribute payment"
      - "Hostages"
      - "Territory concession"
      - "Marriage alliance"
    advantage: "Both sides avoid casualties"
    risk: "Terms may be unfavorable"
```

### 7.3 Player Roles in Sieges

```yaml
siege_roles:
  attacking_players:
    - "Join assault teams (high risk, high reward)"
    - "Operate siege equipment"
    - "Scout for weak points"
    - "Sabotage supplies during blockade"
    - "Negotiate terms as emissary"

  defending_players:
    - "Man the walls (archer, stone dropper)"
    - "Lead sorties against siege equipment"
    - "Maintain morale of defenders"
    - "Manage dwindling supplies"
    - "Seek terms or plan escape"

  duration_expectation:
    assault: "1-4 hours real-time"
    blockade: "Days to weeks (accelerated)"
    negotiation: "Variable (player-driven)"
```

---

## 8. Personal Combat

### 8.1 When Formations Break

```yaml
broken_formation_combat:
  description: |
    When a phalanx breaks, soldiers become individuals.
    This is the most dangerous moment of any battle.

  mechanics:
    - "Stamina matters (exhaustion from formation fighting)"
    - "Weapon skills become relevant"
    - "Armor/shields provide survival time"
    - "Numbers still matter (2v1 is deadly)"

  survival_strategies:
    stay_grouped: "Find allies, reform mini-formations"
    flee_smart: "Run toward friendly lines, not open ground"
    surrender: "Drop weapons, kneel (if enemy takes prisoners)"
    last_stand: "Back to wall, sell your life dearly"
```

### 8.2 Individual Combat Mechanics

```yaml
individual_combat:
  attributes:
    stamina:
      description: "Energy for attacks and defense"
      depletion: "Every action costs stamina"
      recovery: "Rest, but vulnerable while recovering"
      zero_stamina: "Cannot attack, defense severely impaired"

    stance:
      aggressive: "More damage, less defense"
      balanced: "Standard combat"
      defensive: "Less damage, more defense"
      recovering: "No combat, stamina recovery"

  actions:
    attack:
      light: "Fast, low damage, low stamina cost"
      heavy: "Slow, high damage, high stamina cost"
      special: "Weapon-specific techniques (trained)"

    defense:
      block: "Use shield/weapon to stop attack"
      parry: "Deflect attack, create opening"
      dodge: "Avoid attack entirely (stamina intensive)"

    other:
      grapple: "Close-range wrestling"
      disengage: "Create distance"
      surrender: "End combat, accept consequences"

  damage_system:
    wounds:
      minor: "Scratches, bruises (-5% effectiveness)"
      moderate: "Cuts, sprains (-25% effectiveness)"
      severe: "Deep wounds, fractures (-50%, bleeding)"
      critical: "Mortal wound (death without treatment)"

    armor_mitigation:
      - "Armor reduces damage by percentage"
      - "Armor has durability (degrades with hits)"
      - "Location matters (head hits worse than arm)"
```

### 8.3 Ritual Duels

```yaml
ritual_duel:
  description: |
    A formal, consensual combat to settle disputes.
    Historically rare but present in the mythology.

  requirements:
    - "Both parties must agree (in-game contract)"
    - "Witness must be present (NPC or player)"
    - "Terms must be stated (to the death, first blood, submission)"
    - "Weapons must be agreed upon"

  process:
    1: "Challenge issued publicly"
    2: "Terms negotiated"
    3: "Witness secured"
    4: "Combat occurs"
    5: "Winner claims agreed stakes"

  stakes_examples:
    - "Land dispute settled"
    - "Debt cancelled"
    - "Honor restored"
    - "Marriage rights"
    - "Position in hierarchy"

  karma_impact: "Minimal (sanctioned violence)"

  refusing_challenge:
    - "No direct penalty"
    - "Reputation damage (coward)"
    - "Dispute remains unresolved"
```

---

## 9. Consequences of Violence

### 9.1 The Karma System (Combat)

```yaml
karma_combat_impacts:
  warfare_declared:
    killing_enemy_soldiers: "-2 karma per kill"
    killing_enemy_civilians: "-20 karma per kill"
    defending_your_settlement: "0 karma"
    atrocities: "-50 to -100 karma"

  personal_violence:
    self_defense: "0 karma"
    assault_unprovoked: "-15 karma"
    murder: "-50 karma"
    banditry_with_violence: "-30 karma"
    ritual_duel: "-5 karma (consensual)"

  karma_thresholds:
    positive_hero: "+50 and above → respected, leadership opportunities"
    neutral: "-20 to +20 → normal interactions"
    negative_criminal: "-20 to -50 → NPCs wary, prices higher"
    negative_outlaw: "-50 and below → hunted, no safe cities"
```

### 9.2 Legal Consequences

```yaml
legal_consequences:
  jurisdiction: "Temple and/or Lugal courts"

  murder:
    investigation: "Temple priests investigate"
    evidence: "Witnesses, physical evidence"
    penalty_if_convicted:
      - "Blood price to victim's family (massive grain payment)"
      - "Exile from city"
      - "Execution (for repeat offenders or elite victims)"
      - "Debt slavery to victim's family"

  assault:
    penalty_if_convicted:
      - "Fine (grain or silver)"
      - "Compensation to victim"
      - "Public shaming"
      - "Temporary imprisonment"

  theft_with_violence:
    penalty_if_convicted:
      - "Return stolen goods (or value)"
      - "Additional fine (2-5x value)"
      - "Physical punishment (beating)"
      - "Brand marking (repeat offenders)"

  evasion:
    - "Flee jurisdiction → outlaw status"
    - "Cannot return to that city"
    - "Other cities may or may not honor warrants"
```

### 9.3 Witness System Impact

```yaml
witness_combat_trauma:
  killing_in_battle:
    first_kill: "+5 Witness (trauma)"
    subsequent_kills: "+2 Witness each"
    mass_casualties: "+20 Witness (witnessing slaughter)"

  being_wounded:
    minor: "+3 Witness"
    severe: "+10 Witness"
    near_death: "+20 Witness"

  witnessing_atrocities:
    civilian_massacre: "+30 Witness"
    torture: "+25 Witness"
    betrayal_by_ally: "+15 Witness"

  combat_ptsd:
    trigger: "Witness exceeds 70% capacity"
    effects:
      - "Flashbacks during combat (stun chance)"
      - "Nightmares (reduced rest effectiveness)"
      - "Rage episodes (loss of control)"
      - "Combat aversion (penalties to engage)"
```

---

## 10. Defense & Protection

### 10.1 Settlement Defense

```yaml
settlement_defense:
  fortifications:
    walls:
      construction_time: "Months (real-time equivalent)"
      materials: "Mud-brick, labor-intensive"
      maintenance: "Constant (erosion, damage)"
      benefit: "Deters attacks, siege required"

    watchtowers:
      benefit: "Early warning of approach"
      requirement: "Manned (NPC or player)"

    gates:
      benefit: "Controlled access"
      vulnerability: "Primary siege target"

  garrison:
    npc_soldiers:
      cost: "SILA per month per soldier"
      quality: "Varies by pay"
      loyalty: "High if paid, desertion if not"

    militia_system:
      description: "Players and NPCs called up in emergency"
      requirement: "All able-bodied citizens serve"
      training: "Varies (better if regular drills)"

  early_warning:
    scouts: "Patrol territory, report threats"
    watchtowers: "See approaching armies"
    trade_network: "Merchants bring news of distant threats"
```

### 10.2 Personal Defense

```yaml
personal_defense:
  guards:
    npc_bodyguards:
      cost: "50-100 SILA/month"
      quality: "Moderate (better costs more)"
      function: "Accompany, deter, fight if needed"

    player_alliance:
      cost: "Social capital"
      function: "Safety in numbers"

  property_defense:
    locks: "Basic deterrent"
    watchman_npc: "Alerts you to intruders"
    walls_fences: "Slows intruders, defines property"
    dogs: "Early warning, minor combat assistance"

  avoiding_combat:
    travel_groups: "Bandits avoid large groups"
    trade_routes: "Stick to patrolled paths"
    reputation: "Known warriors rarely attacked"
    payment: "Bribe bandits for passage"
```

---

## 11. The Warfare Calendar

### 11.1 Seasonal Constraints

```yaml
warfare_calendar:
  spring:
    months: "March-May"
    warfare_status: "PRIMARY CAMPAIGN SEASON"
    reasons:
      - "Planting done, harvest not yet"
      - "Weather favorable for movement"
      - "Food supplies adequate"
      - "Rivers navigable"

  summer:
    months: "June-August"
    warfare_status: "LIMITED"
    reasons:
      - "Heat exhaustion risk"
      - "Water scarcity for armies"
      - "Must return for harvest"

  autumn:
    months: "September-November"
    warfare_status: "SECONDARY SEASON"
    reasons:
      - "Harvest in (food available)"
      - "Weather cooling"
      - "Last chance before winter"

  winter:
    months: "December-February"
    warfare_status: "RARE"
    reasons:
      - "Cold, rain, mud"
      - "Supply difficulties"
      - "Soldiers needed for other work"
```

### 11.2 Campaign Timing

```yaml
campaign_timing:
  typical_campaign:
    duration: "2-8 weeks"
    start: "After spring planting"
    end: "Before summer heat or harvest"

  siege_timing:
    duration: "Weeks to months"
    start: "When supplies adequate"
    end: "When supplies exhausted or walls fall"

  raid_timing:
    duration: "Days"
    anytime: "Raids can happen year-round"
    preference: "When defenders are busy (harvest, festivals)"
```

---

## 12. Training Data Value

### 12.1 Combat Decision Data

```yaml
combat_training_data:
  tactical_decisions:
    - "When to engage vs withdraw?"
    - "How to position in formation?"
    - "When to call retreat?"
    - "Risk assessment under fire"

  strategic_decisions:
    - "When to declare war?"
    - "How to form alliances?"
    - "Resource allocation for defense?"
    - "Negotiation vs fighting?"

  moral_decisions:
    - "Treatment of prisoners"
    - "Civilian protection"
    - "Proportional response"
    - "Atrocity prevention/perpetration"

  leadership_decisions:
    - "How do commanders emerge?"
    - "How are orders followed/questioned?"
    - "How is morale maintained?"
    - "How are defeats processed?"
```

### 12.2 Post-Conflict Data

```yaml
post_conflict_data:
  reconciliation:
    - "How do former enemies coexist?"
    - "What enables forgiveness?"
    - "How are treaties maintained?"

  trauma_processing:
    - "How do players process violence?"
    - "Do they seek more or avoid it?"
    - "How does combat change behavior?"

  social_impact:
    - "How do communities recover?"
    - "Who becomes leaders post-war?"
    - "How is history remembered/written?"
```

---

## 13. Implementation Notes

### 13.1 MVP Scope

```yaml
mvp_combat:
  included:
    personal_combat:
      - "Basic melee system (stamina, stances, actions)"
      - "3-4 weapon types with distinct feels"
      - "Armor system (damage reduction)"
      - "Karma and legal consequences"

    group_combat:
      - "Simple formation system (stay grouped = bonus)"
      - "NPC soldiers follow player commands"
      - "Morale system (formation breaks at threshold)"

    warfare:
      - "Declaration system between settlements"
      - "Raid scenario (attack outlying targets)"
      - "Basic siege (assault walls)"

  deferred:
    - "Full phalanx mechanics"
    - "War wagons"
    - "Complex siege equipment"
    - "Naval combat"
    - "Campaign system (multi-battle wars)"
```

### 13.2 Balance Considerations

```yaml
balance:
  prevent_griefing:
    - "High karma cost for unprovoked violence"
    - "NPC guards respond to aggression"
    - "New player protection zones"
    - "Declared war requires settlement infrastructure"

  prevent_murder_hobo:
    - "Combat is exhausting (stamina limits)"
    - "Equipment wears out"
    - "Injuries require time to heal"
    - "Reputation affects all interactions"

  reward_cooperation:
    - "Formation fighting is more effective"
    - "Defensive alliances deter attacks"
    - "Shared defense costs less than individual"
```

---

## Appendix: Quick Reference

### Combat Actions Cheat Sheet

| Action | Stamina Cost | Effect |
|--------|--------------|--------|
| Light Attack | Low | Fast, low damage |
| Heavy Attack | High | Slow, high damage |
| Block | Low | Negates attack (shield durability) |
| Parry | Medium | Creates opening for counter |
| Dodge | Medium | Avoids attack entirely |
| Grapple | High | Close-range wrestling |
| Disengage | Low | Creates distance |

### Karma Impact Reference

| Action | Karma Change |
|--------|--------------|
| Self-defense kill | 0 |
| War kill (enemy soldier) | -2 |
| War kill (civilian) | -20 |
| Murder | -50 |
| Assault | -15 |
| Ritual duel kill | -5 |
| Defending settlement | 0 |
| Atrocity | -50 to -100 |

---

*"The victor writes history. The dead write nothing. Choose your battles wisely."*
