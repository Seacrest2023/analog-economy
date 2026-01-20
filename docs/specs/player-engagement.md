# Player Engagement & Retention

> *"A game that teaches survival must first survive itself. Players must want to return—not because we manipulate them, but because each session brings genuine value. The trick is making that value visible."*

## Overview

This specification defines the complete engagement and retention systems for The Analog Economy. Every mechanic here serves dual purposes: keeping players engaged AND generating valuable training data. We reject dark patterns that exploit psychology without delivering value—instead, we create systems where the player's benefit and the game's benefit are aligned.

---

## Design Philosophy

### The Anti-Exploitation Principle

```yaml
design_principles:
  no_dark_patterns:
    what_we_avoid:
      - "Artificial timers that waste player time"
      - "Pay-to-skip mechanics for core content"
      - "Loot boxes with hidden odds"
      - "FOMO that creates anxiety without value"
      - "Streaks that punish life circumstances"

    what_we_embrace:
      - "Every login delivers genuine progress"
      - "Time away has catch-up mechanics"
      - "All purchases are transparent"
      - "Events are opportunities, not obligations"
      - "Flexibility respects player lives"

  the_value_exchange:
    player_gives: "Time, attention, decision-making (training data)"
    player_receives: "Skills, SILA, community, entertainment, purpose"
    both_win: "Engagement metrics track VALUE delivered, not time extracted"
```

### The 99/1 Economy Model

```yaml
economy_model:
  player_driven: "99% of goods and services from human players"
  game_driven: "1% from NPC/system sources"

  npc_gap_filling:
    trigger: "Market shortage of essential item for > 24 hours"
    response: "NPC merchant offers item at 150% market rate"
    purpose: "Prevent game-breaking shortages"
    limit: "Never undercut player prices"

  revenue_philosophy:
    goal: "Make a little off a lot, not a lot off a few"
    avoid: "Whale-hunting, pay-to-win, artificial scarcity"
    embrace: "Volume-based revenue, genuine value exchange"

  caravan_system:
    player_inventory: "99% player goods for sale"
    npc_inventory: "1% exotic items not craftable locally"
    pricing: "Dynamic based on supply/demand"
    revenue: "Small transaction fee on all trades"
```

---

## Part 1: Clear Milestones (The "I'm Progressing" Markers)

### The Cylinder Seal System

```yaml
cylinder_seal:
  concept:
    historical: "Sumerians wore cylinder seals to sign documents"
    gameplay: "Your seal visually evolves with your achievements"
    purpose: "Instantly visible progress marker worn on character"

  implementation:
    starting_seal:
      material: "Rough fired clay"
      design: "Simple geometric pattern"
      meaning: "Newcomer to Eridu"

    progression_tiers:
      tier_1_clay:
        material: "Fired clay"
        achievements_required: 5
        visual: "Basic symbols"
        unlocks: "Basic document signing"

      tier_2_stone:
        material: "Carved limestone"
        achievements_required: 15
        visual: "Animal motifs"
        unlocks: "Contract witnessing"

      tier_3_semi_precious:
        material: "Carnelian or agate"
        achievements_required: 30
        visual: "Complex scenes"
        unlocks: "Guild membership"

      tier_4_precious:
        material: "Lapis lazuli"
        achievements_required: 50
        visual: "Mythological scenes"
        unlocks: "Temple access"

      tier_5_royal:
        material: "Lapis with gold caps"
        achievements_required: 100
        visual: "Divine imagery"
        unlocks: "Political participation"

  customization:
    design_choices: "Player selects from unlocked motifs"
    color_variations: "Based on profession mastery"
    inscription: "Personal motto or title"

  visibility:
    worn: "Visible on character's belt or neck"
    inspection: "Other players can examine details"
    signing: "Used in all contracts—your seal is your signature"

  training_data:
    captures: "Achievement patterns, player goals"
```

### Milestone Categories

