# Daily Life Simulation: Living in Ancient Eridu

> "The gods created humans to serve them. In Eridu, that service was life itself."

## Table of Contents

1. [Design Philosophy](#1-design-philosophy)
2. [The Daily Cycle](#2-the-daily-cycle)
3. [Social Systems](#3-social-systems)
4. [The Legal System](#4-the-legal-system)
5. [Health & Disease](#5-health--disease)
6. [Religious Life](#6-religious-life)
7. [Marriage & Family](#7-marriage--family)
8. [The Ecological Crisis](#8-the-ecological-crisis)
9. [Conflict & Warfare](#9-conflict--warfare)
10. [Death & Dying](#10-death--dying)
11. [Random Life Events](#11-random-life-events)
12. [Commerce & Shopping](#12-commerce--shopping)
13. [Animals & Wildlife](#13-animals--wildlife)
14. [Diet & Food](#14-diet--food)
15. [Training Data Value](#15-training-data-value)
16. [Implementation Notes](#16-implementation-notes)

---

## 1. Design Philosophy

### 1.1 Authentic Simulation

```yaml
authenticity_goals:
  not_a_theme_park:
    description: "Eridu is not a backdrop—it's a living system"
    implications:
      - "NPCs have real lives, not scripted loops"
      - "Systems interact realistically"
      - "Consequences feel organic, not punitive"

  historical_accuracy_with_purpose:
    description: "We simulate reality to capture real behavior"
    balance:
      - "Accurate enough to feel genuine"
      - "Playable enough to be engaging"
      - "Meaningful for training data"

  the_weight_of_existence:
    description: "Life was hard. Players should feel that."
    elements:
      - "Death is common"
      - "Disease is ever-present"
      - "Food is never guaranteed"
      - "The gods are always watching"
```

### 1.2 The Unresolved Crisis

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  THE GREAT UNSOLVED PROBLEM: SALINIZATION                          │
│                                                                     │
│  Every civilization in Mesopotamia eventually collapsed             │
│  because they could not solve this:                                 │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                                                             │   │
│  │  IRRIGATION ──► EVAPORATION ──► SALT ACCUMULATION          │   │
│  │       │                              │                      │   │
│  │       │         HOT SUN              │                      │   │
│  │       ▼            │                 ▼                      │   │
│  │  CROPS GROW        │          SOIL BECOMES TOXIC            │   │
│  │       │            │                 │                      │   │
│  │       │            ▼                 │                      │   │
│  │       │     WATER EVAPORATES         │                      │   │
│  │       │     SALT STAYS               │                      │   │
│  │       │            │                 │                      │   │
│  │       │            ▼                 ▼                      │   │
│  │       │     YEARS PASS ──► WHEAT FAILS ──► SWITCH TO BARLEY │   │
│  │       │                                         │           │   │
│  │       │                               YEARS PASS│           │   │
│  │       │                                         ▼           │   │
│  │       │                              BARLEY FAILS           │   │
│  │       │                                         │           │   │
│  │       │                                         ▼           │   │
│  │       │                              CIVILIZATION COLLAPSES │   │
│  │                                                             │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  This is the TRUE final boss of the Ancient Era.                   │
│  Innovate a solution, or watch everything die.                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.3 Theocratic Reality

```yaml
theocracy_simulation:
  core_truth: "There is no separation of church and state"

  implications:
    government_is_religion:
      - "The temple IS the government"
      - "The king claims divine authority"
      - "Laws are divine decrees"

    no_religious_freedom:
      - "Worship is mandatory, not optional"
      - "Rejecting the gods = treason/insanity"
      - "Personal piety exists within the framework"

    cosmic_worldview:
      - "Humans exist to serve the gods"
      - "Disasters are divine punishment"
      - "Success is divine favor"
      - "Every action has cosmic meaning"
```

---

## 2. The Daily Cycle

### 2.1 A Day in the Life (Farmer)

```yaml
farmer_day:
  pre_dawn_4am:
    activities:
      - "Wake on reed mat"
      - "Brief prayer to personal god"
      - "Cold bread and water"
    feelings: "Exhaustion, routine, resignation"
    game_mechanics:
      - "Stamina starts at 80% (sleep quality matters)"
      - "Hunger at 70% (light breakfast)"

  dawn_5am:
    activities:
      - "Walk to east gate (join other farmers)"
      - "Check on irrigation channels"
      - "Begin field work"
    feelings: "Community, purpose, physical strain beginning"
    game_mechanics:
      - "Travel time to field"
      - "Social interactions possible"
      - "Work minigame begins"

  morning_5am_11am:
    activities:
      - "Heavy labor (plowing, planting, weeding, or harvesting)"
      - "Monitor canal water levels"
      - "Coordinate with neighbors on shared resources"
    feelings: "Hot, tired, watching the sun rise higher"
    game_mechanics:
      - "Stamina depletes"
      - "Thirst increases rapidly"
      - "Skill checks affect output"
      - "Random events possible (tool breaks, animal problem)"

  midday_11am_2pm:
    activities:
      - "Seek shade"
      - "Eat barley bread, onions, drink beer"
      - "Rest (sleep if possible)"
      - "Maybe pray at field shrine"
    feelings: "Relief, exhaustion, social bonding with other farmers"
    game_mechanics:
      - "Mandatory rest or health penalty"
      - "Hunger/thirst restored"
      - "Stamina partially recovers"
      - "Gossip/information exchange"

  afternoon_2pm_6pm:
    activities:
      - "Resume lighter work"
      - "Repair tools"
      - "Prepare for tomorrow"
      - "Start walking back as sun lowers"
    feelings: "Anticipation of evening, tired satisfaction or frustration"
    game_mechanics:
      - "Reduced stamina drain"
      - "Quality-check on day's work"
      - "Travel time back"

  dusk_6pm_8pm:
    activities:
      - "Return through gate"
      - "Deliver produce to temple/granary (if required)"
      - "Return home"
      - "Main meal with family"
    feelings: "Relief, domestic comfort, worry about tomorrow"
    game_mechanics:
      - "Work completion tallied"
      - "Payment received (if piece work)"
      - "Family interactions"
      - "Hunger fully restored"

  evening_8pm_10pm:
    activities:
      - "Stories by fire or lamp light"
      - "Visit beer house (optional)"
      - "Domestic tasks"
      - "Tend to children"
    feelings: "Community, relaxation, worry, prayer"
    game_mechanics:
      - "Social opportunities"
      - "Information gathering"
      - "Family events"
      - "Witness events (if violence/trauma)"

  night_10pm_4am:
    activities:
      - "Sleep on roof (summer) or inside (winter)"
      - "Dreams (may be significant)"
    feelings: "Vulnerability, rest, sometimes fear"
    game_mechanics:
      - "Health restoration"
      - "Stamina restoration"
      - "Sanity restoration"
      - "Disease progression"
      - "Random night events (rare)"
```

### 2.2 A Day in the Life (Craftsman)

```yaml
craftsman_day:
  dawn_5am:
    activities:
      - "Open workshop"
      - "Check kilns/forges (if relevant)"
      - "Prepare materials"
    unique: "Craftsmen work in city, less travel"

  morning_5am_11am:
    activities:
      - "Primary production work"
      - "Apprentice supervision"
      - "Customer interactions"
    game_mechanics:
      - "Crafting minigames"
      - "Quality determination"
      - "Material management"

  midday:
    activities:
      - "Workshop slows (heat)"
      - "Meal"
      - "Business dealings"
    unique: "Can conduct trade during rest period"

  afternoon_2pm_6pm:
    activities:
      - "Resume production"
      - "Finish orders"
      - "Prepare next day's materials"
    game_mechanics:
      - "Complete crafting cycles"
      - "Inventory management"

  evening:
    activities:
      - "Close workshop"
      - "Deliver finished goods"
      - "Collect payments"
      - "Beer house networking"
    unique: "Craftsmen have more evening social time"
```

### 2.3 A Day in the Life (Priest/Scribe)

```yaml
temple_worker_day:
  pre_dawn_4am:
    activities:
      - "Wake in temple dormitory"
      - "Ritual purification (bathing)"
      - "Don temple garments"
    unique: "Must be ritually clean before serving gods"

  dawn_5am:
    activities:
      - "Morning rituals"
      - "Present offerings to Enki statue"
      - "Chanting and incense"
    feelings: "Awe, routine devotion, cosmic duty"
    game_mechanics:
      - "Ritual participation (skill)"
      - "Enki favor affected"

  morning_5am_11am:
    activities:
      - "Administrative duties (scribes)"
      - "Teaching (senior priests)"
      - "Record keeping"
      - "Receiving offerings from public"
    game_mechanics:
      - "Literacy tasks"
      - "Knowledge gathering"
      - "Public interaction"

  midday:
    activities:
      - "Midday rituals"
      - "Communal meal in temple"
      - "Study or rest"
    unique: "Temple provides meals—major benefit"

  afternoon:
    activities:
      - "Continue duties"
      - "Divination (if trained)"
      - "Counsel seekers"
      - "Archive work"
    game_mechanics:
      - "Special temple activities"
      - "Quest-giving role"
      - "Innovation clue access"

  evening_6pm:
    activities:
      - "Evening rituals"
      - "Close temple to public"
      - "Private devotions"
      - "Sleep in temple"
    unique: "Less freedom, but security and status"
```

### 2.4 Seasonal Variations

```yaml
seasonal_cycles:
  spring_march_may:
    name: "Harvest Season"
    characteristics:
      - "Barley harvest (frantic activity)"
      - "Longest workdays"
      - "Everyone mobilized"
      - "Festival: Akitu (New Year)"
    game_impact:
      - "High pay for labor"
      - "Food abundance"
      - "Social events"
      - "Innovation: Storage becomes critical"

  summer_june_august:
    name: "Burning Season"
    characteristics:
      - "Extreme heat (40-50°C)"
      - "Reduced outdoor work"
      - "Night activity increases"
      - "River at lowest"
    game_impact:
      - "Heat exhaustion risk"
      - "Water scarcity"
      - "Disease peak (bad water)"
      - "Innovation: Water management critical"

  autumn_september_november:
    name: "Planting Season"
    characteristics:
      - "Date harvest"
      - "Plowing and sowing"
      - "Cooler weather returns"
      - "Trade season peaks"
    game_impact:
      - "Moderate labor demand"
      - "Travel opportunities"
      - "Planning for next year"

  winter_december_february:
    name: "Resting Season"
    characteristics:
      - "Cool, occasional rain"
      - "Indoor activities"
      - "Craft production peaks"
      - "Stories and teaching"
    game_impact:
      - "Learning opportunities"
      - "Social development"
      - "Innovation: Time to think"

  flood_season_variable:
    name: "The Great Rising"
    timing: "Late spring, unpredictable"
    characteristics:
      - "River swells from mountain snowmelt"
      - "Can be blessing or disaster"
      - "All hands on flood control"
    game_impact:
      - "Major event"
      - "Innovation opportunity (canal system)"
      - "Death risk"
      - "Community cooperation or conflict"
```

---

## 3. Social Systems

### 3.1 Social Hierarchy

```yaml
social_hierarchy:
  ruling_class:
    members:
      - "EN (High Priest/ess) - religious leader"
      - "LUGAL (King) - military/secular leader"
      - "ENSI (Governor) - city administrator"
      - "Royal family"
      - "High-ranking priests"
    percentage: "~1%"
    privileges:
      - "Best food, housing, clothing"
      - "Access to temple inner sanctum"
      - "Command authority"
      - "Divine connection claimed"
    player_accessibility: "Very rare, late-game, exceptional achievement"

  upper_class:
    members:
      - "Senior scribes"
      - "Temple administrators"
      - "Wealthy merchants"
      - "Military commanders"
      - "Master craftsmen (some)"
    percentage: "~4%"
    privileges:
      - "Comfortable living"
      - "Influence"
      - "Literacy (scribes)"
      - "Foreign contacts (merchants)"
    player_accessibility: "Achievable through skill, innovation, or wealth"

  middle_class:
    members:
      - "Craftsmen"
      - "Minor merchants"
      - "Skilled workers"
      - "Lower priests"
      - "Soldiers"
    percentage: "~15%"
    privileges:
      - "Stable income"
      - "Some property ownership"
      - "Respected in community"
    player_accessibility: "Common achievement for dedicated players"

  working_class:
    members:
      - "Farmers"
      - "Laborers"
      - "Fishermen"
      - "Servants"
      - "Most population"
    percentage: "~70%"
    privileges:
      - "Free citizens"
      - "Can own some property"
      - "Protected by law"
    player_accessibility: "Most players start here"

  lowest_class:
    members:
      - "Slaves (wardu)"
      - "Debt bondsmen"
      - "Criminals serving sentences"
    percentage: "~10%"
    status:
      - "Property of owner"
      - "Can be bought/sold"
      - "CAN eventually buy freedom"
      - "Some rights (limited)"
    player_accessibility: "Can fall into through debt; can escape through payment or service"
```

### 3.2 Social Interactions

```yaml
social_mechanics:
  reputation_system:
    scope:
      community: "Known to neighbors, coworkers"
      profession: "Known among craftsmen, farmers, etc."
      temple: "Standing with religious authority"
      city: "Known to officials, widespread fame"

    factors:
      positive:
        - "Work quality"
        - "Honesty in dealings"
        - "Religious observance"
        - "Community contribution"
        - "Innovation"
      negative:
        - "Crime"
        - "Debt"
        - "Impiety"
        - "Breaking oaths"
        - "Neglecting duties"

  social_obligations:
    corvée_labor:
      description: "Mandatory public work (canals, walls, temple)"
      frequency: "Several weeks per year"
      evasion: "Possible but damages reputation severely"

    military_service:
      description: "All free men can be called to fight"
      equipment: "Bring your own (spear, basic)"
      evasion: "Cowardice = severe social penalty"

    religious_participation:
      description: "Attend festivals, make offerings"
      frequency: "Regular (daily possible, festivals mandatory)"
      evasion: "Noticed, damages standing"

    mutual_aid:
      description: "Help neighbors in crisis"
      expectation: "Strongly expected"
      refusal: "Remembered, reciprocity denied later"
```

### 3.3 Class Mobility Events

```yaml
mobility_events:
  upward:
    innovation_recognition:
      trigger: "Solve significant problem"
      effect: "Jump 1-2 social levels possible"
      example: "Improve irrigation → recognized by temple"

    wealth_accumulation:
      trigger: "Accumulate significant capital"
      effect: "Buy into higher class"
      example: "Successful merchant buys land, becomes landowner"

    temple_advancement:
      trigger: "Rise through temple hierarchy"
      effect: "Gradual but stable advancement"
      example: "Initiate → scribe → administrator"

    heroic_act:
      trigger: "Save lives, defend city"
      effect: "Instant recognition"
      example: "Warn city of flood, save hundreds"

  downward:
    debt:
      trigger: "Cannot pay debts"
      effect: "Debt slavery"
      duration: "Until debt paid"
      recovery: "Work off debt, buy freedom"

    crime_conviction:
      trigger: "Convicted of serious crime"
      effect: "Property loss, servitude"
      recovery: "Serve sentence, pay fines"

    disaster:
      trigger: "Flood, fire, disease"
      effect: "Lose everything"
      recovery: "Start over"

    war:
      trigger: "City conquered, taken prisoner"
      effect: "Become slave"
      recovery: "Ransom, escape, earn freedom"
```

---

## 4. The Legal System

### 4.1 Laws of the Land

```yaml
legal_framework:
  basis: "Code of Ur-Nammu (older than Hammurabi)"

  key_principles:
    fines_over_mutilation:
      description: "Unlike later codes, physical crimes punished by silver fines"
      example: "Break someone's bone = pay 60 shekels silver"
      significance: "Surprisingly progressive"

    divine_authority:
      description: "All law comes from the gods through the king"
      implication: "Breaking law = offending gods"

    status_matters:
      description: "Punishments vary by victim and perpetrator status"
      example: "Harming a noble vs. harming a slave = different penalties"

    written_contracts:
      description: "Business deals, marriages, property in writing"
      implication: "Literacy = legal power"

  major_laws:
    theft:
      minor_theft: "Return goods + fine (2-10x value)"
      major_theft: "Return goods + heavy fine or slavery"
      temple_theft: "Death or severe punishment"

    assault:
      minor_injury: "Fine in silver"
      serious_injury: "Larger fine"
      death: "Death penalty or blood money to family"

    property:
      encroachment: "Pay damages + fine"
      canal_neglect: "Pay for damaged crops downstream"
      contract_breach: "Pay penalties specified in contract"

    marriage:
      adultery_by_wife: "Death (though often reduced to divorce)"
      adultery_by_man: "Fine (if with married woman)"
      abandonment: "Divorce penalties"

    religious:
      impiety: "Temple punishment, fines, exile"
      false_oath: "Severe (gods punish liars)"
      temple_violation: "Death possible"
```

### 4.2 Justice Mechanics

```yaml
justice_system:
  no_police:
    reality: "There was no professional police force"
    implications:
      - "Victim must find perpetrator"
      - "Victim must bring them to court"
      - "Community pressure is primary deterrent"

  city_watch:
    role: "Patrol major areas, prevent obvious crime"
    limitations:
      - "Do not investigate"
      - "Do not track criminals"
      - "Maintain order, not justice"

  victim_led_justice:
    process:
      1: "Crime occurs"
      2: "Victim investigates (or hires help)"
      3: "Victim identifies perpetrator"
      4: "Victim brings accusation to court"
      5: "Trial before elders or temple"
      6: "Verdict and punishment"

  courts:
    elder_assembly:
      jurisdiction: "Minor disputes, local matters"
      location: "Public gathering area"
      process: "Both parties speak, elders decide"

    temple_court:
      jurisdiction: "Serious crimes, oaths, religious matters"
      location: "Temple complex"
      process: "Priests oversee, divine judgment invoked"

    royal_court:
      jurisdiction: "Appeals, major cases, inter-city matters"
      location: "Palace (if king present)"
      access: "Limited, expensive"

  evidence_types:
    witnesses:
      weight: "Heavy (especially multiple)"
      requirement: "Must swear oath before gods"

    written_documents:
      weight: "Very heavy"
      examples: "Contracts, deeds, records"

    physical_evidence:
      weight: "Moderate"
      examples: "Stolen goods, marks, damage"

    divine_judgment:
      method: "Ordeal (river ordeal most common)"
      use: "When evidence unclear"
      process: "Accused thrown in river—survival = innocence"
```

### 4.3 Player Legal Interactions

```yaml
player_legal_system:
  as_victim:
    robbery:
      immediate: "Checkpoint reset (as per theft rules)"
      optional_pursuit:
        - "Investigate who robbed you"
        - "Gather evidence"
        - "Bring to court"
        - "Win compensation"
      reward: "Recover time lost + possible fine award"

    assault:
      immediate: "Health damage"
      options:
        - "Pursue legal action"
        - "Seek revenge (karma cost)"
        - "Let it go"

    contract_breach:
      by_npc: "Can sue for damages"
      evidence_needed: "Contract tablet"

  as_accused:
    caught_stealing:
      consequence: "Brought to court by victim (or witness)"
      penalties: "Return goods + fine + reputation damage + karma hit"
      evasion: "Can try to flee (becomes fugitive)"

    violence:
      consequence: "Victim or family pursues"
      penalties: "Fines, possibly death for murder"
      self_defense: "Valid defense if provable"

    debt:
      consequence: "Creditor brings to court"
      penalties: "Payment schedule or debt slavery"

  false_accusations:
    mechanic: "Can accuse others of crimes"
    risk: "If accusation false, YOU pay the penalty they would have"
    use: "Deters frivolous lawsuits"
```

---

## 5. Health & Disease

### 5.1 Medical Worldview

```yaml
medical_beliefs:
  cause_of_illness:
    divine_punishment:
      description: "Sickness is the 'Hand of a God'"
      gods_involved: "Specific gods for specific illnesses"
      cure: "Appease the god"

    demonic_possession:
      description: "Demons enter the body"
      types: "Various named demons for different conditions"
      cure: "Exorcism"

    natural_causes:
      description: "Some practical understanding existed"
      examples: "Bad water, bad food, wounds"
      treatment: "Practical remedies"

  two_types_of_healers:
    asu:
      title: "Physician"
      methods:
        - "Herbal remedies"
        - "Poultices and bandages"
        - "Surgery (basic)"
        - "Dietary advice"
      effectiveness: "Variable, sometimes helpful"
      cost: "Moderate"

    asipu:
      title: "Exorcist"
      methods:
        - "Incantations"
        - "Rituals"
        - "Amulets"
        - "Identifying which god/demon caused illness"
      effectiveness: "Psychological, sometimes harmful"
      cost: "Can be expensive"

  combined_treatment:
    typical: "Both asu and asipu consulted"
    order: "Usually asipu first (identify cause), then asu (treat symptoms)"
```

### 5.2 Common Diseases

```yaml
disease_system:
  gastrointestinal:
    dysentery:
      cause: "Contaminated water (very common)"
      symptoms: "Severe diarrhea, weakness"
      treatment: "Rest, clean water, herbs"
      mortality: "10-30% if untreated"
      game_effect: "-50% stamina, dehydration risk"

    intestinal_worms:
      cause: "Canal water, uncooked food"
      symptoms: "Weakness, stomach pain, malnutrition"
      treatment: "Herbal purges"
      mortality: "Low but chronic"
      game_effect: "-20% stamina ongoing"

  fevers:
    marsh_fever:
      modern: "Malaria (endemic in marshes)"
      symptoms: "Cyclical fever, chills, sweating"
      treatment: "None effective (bark tea sometimes)"
      mortality: "Variable, often chronic"
      game_effect: "Periodic debilitation, -30% stamina during attacks"

    general_fever:
      cause: "Various infections"
      symptoms: "High temperature, delirium"
      treatment: "Rest, cooling, prayers"
      mortality: "Variable"
      game_effect: "Bed rest required"

  injuries:
    wounds:
      cause: "Work accidents, violence"
      symptoms: "Bleeding, pain"
      treatment: "Bandaging, herbal poultices"
      complication: "Infection (high risk)"
      game_effect: "Depends on severity"

    broken_bones:
      cause: "Falls, accidents, violence"
      symptoms: "Inability to use limb"
      treatment: "Splinting (surprisingly effective)"
      recovery: "Weeks to months"
      game_effect: "Major activity limitation"

  neurological:
    bennu:
      modern: "Epilepsy"
      symptoms: "Seizures"
      belief: "Demonic possession"
      treatment: "Exorcism (ineffective)"
      game_effect: "Random incapacitation"

  seasonal:
    summer_plague:
      cause: "Heat + bad water + crowding"
      symptoms: "Multiple disease outbreak"
      timing: "Late summer"
      game_effect: "Major death event possible"
```

### 5.3 Health Mechanics

```yaml
health_mechanics:
  health_meter:
    max: 100
    components:
      current_health: "Immediate physical state"
      disease_status: "Active illnesses (can have multiple)"
      wound_status: "Active injuries"
      chronic_conditions: "Long-term ailments"

  disease_contraction:
    risk_factors:
      water_source:
        canal_water: "10% daily disease chance"
        well_water: "2% daily disease chance"
        temple_water: "0.5% daily disease chance"
        boiled_water: "0.1% daily disease chance"

      food:
        raw_fish: "5% disease chance"
        cooked_food: "1% disease chance"
        spoiled_food: "30% disease chance"

      location:
        marsh: "Higher malaria risk"
        crowded_areas: "Higher contagion risk"
        dirty_streets: "Higher disease risk"

      season:
        summer: "+50% disease risk"
        flood: "+30% disease risk"

  treatment_options:
    self_care:
      cost: "Nothing (except time)"
      effectiveness: "Low-moderate"
      method: "Rest, clean water, basic herbs"

    asu_visit:
      cost: "10-50 sila depending on ailment"
      effectiveness: "Moderate-good for physical ailments"
      availability: "City only"

    asipu_visit:
      cost: "20-100 sila"
      effectiveness: "Psychological, situational"
      benefit: "Identifies 'cause' (game may give clues)"

    temple_healing:
      cost: "Offering (variable)"
      effectiveness: "Favor-dependent"
      requirement: "Temple standing 25+"

  death_from_disease:
    threshold: "Health reaches 0"
    warning: "Health below 20% = danger state"
    prevention: "Seek treatment, rest, good conditions"
```

### 5.4 Sanitation Impact

```yaml
sanitation_reality:
  conditions:
    streets: "Waste often in streets"
    water: "Canals contaminated by upstream cities"
    housing: "Ventilation varies by wealth"
    food_safety: "No refrigeration, preservation limited"

  innovation_opportunity:
    problem: "Disease is everywhere"
    clues:
      - "Notice correlation between water and illness"
      - "Observe that boiled water causes less sickness"
      - "See that wealthy (better water) get sick less"
    innovation: "Public health improvements possible"

  game_integration:
    visible_filth: "Streets show waste"
    npc_sickness: "NPCs get sick, die"
    epidemic_events: "Periodic outbreaks"
    player_choices:
      - "Where to drink water"
      - "Where to live"
      - "What to eat"
      - "When to seek treatment"
```

---

## 6. Religious Life

### 6.1 Mandatory Devotion

```yaml
religious_requirements:
  daily_obligations:
    personal_prayer:
      timing: "Morning, evening"
      to_whom: "Personal god + major gods"
      method: "Brief prayer, small offering possible"
      skipping: "No immediate penalty, cumulative effect"

    public_acknowledgment:
      description: "Participate in visible religious life"
      examples:
        - "Greet priests respectfully"
        - "Observe temple rituals when passing"
        - "Make occasional offerings"
      skipping: "Noticed by NPCs, reputation effect"

  periodic_obligations:
    festival_attendance:
      frequency: "Multiple per year"
      major_festivals:
        - "Akitu (New Year) - mandatory"
        - "Harvest festivals"
        - "Enki's celebration"
      expectation: "All citizens participate"
      skipping: "Major reputation damage"

    temple_service:
      description: "Occasional service expected"
      examples:
        - "Help with temple maintenance"
        - "Contribute to festivals"
        - "Provide offerings"
      expectation: "Based on wealth/status"

  life_event_requirements:
    birth: "Purification rituals"
    naming: "Divine consultation for name"
    marriage: "Religious ceremony required"
    death: "Proper burial rituals essential"
    business: "Oaths sworn before gods"
```

### 6.2 Personal vs. Public Religion

```yaml
religious_layers:
  public_religion:
    focus: "Great gods (Enki, Enlil, An, etc.)"
    participation: "Communal rituals, festivals"
    location: "Temple, public spaces"
    purpose: "Maintain cosmic order, city prosperity"

  personal_religion:
    personal_god:
      description: "Each person has a guardian deity"
      relationship: "More intimate, personal prayers"
      function: "Intercedes with high gods on your behalf"
      game_mechanic: "Players can choose or discover personal god"

    household_shrine:
      description: "Small shrine in home"
      contents: "Figurines, offering spot"
      use: "Daily devotion, family prayers"
      game_mechanic: "Can build, affects home"

    ancestor_veneration:
      description: "Honor deceased family"
      obligations:
        - "Regular offerings to graves"
        - "Remember their names"
        - "Continue family traditions"
      consequence: "Neglected dead can become harmful ghosts"
```

### 6.3 Divine Displeasure

```yaml
divine_consequences:
  signs_of_disfavor:
    personal:
      - "Illness in family"
      - "Failed crops"
      - "Business losses"
      - "Bad dreams"
      - "Accidents"

    community:
      - "Flood"
      - "Drought"
      - "Epidemic"
      - "Defeat in war"
      - "Bad omens"

  response_to_disfavor:
    divination:
      method: "Consult priest (omen reading, liver examination)"
      purpose: "Identify which god is angry and why"
      cost: "Offering + fee"

    appeasement:
      method: "Offerings, prayers, behavior change"
      scale: "Based on severity of offense"
      effectiveness: "Based on sincerity (and game mechanics)"

  game_integration:
    favor_system:
      mechanics: "Track favor with major gods"
      effects: "High favor = blessings, low favor = misfortune"

    misfortune_events:
      trigger: "Low favor, impious behavior"
      examples:
        - "Tool breaks at critical moment"
        - "Disease strikes"
        - "NPC relationships sour"
```

### 6.4 Player Religious Choices

```yaml
player_religion:
  mandatory_minimum:
    - "Acknowledge gods exist"
    - "Participate in major festivals"
    - "Swear oaths by gods when required"
    consequences_of_refusal:
      - "NPC hostility"
      - "Legal vulnerability (oaths matter)"
      - "Social isolation"
      - "Eventually: Treated as insane/possessed"

  optional_devotion:
    temple_favor:
      path: "Become devoted follower"
      benefits: "Better services, access, protection"
      cost: "Time, offerings, obligations"

    skeptic_path:
      available: "Can privately doubt"
      limitations:
        - "Cannot express doubt openly"
        - "Must maintain appearances"
        - "Risk if discovered"
      benefit: "More time for other pursuits"

    seeker_path:
      description: "Investigate the gods deeply"
      leads_to: "Anunnaki mystery content"
      cost: "Witness points (sanity)"
```

---

## 7. Marriage & Family

### 7.1 Marriage as Contract

```yaml
marriage_system:
  nature: "Legal contract between families, not romantic union"

  five_stages:
    1_engagement:
      description: "Families agree in principle"
      formality: "Verbal, witnessed"
      breakable: "With penalty"

    2_contract:
      description: "Written marriage agreement"
      contents:
        - "Bride price amount"
        - "Dowry specifications"
        - "Divorce conditions"
        - "Inheritance terms"
      formality: "Clay tablet, sealed, witnessed"

    3_bride_price:
      description: "Groom's family pays bride's father"
      purpose: "Compensation for raising daughter"
      amount: "Variable by status (10-60 shekels silver)"
      timing: "Before wedding"

    4_wedding:
      description: "Religious ceremony"
      elements:
        - "Procession to groom's house"
        - "Anointing with oil"
        - "Prayers to gods of marriage"
        - "Feast"

    5_dowry_transfer:
      description: "Bride's family provides dowry"
      contents: "Property, goods, servants, silver"
      ownership: "Remains wife's (protection)"
      purpose: "Set up new household"

  player_marriage:
    initiation: "Player or NPC can propose"
    requirements:
      - "Both parties free (or owner's permission)"
      - "Families agree (if applicable)"
      - "Sufficient resources for bride price"
      - "Standing in community"
    benefits:
      - "Social status boost"
      - "Combined households"
      - "Children (legacy)"
      - "Family labor"
    obligations:
      - "Support spouse"
      - "Maintain household"
      - "Fulfill contract terms"
```

### 7.2 Divorce

```yaml
divorce_system:
  husband_initiated:
    ease: "Relatively easy"
    grounds:
      - "Wife childless (main reason)"
      - "Wife neglects duties"
      - "Husband simply wishes it"
    process:
      - "Declare divorce publicly"
      - "Return dowry"
      - "Pay divorce silver (specified in contract)"
    consequences:
      - "Financial cost"
      - "Minor reputation impact"

  wife_initiated:
    ease: "Difficult and risky"
    grounds:
      - "Husband neglects support"
      - "Husband cruel/abusive"
      - "Husband abandons her"
    process:
      - "Must prove grounds"
      - "Risk: If grounds not proven, can be drowned"
      - "If successful: Retains dowry + leaves"
    consequences:
      - "Social stigma"
      - "May return to father's house"
      - "Remarriage difficult"

  player_divorce:
    as_husband:
      action: "Declare divorce"
      cost: "Return dowry + divorce silver"
      reputation: "Minor hit unless wife sympathetic"

    as_wife:
      action: "Bring case to court"
      requirement: "Evidence of grounds"
      risk: "Failure = severe penalty"
      reward: "Success = freedom + property"
```

### 7.3 Children & Family

```yaml
family_mechanics:
  children:
    birth:
      risk: "Childbirth dangerous (mortality ~5-10% for mother)"
      survival: "Child mortality high (30-50% before age 5)"
      celebration: "If survives first days, naming ceremony"

  childbirth_details:
    location: "Virtually all births took place at home"
    nature: "High-risk, all-female event"

    participants:
      midwife:
        title: "Shabsutu"
        role: "Professional birth attendant"
        skills:
          - "Positioning the mother"
          - "Assisting delivery"
          - "Cutting umbilical cord"
          - "Basic emergency interventions"
        availability: "Cities have professional midwives; villages rely on experienced women"

      female_relatives:
        role: "Support, assistance, emotional comfort"
        who: "Mother, sisters, aunts, neighbors"
        men: "Excluded from birth room entirely"

    magical_protection:
      primary_threat:
        name: "Lamashtu"
        description: "Female demon who attacks pregnant women and newborns"
        appearance: "Lion-headed, donkey-toothed, bird-clawed"
        behavior: "Snatches babies, causes miscarriage, kills mothers"

      protective_measures:
        amulets:
          description: "Worn during pregnancy and birth"
          depicting: "Pazuzu (demon who drives away Lamashtu)"

        magic_rolling_pin:
          description: "Inscribed clay cylinder rolled over mother's belly"
          purpose: "Transfer protective incantations to mother and baby"
          inscriptions: "Prayers, spells against Lamashtu"

        prayers:
          to: "Goddess Nintinugga (goddess of healing)"
          purpose: "Divine protection during delivery"
          timing: "Throughout labor"

        door_protection:
          description: "Symbols and substances placed at doorway"
          purpose: "Prevent demons from entering birth room"

    the_birth_process:
      positioning: "Squatting or kneeling (not lying down)"
      duration: "Hours to days"
      complications:
        common:
          - "Prolonged labor"
          - "Breech presentation"
          - "Hemorrhage"
        treatment:
          - "Prayers and incantations"
          - "Herbal remedies"
          - "Positioning changes"
          - "Last resort: appeal to gods"

    post_birth:
      immediate:
        - "Cut umbilical cord"
        - "Clean mother and baby"
        - "First nursing"
        - "Protective amulet placed on baby"

      purification_period:
        duration: "Several days to weeks"
        mother_status: "Ritually impure"
        restrictions:
          - "Cannot enter temple"
          - "Limited household duties"
          - "Gradual return to normal activities"

    wet_nurses:
      prevalence: "Common among wealthy families"
      reasons:
        - "Mother died in childbirth"
        - "Mother unable to nurse"
        - "Status symbol (wealthy)"
        - "Mother needed for work"
      arrangement: "Formal contract, specified payment and duration"
      treatment: "Well-fed, housed; her milk is baby's lifeline"

    game_mechanics:
      pregnancy_event:
        trigger: "Marriage + time (random)"
        duration: "Game-time equivalent of months"
        risks_during: "Reduced stamina, dietary needs, no heavy work"

      birth_event:
        player_involvement: "If female player or male player's wife"
        outcomes:
          - "Successful birth (most common)"
          - "Difficult birth (complications)"
          - "Mother dies (rare but possible)"
          - "Baby dies (more common historically)"
          - "Both survive with complications"

      midwife_access:
        city: "Hire professional shabsutu (cost: 10-30 sila)"
        village: "Rely on local woman (less reliable)"
        temple: "Special blessing available (requires standing)"

      magical_items:
        lamashtu_amulet:
          effect: "-20% birth complications"
          source: "Temple or craftsmen"
          cost: "5-15 sila"

        protective_cylinder:
          effect: "-30% birth complications"
          source: "Asipu (exorcist) or temple"
          cost: "20-50 sila"

    value:
      labor: "Children work from young age"
      inheritance: "Carry on family"
      legacy: "Game: Bloodline continuation"

    obligations:
      to_children: "Feed, house, teach trade"
      from_children: "Work, obey, support parents in old age"

  family_structure:
    nuclear: "Couple + children primary"
    extended: "Grandparents, unmarried relatives may live together"
    head: "Male head of household (legal authority)"
    women: "Run household, often real power"

  player_family:
    having_children:
      requirement: "Marriage + time"
      outcomes: "Random (number, gender, survival)"
      benefit: "Legacy system integration"

    family_events:
      positive:
        - "Child born"
        - "Child comes of age"
        - "Child achieves something"
      negative:
        - "Child illness"
        - "Child death"
        - "Family conflict"

    death_and_legacy:
      on_death: "Children inherit"
      no_children: "Legacy options (adopt, donate to temple, etc.)"
```

---

## 8. The Ecological Crisis

### 8.1 Salinization: The Slow Killer

```yaml
salinization:
  mechanism:
    step_1: "Irrigation water applied to fields"
    step_2: "Hot sun evaporates water"
    step_3: "Salt in water remains in soil"
    step_4: "Years of this = salt accumulation"
    step_5: "Salt levels reach toxic threshold"
    step_6: "Crops fail"

  timeline:
    year_0_50: "New fields productive"
    year_50_100: "Salt begins accumulating"
    year_100_200: "Wheat yields declining"
    year_200_300: "Must switch to salt-tolerant barley"
    year_300_500: "Even barley struggling"
    year_500+: "Land abandonment"

  historical_outcome:
    result: "Southern Mesopotamian cities eventually abandoned"
    Eridu: "Once surrounded by gardens, now desert"
    lesson: "Innovation that doesn't account for long-term = collapse"
```

### 8.2 In-Game Salinization

```yaml
salinization_mechanics:
  soil_quality_system:
    display: "Not shown numerically (realistic)"
    indicators:
      visual:
        - "White crusts on soil surface"
        - "Yellowing crops"
        - "Patchy growth"
        - "Dead zones expanding"
      npc_comments:
        - "The harvest was better when I was young"
        - "My father's father grew wheat here..."
        - "The land is tired"
      yield_changes:
        - "Same effort = less harvest"
        - "Quality declining"

  progression_in_game:
    start_4500_BCE:
      description: "Early signs visible"
      wheat_yield: "90% of maximum"
      barley_yield: "95% of maximum"

    decade_1:
      description: "Problem becoming noticeable"
      wheat_yield: "80%"
      barley_yield: "90%"
      npc_awareness: "Elders worried"

    decade_2:
      description: "Crisis emerging"
      wheat_yield: "60%"
      barley_yield: "85%"
      consequence: "Food pressure increasing"

    decade_3:
      description: "Critical phase"
      wheat_yield: "30% (switching to barley)"
      barley_yield: "75%"
      consequence: "Social tension, water conflicts"

  player_interaction:
    observation:
      - "See declining yields over time"
      - "Hear NPC concerns"
      - "Notice abandoned fields"

    investigation:
      - "Talk to elders about past"
      - "Compare field conditions"
      - "Taste soil (salt!)"

    innovation_opportunity:
      clues:
        - "Notice correlation: irrigation → salt"
        - "See that fallow fields recover slightly"
        - "Observe drainage patterns"

      potential_solutions:
        fallow_rotation:
          description: "Leave fields empty periodically"
          effectiveness: "Slows but doesn't stop"
          difficulty: "Medium (social coordination)"

        drainage_systems:
          description: "Create channels to drain salt water"
          effectiveness: "Significant improvement"
          difficulty: "Hard (major construction)"

        crop_rotation:
          description: "Alternate crops systematically"
          effectiveness: "Moderate"
          difficulty: "Easy to try"

        new_irrigation:
          description: "Flood irrigation instead of continuous"
          effectiveness: "Good"
          difficulty: "Medium (change practices)"

        the_true_solution:
          description: "[Let players discover]"
          hint: "What if we could flush the salt away?"
          effectiveness: "Best available"
          difficulty: "Very hard (requires understanding)"
```

### 8.3 Water Wars

```yaml
water_conflict:
  context:
    problem: "Water is life. As land degrades, water becomes more valuable."
    tension: "Upstream cities control downstream cities' water"
    history: "Many Mesopotamian wars were water wars"

  inter_city_dynamics:
    upstream_advantage:
      - "Can block water to downstream"
      - "Can flood downstream"
      - "Political leverage"

    downstream_vulnerability:
      - "Dependent on upstream"
      - "Must negotiate or fight"
      - "Often poorer as a result"

  in_game_events:
    water_shortage:
      trigger: "Low river year, upstream blockage"
      effects:
        - "Reduced irrigation"
        - "Crop stress"
        - "Price increases"
        - "Social tension"
      player_options:
        - "Negotiate with upstream"
        - "Prepare for conflict"
        - "Innovate water storage"

    water_conflict:
      trigger: "Prolonged shortage, insult to honor"
      forms:
        - "Sabotage of canals"
        - "Border raids"
        - "Full warfare"
      player_role:
        - "Participate in defense"
        - "Mediate peace"
        - "Exploit chaos"
```

---

## 9. Conflict & Warfare

### 9.1 Causes of Conflict

```yaml
conflict_causes:
  water_rights:
    frequency: "Most common"
    trigger: "Upstream diverts water, canals damaged"
    resolution: "Negotiation, arbitration, or war"

  land_disputes:
    frequency: "Common"
    trigger: "Boundary disagreements, encroachment"
    resolution: "Court, survey, or force"

  honor:
    frequency: "Occasional"
    trigger: "Insult, broken oath, personal grudge"
    escalation: "Can pull families, then communities into conflict"

  resources:
    frequency: "During scarcity"
    trigger: "Food shortage, material needs"
    target: "Raids on caravans, settlements"

  external_invasion:
    frequency: "Periodic"
    sources: "Mountain tribes (Gutians), Elamites, nomads"
    trigger: "Central power weakness, opportunity"
```

### 9.2 Warfare Mechanics

```yaml
warfare_system:
  militia_system:
    description: "All free men expected to fight"
    equipment: "Bring your own weapons"
    typical_arms:
      - "Copper/bronze spear"
      - "Axe"
      - "Slingshot"
      - "Shield (if wealthy)"
    training: "Minimal for most, better for elite"

  military_organization:
    leader: "King/war leader"
    officers: "Noble commanders"
    units: "Based on neighborhood/profession"
    tactics: "Phalanx-like formations, missile support"

  siege_warfare:
    methods:
      - "Battering ram against gates"
      - "Sappers undermine walls"
      - "Scaling ladders"
      - "Starvation siege"
    defense:
      - "Thick mud-brick walls"
      - "Towers for archers"
      - "Pouring materials on attackers"
      - "Stockpiled food/water"

  psychological_warfare:
    methods:
      - "Impaled enemies outside walls"
      - "Threats and demands"
      - "Displays of strength"
```

### 9.3 Player Combat

```yaml
player_combat:
  combat_system:
    type: "Skill-based, not twitch"
    factors:
      - "Weapon skill"
      - "Stamina"
      - "Equipment quality"
      - "Tactical decisions"
      - "Numbers"

  military_service:
    call_to_arms:
      trigger: "War declared, invasion"
      expectation: "All able men answer"
      equipment: "Player must have or acquire"

    evasion:
      possible: "Can try to avoid"
      consequences:
        - "Severe reputation damage"
        - "Possible legal penalty"
        - "Labeled coward"

  combat_outcomes:
    victory:
      personal: "Loot, reputation, possible advancement"
      city: "Resources, territory, glory"

    defeat:
      personal: "Death, injury, capture"
      city: "Loss of resources, subjugation"

    capture:
      outcome: "Become slave unless ransomed"
      ransom: "Family/friends must pay"
      escape: "Possible but difficult"

  karma_and_combat:
    self_defense: "Neutral (0)"
    declared_war: "Minor negative (-5 per kill)"
    atrocities: "Major negative (-50 to -100)"
    mercy_shown: "Positive (+10 to +25)"
```

### 9.4 Civil Unrest

```yaml
civil_unrest:
  triggers:
    famine:
      threshold: "Food prices 3x normal, shortages"
      manifestation: "Looting, breakdown of order"

    oppression:
      threshold: "Corvée too heavy, taxes crushing"
      manifestation: "Work stoppages, migration"

    succession_crisis:
      threshold: "Leadership unclear"
      manifestation: "Factions, violence"

  player_options:
    join_unrest:
      role: "Participant in uprising"
      risk: "Death if suppressed"
      reward: "Change in power structure"

    support_order:
      role: "Help maintain stability"
      reward: "Favor with authorities"
      risk: "Target of rebels"

    exploit_chaos:
      role: "Use disorder for personal gain"
      risk: "Multiple enemies"
      reward: "Opportunity for advancement"

    flee:
      role: "Leave area until settled"
      cost: "Abandon property, relationships"
      safety: "Remove from danger"
```

---

## 10. Death & Dying

### 10.1 Causes of Death

```yaml
mortality:
  common_causes:
    disease: "40% of deaths"
    childbirth: "10% (for women)"
    malnutrition: "15%"
    violence: "10%"
    accidents: "15%"
    old_age: "10% (reaching old age rare)"

  life_expectancy:
    birth: "~30-35 years average"
    if_survive_childhood: "~45-50 possible"
    reaching_60: "Rare, respected as elder"

  infant_mortality:
    rate: "30-50% before age 5"
    causes: "Disease, malnutrition, accidents"
    cultural_response: "Naming delayed until survival likely"
```

### 10.2 Death Rituals

```yaml
death_rituals:
  preparation:
    body_washing: "By family members"
    anointing: "Oil and herbs"
    dressing: "Best clothes"
    items: "Personal belongings for afterlife"

  burial:
    location: "Family grave, cemetery, sometimes under house floor"
    method: "Inhumation (burial), not cremation"
    grave_goods:
      poor: "Minimal (pot, food)"
      wealthy: "Extensive (jewelry, weapons, servants in extreme cases)"

  mourning:
    duration: "Days to weeks depending on status"
    practices:
      - "Wailing"
      - "Torn clothes"
      - "Disheveled appearance"
      - "Restricted activities"

  ongoing_obligations:
    food_offerings: "Regular offerings to the dead"
    water_offerings: "The dead are thirsty"
    remembrance: "Speak their name"
    consequence: "Neglected dead become harmful ghosts"
```

### 10.3 The Afterlife

```yaml
afterlife_beliefs:
  the_underworld:
    name: "Kur, Irkalla"
    description: "Dark, dusty place beneath the earth"
    ruler: "Ereshkigal (Queen of the Dead)"

  the_dead:
    existence: "Shadow existence, no joy"
    needs: "Still need food, water from living"
    fate: "Same for rich and poor mostly"

  ghosts:
    cause: "Improper burial, neglected offerings"
    effects: "Haunt the living, cause illness"
    remedy: "Proper offerings, exorcism"

  player_integration:
    ancestor_hall: "Visit deceased characters"
    ghost_events: "Neglected dead may appear"
    karma_connection: "Afterlife quality varies by karma"
```

---

## 11. Random Life Events

### 11.1 Event Categories

```yaml
random_events:
  positive:
    windfall:
      examples:
        - "Find valuable item"
        - "Unexpected inheritance"
        - "Merchant overpays"
      frequency: "Rare"

    opportunity:
      examples:
        - "Job offer from important person"
        - "Invitation to exclusive event"
        - "Meet traveler with knowledge"
      frequency: "Occasional"

    blessing:
      examples:
        - "Good omen seen"
        - "Divine favor sign"
        - "Health improvement"
      frequency: "Based on religious standing"

  negative:
    misfortune:
      examples:
        - "Tool breaks"
        - "Goods spoil"
        - "Minor theft"
      frequency: "Regular"

    illness:
      examples:
        - "Contract disease"
        - "Family member sick"
        - "Workplace injury"
      frequency: "Regular"

    disaster:
      examples:
        - "House fire"
        - "Flood damage"
        - "Death in family"
      frequency: "Occasional"

  neutral:
    encounters:
      examples:
        - "Meet interesting NPC"
        - "Witness unusual event"
        - "Hear strange rumor"
      frequency: "Regular"

    opportunities:
      examples:
        - "New job posting"
        - "Business opportunity"
        - "Quest hook"
      frequency: "Regular"
```

### 11.2 Event Examples

```yaml
detailed_events:
  the_omen:
    trigger: "Random or based on actions"
    description: |
      You see a hawk diving on a fish in the canal.
      An old woman gasps: "The gods speak!"
    options:
      - "Seek interpretation from priest"
      - "Ignore it"
      - "Ask the woman what it means"
    outcomes:
      interpret: "Gain clue about future event"
      ignore: "Miss opportunity, slight impiety"
      ask: "Local knowledge, social connection"

  the_traveler:
    trigger: "Random at harbor or gate"
    description: |
      A dusty merchant from Dilmun seeks lodging.
      He carries unusual goods and stranger stories.
    options:
      - "Offer hospitality"
      - "Trade with him"
      - "Listen to his stories"
    outcomes:
      hospitality: "+Reputation, learn foreign knowledge"
      trade: "Acquire exotic goods"
      listen: "Lore clues, map information"

  the_dispute:
    trigger: "Random in neighborhood"
    description: |
      Two neighbors argue loudly. One claims the other
      let his canal overflow and ruined his vegetables.
    options:
      - "Mediate"
      - "Support one side"
      - "Ignore"
    outcomes:
      mediate: "+Reputation, make two contacts (or enemies)"
      support: "Ally + enemy"
      ignore: "No effect (miss opportunity)"

  the_stranger_at_night:
    trigger: "Random at night in city"
    description: |
      A shadowy figure approaches in the darkness.
      "Friend, I need help. I've been robbed and
      have nowhere to sleep."
    options:
      - "Offer shelter"
      - "Give some barley"
      - "Refuse and walk away"
      - "Alert the watch"
    outcomes:
      shelter: "Could be genuine (reputation+), could be thief (risk)"
      give: "Safe middle ground, minor reputation+"
      refuse: "No effect (missed opportunity or avoided danger)"
      alert: "Watch investigates (50% catches criminal, 50% innocent)"

  the_birth:
    trigger: "Random if married"
    description: |
      Your wife is in labor. The midwife has been called.
      The household is anxious.
    options:
      - "Stay and support"
      - "Make offerings at temple"
      - "Continue working (historically common)"
    outcomes:
      - "Child born or dies (random)"
      - "Wife survives or dies (random, modified by wealth/care)"
      - "Karma effect based on choice and outcome"

  the_death:
    trigger: "Random for known NPCs"
    description: |
      Word reaches you: [NPC NAME] has died.
      [Cause of death]. The funeral is tomorrow.
    options:
      - "Attend funeral"
      - "Send condolences"
      - "Ignore"
    outcomes:
      attend: "Social obligation fulfilled, possible inheritance/debt"
      condolences: "Minimum acceptable response"
      ignore: "Reputation damage with connected NPCs"
```

---

## 12. Commerce & Shopping

### 12.1 The Marketplace

```yaml
marketplace_overview:
  location: "Near temple, along main processional way, harbor area"
  timing: "Morning hours (before midday heat)"
  nature: "Not permanent shops—temporary stalls, ground displays, ambulant sellers"

  marketplace_atmosphere:
    sounds:
      - "Haggling voices"
      - "Braying donkeys"
      - "Potter's wheel"
      - "Copper being hammered"
      - "Children playing"
    smells:
      - "Fresh bread from ovens"
      - "Fish from the harbor"
      - "Incense from temple"
      - "Animal dung"
      - "Date wine and beer"
    sights:
      - "Colorful textiles hung on poles"
      - "Glinting copper and jewelry"
      - "Piles of grain and vegetables"
      - "Craftsmen at work"
      - "Temple looming over all"
```

### 12.2 Jewelry: The Ultimate Status Symbol

```yaml
jewelry_system:
  importance: "Jewelry is the primary display of wealth and status"

  who_wears_jewelry:
    both_genders: "Men and women wore extensive jewelry"
    class_indicator: "Quality and material instantly shows social standing"
    religious_significance: "Some items carry divine protection"

  popular_items:
    collar_necklaces:
      description: "Wide collar necklaces with multiple strands"
      materials: "Beads of various stones, gold spacers"
      worn_by: "Both genders"
      status_indicator: "Width and material = wealth"

    earrings:
      description: "Heavy hoop or pendant earrings"
      materials: "Gold, silver, or bronze"
      worn_by: "Both genders (men too!)"
      note: "Large earrings = significant wealth display"

    cylinder_seals:
      description: "Carved cylinder worn on pin or string"
      function: "Personal signature—rolled on clay to mark property/contracts"
      material: "Stone (valuable) or clay (common)"
      importance: "Essential for anyone doing business"
      uniqueness: "Each seal is unique—your identity"

    rings:
      description: "Finger and toe rings"
      materials: "Gold, silver, bronze"
      function: "Pure adornment, sometimes signet function"

    bracelets:
      description: "Thick bangles, sometimes hinged"
      materials: "Gold, silver, bronze, shell"
      worn_by: "Both genders, multiple at once"

    hair_ornaments:
      description: "Pins, combs, ribbons with beads"
      worn_by: "Women primarily"
      special: "Gold leaf hair decorations for wealthy"

  precious_materials:
    lapis_lazuli:
      description: "Deep blue stone with gold flecks"
      source: "Afghanistan (Badakhshan mines)"
      rarity: "Extremely valuable—came thousands of miles"
      significance: "Color of heaven, associated with gods"
      price: "Small bead = 5-10 sila; large piece = months of wages"

    carnelian:
      description: "Red-orange semi-precious stone"
      source: "Indus Valley (India/Pakistan)"
      rarity: "Very valuable, long trade routes"
      significance: "Blood-colored, protective properties"
      price: "Moderate to high depending on quality"

    gold:
      description: "The eternal metal"
      sources: "Turkey (Anatolia), Egypt"
      rarity: "Rare, reserved for wealthy and temples"
      significance: "Flesh of the gods"
      forms: "Sheet, wire, cast, granulation"

    silver:
      description: "The money metal"
      sources: "Turkey, Iran"
      use: "Currency and jewelry"
      significance: "More common than gold but still valuable"

    shell:
      description: "Cowrie shells, mother of pearl"
      source: "Persian Gulf, Indian Ocean"
      use: "Common people's jewelry"
      significance: "Beauty accessible to lower classes"

  game_mechanics:
    jewelry_as_wealth:
      function: "Portable, displayable wealth"
      benefits:
        - "Instant status recognition by NPCs"
        - "Can be traded/sold in emergencies"
        - "Marriage negotiations affected"
        - "Some items provide minor buffs (cylinder seal = +business)"

    acquisition:
      purchase: "From jewelers in craftsmen district"
      commission: "Custom piece (expensive, unique)"
      inheritance: "Family pieces"
      loot: "Found or stolen (with consequences)"
      gift: "From patron, temple, or admirer"

    wearing_effects:
      high_quality_jewelry:
        reputation: "+5-20 depending on quality"
        npc_reactions: "Treated with more respect"
        risk: "Target for theft"

      inappropriate_jewelry:
        wearing_above_station: "NPCs suspicious, questions asked"
        wearing_temple_jewelry: "Sacrilege if not entitled"
```

### 12.3 Mass-Produced Goods

```yaml
mass_production:
  the_potters_wheel:
    innovation: "Potter's wheel (already invented by 4500 BCE)"
    impact: "Transformed pottery from expensive craft to cheap commodity"

  pottery:
    types:
      beveled_rim_bowls:
        description: "Simple, mass-produced food bowls"
        use: "Daily meals, ration distribution"
        quality: "Rough, utilitarian"
        price: "Essentially disposable—0.2 sila"
        note: "Found in thousands at archaeological sites"

      storage_jars:
        description: "Large vessels for grain, oil, beer"
        use: "Household storage"
        quality: "Functional, some decorated"
        price: "2-10 sila depending on size"

      fine_pottery:
        description: "Decorated, well-made vessels"
        use: "Temple offerings, wealthy households"
        quality: "Painted, burnished"
        price: "10-50 sila"

    pottery_markets:
      cheap_section: "Stacks of basic bowls, anyone can afford"
      quality_section: "Better vessels for those with means"
      custom_orders: "Commission specific pieces"

  textiles:
    production: "Major industry—temple and private workshops"

    types:
      rough_wool:
        description: "Basic cloth for common people"
        use: "Simple garments, wrappings"
        price: "1-3 sila per length"

      fine_wool:
        description: "Softer, better processed wool"
        use: "Better garments, blankets"
        price: "5-15 sila per length"

      linen:
        description: "Flax-based cloth"
        use: "Priestly garments, luxury wear"
        price: "20-100 sila per length"
        note: "Egypt famous for linen; imported"

      dyed_textiles:
        description: "Colored cloth (red, blue, yellow)"
        use: "Status display, special occasions"
        price: "2-5x base price"
        rare_colors: "Purple (shellfish dye) extremely expensive"

    ready_made_garments:
      simple_tunic: "5-10 sila"
      quality_tunic: "20-50 sila"
      cloak: "10-30 sila"
      priestly_robe: "100+ sila"

  furniture:
    availability: "Most people have minimal furniture"

    common_items:
      reed_mats:
        description: "Woven reeds for floor, sleeping"
        use: "Universal—everyone has these"
        price: "0.5-2 sila"

      wooden_stools:
        description: "Simple three or four-legged stools"
        use: "Sitting (important people)"
        price: "5-15 sila"
        note: "Chairs with backs = high status"

      storage_chests:
        description: "Wooden or basketry boxes"
        use: "Storing valuables, clothes"
        price: "10-30 sila"

      beds:
        description: "Wooden frame with rope or reed base"
        use: "Wealthy households only"
        price: "50-200 sila"
        note: "Most people sleep on mats"

      tables:
        description: "Low tables for food service"
        use: "Wealthy households"
        price: "20-50 sila"

    luxury_furniture:
      inlaid_chairs: "Reserved for temples, royalty"
      decorated_chests: "Carved, inlaid with shell or stone"
      beds_with_headrests: "Ultimate luxury"
```

### 12.4 Shopping Mechanics

```yaml
shopping_system:
  haggling:
    description: "All prices negotiable"
    mechanics:
      base_price: "Seller's opening price (inflated)"
      target_price: "Fair market value"
      floor_price: "Absolute minimum seller accepts"

    skill_factors:
      player_charisma: "Affects starting position"
      reputation: "Known customers get better deals"
      relationship: "Repeat business = trust"
      scarcity: "Rare items = less negotiation room"

    haggling_minigame:
      options:
        - "Accept price (quick, overpay)"
        - "Counter-offer (risk offending)"
        - "Walk away (may be called back)"
        - "Compare to other sellers (time cost)"
      outcomes:
        - "Deal at good price"
        - "Deal at poor price"
        - "No deal (seller offended)"
        - "Relationship built (future discounts)"

  payment_methods:
    barley:
      description: "Standard payment for small purchases"
      acceptance: "Universal"
      convenience: "Must carry physical grain"

    silver:
      description: "Weighed silver for larger purchases"
      acceptance: "Merchants, craftsmen"
      convenience: "Compact, but must verify weight"
      note: "Scales present at every transaction"

    barter:
      description: "Trade goods directly"
      acceptance: "Common, especially for equals"
      convenience: "Depends on matching needs"

    credit:
      description: "Deferred payment (recorded on clay)"
      acceptance: "Only with established reputation"
      risk: "Debt slavery if default"

  vendor_types:
    street_sellers:
      goods: "Food, simple pottery, trinkets"
      prices: "Cheapest"
      reliability: "Variable"
      location: "Throughout city"

    market_stalls:
      goods: "Mid-range goods, varied selection"
      prices: "Moderate"
      reliability: "Regular sellers, reputation matters"
      location: "Marketplace"

    craftsmen_shops:
      goods: "Quality crafted items"
      prices: "Higher"
      reliability: "High—reputation is their livelihood"
      location: "Craftsmen district"

    temple_shops:
      goods: "Religious items, high-quality goods"
      prices: "Fixed (no haggling)"
      reliability: "Guaranteed"
      location: "Temple complex"

    traveling_merchants:
      goods: "Exotic items from distant lands"
      prices: "High (rarity premium)"
      reliability: "Variable—may never see again"
      location: "Harbor, caravanserai"
```

### 12.5 What Players Can Buy

```yaml
purchasable_items:
  essential_goods:
    food:
      barley: "Base unit"
      bread: "0.5 sila/loaf"
      fish_fresh: "2-3 sila"
      fish_dried: "1-2 sila"
      dates: "1-2 sila/basket"
      onions: "0.2 sila/bundle"
      beer: "0.5-2 sila/jar"
      meat: "5-10 sila (special occasions)"

    water:
      canal_water: "Free but risky"
      well_water: "Small fee"
      temple_water: "Offering required"

  tools_and_equipment:
    farming:
      copper_sickle: "20-30 sila"
      wooden_hoe: "5-10 sila"
      plow: "50-100 sila"
      seed_grain: "Seasonal price varies"

    fishing:
      nets: "10-30 sila"
      hooks: "1-3 sila"
      boat: "100-500 sila"

    crafting:
      potters_wheel_access: "Rent: 1 sila/day"
      loom: "30-50 sila"
      copper_tools: "10-50 sila depending on type"

  status_items:
    jewelry:
      shell_necklace: "2-5 sila"
      carnelian_beads: "20-50 sila"
      lapis_lazuli_pendant: "100-500 sila"
      gold_earrings: "200-1000 sila"
      cylinder_seal_basic: "10-20 sila"
      cylinder_seal_fine: "50-200 sila"

    clothing:
      basic_tunic: "5-10 sila"
      quality_tunic: "20-50 sila"
      linen_garment: "50-100 sila"
      dyed_wool_cloak: "30-80 sila"

  religious_items:
    small_figurine: "1-5 sila"
    offering_bowl: "2-5 sila"
    incense: "5-20 sila"
    protective_amulet: "5-30 sila"
    lamashtu_protection: "10-50 sila"

  housing:
    rent_reed_hut: "5-10 sila/month"
    rent_mud_brick_room: "15-30 sila/month"
    rent_small_house: "50-100 sila/month"
    buy_small_house: "500-2000 sila"
    buy_nice_house: "5000-20000 sila"
```

---

## 13. Animals & Wildlife

> The marshes teemed with life—some that served you, some you served, and some that would kill you.

### 13.1 The Wilderness Danger System

```yaml
wilderness_danger:
  design_purpose: |
    If players venture too far from their mission—wandering aimlessly,
    hiding in the wilderness, avoiding objectives—the game comes after them.
    This is a TIME-BASED game. Players must stay focused.

  the_principle:
    statement: "There is only so long you can be in the wild"
    mechanic: "Predator danger increases with time away from civilization"
    effect: "Natural consequence, not artificial wall"

  danger_escalation:
    time_in_wilderness:
      0_1_hours:
        danger_level: "Low"
        encounters: "Occasional wildlife sighting (deer, birds)"
        predator_chance: "5%"

      1_4_hours:
        danger_level: "Moderate"
        encounters: "More frequent wildlife"
        predator_chance: "15%"
        warning_signs:
          - "Distant howls"
          - "Tracks in mud"
          - "Nervous animal behavior"

      4_8_hours:
        danger_level: "High"
        encounters: "Predators actively hunting"
        predator_chance: "40%"
        warning_signs:
          - "Stalking shadows"
          - "Circling movement"
          - "Direct sightings"

      8_plus_hours:
        danger_level: "Extreme"
        encounters: "Multiple predators, pack behavior"
        predator_chance: "75%"
        warning_signs:
          - "You are being hunted"
          - "Escape routes closing"
          - "Fight or die"

  distance_from_safety:
    safe_zones:
      - "City walls"
      - "Established villages"
      - "Patrolled trade routes"
      - "Active work sites (fields, quarries)"

    danger_multipliers:
      near_city: "0.5x danger"
      farmland: "1x danger"
      open_plains: "1.5x danger"
      marshes: "2x danger (crocodiles, ambush terrain)"
      deep_wilderness: "3x danger"

  time_of_day:
    dawn_dusk: "2x predator activity (hunting hours)"
    night: "3x predator activity"
    midday: "0.5x predator activity (lions sleep)"

  training_data_value:
    questions:
      - "How do players balance risk vs. reward in wilderness?"
      - "What triggers retreat vs. pushing forward?"
      - "How does danger affect decision-making speed?"
```

### 13.2 Predators

```yaml
predators:
  note: "Ancient Eridu sat near lush marshes—far different from modern desert"

  asiatic_lion:
    status: "Apex predator (now extinct in Iraq)"
    habitat: "Plains, marsh edges, anywhere with prey"
    behavior:
      - "Males solitary or in pairs"
      - "Females in small prides"
      - "Ambush hunters, prefer dawn/dusk"
    danger_level: "Extreme"
    encounter_type: "Sudden ambush or stalking approach"
    combat:
      health: "Very high"
      damage: "Lethal in 2-3 hits"
      escape: "Difficult—lions are fast"
    deterrents:
      - "Fire (strongest deterrent)"
      - "Groups of 4+ people"
      - "Loud noise"
      - "Spears presented"
    game_mechanics:
      - "Roar warns of presence"
      - "Will stalk before attacking"
      - "May test defenses before committing"
      - "Will retreat if injured"

  leopard:
    status: "Solitary stealth predator"
    habitat: "Rocky areas, trees, marsh vegetation"
    behavior:
      - "Ambush from above or cover"
      - "Drag kills into trees"
      - "Primarily nocturnal"
    danger_level: "Very High"
    encounter_type: "Sudden ambush—little warning"
    combat:
      health: "High"
      damage: "High (throat attack)"
      escape: "Moderate—leopards commit or flee"
    deterrents:
      - "Never being alone"
      - "Constant vigilance"
      - "Fire"
    game_mechanics:
      - "Minimal warning before attack"
      - "Targets isolated individuals"
      - "May flee after first strike if resisted"

  wolves:
    status: "Pack predators"
    habitat: "Plains, forest edges"
    behavior:
      - "Hunt in packs of 5-15"
      - "Test prey for weakness"
      - "Coordinate attacks"
    danger_level: "High (pack), Moderate (individual)"
    encounter_type: "Circling, testing, then attack"
    combat:
      health: "Moderate per wolf"
      damage: "Moderate per wolf, deadly in pack"
      escape: "Possible if you wound lead wolves"
    deterrents:
      - "Fire"
      - "Wounding pack members"
      - "Appearing strong/healthy"
    game_mechanics:
      - "Howling alerts to presence"
      - "Will follow at distance first"
      - "Target weak, slow, or isolated"

  hyenas:
    status: "Opportunistic pack predators/scavengers"
    habitat: "Near settlements, following herds"
    behavior:
      - "Hunt in clans"
      - "Will attack lone humans"
      - "Extremely persistent"
    danger_level: "High (clan), Moderate (individual)"
    encounter_type: "Bold approach, testing courage"
    combat:
      health: "Moderate"
      damage: "Moderate but crushing bite"
      escape: "Possible—hyenas test before committing"
    deterrents:
      - "Standing ground"
      - "Fire"
      - "Groups"
    game_mechanics:
      - "Laughing calls signal presence"
      - "Will shadow travelers"
      - "Attack if weakness shown"

  marsh_crocodile:
    status: "Aquatic ambush predator"
    habitat: "Rivers, canals, marshes"
    behavior:
      - "Lie submerged waiting"
      - "Explosive ambush"
      - "Drag into water"
    danger_level: "Extreme (in water), Low (on land)"
    encounter_type: "No warning—sudden grab"
    combat:
      health: "Very high"
      damage: "Lethal grab"
      escape: "Almost impossible once grabbed"
    deterrents:
      - "Never enter unknown water"
      - "Watch for eyes at waterline"
      - "Use established crossing points"
    game_mechanics:
      - "Invisible until attack"
      - "One-hit potential kill"
      - "Only attacks at water's edge"
```

### 13.3 Pets & Companion Animals

```yaml
pets:
  historical_note: |
    To enter Eridu was to see collared dogs roaming freely.
    Dogs wore wide collars and leashes—beloved family companions.

  dogs:
    status: "The first pet—remarkably common and elevated status"
    types:
      mastiff:
        description: "Large, powerful, thick-bodied"
        use: "Guarding homes, herding livestock, protection"
        temperament: "Loyal, territorial, intimidating"
        game_benefits:
          - "+50% theft deterrence at home"
          - "Warning of intruders"
          - "Combat support (moderate damage)"
        cost: "30-80 sila"

      saluki_greyhound:
        description: "Slender, fast, elegant"
        use: "Hunting gazelle and small game"
        temperament: "Independent, swift, keen sight"
        game_benefits:
          - "+30% hunting success"
          - "Can run down wounded prey"
          - "Status symbol"
        cost: "50-150 sila"

    cultural_significance:
      collars: "Wide leather or woven collars—sign of ownership"
      spiritual: "Clay 'Nimrud dogs' buried under doorsteps to protect from demons"
      legal: "Dogs had legal protections—killing someone's dog required compensation"

    game_mechanics:
      acquisition: "Buy, breed, or receive as gift"
      care: "Must feed daily (2-3 sila equivalent)"
      bonding: "Loyalty increases with time and care"
      death: "Dogs can die (predators, disease, age)—emotional event"

  cats:
    status: "Practical companions"
    use: "Rodent control near grain storage"
    presence: "Common in households, granaries, temples"
    game_benefits:
      - "-50% food spoilage at home"
      - "Minor pest control buff"
    cost: "5-15 sila"
    note: "Less emotionally bonded than dogs in this era"

  exotic_pets:
    availability: "Wealthy citizens and royalty only"
    types:
      monkeys:
        source: "Traded from Indus Valley"
        use: "Entertainment, status"
        cost: "200-500 sila"

      trained_birds:
        types: ["Ibis", "Heron", "Falcon"]
        use: "Status, sometimes hunting"
        cost: "50-200 sila"

      trained_pelican:
        description: "Can fish for owner"
        use: "Novelty fishing method"
        cost: "100-300 sila"
        note: "Historical oddity—actually documented"
```

### 13.4 Livestock

```yaml
livestock:
  economic_importance: "Eridu's economy depended on these animals"

  sheep:
    status: "Most economically vital livestock"
    products:
      wool: "Massive textile industry depended on sheep wool"
      milk: "Sheep milk for drinking, cheese"
      meat: "Mutton—the common meat"
    numbers: "Large flocks managed by shepherds"
    game_mechanics:
      ownership:
        small_flock: "5-20 sheep (50-200 sila investment)"
        medium_flock: "20-100 sheep (requires hired shepherd)"
        large_flock: "100+ sheep (significant operation)"
      income:
        wool_shearing: "Annual income, timed event"
        milk: "Daily small income"
        meat: "Slaughter for special occasions or sale"
      risks:
        - "Predator attacks"
        - "Disease"
        - "Theft"
        - "Drought (no grazing)"

  goats:
    status: "Among first domesticated animals (~8000 BCE)"
    products:
      milk: "More common than sheep milk"
      meat: "Goat meat common for poor"
      hide: "Leather, water skins"
    advantage: "Hardier than sheep, eat anything"
    game_mechanics:
      cost: "5-15 sila per goat"
      care: "Lower maintenance than sheep"
      note: "Good starter livestock"

  cattle:
    status: "Valuable draft animals"
    use:
      primary: "Heavy labor—plowing, pulling carts"
      secondary: "Milk (limited), meat (luxury)"
    cost: "Very expensive (100-500 sila)"
    game_mechanics:
      ownership: "Wealthy farmers, temple estates"
      benefit: "+50% farming efficiency if own plow team"
      risk: "Major loss if dies"
    note: "Too valuable to slaughter for most people"

  onagers_and_donkeys:
    onagers:
      description: "Wild donkeys—stubborn but strong"
      use: "Pulling heavy wagons, trade caravans"
      status: "Used before horses arrived (~2000 BCE)"
      temperament: "Difficult to control"
      game_mechanics:
        cost: "40-100 sila"
        benefit: "Heavy hauling capability"
        downside: "Unreliable, may refuse commands"

    donkeys:
      description: "Domesticated, more tractable"
      use: "Pack animals, light transport"
      cost: "20-60 sila"
      game_mechanics:
        benefit: "Reliable transport, carry 100+ sila goods"
        care: "Must feed, water, rest"

  poultry:
    types:
      ducks: "Common, marsh-friendly"
      geese: "Good guards, meat, feathers"
      chickens: "Called 'the king's birds'—later introduction"
    products: "Meat, eggs"
    cost: "1-5 sila per bird"
    game_mechanics:
      benefit: "Steady egg production (food)"
      space: "Can keep in small urban spaces"
      risk: "Predators (foxes, cats, thieves)"

  bees:
    product: "Honey—the only sweetener"
    value: "High—honey is precious"
    game_mechanics:
      hive_cost: "20-50 sila to establish"
      income: "Periodic honey harvest"
      skill: "Beekeeping knowledge required"
      risk: "Swarm loss, disease"
```

### 13.5 Wildlife & Hunting

```yaml
wildlife:
  environment: |
    Ancient Eridu sat near Persian Gulf marshes—far more lush than today.
    Massive herds roamed plains, waters teemed with life.

  huntable_game:
    gazelle:
      habitat: "Open plains"
      abundance: "Common—massive herds"
      hunting_method: "Chase with dogs, bow, or drive into traps"
      meat_value: "Good quality, valued"
      difficulty: "Moderate (fast but predictable)"

    deer:
      habitat: "Marsh edges, wooded areas"
      abundance: "Moderate"
      hunting_method: "Stalking, ambush"
      meat_value: "Excellent quality"
      difficulty: "Moderate"

    wild_onager:
      habitat: "Open plains"
      abundance: "Common"
      hunting_method: "Chase, drive hunts"
      meat_value: "Acceptable"
      difficulty: "Hard (very fast, stamina)"

    wild_boar:
      habitat: "Marshlands, vegetation"
      abundance: "Moderate"
      hunting_method: "Dogs, spears—dangerous close combat"
      meat_value: "Good, fatty"
      difficulty: "Hard (aggressive, can kill hunters)"

    wild_cattle_aurochs:
      habitat: "Plains, marsh edges"
      abundance: "Rare"
      hunting_method: "Group hunt only—extremely dangerous"
      meat_value: "Excellent, massive quantity"
      difficulty: "Very Hard (can kill multiple hunters)"
      note: "Prestigious hunt—success brings major reputation"

  waterfowl:
    types: ["Ducks", "Geese", "Herons", "Various marsh birds"]
    habitat: "Marshes, canals, rivers"
    hunting_method: "Nets, thrown sticks, bow"
    abundance: "Very common"
    difficulty: "Easy to Moderate"
    note: "Common people's hunting—accessible protein"

  fish:
    abundance: "Staple food—over 50 species in texts"
    methods:
      nets: "Most common, efficient"
      hooks: "Line fishing"
      traps: "Basket traps in canals"
      spears: "For larger fish"
    game_mechanics:
      fishing_locations: "Canals, rivers, marshes"
      skill_based: "Better fishers catch more"
      equipment: "Nets (10-30 sila), hooks (1-3 sila)"
    note: "Many preferred 'fish farm' fish over wild-caught"

  extinct_locally:
    elephants:
      status: "Once lived in region, hunted to local extinction"
      game_implication: "Mentioned in old stories, no longer present"

    note: "The environment was far richer than players might expect"

  hunting_mechanics:
    who_hunts:
      wealthy: "Sport hunting with dogs, servants, equipment"
      common: "Marsh people, plains dwellers—for food"
      professional: "Hunters who sell meat in markets"

    time_investment:
      short_hunt: "2-4 hours, small game, near settlements"
      day_hunt: "Full day, larger game, further out"
      expedition: "Multiple days, dangerous, prestigious targets"

    danger_balance:
      the_tradeoff: |
        Hunting provides food and profit, BUT:
        - Time away from objectives
        - Predator danger increases
        - Miss innovation opportunities
        - Event timers keep running

      optimal_strategy: "Short hunts near safety, not wilderness expeditions"
```

### 13.6 Animal Encounters as Game Events

```yaml
animal_events:
  positive:
    good_hunting:
      trigger: "Successful hunt"
      outcome: "Food, income, reputation"

    livestock_birth:
      trigger: "Animal gives birth"
      outcome: "Increased herd, good omen"

    dog_saves_life:
      trigger: "Dog alerts to or fights off predator"
      outcome: "Survival, deepened bond"

  negative:
    predator_attack:
      trigger: "Wilderness danger, bad luck"
      outcome: "Injury, death, livestock loss"
      types:
        personal: "You are attacked"
        livestock: "Your animals are attacked"
        family: "Family member attacked"

    livestock_disease:
      trigger: "Random, seasonal"
      outcome: "Animal death, potential spread"

    pet_death:
      trigger: "Age, disease, predator"
      outcome: "Emotional event, karma implications"
      note: "Players often strongly affected"

  neutral:
    animal_market:
      trigger: "Periodic event"
      outcome: "Opportunity to buy/sell livestock"

    wild_animal_sighting:
      trigger: "Travel, exploration"
      outcome: "Information, potential hunt, potential danger"
```

---

## 14. Diet & Food

> "The Sumerians ate well when the gods were pleased. When they weren't, you ate whatever you could find."

### 14.1 Staple Foods

```yaml
staple_diet:
  grains:
    barley:
      status: "THE staple—base of everything"
      forms:
        - "Bread (most common food)"
        - "Porridge"
        - "Beer (liquid bread)"
      availability: "Universal, cheap"
      note: "Wages paid in barley"

    wheat:
      status: "Better grain, more valuable"
      forms: "Better bread, treats"
      availability: "More expensive, declining due to salinization"

  vegetables:
    onions:
      status: "Ubiquitous, daily consumption"
      use: "Eaten raw, cooked, flavoring"
      price: "Very cheap (0.2 sila/bundle)"

    garlic:
      status: "Common, valued for flavor and medicine"

    leeks:
      status: "Common in stews"

    legumes:
      types: ["Lentils", "Chickpeas", "Beans"]
      status: "Important protein source for poor"

  fruits:
    dates:
      status: "Primary fruit—extremely important"
      forms: "Fresh, dried, date syrup (sweetener)"
      use: "Eaten alone, baking, brewing"
      availability: "Common, major crop"

    figs:
      status: "Common fruit"

    pomegranates:
      status: "Valued, somewhat luxury"

    grapes:
      status: "For wine (luxury)"

  dairy:
    milk:
      sources: "Sheep, goat, some cattle"
      use: "Drinking, cheese, cooking"

    cheese:
      status: "Common preservation method for milk"
      types: "Fresh and aged varieties"

    butter_ghee:
      status: "Clarified butter for cooking"
```

### 14.2 Meat in the Diet

```yaml
meat_consumption:
  frequency: "Not daily for common people—special occasions, wealth indicator"

  common_meats:
    mutton:
      status: "MOST common meat—the standard"
      source: "Abundant sheep"
      preparation: "Stews, roasted, dried"
      price: "5-10 sila per portion"
      availability: "Accessible to working class occasionally"

    goat:
      status: "Second most common"
      source: "Domesticated goats"
      preparation: "Similar to mutton"
      price: "3-8 sila per portion"
      note: "Slightly cheaper than mutton"

    pork:
      status: "Common in early periods"
      source: "Domesticated pigs"
      preparation: "Roasted, stewed"
      price: "4-9 sila per portion"
      note: |
        Pork consumption became taboo after ~2400 BCE.
        In 4500 BCE setting, pork is still acceptable.
      game_mechanic: "Available, but some NPCs disapprove"

    poultry:
      types: "Duck, goose, chicken"
      status: "Common, accessible"
      price: "2-5 sila per bird"
      note: "Eggs also important protein source"

  luxury_meats:
    beef:
      status: "LUXURY—cattle too valuable as draft animals"
      who_eats: "Wealthy, temple feasts, royalty"
      preparation: "Elaborate dishes, roasted whole"
      price: "20-50 sila per portion"
      note: "Common people rarely taste beef"

  hunted_game:
    gazelle:
      status: "Wild-caught, valued"
      availability: "Depends on hunting success"
      price: "Variable—8-15 sila"

    deer:
      status: "Excellent quality"
      price: "10-20 sila"

    wild_boar:
      status: "Rich, fatty meat"
      price: "8-15 sila"
      note: "Hunting dangerous"

    wild_fowl:
      status: "Common supplement"
      price: "1-4 sila per bird"
```

### 14.3 Fish & Aquatic Foods

```yaml
fish:
  importance: |
    Fish was a STAPLE food for both rich and poor.
    Over 50 species mentioned in Sumerian texts.
    Often purchased from street vendors.

  sources:
    fish_farms:
      description: "Managed ponds and canal sections"
      preference: "Many preferred farm fish to wild-caught"
      reason: "Consistent quality, availability"

    wild_caught:
      locations: "Rivers, canals, marshes, gulf"
      method: "Nets, traps, hooks, spears"

    street_vendors:
      description: "Fish sellers throughout city"
      offerings: "Fresh, smoked, dried, salted"

  preparation:
    fresh: "Grilled, stewed"
    dried: "Preserved for storage"
    salted: "Long-term preservation"
    smoked: "Flavor and preservation"

  price:
    fresh_common: "2-3 sila"
    dried: "1-2 sila"
    premium_species: "5-10 sila"

  other_aquatic:
    turtles:
      status: "Eaten, shell used for tools"
      availability: "Marsh areas"

    shellfish:
      status: "Collected in marshes and coast"

  game_mechanics:
    fishing_profession:
      starting_class: "Fisher (available)"
      income: "Steady, scalable"
      equipment: "Nets, boat optional"

    food_source:
      benefit: "Reliable protein, available to all classes"
      risk: "Seasonal variation, weather dependent"
```

### 14.4 Food Preparation & Preservation

```yaml
food_preparation:
  cooking_methods:
    stews_and_soups:
      status: "Most common preparation"
      description: "Meat, vegetables, grains combined"
      benefit: "Stretches ingredients, easier to digest"

    roasting:
      status: "Common for meat"
      method: "Spit roasting, clay ovens"

    baking:
      status: "Daily for bread"
      equipment: "Clay ovens (tannur)"

    boiling:
      status: "Common"
      vessels: "Clay pots"

  preservation:
    drying:
      foods: "Meat, fish, fruits, vegetables"
      method: "Sun-drying"
      duration: "Months to year"

    salting:
      foods: "Meat, fish"
      method: "Salt curing"
      duration: "Long-term"

    smoking:
      foods: "Meat, fish"
      method: "Smoke houses, fires"
      duration: "Months"

    fermentation:
      foods: "Beer, bread (sourdough)"
      importance: "Major part of diet"

    honey:
      use: "Preservative for fruits, some meats"
      note: "Expensive but effective"

  storage:
    granaries: "Large-scale grain storage"
    pottery_jars: "Household storage"
    underground: "Cooler temperatures"
    problem: "Rodents, insects, spoilage constant threat"

  game_mechanics:
    food_spoilage:
      fresh_food: "Spoils in 1-2 days"
      preserved: "Lasts weeks to months"
      storage_quality: "Better storage = less spoilage"

    cooking_skill:
      benefit: "Better nutrition from same ingredients"
      recipes: "Discoverable, tradeable"
```

### 14.5 Food Prices & Economy

```yaml
food_economy:
  daily_food_cost:
    subsistence: "2-3 sila barley equivalent"
    comfortable: "5-8 sila equivalent"
    wealthy: "15-30 sila equivalent"

  price_reference:
    basic_foods:
      barley_1_sila: "1 (base unit)"
      bread_loaf: "0.5"
      onions_bundle: "0.2"
      dates_basket: "1-2"
      beer_jar: "0.5-2"
      fish_fresh: "2-3"

    meat_prices:
      mutton_portion: "5-10"
      goat_portion: "3-8"
      pork_portion: "4-9"
      beef_portion: "20-50"
      poultry_bird: "2-5"

    luxury_items:
      honey_jar: "10-30"
      wine_jar: "20-50"
      exotic_spices: "50-200"

  seasonal_variation:
    harvest_time: "-20% grain prices"
    drought: "+50-100% all food prices"
    flood: "+30% prices, some foods unavailable"
    festival: "+20% meat prices (demand)"

  hunger_mechanics:
    satiation: "Decreases over time"
    consequences:
      hungry: "-10% stamina regen"
      very_hungry: "-25% stamina, concentration penalties"
      starving: "-50% stamina, health damage"
      starvation: "Death if prolonged"
```

---

## 15. Training Data Value

### 15.1 Life Simulation Data

```yaml
life_simulation_data:
  questions_studied:
    daily_decisions:
      - "How do humans prioritize when resources are limited?"
      - "What trade-offs do people make between work and rest?"
      - "How do routines form and adapt?"

    social_navigation:
      - "How do people build relationships under hierarchy?"
      - "What motivates social obligation fulfillment?"
      - "How is trust established and maintained?"

    crisis_response:
      - "How do humans respond to slow-moving crises (salinization)?"
      - "What triggers action vs. denial?"
      - "How do communities coordinate (or fail to)?"

    moral_decisions:
      - "How do people balance self-interest and community?"
      - "What role does belief play in behavior?"
      - "How are difficult trade-offs resolved?"

  data_captured:
    time_allocation:
      - "How players spend their days"
      - "Work vs. social vs. personal time"
      - "Response to time pressure"

    resource_management:
      - "Earning and spending patterns"
      - "Saving vs. consumption"
      - "Risk tolerance"

    relationship_building:
      - "Who players connect with"
      - "Effort invested in relationships"
      - "Response to social obligations"

    problem_recognition:
      - "When do players notice salinization?"
      - "What triggers investigation?"
      - "Innovation timing and approach"
```

### 15.2 High-Value Scenarios

```yaml
high_value_scenarios:
  ecological_crisis:
    description: "Long-term problem requiring collective action"
    data_value: "How humans respond to slow disasters"
    questions:
      - "When do players recognize the pattern?"
      - "What motivates action vs. denial?"
      - "How do players organize others?"

  legal_disputes:
    description: "Navigate victim-led justice"
    data_value: "Justice-seeking behavior"
    questions:
      - "When do players pursue legal action?"
      - "How do they gather evidence?"
      - "What settlements are accepted?"

  disease_outbreaks:
    description: "Health crisis with limited options"
    data_value: "Health decision-making"
    questions:
      - "How do players evaluate treatment options?"
      - "What prevention measures are taken?"
      - "How does fear affect behavior?"

  religious_obligations:
    description: "Balance personal goals with social expectations"
    data_value: "Conformity vs. individualism"
    questions:
      - "How much do players participate?"
      - "How do they handle doubt?"
      - "What triggers full engagement vs. minimum?"
```

---

## 16. Implementation Notes

### 16.1 MVP Scope

```yaml
mvp_life_simulation:
  included:
    daily_cycle:
      - "Basic time system (dawn/day/evening/night)"
      - "Work schedules"
      - "Sleep requirements"

    health:
      - "Disease system (3-5 diseases)"
      - "Basic treatment options"
      - "Health meter"

    social:
      - "Reputation system"
      - "Basic relationship tracking"
      - "Marriage (simplified)"

    legal:
      - "Theft resolution"
      - "Basic disputes"

    religion:
      - "Temple favor"
      - "Basic obligations"

    salinization:
      - "Visible decline over time"
      - "Innovation opportunity"

  deferred:
    - "Full disease system"
    - "Complex legal cases"
    - "Warfare system"
    - "All random events"
    - "Children/family system"
```

### 16.2 Authenticity vs. Playability

```yaml
balance_decisions:
  disease_frequency:
    historical: "Constant, debilitating"
    game: "Reduced but present"
    reason: "Must be playable while being meaningful"

  death_rate:
    historical: "High, constant"
    game: "Significant but not overwhelming"
    reason: "Death meaningful, not frustrating"

  religious_requirements:
    historical: "Pervasive, constant"
    game: "Periodic checks, festival requirements"
    reason: "Flavor without tedium"

  salinization_speed:
    historical: "Centuries"
    game: "Visible within player lifetime"
    reason: "Must be solvable challenge, not background"
```

---

## Appendix: Quick Reference

### Daily Needs

| Need | Frequency | Consequence of Neglect |
|------|-----------|----------------------|
| Food | 2-3 meals/day | Hunger debuff → starvation |
| Water | Constant | Thirst → dehydration → death |
| Sleep | 6-8 hours/night | Stamina loss → collapse |
| Shelter | Every night | Health risk, exposure |
| Social | Weekly minimum | Reputation loss, isolation |
| Religious | Daily/weekly | Favor loss, misfortune |

### Disease Risk Factors

| Factor | Disease Risk |
|--------|-------------|
| Canal water | +10% daily |
| Well water | +2% daily |
| Crowded area | +5% daily |
| Summer season | +50% overall |
| Poor nutrition | +30% overall |
| Exhaustion | +20% overall |

### Legal Penalties

| Crime | Typical Penalty |
|-------|-----------------|
| Minor theft | Return + 2x fine |
| Major theft | Return + 10x fine or slavery |
| Assault | Silver fine (based on injury) |
| Murder | Death or blood money |
| Adultery (woman) | Death (often reduced) |
| Impiety | Temple punishment |
| Broken oath | Severe (divine wrath) |

---

*"The sun rises. The gods wait. The fields thirst. This is your life. Make of it what you can."*
