# Entertainment & Leisure

> *"All work and no play makes a dull Sumerian. The tavern is where deals are made, the lyre is where souls are fed, and the game board is where fortunes turn."*

## Overview

Entertainment in Eridu is not mere distraction—it's economic opportunity, social infrastructure, and sanity restoration. Musicians earn from temple ceremonies and tavern tips. Gamblers risk SILA on the Royal Game of Ur. Taverns serve as information hubs where quests originate and reputations are built. This system creates multiple earning paths while enriching the living world.

---

## Design Philosophy

### Core Principles

1. **Entertainment as Economy**: Performance and gaming are legitimate income sources
2. **Social Infrastructure**: Taverns and gatherings are where connections form
3. **Sanity Restoration**: Leisure activities restore mental health
4. **Skill Expression**: Musical and gaming mastery create prestige
5. **Training Data Value**: Social reasoning, performance improvement, risk assessment

### The Leisure Necessity

```yaml
leisure_mechanics:
  sanity_without_leisure:
    week_1: "Mild irritability"
    week_2: "Fatigue accumulates faster"
    week_3: "Social interactions suffer"
    week_4: "Sanity drain begins (-2/day)"

  leisure_benefits:
    social_events: "+5-15 sanity"
    music_listening: "+3-10 sanity"
    game_playing: "+5-10 sanity (win or lose)"
    tavern_relaxation: "+5-8 sanity"
```

---

## Music System

### Instruments of Eridu

```yaml
instruments:
  lyre:
    description: "Grand stringed instrument with bull's head decoration"
    difficulty: "High"
    prestige: "Maximum"
    cost: "500-2000 SILA (gold/lapis decoration)"
    learning_time: "Months to basic proficiency"
    venues: "Temple ceremonies, royal courts, elite banquets"
    earnings_potential: "100-500 SILA per performance"
    sila_to_learn: 75

  harp:
    description: "Vertical stringed instrument"
    difficulty: "Medium-High"
    prestige: "High"
    cost: "200-800 SILA"
    learning_time: "Weeks to months"
    venues: "Temples, wealthy homes, festivals"
    earnings_potential: "50-200 SILA per performance"
    sila_to_learn: 50

  reed_pipes:
    description: "Simple wind instrument from marsh reeds"
    difficulty: "Low"
    prestige: "Low (shepherd's instrument)"
    cost: "5-20 SILA (or craft free from reeds)"
    learning_time: "Days to weeks"
    venues: "Taverns, streets, casual gatherings"
    earnings_potential: "5-30 SILA tips"
    sila_to_learn: 20

  drums:
    description: "Hand drums and frame drums"
    difficulty: "Medium"
    prestige: "Medium"
    cost: "30-100 SILA"
    learning_time: "Weeks"
    venues: "Ceremonies, festivals, taverns"
    earnings_potential: "20-75 SILA per performance"
    sila_to_learn: 30

  sistrum:
    description: "Rattle used in temple ceremonies"
    difficulty: "Low"
    prestige: "Medium (sacred context)"
    cost: "50-150 SILA"
    learning_time: "Days"
    venues: "Temple only"
    earnings_potential: "Temple rations + karma"
    sila_to_learn: 25

  cymbals:
    description: "Metal percussion"
    difficulty: "Low-Medium"
    prestige: "Medium"
    cost: "40-100 SILA (bronze)"
    learning_time: "Weeks"
    venues: "Temples, festivals"
    earnings_potential: "25-60 SILA per performance"
    sila_to_learn: 25
```

### Musician Skill Tree