```yaml
milestone_categories:
  survival_milestones:
    first_night: "Survive your first night"
    first_week: "Survive 7 days"
    first_season: "Survive a full season"
    first_year: "Survive a full year"
    flood_survivor: "Survive the annual flood"
    disease_survivor: "Recover from illness"

  economic_milestones:
    first_trade: "Complete your first barter"
    first_100_sila: "Accumulate 100 SILA"
    first_1000_sila: "Accumulate 1000 SILA"
    first_property: "Own land or building"
    first_employee: "Hire an NPC worker"
    first_tappu: "Complete investment partnership"

  craft_milestones:
    first_tool: "Craft your first tool"
    first_pottery: "Fire your first pot"
    first_bronze: "Pour your first bronze"
    first_masterwork: "Create quality 90+ item"
    first_innovation: "Discover new technique"

  social_milestones:
    first_friend: "Reach relationship level 50 with NPC"
    first_guild: "Join a professional guild"
    first_student: "Take on an apprentice"
    first_witness: "Witness a legal contract"
    first_temple_role: "Receive temple position"

  knowledge_milestones:
    first_codex: "Contribute to the Codex"
    first_literacy: "Learn basic cuneiform"
    journeyman: "Reach Tier 3 in any profession"
    master: "Reach Tier 4 in any profession"
    polymath: "Reach Tier 3 in three professions"

  special_milestones:
    anunnaki_fragment: "Find a mysterious metal fragment"
    divine_vision: "Experience a divine dream"
    server_first: "First on server to achieve X"
```

### Progress Tracking UI

```yaml
progress_ui:
  seal_display:
    location: "Character panel, always visible"
    hover: "Shows next upgrade requirements"
    click: "Opens achievement gallery"

  milestone_journal:
    format: "Clay tablet metaphor"
    sections:
      - "Completed (with dates)"
      - "In Progress (with %)"
      - "Locked (requirements shown)"
      - "Hidden (discovered through play)"

  notifications:
    on_complete:
      visual: "Seal glows, stone chips away revealing new layer"
      audio: "Satisfying chime + crowd murmur"
      text: "Achievement unlocked: [NAME]"
      reward: "SILA + karma + unlock"

  sharing:
    social: "Can share achievements to external platforms"
    in_game: "Achievements visible on player inspection"
```

---

## Part 2: Dopamine Loops (The Reward Cadence)

### The 30-Second Loop (Micro-Mastery)

```yaml
micro_loop_30_seconds:
  name: "Eureka Sparks"
  concept: "Tiny rewards for correct execution"

  triggers:
    perfect_craft: "Hit timing window exactly"
    efficient_action: "Complete task under par time"
    skill_application: "Use learned technique correctly"
    discovery: "Notice something new"

  rewards:
    visual: "Golden spark particle effect"
    audio: "Satisfying 'ting' sound"
    haptic: "Controller vibration pulse"
    currency: "+1-5 copper bits (micro-currency)"

  purpose:
    player: "Instant feedback on mastery"
    training: "Marks high-quality action execution"

  examples:
    pottery: "Center clay perfectly on wheel → Spark"
    smithing: "Strike at optimal temperature → Spark"
    farming: "Plant at correct depth → Spark"
    fishing: "Set hook at right moment → Spark"
```

### The 5-Minute Loop (Task Completion)

```yaml
five_minute_loop:
  name: "Task Satisfaction"
  concept: "Complete discrete activities for tangible rewards"

  typical_tasks:
    gather_10_reeds: "~3-5 minutes"
    catch_3_fish: "~5 minutes"
    craft_simple_item: "~5 minutes"
    complete_npc_errand: "~5-7 minutes"

  rewards:
    sila: "5-25 SILA per task"
    karma: "+1-3 for helpful tasks"
    items: "Materials, tools, consumables"
    progress: "Skill XP toward next tier"

  feedback:
    completion_sound: "Satisfying 'task done' audio"
    ui_update: "Progress bar fills/completes"
    npc_reaction: "Thanks or acknowledgment"

  chaining:
    concept: "One task leads naturally to next"
    example: "Gather reeds → Make basket → Fill with fish → Sell at market"
```

### The 45-Minute Loop (Day Cycle)

```yaml
day_cycle_loop:
  name: "The Sumerian Day"
  concept: "Each in-game day is 45 real minutes"

  day_structure:
    dawn: "0:00-0:05 (Sunrise Bonus awarded)"
    morning: "0:05-0:15 (Peak work efficiency)"
    midday: "0:15-0:25 (Heat, slower work)"
    afternoon: "0:25-0:35 (Work resumes)"
    evening: "0:35-0:40 (Social time, markets)"
    night: "0:40-0:45 (Rest or risk)"

  sunrise_bonus:
    trigger: "Player present at dawn"
    rewards:
      health: "+10% max health for the day"
      stamina: "Full restoration"
      luck: "+5% rare find chance"
      sila: "10 SILA 'new day' bonus"

  night_mechanics:
    risks:
      - "Predators more active"
      - "Visibility reduced"
      - "Stamina drain increased outdoors"
    rewards:
      - "Night fishing bonus"
      - "Star observation (astronomy skill)"
      - "Social activities in taverns"

  one_more_day:
    psychology: "Players naturally want to see tomorrow"
    design: "Dawn always feels rewarding"
```

