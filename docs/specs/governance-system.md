# Governance System Specification

> "The assembly is the voice of the people. The king is but the servant of Enki."

## Table of Contents

1. [Governance Philosophy](#1-governance-philosophy)
2. [The Two-House Assembly](#2-the-two-house-assembly)
3. [Voting System](#3-voting-system)
4. [Temple Administration](#4-temple-administration)
5. [Government Services](#5-government-services)
6. [Performance Metrics](#6-performance-metrics)
7. [Player Participation](#7-player-participation)
8. [Evolution & Autocracy](#8-evolution--autocracy)

---

## 1. Governance Philosophy

### 1.1 Historical Basis

```yaml
governance_history:
  context: "Before autocratic kings, Sumerian cities had assemblies"

  eridu_period: "~4500-4000 BCE"
  governance_type: "Theocratic democracy"
  authority_source: "Will of Enki through assembly consensus"

  key_principle:
    statement: "Power derives from the people, not the ruler"
    implementation: "Assembly decides major issues"
    exception: "Emergency powers during war"
```

### 1.2 Gameplay Integration

```yaml
governance_gameplay:
  why_it_matters:
    - "Players elect leaders who affect city policies"
    - "Taxes, trade rules, war decisions involve community"
    - "Passive income from temple positions"
    - "Political careers possible for players"

  player_agency:
    vote: "All adult free males can vote"
    run_for_office: "Build reputation to become candidate"
    propose: "Bring issues before assembly"
    serve: "Work in temple administration"

  training_data_value:
    captures:
      - "How humans form consensus"
      - "Political negotiation strategies"
      - "Community decision-making"
      - "Balance of power dynamics"
```

---

## 2. The Two-House Assembly

> Long before autocratic kings, Eridu was managed by a two-house assembly.

### 2.1 Upper House: Council of Elders (Abba)

```yaml
council_of_elders:
  sumerian_name: "Abba"
  description: "City-fathers, heads of prominent families"

  composition:
    member_count: 20
    qualifications:
      age: "50+ years old"
      status: "Free citizen, property owner"
      reputation: "High standing in community"
      lineage: "Head of established family"

  selection:
    method: "Hereditary + merit"
    term: "Life appointment"
    removal: "Death, scandal, or assembly vote"

  powers:
    - "Advise on all major decisions"
    - "Propose legislation"
    - "First review of war declarations"
    - "Interpret religious law"
    - "Manage temple affairs"

  tendencies:
    political_stance: "Conservative, cautious"
    typical_positions:
      - "Advocate for peace"
      - "Preserve tradition"
      - "Protect family interests"
      - "Favor established merchants"

  player_path:
    requirements:
      - "Own significant property (5+ plots)"
      - "Reputation 500+"
      - "Age 50+ (in-game years)"
      - "No major crimes"
    benefits:
      - "Vote in Elder Council"
      - "Propose legislation"
      - "Temple dividend (passive income)"
      - "Status and influence"
```

### 2.2 Lower House: General Assembly (Gurus)

```yaml
general_assembly:
  sumerian_name: "Gurus"
  description: "Adult free males—'men of the city'"

  composition:
    members: "All adult free male citizens"
    estimated_size: "500-2000 depending on population"
    quorum: "10% of eligible voters"

  qualifications:
    age: "15+ years old (adult)"
    status: "Free citizen (not slave)"
    gender: "Male (historical accuracy)"
    residence: "Eridu citizen"

  powers:
    - "Ultimate sovereignty in crises"
    - "Can override Elder Council"
    - "Grant temporary kingship"
    - "Declare war"
    - "Major tax decisions"
    - "Public trials"

  tendencies:
    political_stance: "More aggressive, action-oriented"
    typical_positions:
      - "Favor war when threatened"
      - "Demand action on problems"
      - "Support change and innovation"
      - "Champion common citizens"

  player_path:
    requirements:
      - "Adult male character"
      - "Free citizen status"
      - "Eridu resident"
    benefits:
      - "Vote on major issues"
      - "Attend assembly meetings"
      - "Participate in trials"
      - "Voice in city direction"
```

### 2.3 The Lugal (War-Leader/King)

```yaml
lugal:
  title: "Lugal (Big Man)"
  description: "Temporary leader during emergencies"

  historical_evolution:
    early_period: "Elected only for crises"
    middle_period: "Increasingly permanent"
    late_period: "Hereditary kingship"

  selection:
    nominated_by: "Council of Elders"
    approved_by: "General Assembly"
    method: "Acclaim (see voting system)"
    term: "Duration of crisis (originally)"

  powers_during_crisis:
    - "Command military forces"
    - "Requisition resources"
    - "Issue emergency decrees"
    - "Negotiate with enemies"
    - "Punish deserters"

  limitations:
    - "Cannot overrule assembly on major peace terms"
    - "Cannot declare new wars alone"
    - "Cannot change religious law"
    - "Must account for resources used"

  player_path:
    requirements:
      - "Military reputation 200+"
      - "General reputation 400+"
      - "Won at least 1 significant battle"
      - "Elder nomination"
      - "Assembly approval"
    benefits:
      - "Command city military"
      - "Major passive income during term"
      - "Historical legacy"
      - "NFT: Leadership Badge"
```

---

## 3. Voting System

> They did not use paper ballots, but had formalized "voting" processes.

### 3.1 The Unanimity Principle

```yaml
consensus_voting:
  philosophy:
    goal: "Total consensus, not majority rule"
    reason: "Community must be unified for action"
    process: "Debate until opposition withdraws"

  how_it_works:
    1_proposal: "Issue raised by speaker"
    2_debate: "Open discussion, all may speak"
    3_deliberation: "Private conversations, lobbying"
    4_call_for_vote: "Leader asks 'Does anyone oppose?'"
    5_resolution:
      unanimous: "No opposition = passed"
      opposition: "More debate or issue tabled"

  handling_opposition:
    persuasion: "Convince opponents"
    compromise: "Modify proposal"
    pressure: "Social pressure to conform"
    deferral: "Table issue for later"
    override: "Lower House can override Elders (rare)"
```

### 3.2 The Weapons Clash (Vote Expression)

```yaml
weapons_clash_voting:
  description: "Votes expressed by shouting or banging weapons"

  method:
    for_approval:
      action: "Bang spears on shields, shout approval"
      volume: "Intensity indicates strength of support"

    for_opposition:
      action: "Silence, or shout disapproval"
      volume: "Intensity indicates strength of opposition"

  determining_outcome:
    leader_judgment: "Presiding elder senses 'will of the people'"
    clear_majority: "Obvious from sound"
    unclear: "Call for formal count or more debate"

  gameplay_implementation:
    ui_element: "Vote slider: Strong Oppose ↔ Strong Support"
    aggregation: "AI calculates consensus level"
    visualization: "Sound/visual effect showing community response"
    threshold: "80%+ support = passes, <60% = fails, 60-80% = more debate"
```

### 3.3 Assembly Procedures

```yaml
assembly_procedures:
  calling_assembly:
    who_can_call:
      - "Council of Elders (routine)"
      - "Lugal (emergency)"
      - "Petition of 50+ citizens (special)"

    notice:
      routine: "7 days advance notice"
      urgent: "1 day notice"
      emergency: "Immediate (war, disaster)"

    location: "Open area before ziggurat"

  meeting_structure:
    opening:
      - "Priest invokes Enki's blessing"
      - "Review of agenda"

    debate:
      - "Elder presents issue"
      - "Open floor for speakers"
      - "Time limit per speaker"
      - "Rebuttal allowed"

    voting:
      - "Call for consensus"
      - "Weapons clash if needed"
      - "Result announced"

    closing:
      - "Priest records decision"
      - "Implementation assigned"

  player_participation:
    attending: "Open to all eligible citizens"
    speaking: "Must request permission, reputation affects priority"
    voting: "All present can vote"
    absent: "Can submit proxy vote through family member"
```

### 3.4 Veto and Override

```yaml
veto_system:
  elder_veto:
    description: "Elders can block Assembly proposals"
    method: "Majority of Elders refuse to implement"
    override: "Assembly can override with supermajority (90%+)"

  historical_example:
    event: "Gilgamesh and Agga"
    situation: "King sought war, Elders refused"
    resolution: "Gilgamesh appealed to Lower House, which approved war"
    lesson: "Lower House can override Elder caution"

  gameplay_implementation:
    elder_block: "Triggers override vote in Assembly"
    override_threshold: "90% Assembly support"
    cooldown: "Same issue cannot be raised for 30 days if failed"
```

---

## 4. Temple Administration

> The temple is the heart of city governance and economy.

### 4.1 Temple Structure

```yaml
temple_hierarchy:
  high_priest:
    title: "En" (High Priest/Priestess of Enki)
    selection: "Divine signs, Elder approval"
    term: "Life"
    powers:
      - "Interpret Enki's will"
      - "Manage temple economy"
      - "Lead major rituals"
      - "Veto irreligious laws"

  senior_priests:
    count: 7
    roles:
      - "Daily rituals"
      - "Specific domains (grain, wool, justice, etc.)"
      - "Teach scribes"
    selection: "Trained from youth, merit-based"

  junior_priests:
    count: ~20
    roles:
      - "Assist rituals"
      - "Record keeping"
      - "Distribute rations"

  temple_workers:
    categories:
      - "Scribes (accounting)"
      - "Craftsmen (temple goods)"
      - "Farmers (temple lands)"
      - "Servants (maintenance)"
```

### 4.2 Temple Economy

```yaml
temple_economy:
  functions:
    warehouse: "Stores city's grain surplus"
    bank: "Lends grain and silver"
    employer: "Largest employer in city"
    redistributor: "Provides rations to workers"

  income_sources:
    tithes: "10% of harvest from all citizens"
    temple_lands: "Farms owned by temple"
    offerings: "Voluntary donations"
    fees: "Ritual services, legal documents"
    trade: "Temple merchants"

  expenditures:
    rations: "Feed temple workers"
    rituals: "Supplies for ceremonies"
    maintenance: "Building upkeep"
    charity: "Support for poor, orphans, widows"
    public_works: "Irrigation, walls (funded by temple)"

  player_interaction:
    can_work_for_temple: true
    can_donate: true
    can_borrow: "Grain loans with interest"
    can_store: "Deposit goods (small fee)"
```

### 4.3 Temple Positions (Player Careers)

```yaml
temple_careers:
  scribe:
    requirements:
      - "Literacy skill 50+"
      - "Good reputation"
    duties:
      - "Record transactions"
      - "Copy tablets"
      - "Administrative work"
    income: "5 SILA/day + rations"
    benefits: "Access to knowledge, status"

  temple_merchant:
    requirements:
      - "Trading skill 40+"
      - "Capital (100+ SILA)"
      - "Temple approval"
    duties:
      - "Conduct temple trade expeditions"
      - "Sell temple surplus"
    income: "Commission on trades (5-10%)"
    benefits: "Access to imports, protection"

  ritual_assistant:
    requirements:
      - "Religious knowledge 30+"
      - "Clean reputation"
    duties:
      - "Assist in ceremonies"
      - "Prepare offerings"
    income: "3 SILA/day + rations + blessings"
    benefits: "Divine favor buffs"

  temple_guard:
    requirements:
      - "Combat skill 30+"
      - "Loyalty proven"
    duties:
      - "Protect temple"
      - "Guard treasury"
      - "Escort shipments"
    income: "4 SILA/day + equipment + rations"
    benefits: "Status, equipment access"
```

---

## 5. Government Services

> The government provides essential services that individual citizens cannot.

### 5.1 Infrastructure & Public Works

```yaml
infrastructure_services:
  irrigation_maintenance:
    description: "Most vital service—controlling water"
    activities:
      - "Dig new canals"
      - "Dredge existing canals"
      - "Maintain levees"
      - "Coordinate water distribution"

    labor_system:
      corvee: "All citizens owe labor days"
      managed_by: "Temple administration"
      compensation: "Rations during work"

    failure_consequences:
      - "Flooding destroys crops"
      - "Drought kills harvest"
      - "Salinization (long-term)"

    player_involvement:
      can_work: "Fulfill corvee obligation"
      can_supervise: "With engineering skill"
      can_innovate: "Propose improvements"

  defense_security:
    city_walls:
      construction: "Massive mud-brick walls"
      maintenance: "Constant repair needed"
      gates: "Controlled access points"

    city_watch:
      function: "Internal security"
      patrols: "Night watch, market oversight"
      players_can_join: true

  roads:
    processional_ways:
      description: "Paved roads to ziggurat"
      material: "Bitumen and kiln-fired bricks"
    market_streets:
      description: "Maintained for commerce"
      cleaning: "Regular debris removal"
```

### 5.2 Social Welfare

```yaml
social_welfare:
  food_redistribution:
    rations_system:
      description: "Temple provides food to workers"
      recipients:
        - "Temple employees"
        - "Corvee workers"
        - "Poor and destitute"
      contents:
        - "Barley (basic)"
        - "Oil"
        - "Wool (for clothing)"
        - "Beer"

    disaster_relief:
      trigger: "Drought, flood, invasion"
      response: "Temple opens granaries"
      limitation: "Finite reserves"

  employment:
    temple_as_employer:
      note: "Single largest employer"
      jobs:
        - "Farmers on temple land"
        - "Weavers in temple workshops"
        - "Scribes and administrators"
        - "Construction laborers"

    wage_rates:
      unskilled: "2-3 SILA/day"
      skilled: "4-6 SILA/day"
      specialized: "8-15 SILA/day"
```

### 5.3 Religious & Judicial Services

```yaml
religious_services:
  daily_rituals:
    description: "Priests maintain cosmic order"
    function: "Keep gods happy, protect city"
    public_access: "Can observe major rituals"

  festivals:
    types:
      - "New Year (Akitu)"
      - "Harvest festivals"
      - "Moon festivals"
      - "God-specific celebrations"
    purpose:
      - "Community bonding"
      - "Entertainment"
      - "Divine favor"
    player_participation: "Attend, contribute, perform"

  healthcare:
    asu_physician:
      description: "Medical doctor using herbs and surgery"
      services: "Wounds, illness, childbirth"
      payment: "Based on severity"

    asipu_exorcist:
      description: "Spiritual healer"
      services: "Demonic illness, curses, mental health"
      payment: "Offerings and fees"

    temple_healing:
      description: "Prayer and ritual healing"
      payment: "Offerings to Enki"

judicial_services:
  legal_system:
    courts:
      temple_court: "Religious matters, contracts"
      assembly_court: "Major crimes, disputes"
      elder_arbitration: "Family and property"

    citizen_juries:
      description: "Assembly serves as jury"
      process:
        1: "Charges presented"
        2: "Prosecution arguments"
        3: "Defense arguments"
        4: "Assembly votes"
      example: "1850 BCE murder trial—assembly spared a wife"

  contract_services:
    scribe_services: "Write legal contracts"
    witness_registration: "Official witnesses"
    seal_verification: "Authenticate documents"
```

### 5.4 Commerce & Trade Facilitation

```yaml
commerce_services:
  standardization:
    weights_measures:
      description: "Official standards for fair trade"
      managed_by: "Temple"
      enforcement: "Cheating = punishment"

    quality_standards:
      description: "Minimum quality for certain goods"
      examples: "Beer strength, textile quality"

  trade_expeditions:
    temple_funded:
      description: "Official trade missions"
      destinations: "Dilmun, Magan, Meluhha"
      goods: "Copper, timber, luxury goods"
      risk_sharing: "Temple bears loss"

    merchant_licensing:
      description: "Authorized traders"
      benefits: "Protection, access"
      obligations: "Temple share of profits"
```

---

## 6. Performance Metrics

> Government performance should be measured and affect player satisfaction.

### 6.1 Infrastructure Score

```yaml
infrastructure_metrics:
  irrigation_health:
    measures:
      - "Canal water flow rate"
      - "Levee condition"
      - "Flood incidents"
      - "Drought response time"

    scoring:
      excellent: "90-100 (no flooding, adequate water)"
      good: "70-89"
      fair: "50-69"
      poor: "30-49"
      failing: "0-29 (frequent disasters)"

    consequences:
      high_score:
        - "+20% crop yields"
        - "Lower disease rates"
        - "Population growth"
      low_score:
        - "Crop failures"
        - "Famine risk"
        - "Population decline"
        - "Unrest"

  defense_score:
    measures:
      - "Wall condition"
      - "Guard strength"
      - "Response time to threats"

    consequences:
      high_score: "Deters attacks, citizens feel safe"
      low_score: "Vulnerable to raids, unrest"

  roads_score:
    measures:
      - "Road condition"
      - "Travel time within city"
      - "Market accessibility"

    consequences:
      high_score: "+10% trade efficiency"
      low_score: "Slower commerce, accidents"
```

### 6.2 Social Welfare Score

```yaml
welfare_metrics:
  food_security:
    measures:
      - "Grain reserves (months of supply)"
      - "Ration availability"
      - "Malnutrition rates"

    scoring:
      excellent: "12+ months reserves, all fed"
      good: "6-12 months"
      fair: "3-6 months"
      poor: "1-3 months"
      crisis: "<1 month (famine imminent)"

    consequences:
      high_score: "Population growth, loyalty"
      low_score: "Starvation, riots, exodus"

  employment_rate:
    measures:
      - "% of working-age adults employed"
      - "Wage levels vs. cost of living"

    consequences:
      high_employment: "Prosperity, tax revenue"
      low_employment: "Crime, unrest"

  healthcare_access:
    measures:
      - "Healer availability"
      - "Disease outbreak frequency"
      - "Mortality rates"

    consequences:
      good_healthcare: "Longer lifespan, productivity"
      poor_healthcare: "Epidemics, population loss"
```

### 6.3 Justice Score

```yaml
justice_metrics:
  fairness:
    measures:
      - "Consistent verdicts for similar crimes"
      - "Rich vs. poor treatment equality"
      - "Time to resolve disputes"

    player_perception: "Survey after legal interactions"

  crime_rate:
    measures:
      - "Theft incidents"
      - "Violent crimes"
      - "Contract disputes"

    consequences:
      low_crime: "Safe commerce, trust"
      high_crime: "Economic damage, fear"

  corruption:
    measures:
      - "Bribery reports"
      - "Official misconduct"
      - "Public trust surveys"

    consequences:
      low_corruption: "Efficient government"
      high_corruption: "Waste, unfairness, unrest"
```

### 6.4 Economic Score

```yaml
economic_metrics:
  trade_volume:
    measures:
      - "Imports arriving"
      - "Exports leaving"
      - "Market activity"

    consequences:
      high_trade: "Prosperity, rare goods available"
      low_trade: "Shortages, high prices"

  price_stability:
    measures:
      - "Price variance over time"
      - "Inflation rate"
      - "Availability of essentials"

    consequences:
      stable_prices: "Planning possible, fair trade"
      volatile_prices: "Hoarding, speculation, hardship"

  innovation_rate:
    measures:
      - "New techniques discovered"
      - "Adoption of improvements"
      - "Economic diversification"

    consequences:
      high_innovation: "Competitive advantage"
      low_innovation: "Stagnation, decline"
```

### 6.5 Overall Government Rating

```yaml
government_rating:
  calculation:
    infrastructure: "25%"
    welfare: "25%"
    justice: "20%"
    economy: "20%"
    religious: "10%"

  rating_levels:
    golden_age: "90-100"
    prosperous: "75-89"
    stable: "60-74"
    troubled: "40-59"
    crisis: "20-39"
    collapse: "0-19"

  player_impact:
    high_rating:
      - "Bonuses to all activities"
      - "Lower taxes"
      - "Better services"
      - "Attract immigrants"
    low_rating:
      - "Penalties to productivity"
      - "Higher taxes"
      - "Service failures"
      - "Emigration, unrest"

  political_consequences:
    very_low_rating:
      - "Calls for new leadership"
      - "Assembly votes of no confidence"
      - "Potential uprising"
```

---

## 7. Player Participation

### 7.1 Civic Duties

```yaml
civic_duties:
  corvee_labor:
    description: "Mandatory public work days"
    frequency: "10 days per year"
    tasks:
      - "Canal maintenance"
      - "Wall repair"
      - "Public construction"
    penalty_for_avoidance: "Fine or reputation loss"
    exemptions: "Elders, priests, military service"

  military_service:
    description: "Defense when called"
    who: "All adult males"
    when: "War or emergency"
    penalty: "Severe (exile or death)"

  taxation:
    temple_tithe: "10% of produce"
    trade_tax: "5% on transactions"
    property_tax: "Based on land holdings"

  jury_duty:
    description: "Serve in assembly trials"
    frequency: "When called"
    compensation: "Small payment"
```

### 7.2 Political Careers

```yaml
political_careers:
  assembly_speaker:
    description: "Regularly speaks at assembly"
    requirements:
      - "Reputation 200+"
      - "Speaking skill 40+"
    benefits:
      - "Influence decisions"
      - "Build reputation"
      - "Path to Elder status"

  ward_representative:
    description: "Represents neighborhood interests"
    requirements:
      - "Local reputation 100+"
      - "Resident 5+ years"
    duties:
      - "Gather neighbor concerns"
      - "Present to assembly"
      - "Distribute information"
    benefits:
      - "Local influence"
      - "Small stipend"

  temple_administrator:
    description: "Manage temple affairs"
    requirements:
      - "Scribe skills"
      - "Temple trust"
    duties:
      - "Oversee departments"
      - "Manage budgets"
      - "Report to High Priest"
    benefits:
      - "Good income"
      - "Power over resources"
      - "Access to information"

  military_commander:
    description: "Lead city forces"
    requirements:
      - "Combat skill 60+"
      - "Military reputation 150+"
      - "Lugal appointment"
    benefits:
      - "High status"
      - "Equipment access"
      - "War spoils share"
```

### 7.3 Running for Elder Council

```yaml
elder_election:
  eligibility:
    age: "50+ years"
    property: "5+ plots owned"
    reputation: "500+ total"
    citizenship: "Eridu native or 20+ years resident"
    no_crimes: "Clean legal record"

  process:
    vacancy: "When elder dies or removed"
    nomination: "Existing elders nominate candidates"
    vetting: "Assembly reviews candidates"
    selection: "Assembly acclaim"

  campaign:
    activities:
      - "Public speeches"
      - "Charitable donations"
      - "Temple offerings"
      - "Building relationships"

    costs:
      - "Time away from business"
      - "Gifts and donations"
      - "Political favors"

  once_elected:
    duties:
      - "Attend council meetings"
      - "Vote on proposals"
      - "Advise assembly"
    benefits:
      - "Temple dividend (10 SILA/month)"
      - "Political influence"
      - "Legacy status"
      - "NFT: Elder Badge"
```

---

## 8. Evolution & Autocracy

> Over time, democratic institutions may weaken as power concentrates.

### 8.1 Historical Trajectory

```yaml
political_evolution:
  early_period:
    name: "Assembly Dominance"
    characteristics:
      - "Full democratic participation"
      - "Temporary war leaders"
      - "Elder council advisory"
    triggers_next: "Prolonged warfare"

  middle_period:
    name: "Lugal Ascendancy"
    characteristics:
      - "Permanent war leader"
      - "Growing royal power"
      - "Assembly still consulted"
    triggers_next: "Economic complexity, external threats"

  late_period:
    name: "Divine Kingship"
    characteristics:
      - "King claims divine mandate"
      - "Assembly becomes rubber stamp"
      - "Hereditary succession"
    note: "This is the historical outcome"
```

### 8.2 Player Agency in Political Evolution

```yaml
player_agency:
  preserve_democracy:
    actions:
      - "Vote against permanent kingship"
      - "Support assembly rights"
      - "Hold leaders accountable"
    benefits: "More player voice in government"
    challenges: "Slower crisis response"

  accept_autocracy:
    actions:
      - "Support strong leader"
      - "Trade freedom for security"
    benefits: "Faster decisions, unity"
    drawbacks: "Less player voice"

  revolution:
    trigger: "Very low government rating + leader unpopularity"
    player_role: "Can join or oppose"
    outcome: "New government type"

  alternate_history:
    possibility: "Players could maintain democracy"
    training_data: "How do societies balance freedom and security?"
```

### 8.3 Government Types (Possible Outcomes)

```yaml
government_types:
  theocratic_democracy:
    description: "Original Eridu system"
    features:
      - "Two-house assembly"
      - "Temple centrality"
      - "Temporary leaders"
    player_impact: "Maximum political participation"

  constitutional_monarchy:
    description: "King limited by assembly"
    features:
      - "Permanent king"
      - "Assembly retains veto on major issues"
      - "Written laws"
    player_impact: "Moderate participation"

  absolute_monarchy:
    description: "King rules alone"
    features:
      - "Divine right of king"
      - "Assembly ceremonial only"
      - "Royal decree is law"
    player_impact: "Minimal participation, favor-seeking"

  temple_state:
    description: "Priests rule directly"
    features:
      - "High Priest as ruler"
      - "Religious law supreme"
      - "Temple controls economy"
    player_impact: "Religious careers important"
```

---

## Appendix: Quick Reference

### Assembly Vote Thresholds

| Outcome | Support Required |
|---------|------------------|
| Pass (clear) | 80%+ |
| More debate | 60-79% |
| Fail | <60% |
| Override Elder veto | 90%+ |

### Government Position Requirements

| Position | Reputation | Special Requirement |
|----------|------------|---------------------|
| Assembly voter | 0 | Adult free male |
| Speaker | 200+ | Speaking skill 40+ |
| Ward Rep | 100+ local | 5+ years resident |
| Elder | 500+ | Age 50+, 5+ plots |
| Lugal | 400+ | Military 200+, battle won |

### Service Costs

| Service | Price |
|---------|-------|
| Contract writing | 5-20 SILA |
| Court filing | 10 SILA |
| Healing (minor) | 10-30 SILA |
| Healing (major) | 50-200 SILA |
| Property registration | 20-100 SILA |

---

*"The assembly speaks for the living. The temple speaks for the gods. The king speaks for both—but only when they permit."*