```yaml
musician_skill_tree:
  tier_1_novice:
    skills:
      basic_rhythm:
        description: "Keep time with simple beats"
        sila_reward: 15
        unlocks: "Drum accompaniment jobs"

      simple_melodies:
        description: "Play basic tunes on chosen instrument"
        sila_reward: 20
        unlocks: "Street performance"

      instrument_care:
        description: "Maintain and tune your instrument"
        sila_reward: 10
        importance: "Neglected instruments lose quality"

    earnings: "5-20 SILA tips"
    venues: "Streets, small taverns"

  tier_2_apprentice:
    requirements: "Tier 1 + 20 performances"
    skills:
      traditional_songs:
        description: "Learn classic Sumerian repertoire"
        sila_reward: 30
        library: "Work songs, love songs, praise songs"

      harmony_basics:
        description: "Play with other musicians"
        sila_reward: 25
        unlocks: "Ensemble performance"

      audience_reading:
        description: "Adjust performance to crowd mood"
        sila_reward: 30
        benefit: "Better tips, return invitations"

    earnings: "20-50 SILA per performance"
    venues: "Larger taverns, private parties"

  tier_3_journeyman:
    requirements: "Tier 2 + 50 performances + reputation"
    skills:
      temple_hymns:
        description: "Learn sacred music for ceremonies"
        sila_reward: 50
        requirement: "Temple approval"
        karma: "+5 per temple performance"

      epic_recitation:
        description: "Accompany oral storytelling"
        sila_reward: 60
        content: "Gilgamesh, Enki myths, city legends"

      improvisation:
        description: "Create music spontaneously"
        sila_reward: 50
        prestige: "Marks true mastery"

    earnings: "50-150 SILA per performance"
    venues: "Temples, elite homes, major taverns"

  tier_4_master:
    requirements: "Tier 3 + 100 performances + patron"
    skills:
      composition:
        description: "Create original works"
        sila_reward: 100
        legacy: "Songs may outlive you"

      royal_performance:
        description: "Play for city leadership"
        sila_reward: 150
        access: "Elite social circles"

      teaching:
        description: "Train apprentice musicians"
        sila_reward: 75
        income: "Ongoing student fees"

    earnings: "100-500 SILA per performance"
    venues: "Royal court, major temples, festivals"
```

### Performance Venues

```yaml
performance_venues:
  temple_ceremonies:
    access: "By invitation/audition"
    frequency: "Daily meals, festivals"
    payment: "Temple rations + 50-200 SILA"
    karma: "+5-15 per performance"
    sanity_gain: "+15"
    reputation: "Sacred honor"

  taverns:
    access: "Open (negotiate with owner)"
    frequency: "Nightly"
    payment: "Tips from patrons (variable)"
    karma: "+2"
    sanity_gain: "+10"
    networking: "Quest hooks, business contacts"

  private_banquets:
    access: "Hired by wealthy families"
    frequency: "Occasional"
    payment: "50-200 SILA flat fee"
    karma: "+3"
    sanity_gain: "+12"
    reputation: "Social climbing opportunity"

  street_corners:
    access: "Open"
    frequency: "Anytime"
    payment: "Coins tossed by passersby (5-30 SILA)"
    karma: "0"
    sanity_gain: "+5"
    risk: "Weather, competition, guards if blocking traffic"

  festivals:
    access: "Merit-based selection"
    frequency: "Seasonal"
    payment: "100-300 SILA + feast participation"
    karma: "+10"
    sanity_gain: "+20"
    reputation: "City-wide recognition"

  funerals:
    access: "Gala priest specialty or hired"
    frequency: "As needed"
    payment: "50-150 SILA"
    karma: "+8"
    sanity_cost: "-5 (emotionally draining)"
    specialty: "Lamentation songs"
```

### Performance Mechanics

```yaml
performance_factors:
  skill_level:
    weight: 40%
    description: "Technical mastery of instrument"

  song_selection:
    weight: 20%
    description: "Appropriate choice for venue/audience"

  audience_mood:
    weight: 15%
    description: "Reading and responding to crowd"

  instrument_condition:
    weight: 10%
    description: "Well-maintained instruments sound better"

  reputation:
    weight: 15%
    description: "Known performers draw better crowds"

performance_outcomes:
  exceptional:
    trigger: "95%+ score"
    result: "Double tips, return invitation, reputation boost"

  good:
    trigger: "70-94% score"
    result: "Standard payment, satisfied audience"

  adequate:
    trigger: "50-69% score"
    result: "Reduced tips, polite response"

  poor:
    trigger: "Below 50%"
    result: "Minimal payment, reputation damage, possible ejection"
```

---

## Games & Gambling

### The Royal Game of Ur

```yaml
royal_game_of_ur:
  description: "Two-player race game, ancestor of backgammon"

  equipment:
    board: "20 squares in distinctive pattern"
    pieces: "7 per player (black and white)"
    dice: "4 tetrahedral (pyramid) dice"
    cost: "30-200 SILA depending on materials"

  rules:
    objective: "Move all 7 pieces off the board before opponent"
    movement: "Roll dice, move pieces"
    captures: "Land on opponent's piece to send it back"
    safe_squares: "Rosette squares protect from capture"

  skill_elements:
    probability: "Understanding dice odds"
    positioning: "Strategic piece placement"
    risk_assessment: "When to play safe vs aggressive"

  learning_curve:
    novice: "Know the rules"
    apprentice: "Basic strategy"
    journeyman: "Advanced tactics"
    master: "Tournament-level play"
    grandmaster: "City champion"

  sila_rewards:
    learn_rules: 10
    win_first_game: 15
    win_10_games: 25
    tournament_win: 50
```