### The 4-Hour Loop (Session Goals)

```yaml
session_loop:
  name: "Session Accomplishment"
  concept: "Meaningful progress in a typical play session"

  session_goals:
    auto_generated: "Based on player's current state"
    examples:
      - "Complete current quest stage"
      - "Reach next skill tier"
      - "Earn 500 SILA"
      - "Build shelter improvement"
      - "Attend upcoming festival"

  progress_bar:
    visibility: "Subtle UI element"
    components: "3-5 goals per session"
    completion_reward: "Bonus SILA + session summary"

  session_summary:
    on_logout:
      display: "What you accomplished today"
      preview: "What's waiting tomorrow"
      tease: "Upcoming events you might miss"
```

### The Daily Loop (24 Hours)

```yaml
daily_loop:
  name: "The Temple Tribute"
  concept: "Gods demand specific offerings daily"

  divine_demands:
    rotation: "Different demand each real-world day"
    announcement: "Temple crier at dawn"

    schedule:
      monday:
        deity: "Enlil (Wind/Authority)"
        demand: "500 units grain contributed"
        buff: "+10% stamina regen"
        theme: "Leadership and work"

      tuesday:
        deity: "Inanna (Love/War)"
        demand: "100 units textiles contributed"
        buff: "+10% social influence"
        theme: "Relationships and conflict"

      wednesday:
        deity: "Enki (Wisdom/Water)"
        demand: "200 units fish contributed"
        buff: "+10% learning speed"
        theme: "Knowledge and innovation"

      thursday:
        deity: "Nanna (Moon)"
        demand: "50 units silver/jewelry contributed"
        buff: "+10% trade prices"
        theme: "Commerce and cycles"

      friday:
        deity: "Utu (Sun/Justice)"
        demand: "Community service hours"
        buff: "+10% karma gain"
        theme: "Justice and truth"

      saturday:
        deity: "Ninhursag (Earth/Fertility)"
        demand: "100 units crops contributed"
        buff: "+10% harvest yields"
        theme: "Growth and nature"

      sunday:
        deity: "An (Heaven)"
        demand: "Temple attendance"
        buff: "+10% all stats"
        theme: "Rest and reflection"

  contribution_mechanics:
    pool: "Server-wide contribution goal"
    individual: "Your contribution tracked"
    reward_tier:
      any_contribution: "Basic buff (24 hours)"
      top_10_percent: "Enhanced buff (24 hours)"
      top_contributor: "Title + SILA bonus"

  missing_contribution:
    penalty: "No buff (not a debuff)"
    catch_up: "Can contribute extra next day"
    no_punishment: "Just missed opportunity"
```

### The Weekly Loop

```yaml
weekly_loop:
  name: "The King's Accounting"
  concept: "Weekly reset of competitive elements"

  weekly_reset:
    day: "Real-world Sunday midnight"

    resets:
      leaderboards: "Fresh competition"
      tribute_totals: "New week's goals"
      special_quests: "Weekly quest refresh"

    does_not_reset:
      progress: "All advancement permanent"
      inventory: "All items kept"
      karma: "Persistent always"

  weekly_rewards:
    participation: "Logged in 3+ days"
    consistency: "Logged in all 7 days"
    contribution: "Met weekly community goals"

  the_sabbath_market:
    timing: "Every Sunday (real-world)"
    event: "Special merchant caravan arrives"
    exclusives: "Rare items only available weekly"
    social: "Peak player gathering time"
```

---

## Part 3: Reputation Visibility (The Visual Flex)

### Material Hierarchy System