### Gaming Stakes

```yaml
gambling_levels:
  friendly:
    stakes: "Reputation only"
    risk: "None"
    benefit: "Sanity +5, social connection"

  casual_wager:
    stakes: "5-20 SILA"
    risk: "Minor loss"
    benefit: "Sanity +8, excitement"

  serious_gambling:
    stakes: "50-200 SILA"
    risk: "Significant loss"
    benefit: "Sanity +10, major wins possible"
    karma: "-1 if gambling excessively"

  high_stakes:
    stakes: "500+ SILA or property"
    risk: "Life-changing loss"
    benefit: "Massive potential gain"
    karma: "-3 per session"
    requirement: "Both parties consent, witnesses"

gambling_addiction:
  trigger: "10+ serious gambling sessions in 30 days"
  effect: "Compulsion mechanic - must succeed willpower check to resist"
  recovery: "Temple intervention, abstinence period"
  karma_cost: "-20 if addiction develops"
```

### Other Games

```yaml
other_games:
  dice_games:
    description: "Simple chance games with carved dice"
    location: "Taverns, street corners"
    stakes: "1-50 SILA typically"
    skill: "Minimal - pure chance"
    social: "Casual entertainment"

  knucklebones:
    description: "Tossing animal bones for points"
    location: "Anywhere informal"
    stakes: "Small wagers"
    skill: "Some dexterity"
    popularity: "Common among workers"

  riddle_contests:
    description: "Intellectual competition"
    location: "Taverns, educated gatherings"
    stakes: "Reputation, small wagers"
    skill: "Intelligence, knowledge"
    prestige: "High among scholars"

  wrestling:
    description: "Physical competition"
    location: "Public spaces, festivals"
    stakes: "Glory, wagers by spectators"
    skill: "Strength, technique"
    risk: "Injury possible"
```

### Tournament System

```yaml
tournaments:
  royal_game_championship:
    frequency: "Monthly at major taverns"
    entry_fee: "20 SILA"
    prize_pool: "All entry fees to winner"
    format: "Elimination brackets"
    prestige: "City-wide recognition"

  festival_competitions:
    frequency: "During major festivals"
    entry: "Open to all"
    prizes: "Temple-sponsored rewards"
    visibility: "Maximum - crowds watch"

  private_tournaments:
    frequency: "Hosted by wealthy patrons"
    entry: "Invitation only"
    prizes: "Valuable goods, positions"
    networking: "Elite social access"
```

---

## Tavern Culture

### The Tavern as Social Hub

```yaml
tavern_functions:
  drinking_establishment:
    primary_product: "Beer (several grades)"
    secondary: "Wine, date wine"
    food: "Simple fare available"

  information_exchange:
    gossip: "Hear news from across the city"
    rumors: "Quest hooks and opportunities"
    prices: "Market information"
    politics: "Who's up, who's down"

  business_venue:
    deals: "Contracts negotiated"
    hiring: "Find workers or employers"
    partnerships: "Meet potential collaborators"

  entertainment_center:
    music: "Live performances"
    games: "Gambling and friendly matches"
    storytelling: "Epic recitations"

  sanctuary:
    neutral_ground: "Disputes paused inside"
    rest: "Sanity restoration"
    escape: "From daily pressures"
```

### Tavern Keeper (Kar-kid)

```yaml
kar_kid:
  description: "Female tavern keeper - respected profession"

  services:
    drinks:
      common_beer: "2 SILA"
      quality_beer: "5 SILA"
      ceremonial_beer: "10 SILA"
      wine: "15-30 SILA"

    food:
      bread_and_dates: "3 SILA"
      fish_stew: "8 SILA"
      roasted_meat: "15 SILA"

    information:
      casual_gossip: "Buy drinks"
      specific_intel: "5-20 SILA tip"
      introductions: "Relationship + favor"

  reputation_system:
    regular_customer: "Better service, credit possible"
    known_troublemaker: "Refused entry"
    good_tipper: "Priority seating, information access"
```

### Tavern Activities