```yaml
material_hierarchy:
  concept: "Your clothing and accessories show your status"
  historical: "Sumerian society was highly stratified by dress"

  clothing_tiers:
    tier_0_rags:
      material: "Rough unprocessed fibers"
      color: "Brown/grey"
      meaning: "New arrival, no status"
      requirement: "Starting gear"

    tier_1_basic_linen:
      material: "Plain woven linen"
      color: "Natural beige"
      meaning: "Established worker"
      requirement: "20+ days survived"

    tier_2_bleached_linen:
      material: "Bleached white linen"
      color: "Clean white"
      meaning: "Respectable citizen"
      requirement: "Tier 2 profession + 500 SILA"

    tier_3_dyed_garments:
      material: "Colored wool/linen"
      colors:
        red: "Merchant success"
        yellow: "Agricultural mastery"
        green: "Healing profession"
      meaning: "Profession master"
      requirement: "Tier 3 profession + 2000 SILA"

    tier_4_indigo_blue:
      material: "Rare indigo-dyed wool"
      color: "Deep blue"
      meaning: "Elite status"
      requirement: "Tier 4 profession + 5000 SILA"

    tier_5_royal_regalia:
      material: "Gold thread, lapis accents"
      color: "Blue and gold"
      meaning: "Legendary status"
      requirement: "Major achievement + 10000 SILA"

  jewelry_progression:
    none: "Starting"
    shell_beads: "First milestone"
    copper_jewelry: "Economic milestone"
    silver_jewelry: "Craft milestone"
    gold_jewelry: "Social milestone"
    lapis_and_gold: "Ascension progress"

  visual_recognition:
    at_a_glance: "Players can immediately gauge others"
    no_hiding: "Cannot disguise status (karma penalty)"
    inspection: "Detailed view shows specific achievements"
```

### Title System

```yaml
title_system:
  display: "Shown above player name"

  title_categories:
    profession:
      format: "[Profession] [Name]"
      examples:
        - "Engar Ur-Namma" (Farmer)
        - "Simug Gilgamesh" (Smith)
        - "Dubsar Enlil-bani" (Scribe)

    achievement:
      format: "[Title] [Name]"
      examples:
        - "Flood-Walker Ur-Namma"
        - "Bronze-Bringer Gilgamesh"
        - "Canal-Builder Enlil-bani"

    social:
      format: "[Role] [Name]"
      examples:
        - "Elder Ur-Namma"
        - "Witness Gilgamesh"
        - "Guildmaster Enlil-bani"

    divine:
      format: "[Blessing] [Name]"
      examples:
        - "Enki-Blessed Ur-Namma"
        - "Touched-by-Apkallu Gilgamesh"

  title_switching:
    allowed: "Player can choose displayed title"
    limit: "One title at a time"
    all_earned: "All earned titles visible in profile"
```

---

## Part 4: Seasonal Events (Live Ops)

### The Festival Calendar

```yaml
festival_calendar:
  concept: "Regular events tied to Sumerian calendar"
  purpose: "Reasons to log in at specific times"

  major_festivals:
    akitu_new_year:
      timing: "First week of each month (real-world)"
      duration: "3 days"
      activities:
        - "Grand procession through city"
        - "Temple offerings (bonus karma)"
        - "Feast participation (social buffs)"
        - "New Year markets (rare items)"
        - "Prophecy event (hints about coming content)"
      rewards:
        participation: "Festival Crown cosmetic"
        contribution: "Year's Blessing buff (1 week)"

    harvest_festival:
      timing: "End of each season (in-game)"
      duration: "2 days"
      activities:
        - "Harvest competition"
        - "Craft fair (sell at bonus prices)"
        - "Feasting (food buffs)"
        - "Dance and music (entertainment XP)"
      rewards:
        best_harvest: "Golden Sickle cosmetic"
        participation: "Abundance buff"

    flood_memorial:
      timing: "After annual flood event"
      duration: "1 day"
      activities:
        - "Commemorate the lost"
        - "Rebuild together (community quest)"
        - "Flood stories (lore reveals)"
      rewards:
        survival: "Flood Survivor title"
        helping: "Karma bonus"

  environmental_events:
    river_recedes:
      trigger: "Random, ~once per month"
      duration: "4-8 hours real-time"
      opportunity: "Harvest rare materials from exposed riverbed"
      items: "High-purity clay, river pearls, ancient artifacts"

    dust_storm:
      trigger: "Random, ~once per month"
      duration: "2-4 hours real-time"
      effect: "Outdoor visibility near zero"
      opportunity:
        social: "Tavern storytelling (2x social XP)"
        crafting: "Indoor crafts (1.5x progress)"
        mystery: "Strange visions during storm"

    celestial_event:
      trigger: "Tied to real-world astronomical events"
      types:
        - "Eclipse (mystery quest unlocks)"
        - "Meteor shower (rare materials)"
        - "Planetary alignment (divine blessings)"

  limited_merchants:
    dilmun_trader:
      frequency: "Weekly (randomized day)"
      duration: "6 hours"
      goods: "Exotic items not available locally"
      pricing: "Premium but exclusive"

    wandering_sage:
      frequency: "Monthly"
      duration: "2 hours"
      service: "Reveals hidden knowledge for SILA"
      rarity: "Location announced 1 hour before arrival"
```

### Event Notification System

```yaml
event_notifications:
  in_game:
    herald: "Town crier announces upcoming events"
    temple: "Priests announce religious festivals"
    merchants: "Traders hint at caravan arrivals"

  out_of_game:
    email: "Weekly digest of upcoming events (opt-in)"
    push: "Mobile notification for time-sensitive events (opt-in)"
    social: "Community calendar maintained"

  advance_warning:
    major_events: "7 days notice"
    minor_events: "24 hours notice"
    surprise_events: "Herald announcement only (FOMO lite)"

  miss_protection:
    recurring: "Most events repeat monthly"
    catch_up: "Off-peak hours often have mini-versions"
    no_permanent_loss: "No exclusive items that never return"
```

---

## Part 5: Achievements & Trophies (The Legacy)

### Votive Statue System

```yaml
votive_statues:
  concept:
    historical: "Sumerians placed statues in temples to pray eternally"
    gameplay: "Major achievements earn a statue in the city"

  statue_tiers:
    personal_achievement:
      location: "Small niche in appropriate guild hall"
      size: "Hand-sized figurine"
      visibility: "Guild members see it"
      examples:
        - "First bronze pour"
        - "Journeyman in profession"
        - "100 trades completed"

    community_achievement:
      location: "Public spaces (markets, plazas)"
      size: "Knee-height statue"
      visibility: "All players in area"
      examples:
        - "Top contributor to festival"
        - "Saved X players from flood"
        - "Built public infrastructure"

    server_achievement:
      location: "Central Ziggurat"
      size: "Life-sized statue"
      visibility: "All players who visit temple"
      examples:
        - "Server first innovation"
        - "Founded successful settlement"
        - "Ascended to next era"

    legendary_achievement:
      location: "Permanent monument"
      size: "Larger than life"
      visibility: "Visible from distance"
      examples:
        - "Completed Anunnaki quest"
        - "First to Moksha (liberation)"
        - "Extraordinary service"

  statue_details:
    appearance: "Resembles player character at time of achievement"
    inscription: "Achievement name and date"
    interaction: "Other players can 'pay respects' (+karma)"

  persistence:
    personal: "Until player moves to new era"
    community: "Duration of current 'reign' (monthly)"
    server: "Duration of current era"
    legendary: "Permanent (cross-era)"
```

### Achievement Categories

```yaml
achievement_categories:
  exploration:
    - "Discover all Eridu zones"
    - "Find hidden locations"
    - "Map trade routes"
    - "Explore during night"
    - "Survive in every biome"

  mastery:
    - "Reach Tier 2/3/4 in profession"
    - "Create masterwork item"
    - "Discover innovation"
    - "Teach 10 students"
    - "Complete full supply chain solo"

  social:
    - "Witness 50 contracts"
    - "Mediate 10 disputes"
    - "Host successful feast"
    - "Lead community project"
    - "Maximum reputation with faction"

  economic:
    - "Accumulate wealth milestones"
    - "Complete Tappu partnerships"
    - "Employ X workers"
    - "Dominate market sector"
    - "Build trading empire"

  survival:
    - "Survive disasters"
    - "Recover from zero health"
    - "Live X days consecutively"
    - "Survive without shelter"
    - "Overcome disease"

  hidden:
    - "Find all Anunnaki fragments"
    - "Decode ancient text"
    - "Witness divine event"
    - "Discover Easter eggs"
    - "Secret achievements"
```

---

## Part 6: Leaderboards (Competition)

### The Scribe's Tablet System