```yaml
tavern_activities:
  drinking:
    effect: "Social lubrication, sanity restoration"
    cost: "2-30 SILA depending on drink"
    sanity: "+5 (moderate), -10 (excessive)"
    risk: "Drunkenness impairs judgment"

  socializing:
    effect: "Build relationships, gather information"
    cost: "Drinks for others (5-50 SILA)"
    benefit: "Network expansion, quest hooks"
    sanity: "+8"

  gambling:
    effect: "Risk/reward entertainment"
    cost: "Variable stakes"
    benefit: "Potential winnings, excitement"
    sanity: "+5-10"
    risk: "Losses, addiction"

  listening_to_music:
    effect: "Passive entertainment"
    cost: "Tip the musician (optional)"
    sanity: "+3-10 depending on quality"

  watching_games:
    effect: "Spectator entertainment"
    cost: "None (may bet on outcomes)"
    sanity: "+3"

  business_meetings:
    effect: "Neutral ground for negotiations"
    cost: "Buy drinks for all parties"
    benefit: "Deals made, contracts formed"
    etiquette: "Host pays for drinks"
```

### Famous Taverns of Eridu

```yaml
notable_taverns:
  the_silver_fish:
    location: "Harbor district"
    clientele: "Sailors, fishermen, traders"
    specialty: "Fresh catch, foreign news"
    atmosphere: "Rowdy, cosmopolitan"
    quest_hooks: "Trade opportunities, travel, smuggling"

  enkis_cup:
    location: "Near temple district"
    clientele: "Temple workers, craftsmen"
    specialty: "Quality beer, respectable"
    atmosphere: "Moderate, religious"
    quest_hooks: "Temple-related, community service"

  the_dusty_road:
    location: "Caravan stop area"
    clientele: "Travelers, merchants"
    specialty: "Foreign goods, exotic drinks"
    atmosphere: "Transient, exciting"
    quest_hooks: "Long-distance trade, exploration"

  the_reed_mat:
    location: "Commoner quarter"
    clientele: "Workers, farmers"
    specialty: "Cheap beer, honest company"
    atmosphere: "Simple, friendly"
    quest_hooks: "Local problems, labor opportunities"
```

---

## Storytelling & Oral Tradition

### Epic Recitation

```yaml
epic_tradition:
  major_works:
    gilgamesh:
      description: "Tale of heroism, friendship, mortality"
      length: "Hours for full recitation"
      popularity: "Universal appeal"

    enki_and_ninhursag:
      description: "Creation myth featuring Eridu's patron"
      length: "1-2 hours"
      local_relevance: "Highest in Eridu"

    descent_of_inanna:
      description: "Journey to the underworld"
      length: "1-2 hours"
      themes: "Death, rebirth, sacrifice"

    lugalbanda:
      description: "Royal hero tales"
      length: "Variable by episode"
      audience: "Appeals to ambitious youth"

  performer_requirements:
    memory: "Entire epics memorized"
    voice: "Dramatic delivery"
    music: "Often accompanied by lyre"
    stamina: "Hours of performance"

  earnings:
    tavern_recitation: "30-100 SILA + tips"
    private_performance: "100-300 SILA"
    festival_feature: "200-500 SILA"
    temple_ceremony: "Rations + karma"
```

### Storyteller Path

```yaml
storyteller_profession:
  entry: "Learn one major epic"
  progression:
    novice: "Can recite basic stories"
    apprentice: "One major epic memorized"
    journeyman: "Multiple epics, regional tales"
    master: "Complete repertoire, original compositions"

  skills:
    memorization:
      description: "Retain vast amounts of text"
      sila_reward: 50

    dramatic_delivery:
      description: "Voice modulation, pacing, emotion"
      sila_reward: 40

    audience_engagement:
      description: "Read crowd, adjust performance"
      sila_reward: 35

    musical_accompaniment:
      description: "Self-accompany on instrument"
      sila_reward: 45

  cultural_importance:
    - "Preserves history and values"
    - "Entertains and educates"
    - "Connects community to past"
    - "Training data: oral knowledge transmission"
```

---

## Hunting & Fishing as Leisure

### Sport Hunting