```yaml
scribes_tablet:
  concept:
    historical: "Public records kept on stone tablets"
    gameplay: "Physical leaderboard in town square"

  location:
    primary: "Central market plaza"
    secondary: "Guild halls (profession-specific)"
    temple: "Karma and service leaderboards"

  categories:
    the_philanthropist:
      metric: "Most resources contributed to community"
      reset: "Monthly"
      reward: "Philanthropy title, karma bonus"

    the_genius:
      metric: "Most innovations discovered"
      reset: "Era"
      reward: "Innovation title, permanent statue"

    the_survivor:
      metric: "Oldest continuous lineage"
      reset: "Never"
      reward: "Elder title, respect mechanics"

    the_merchant_prince:
      metric: "Highest trade volume"
      reset: "Monthly"
      reward: "Trade title, market stall priority"

    the_master_crafter:
      metric: "Highest quality items produced"
      reset: "Monthly"
      reward: "Master title, commission priority"

    the_witness:
      metric: "Most contracts witnessed accurately"
      reset: "Monthly"
      reward: "Witness title, legal standing"

  visibility:
    public: "Top 10 visible to all"
    personal: "Your rank always visible to you"
    anonymous: "Option to hide from public boards"

  anti_gaming:
    quality_over_quantity: "Many metrics quality-weighted"
    sybil_protection: "Account age requirements"
    karma_filter: "Low-karma excluded from boards"
```

### Competition Events

```yaml
competition_events:
  craft_competitions:
    frequency: "Weekly"
    format: "Best item in category wins"
    judging: "Quality score + community vote"
    prizes: "SILA + materials + title"

  harvest_races:
    frequency: "Seasonal"
    format: "Most yield in time limit"
    categories: "Different crops"
    prizes: "Tools + seeds + title"

  trading_tournaments:
    frequency: "Monthly"
    format: "Highest profit margin"
    rules: "Starting capital provided"
    prizes: "SILA + exclusive goods"

  innovation_challenges:
    frequency: "As needed"
    format: "Solve specific problem"
    judging: "Effectiveness + novelty"
    prizes: "Major SILA + permanent recognition"
```

---

## Part 7: Daily & Weekly Hooks

### Login Incentives

```yaml
login_system:
  daily_gift:
    day_1: "50 SILA"
    day_2: "100 SILA"
    day_3: "Materials bundle"
    day_4: "150 SILA"
    day_5: "Tool or weapon"
    day_6: "200 SILA"
    day_7: "Choice of reward + cosmetic"

  streak_bonus:
    concept: "Consecutive days multiply rewards"
    multiplier: "1.1x per day, max 2x at 10 days"
    protection: "One 'grace day' per week"
    reset: "Gradual reduction, not cliff"

  comeback_bonus:
    trigger: "Player absent 3+ days"
    reward: "Catch-up package with materials"
    purpose: "Reduce 'too far behind' feeling"

  no_punishment:
    principle: "Missing days loses BONUS, not PROGRESS"
    never: "No decay, no resource loss, no debuffs"
```

### Rested Bonus System

```yaml
rested_bonus:
  concept: "Time offline accumulates bonus"

  accumulation:
    rate: "1 hour offline = 5% bonus XP"
    cap: "Maximum 200% bonus (40 hours)"
    location: "Must log out in safe area"

  consumption:
    rate: "Depletes as you earn XP"
    display: "Blue bar overlaying XP bar"

  purpose:
    casual_players: "Catch up to hardcore"
    life_balance: "Reward not playing constantly"
    healthy_gaming: "Discourage 24/7 sessions"
```

### Social Hooks

```yaml
social_hooks:
  play_with_friends:
    bonus: "10% XP when grouped"
    referral: "Bonus for bringing new players"
    mentorship: "Rewards for teaching newcomers"

  guild_activities:
    daily_quest: "Guild-specific daily task"
    weekly_goal: "Collective contribution target"
    guild_perks: "Unlocked by active participation"

  community_events:
    player_hosted: "Tools to create events"
    social_calendar: "Coordinate play times"
    community_goals: "Server-wide objectives"
```

---

## Part 8: The Caravan System

### Regular Caravans

```yaml
caravan_system:
  concept: "Traveling merchants bring opportunities"

  caravan_types:
    local_trader:
      frequency: "Daily"
      inventory: "Common goods, fair prices"
      purpose: "Gap-fill for market shortages"

    regional_merchant:
      frequency: "Every 3 days"
      inventory: "Regional specialties"
      purpose: "Trade route simulation"

    exotic_caravan:
      frequency: "Weekly"
      inventory: "Rare items from distant lands"
      purpose: "Exclusive goods, event feeling"

    mystery_trader:
      frequency: "Random"
      inventory: "Unusual items, hints, quests"
      purpose: "Discovery and surprise"

  player_goods:
    consignment: "Players can give goods to caravan"
    pricing: "Player sets price"
    reach: "Caravan sells in other areas"
    fee: "5% transaction fee to game"

  npc_goods:
    trigger: "Essential item unavailable for 24+ hours"
    pricing: "150% of normal market rate"
    limit: "Cannot undercut player prices"
    signal: "Shows healthy price for producers"
```

### Market Dynamics

```yaml
market_dynamics:
  player_driven:
    percentage: "99% of transactions player-to-player"
    pricing: "Free market, player-set prices"
    specialization: "Encourages regional differences"

  npc_backstop:
    percentage: "1% NPC gap-filling"
    trigger: "Extended shortage of essential"
    pricing: "Always above player average"
    message: "Opportunity for player suppliers"

  transaction_fees:
    market_stall: "2% fee"
    caravan_consignment: "5% fee"
    direct_trade: "0% fee"
    purpose: "Revenue + market incentive"

  price_transparency:
    history: "Recent transaction prices visible"
    average: "Running average displayed"
    trend: "Price direction indicator"
```

---

## Part 9: Retention Analytics

### Engagement Metrics

```yaml
engagement_metrics:
  tracked:
    session_length: "Average play time"
    return_rate: "Day 1, 7, 30 retention"
    engagement_depth: "Activities per session"
    social_connection: "Friends, guild, trades"
    progress_velocity: "Milestones per hour"

  health_indicators:
    green: "Engaged, progressing, social"
    yellow: "Slowing progress, solo play"
    red: "Declining sessions, risk of churn"

  interventions:
    yellow_state:
      - "Easier quests offered"
      - "Social matching suggestions"
      - "Comeback bonuses prepared"

    red_state:
      - "Re-engagement email (opt-in)"
      - "Special returning player rewards"
      - "Survey for feedback"
```

### Anti-Churn Mechanics

```yaml
anti_churn:
  early_game:
    first_hour: "Ensure survival success"
    first_day: "Clear milestone achieved"
    first_week: "Social connection made"

  mid_game:
    plateau_detection: "Identify stuck players"
    hint_system: "Subtle guidance"
    alternative_paths: "Multiple progression routes"

  late_game:
    end_game_content: "Ascension path visible"
    mastery_depth: "Always more to learn"
    social_leadership: "Mentor/elder roles"

  leave_well:
    graceful_exit: "Clean stopping points"
    preservation: "Progress saved indefinitely"
    welcome_back: "Easy return anytime"
```

---

## Implementation Notes

### Database Schema

```yaml
engagement_schema:
  player_engagement:
    player_id: uuid
    cylinder_seal_tier: integer
    achievement_count: integer
    current_streak: integer
    longest_streak: integer
    last_login: datetime
    total_play_time: integer
    rested_bonus: float

  achievement_record:
    achievement_id: uuid
    player_id: uuid
    earned_at: datetime
    category: string
    is_hidden: boolean
    votive_placed: boolean

  leaderboard_entry:
    board_id: string
    player_id: uuid
    score: integer
    rank: integer
    period: string
    updated_at: datetime

  daily_contribution:
    player_id: uuid
    date: date
    deity: string
    amount: integer
    buff_active: boolean
```

---

## Appendix: Best Practices from Successful Games

### What We Adopt

| Source | Mechanic | Our Adaptation |
|--------|----------|----------------|
| **WoW** | Rested XP | Offline time grants bonus |
| **GW2** | Daily achievements | Temple Tribute system |
| **Stardew** | Seasonal events | Festival calendar |
| **Destiny** | Weekly reset | King's Accounting |
| **Animal Crossing** | Real-time events | Real-world calendar tie-ins |
| **Path of Exile** | League resets | Monthly leaderboard resets |
| **EVE Online** | Player economy | 99% player-driven market |

### What We Reject

| Dark Pattern | Why We Reject | Our Alternative |
|--------------|---------------|-----------------|
| Aggressive timers | Creates anxiety | Flexible deadlines |
| Loss aversion | Punishes absence | Bonus for presence |
| Hidden odds | Dishonest | Transparent systems |
| Whale-hunting | Exploitative | Volume-based revenue |
| Fear of missing out | Manipulative | Events recur, nothing lost forever |

---

*"The best games don't trap you—they welcome you back. We're not building a cage; we're building a world worth returning to. Every mechanic should make the player's life richer, not demand it."*