```yaml
sport_hunting:
  note: "Distinguished from subsistence hunting"

  prestigious_quarry:
    lion:
      rarity: "Rare, dangerous"
      prestige: "Maximum - royal sport"
      skill: "Expert required"
      reward: "Legendary reputation"

    wild_cattle:
      rarity: "Uncommon"
      prestige: "High"
      skill: "Advanced"
      reward: "Major reputation, meat"

    gazelle:
      rarity: "Common"
      prestige: "Moderate"
      skill: "Intermediate"
      reward: "Respectable, practical"

    waterfowl:
      rarity: "Abundant"
      prestige: "Low"
      skill: "Basic"
      reward: "Food, light entertainment"

  hunting_parties:
    organization: "Led by land owner or noble"
    participation: "Invitation = social honor"
    supplies: "Host provides"
    sharing: "Quarry divided by contribution"

  training_data_value:
    - "Tracking and prediction"
    - "Risk assessment"
    - "Team coordination"
    - "Resource management"
```

### Sport Fishing

```yaml
sport_fishing:
  distinction: "Leisure vs. commercial fishing"

  locations:
    canals: "Easy access, moderate catch"
    river: "Better fish, some travel"
    marshes: "Best variety, expedition required"

  methods:
    line_fishing: "Relaxing, individual"
    net_fishing: "Active, social"
    spear_fishing: "Skill-based, exciting"

  benefits:
    sanity: "+10 for peaceful fishing"
    food: "Catch provides meals"
    social: "Fishing companions bond"

  competitions:
    biggest_catch: "Weight-based prizes"
    most_caught: "Quantity contests"
    rarest_species: "Specialty recognition"
```

---

## Social Gatherings

### Feasting

```yaml
feasting:
  types:
    family_feast:
      occasion: "Births, marriages, accomplishments"
      scale: "10-30 people"
      cost: "50-200 SILA"
      host_benefit: "Reputation, family bonds"

    business_banquet:
      occasion: "Deal celebration, partnership"
      scale: "5-15 people"
      cost: "100-500 SILA"
      purpose: "Relationship building"

    victory_celebration:
      occasion: "Military success, major achievement"
      scale: "Dozens to hundreds"
      cost: "500-5000 SILA"
      sponsor: "Leader or wealthy patron"

    temple_feast:
      occasion: "Festivals, god's honor"
      scale: "Entire community"
      cost: "Temple-sponsored"
      benefit: "Karma, community connection"

  elements:
    food: "Roasted meat, bread, dates, vegetables"
    drink: "Beer and wine in abundance"
    music: "Live performers"
    storytelling: "Entertainment and education"
    gifts: "Host provides small tokens"
```

### Sanity Through Community

```yaml
community_sanity:
  principle: "Humans need social connection"

  activities_and_benefits:
    casual_conversation:
      time: "15+ minutes"
      sanity: "+3"

    shared_meal:
      time: "30+ minutes"
      sanity: "+5"

    group_entertainment:
      time: "1+ hours"
      sanity: "+10"

    festival_participation:
      time: "Full day"
      sanity: "+15-25"

    intimate_gathering:
      time: "Evening"
      sanity: "+12"

  isolation_penalty:
    3_days_alone: "Loneliness debuff"
    7_days_alone: "Sanity drain begins"
    14_days_alone: "Severe sanity impact"
```

---

## Implementation Notes

### Database Schema

```yaml
entertainment_records:
  musician_profile:
    player_id: uuid
    instruments: array
    skill_levels: object
    songs_known: array
    performances: integer
    reputation: integer
    regular_venues: array

  gambling_record:
    player_id: uuid
    games_played: integer
    total_wagered: integer
    total_won: integer
    addiction_score: integer
    tournament_wins: array

  social_activity:
    player_id: uuid
    tavern_visits: array
    feasts_attended: integer
    feasts_hosted: integer
    social_network: graph
```

### Training Data Capture

```yaml
training_data_points:
  performance_decisions:
    - "Song selection rationale"
    - "Audience adaptation"
    - "Venue negotiation"

  gambling_reasoning:
    - "Risk assessment in games"
    - "When to bet, fold, bluff"
    - "Stakes decisions"

  social_navigation:
    - "Relationship building strategies"
    - "Information gathering techniques"
    - "Conflict avoidance in taverns"
```

---

## Appendix: Sumerian Entertainment Terms

| Term | Meaning | Gameplay Role |
|------|---------|---------------|
| **Nar** | Musician | Performance profession |
| **Kar-kid** | Tavern keeper (female) | Tavern owner NPC |
| **Gala** | Lamentation singer | Funeral performer |
| **Kaš** | Beer | Primary tavern drink |
| **Gestin** | Wine | Premium drink |
| **Šu-zi-ga** | "Royal Game" | Main board game |

---

*"The wise worker knows when to set down the tool. The lyre rests the hands. The game sharpens the mind. The tavern feeds the soul. Work without play is a drought upon the spirit."*
