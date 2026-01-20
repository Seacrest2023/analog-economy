# Character Creation: The Cast of Eridu

> "You do not choose your birth. You choose what you do with it."

## Table of Contents

1. [Overview](#1-overview)
2. [Design Philosophy](#2-design-philosophy)
3. [Entry Paths](#3-entry-paths)
4. [The Social Hierarchy](#4-the-social-hierarchy)
5. [Character Backgrounds](#5-character-backgrounds)
6. [Starting Conditions by Background](#6-starting-conditions-by-background)
7. [The Land Purchase Shortcut](#7-the-land-purchase-shortcut)
8. [Physical Customization](#8-physical-customization)
9. [Name Generation](#9-name-generation)
10. [The First Moments](#10-the-first-moments)
11. [Training Data Value](#11-training-data-value)
12. [Implementation Notes](#12-implementation-notes)

---

## 1. Overview

Character creation in The Analog Economy is not a fantasy power trip. It mirrors the reality of ancient life: most people were born into hardship, and only through skill, luck, or wealth could they rise above their station.

### Core Principles

| Principle | Implementation |
|-----------|----------------|
| **Random by default** | Free players receive randomized backgrounds from commoner/marginalized tiers |
| **Buy your way up** | Land purchases instantly elevate social standing (with corresponding burdens) |
| **Earn your way up** | Players can be elected or appointed to higher positions through gameplay |
| **No chosen ones** | Every player starts as an ordinary person, not a prophesied hero |
| **Historical authenticity** | All roles existed in ancient Eridu (c. 4500-2000 BCE) |

---

## 2. Design Philosophy

### 2.1 The Lottery of Birth

In real ancient Mesopotamia, your birth determined nearly everything:

```
HISTORICAL REALITY
├── 5% born to elite families → paths to power
├── 20% born to artisan families → skilled trades
├── 60% born as commoners → subsistence farming/labor
└── 15% born marginalized → slavery, debt, disability
```

Our game reflects this. Free-to-play characters are randomly assigned from the bottom 75% of society. This creates:

- **Authentic starting conditions** - Most ancient people struggled
- **Meaningful progression** - Rising from nothing feels earned
- **Training data diversity** - We capture decisions from all social strata
- **Economic balance** - Premium purchases have real meaning

### 2.2 The Meritocracy Layer

While birth is random, advancement is earned:

```yaml
advancement_paths:
  skill_mastery:
    - "Master a craft → Become a respected artisan"
    - "Learn the scribal arts → Join the bureaucracy"
    - "Excel at trade → Become a Dam-gar merchant"

  social_climbing:
    - "Gain Temple favor → Appointed to positions"
    - "Gain community respect → Elected to councils"
    - "Marry up → Join a higher-status family"

  economic_purchase:
    - "Buy land → Instant elevation to landowner class"
    - "Buy NFT deed → Permanent elite status"
    - "Sponsor temple projects → Gain priestly favor"
```

### 2.3 Risk Scales with Reward

Higher starting positions come with higher stakes:

| Starting Position | Initial Advantage | Risk Factor |
|-------------------|-------------------|-------------|
| Marginalized | None | Low (little to lose) |
| Commoner | Basic stability | Low-Medium |
| Artisan | Skill + workshop access | Medium |
| Landowner | Property + income | High (must defend, maintain, pay taxes) |
| Elite | Everything | Very High (politics, assassination, obligations) |

---

## 3. Entry Paths

### 3.1 Free-to-Play Entry (Default)

```yaml
free_entry:
  process:
    1: "Create account"
    2: "System randomly assigns background"
    3: "Background determines starting location, possessions, relationships"
    4: "Player can re-roll ONCE for free"
    5: "Additional re-rolls cost SILA (earned in-game)"

  background_pool:
    tier_commoner: 70%  # Farmer, Fisher, Laborer, etc.
    tier_marginalized: 30%  # Debtor, Refugee, Marsh Dweller, etc.

  rationale: |
    Most free players start at the bottom. This:
    - Reflects historical reality
    - Creates shared struggle (community building)
    - Makes progression meaningful
    - Generates diverse training data
```

### 3.2 SILA Purchase Entry

Players who have earned SILA (through gameplay or purchase) can buy better starting conditions:

```yaml
sila_entry:
  background_unlock:
    artisan_backgrounds:
      cost: "500 SILA"
      examples: ["Apprentice Smith", "Weaver's Child", "Potter's Family"]
      advantage: "Start with basic craft skills, workshop access"

    professional_backgrounds:
      cost: "1,000 SILA"
      examples: ["Scribe Student", "Merchant's Nephew", "Healer's Apprentice"]
      advantage: "Start with literacy or specialized knowledge"

  re_rolls:
    cost: "50 SILA per re-roll"
    limit: "5 per character creation"
```

### 3.3 Land Purchase Entry (ANALOG/NFT)

The "buy your way in" path for serious investment:

```yaml
land_purchase_entry:
  description: |
    Purchasing land immediately elevates your social standing.
    You skip the struggle but inherit the burdens of property ownership.

  tiers:
    small_plot:
      cost: "100 ANALOG + gas fees"
      type: "Leasehold (50-year term)"
      location: "Outskirts, field zones"
      social_class: "Landed Commoner"
      starting_position: "You own a small farm plot"
      obligations:
        - "Temple tax (10% of harvest)"
        - "Canal maintenance duty"
        - "Defense contribution during raids"

    artisan_workshop:
      cost: "250 ANALOG + gas fees"
      type: "Leasehold (50-year term)"
      location: "Artisan quarter"
      social_class: "Artisan"
      starting_position: "You own a workshop space"
      obligations:
        - "Guild fees"
        - "Temple tax on production"
        - "Maintain building or lose lease"

    estate_deed:
      cost: "1,000 ANALOG + gas fees"
      type: "NFT (permanent ownership)"
      location: "Prime agricultural or urban land"
      social_class: "Elite"
      starting_position: "You own significant property"
      obligations:
        - "Heavy taxation"
        - "Military service expectations"
        - "Temple donation expectations"
        - "Political entanglements"
        - "Target for rivals"
```

---

## 4. The Social Hierarchy

### 4.1 The Pyramid of Eridu

```
                    ┌─────────────┐
                    │  DIVINE &   │  ~0.1%
                    │   RULING    │  Ensi/Lugal, Nin, Sanga
                    │    ELITE    │
                    ├─────────────┤
                    │   TEMPLE    │  ~5%
                    │  PERSONNEL  │  En, Gala, Priests
                    ├─────────────┤
                    │ BUREAUCRACY │  ~5%
                    │    & PRO    │  Scribes, Merchants, Foremen
                    ├─────────────┤
                    │             │
                    │  COMMONERS  │  ~60%
                    │ "Men of the │  Farmers, Fishers, Craftsmen
                    │    City"    │
                    │             │
                    ├─────────────┤
                    │ MARGINALIZED│  ~15%
                    │ & DEPENDENT │  Slaves, Debtors, Disabled
                    └─────────────┘
```

### 4.2 Class Details

```yaml
social_classes:
  divine_ruling_elite:
    description: "The apex of society, bridging gods and people"
    playable: false  # NPCs only at game start
    attainable: true  # Can be elected/appointed later
    titles:
      ensi_lugal: "Priest-King / Big Man - absolute ruler"
      sanga: "Temple Administrator - controls economy"
      nin: "Queen/High Priestess - manages estates, textiles"
      royal_scribe: "Records King's decrees, stands at right hand"

  temple_personnel:
    description: "Religion is the city's primary industry"
    playable: false  # Cannot start here
    attainable: true  # Through high Temple favor
    titles:
      en: "High Priest/Priestess - spiritual spouse of Enki"
      gala: "Lamentation Priest - gender-fluid clergy, Eme-sal dialect"
      ishib: "Purification Priest - libations, cleansing"
      asipu: "Exorcist - drives out demons with incantations"
      asu: "Physician - herbal medicine, practical healing"
      naditu: "Cloistered women - business, no children"

  bureaucracy_professional:
    description: "The educated class that keeps society running"
    playable_via: "SILA purchase (1,000+)"
    attainable: true  # Through skill mastery
    titles:
      dub_sar: "Scribe - the 'IT professional' of Sumer"
      dam_gar: "Merchant - travels to foreign lands for trade"
      ugula: "Foreman - supervises labor gangs"
      sa_gid: "Surveyor - 'Man of the Rope', measures fields"

  commoners:
    description: "Free citizens, the backbone of society"
    playable_via: "Default random pool (70%)"
    titles:
      engar: "Farmer - manages plow oxen, irrigation"
      shu_ku: "Fisherman - vital food provider"
      ush_bar: "Weaver - usually female, textile production"
      simug: "Smith - magician of metal, smelts bronze"
      nagar: "Carpenter/Boatwright - builds barges, chariots"
      lungaa: "Brewer - makes beer, often female"
      bahar: "Potter - mass produces clay vessels"

  marginalized_dependent:
    description: "Those at society's edges"
    playable_via: "Default random pool (30%)"
    titles:
      wardu: "Slave - prisoner of war, branded"
      debtor: "Sold self/children to pay loans"
      igi_nu_du: "'The One Who Does Not See' - blind workers"
      kar_kid: "Tavern Keeper/Prostitute - society's fringes"
      marsh_dweller: "Nomadic, lives in reed huts outside city"
```

---

## 5. Character Backgrounds

### 5.1 Commoner Backgrounds (Free Pool - 70%)

```yaml
commoner_backgrounds:
  the_farmer_child:
    description: "Born to a family working temple lands"
    starting_location: "Commoner quarter, edge of fields"
    starting_skills:
      - "Basic agriculture (seeding, harvesting)"
      - "Animal handling (oxen)"
      - "Weather reading"
    starting_possessions:
      - "Worn linen garment"
      - "Personal eating bowl"
      - "Family connection (can sleep at home)"
    starting_relationships:
      - "Family (farmer parents, siblings)"
      - "Neighbors (other farming families)"
    initial_quest: "Help with the harvest"

  the_fisher_youth:
    description: "Raised on the marshes, comfortable with water"
    starting_location: "Marsh edge settlement"
    starting_skills:
      - "Swimming"
      - "Basic fishing (nets, lines)"
      - "Reed craft (simple boats)"
    starting_possessions:
      - "Reed skirt"
      - "Small fishing net"
      - "Knowledge of marsh paths"
    starting_relationships:
      - "Marsh community (outsiders to city)"
      - "Fish market vendors"
    initial_quest: "Bring catch to the harbor market"

  the_craftsman_apprentice:
    description: "Recently apprenticed to a city artisan"
    starting_location: "Artisan quarter"
    starting_skills:
      - "Basic craft knowledge (random: pottery, weaving, or carpentry)"
      - "Tool maintenance"
      - "Material identification"
    starting_possessions:
      - "Apprentice garment"
      - "Basic tools of trade"
      - "Lodging at master's workshop"
    starting_relationships:
      - "Master craftsman (demanding)"
      - "Fellow apprentices (competitive)"
    initial_quest: "Complete a task for your master"

  the_laborer:
    description: "Strong back, no trade, working for daily rations"
    starting_location: "Commoner quarter"
    starting_skills:
      - "Heavy lifting"
      - "Endurance"
      - "Canal digging basics"
    starting_possessions:
      - "Minimal clothing"
      - "Strong body"
      - "Nothing else"
    starting_relationships:
      - "Labor gang (temporary bonds)"
      - "Ugula foreman (controls your work)"
    initial_quest: "Report to the canal project for work"

  the_brewer_family:
    description: "Part of a household brewing operation"
    starting_location: "Commoner quarter near grain stores"
    starting_skills:
      - "Basic brewing knowledge"
      - "Grain identification"
      - "Customer service"
    starting_possessions:
      - "Work garment"
      - "Small beer ration"
      - "Knowledge of beer house locations"
    starting_relationships:
      - "Family brewing operation"
      - "Regular customers"
      - "Grain suppliers"
    initial_quest: "Deliver beer to the temple workers"
```

### 5.2 Marginalized Backgrounds (Free Pool - 30%)

```yaml
marginalized_backgrounds:
  the_debtor:
    description: "Family sold into debt-slavery to pay loans"
    starting_location: "Creditor's household"
    starting_skills:
      - "Obedience (survival skill)"
      - "One useful skill from previous life"
    starting_possessions:
      - "Nothing (all belongs to creditor)"
    starting_relationships:
      - "Creditor (owner, can be cruel or kind)"
      - "Other debt-servants"
    special_condition:
      name: "Debt Obligation"
      description: "Must work off debt (1,000 SILA equivalent)"
      freedom_path: "Pay off debt OR wait 3 years OR creditor releases you"
    initial_quest: "Perform your duties without incident"

  the_refugee:
    description: "Fled a failed settlement, arrived with nothing"
    starting_location: "Temple courtyard (no home)"
    starting_skills:
      - "Survival instincts"
      - "Travel knowledge"
      - "Distrust (protective)"
    starting_possessions:
      - "Ragged clothing"
      - "Trauma (Witness penalty: -10 starting capacity)"
    starting_relationships:
      - "None (must build from scratch)"
    special_condition:
      name: "Stranger"
      description: "NPCs are suspicious, prices higher, jobs harder to get"
      resolution: "Build reputation through consistent good behavior"
    initial_quest: "Find food and shelter before nightfall"

  the_marsh_dweller:
    description: "Born to nomadic people outside city walls"
    starting_location: "Deep marshes"
    starting_skills:
      - "Marsh survival (expert)"
      - "Reed construction"
      - "Fowling and fishing"
      - "Herbal knowledge (marsh plants)"
    starting_possessions:
      - "Reed garments"
      - "Small reed boat"
      - "Hunting tools"
    starting_relationships:
      - "Marsh tribe (strong)"
      - "City folk (mutual distrust)"
    special_condition:
      name: "Outsider"
      description: "Not recognized as citizen, cannot own city property"
      resolution: "Gain Temple favor OR marry a citizen"
    initial_quest: "Trade marsh goods at the city edge"

  the_blind_worker:
    description: "Lost sight but gained other senses"
    starting_location: "Temple work quarters"
    starting_skills:
      - "Acute hearing"
      - "Touch sensitivity"
      - "Grinding grain (blind work)"
      - "Memory (no writing, must remember)"
    starting_possessions:
      - "Simple garment"
      - "Walking stick"
      - "Guaranteed temple rations"
    special_condition:
      name: "Igi-nu-du"
      description: "Cannot read, limited mobility, but protected by Temple"
      advantages: "Never starve, unique sensory abilities"
    initial_quest: "Complete your temple duties"

  the_tavern_child:
    description: "Raised in the rough world of taverns and streets"
    starting_location: "Tavern district"
    starting_skills:
      - "Street smarts"
      - "Gossip network"
      - "Basic brewing/serving"
      - "Spotting trouble"
    starting_possessions:
      - "City clothing"
      - "Knowledge of back alleys"
      - "A few contacts"
    starting_relationships:
      - "Tavern keeper (protector/employer)"
      - "Regular patrons"
      - "City underworld (aware of)"
    initial_quest: "Collect information for the tavern keeper"
```

### 5.3 Artisan Backgrounds (SILA Purchase - 500)

```yaml
artisan_backgrounds:
  the_smith_apprentice:
    description: "Learning the sacred art of metalworking"
    starting_location: "Forge district"
    starting_skills:
      - "Fire management"
      - "Basic metallurgy theory"
      - "Bellows operation"
    starting_possessions:
      - "Leather apron"
      - "Personal tools"
      - "Workshop access"
    starting_relationships:
      - "Master Simug (teacher)"
      - "Metal merchants (suppliers)"
    advancement_path: "Full smith → Master → Temple contractor"

  the_weaver_daughter:
    description: "Training in Eridu's primary export industry"
    starting_location: "Temple textile workshop"
    starting_skills:
      - "Basic weaving"
      - "Wool preparation"
      - "Pattern recognition"
    starting_possessions:
      - "Quality garments"
      - "Personal loom tools"
      - "Temple workshop access"
    starting_relationships:
      - "Master weavers (mostly women)"
      - "Wool merchants"
    advancement_path: "Full weaver → Pattern master → Workshop supervisor"

  the_potter_family:
    description: "From a lineage of clay workers"
    starting_location: "Pottery district"
    starting_skills:
      - "Clay preparation"
      - "Basic wheel throwing"
      - "Kiln firing basics"
    starting_possessions:
      - "Potter's tools"
      - "Small kiln access"
      - "Clay source knowledge"
    starting_relationships:
      - "Potter family"
      - "Kiln fuel suppliers"
    advancement_path: "Journeyman → Master potter → Temple supplier"
```

### 5.4 Professional Backgrounds (SILA Purchase - 1,000)

```yaml
professional_backgrounds:
  the_scribe_student:
    description: "Training at the Edubba (tablet house)"
    starting_location: "Temple scribal school"
    starting_skills:
      - "Basic cuneiform (50 signs)"
      - "Mathematics (counting, measuring)"
      - "Tablet preparation"
    starting_possessions:
      - "Student tablet"
      - "Stylus"
      - "Quality garments"
    starting_relationships:
      - "Ummia (teacher)"
      - "Fellow students"
      - "Temple administration (observing)"
    special_advantage: "Literacy is rare and powerful"
    advancement_path: "Junior scribe → Senior scribe → Temple administrator"

  the_merchant_nephew:
    description: "Family has trading connections"
    starting_location: "Harbor district"
    starting_skills:
      - "Basic arithmetic"
      - "Trade good identification"
      - "Bargaining basics"
      - "Foreign language fragments"
    starting_possessions:
      - "Travel garments"
      - "Small trade goods (10 SILA value)"
      - "Uncle's letter of introduction"
    starting_relationships:
      - "Merchant uncle (mentor, sometimes away)"
      - "Harbor workers"
      - "Foreign trader contacts"
    advancement_path: "Trade assistant → Independent trader → Dam-gar"

  the_healer_apprentice:
    description: "Learning the dual arts of medicine and magic"
    starting_location: "Temple medical quarters"
    starting_skills:
      - "Herbal identification"
      - "Wound cleaning"
      - "Basic incantations"
    starting_possessions:
      - "Healer's bag"
      - "Herb samples"
      - "Protective amulet"
    starting_relationships:
      - "Master Asu (physician)"
      - "Asipu (exorcist, different approach)"
      - "Patients (grateful or not)"
    advancement_path: "Healer → Temple physician → Chief Asu"
```

---

## 6. Starting Conditions by Background

### 6.1 Starting Resources Matrix

| Background Tier | Hunger | Thirst | Health | SILA | Shelter | Social Standing |
|-----------------|--------|--------|--------|------|---------|-----------------|
| Marginalized | 70% | 60% | 80% | 0 | None/Unstable | Outsider |
| Commoner | 85% | 80% | 100% | 0-5 | Family/Shared | Citizen |
| Artisan | 90% | 90% | 100% | 10-20 | Workshop | Respected |
| Professional | 95% | 95% | 100% | 25-50 | Quality housing | Influential |
| Landowner | 100% | 100% | 100% | 50-100 | Private property | Elite |

### 6.2 Starting Skills Matrix

```yaml
starting_skills_by_tier:
  marginalized:
    guaranteed: ["Survival instinct"]
    random_1_of: ["Begging", "Stealth", "Endurance", "Street smarts"]

  commoner:
    guaranteed: ["Basic trade skill (varies by background)"]
    random_1_of: ["Cooking", "Mending", "Haggling", "Gossip"]

  artisan:
    guaranteed: ["Craft specialty (intermediate)", "Tool use"]
    random_1_of: ["Quality assessment", "Customer relations", "Material sourcing"]

  professional:
    guaranteed: ["Literacy OR Trade network OR Medical basics"]
    bonus: ["Mathematics", "Record keeping", "Formal speech"]

  landowner:
    guaranteed: ["Property management", "Basic agriculture OR craft"]
    bonus: ["Negotiation", "Contract law", "Supervisor skills"]
```

---

## 7. The Land Purchase Shortcut

### 7.1 What Buying Land Really Means

```yaml
land_purchase_reality:
  what_you_get:
    - "Immediate social elevation"
    - "Property that generates income (if managed)"
    - "NPC workers to delegate tasks"
    - "A place in the elite social network"
    - "Hereditary asset (passes to next life)"

  what_you_also_get:
    - "Taxes (10-30% of production to Temple)"
    - "Maintenance obligations (buildings decay)"
    - "Defense responsibilities (must protect)"
    - "Social expectations (donations, participation)"
    - "Enemies (rivals want your land)"
    - "Complexity (more to manage)"

  the_balance: |
    Land purchase is NOT "pay to win." It's "pay to play a harder game
    with higher stakes." A smart commoner who rises through skill may
    end up more stable than a careless landowner who loses everything.
```

### 7.2 Land Purchase Character Generation

When a player purchases land, character creation changes:

```yaml
landowner_creation:
  step_1_property_selection:
    - "Choose land type (farm, workshop, estate)"
    - "Choose location (from available plots)"
    - "Complete ANALOG transaction"

  step_2_background_generation:
    description: "System generates a backstory for how you acquired land"
    options:
      inheritance: "Family died, you inherited (new to management)"
      merchant_success: "Made fortune in trade, bought property"
      temple_reward: "Granted land for service to the temple"
      marriage: "Married into a landed family"
      mystery: "Arrived with wealth from elsewhere (foreign merchant)"

  step_3_starting_conditions:
    location: "Your property"
    possessions: "Everything on the land"
    npcs: "Basic workers already in place"
    obligations: "First tax payment due in 30 days"
    tutorial: "Property management introduction"

  step_4_the_catch:
    - "You own land but may not know how to work it"
    - "Must still learn the skills (farming, smithing, etc.)"
    - "NPCs handle basics but you need mastery for growth"
    - "Rivals and neighbors are watching the newcomer"
```

---

## 8. Physical Customization

### 8.1 Customization Options

Physical appearance has limited customization to maintain historical accuracy:

```yaml
physical_customization:
  fixed_by_era:
    skin_tone: "Range appropriate to Mesopotamian population"
    body_type: "Realistic range (no superhero physiques)"
    height: "Historical average range (shorter than modern)"

  customizable:
    face_shape: "8 base options with sliders"
    eye_shape: "6 options"
    nose_shape: "6 options"
    hair_style: "Era-appropriate options (10-15)"
    hair_color: "Black, dark brown only (historical)"
    facial_hair: "Men: clean, stubble, short beard, long beard"
    scars_marks: "Optional distinguishing features"

  class_indicators:
    marginalized:
      - "Debt brand possible (abbuttum haircut)"
      - "Worn, patched clothing"
      - "Signs of hard labor"
    commoner:
      - "Simple, practical clothing"
      - "Work-calloused hands"
      - "Weathered skin"
    artisan:
      - "Craft-specific marks (smith burns, potter dust)"
      - "Better quality clothing"
      - "Tools visible"
    elite:
      - "Fine linen garments"
      - "Jewelry options"
      - "Softer hands"
```

### 8.2 What You Cannot Change

```yaml
fixed_characteristics:
  gender:
    note: "Selected at creation, affects available roles"
    historical_context: |
      Gender roles were distinct but not absolute in Sumer.
      Women could own property, run businesses, and hold religious office.
      Some roles (Gala priests) were explicitly gender-fluid.
    gameplay_impact: "Some professions historically gendered (weaving=female, smithing=male)"
    flexibility: "Players can pursue any path, but may face historical social friction"

  age:
    starting_age: "Young adult (equivalent to 16-20)"
    aging: "Characters age over time"
    death: "Natural death possible from old age"

  family_background:
    assigned: "Based on chosen/random background"
    cannot_change: "You cannot choose to be born royal"
```

---

## 9. Name Generation

### 9.1 Sumerian Naming Conventions

```yaml
naming_system:
  structure: "Sumerians used single names, often with meaning"

  male_name_elements:
    divine:
      - "En-" (lord)
      - "Lugal-" (king)
      - "Ur-" (man of)
      - "-ki-ag" (beloved of)
    descriptive:
      - "-banda" (young, junior)
      - "-gal" (great)
      - "-zi" (true, faithful)
    deity_references:
      - "-Enki" (god of wisdom)
      - "-Nanna" (moon god)
      - "-Utu" (sun god)

  female_name_elements:
    divine:
      - "Nin-" (lady)
      - "Ama-" (mother)
    descriptive:
      - "-kala" (precious)
      - "-shag" (heart)
      - "-gen" (true)
    deity_references:
      - "-Inanna" (goddess of love/war)
      - "-Nisaba" (goddess of writing)

  example_names:
    male:
      - "Ur-Nammu" (Man of Nammu)
      - "Enki-mansum" (Enki gave to me)
      - "Lugal-zagesi" (King of Zagesi)
      - "Dudu" (Beloved)
    female:
      - "Nin-kagina" (Lady of truth)
      - "Shagshag" (Heart of hearts)
      - "Ama-kalamma" (Mother of the land)
      - "Ninlil-zimu" (Lady Enlil, my life)
```

### 9.2 Name Generation Interface

```yaml
name_generation:
  option_1_generator:
    - "System suggests 5 historically appropriate names"
    - "Player can regenerate unlimited times"
    - "Names are checked against existing players (uniqueness)"

  option_2_custom:
    - "Player enters custom name"
    - "System validates against Sumerian conventions"
    - "Warns if historically implausible"
    - "Allows anyway (player choice)"

  option_3_meaningful:
    - "Player selects meaning elements"
    - "System generates name from meaning"
    - "Example: 'Beloved of Enki' + 'faithful' → 'Enki-ki-ag-zi'"
```

---

## 10. The First Moments

### 10.1 The Drop Scene

Every player's first moments are crafted based on their background:

```yaml
first_moments:
  marginalized_refugee:
    scene: |
      You stand at the edge of the Temple courtyard as the morning
      announcements echo off mud-brick walls. You arrived last night
      with nothing. Your stomach aches. The crowd ignores you—another
      refugee from the failed settlements upriver.

      The priest finishes speaking. People disperse to their lives.
      You have no life here. Not yet.

      What do you do?
    immediate_pressures:
      - "Hunger at 70%"
      - "No shelter for tonight"
      - "No relationships"
      - "NPCs are suspicious"

  commoner_farmer:
    scene: |
      The rooster's cry came too early. Your father is already up,
      checking the irrigation channel that feeds your family's plot.
      It's planting season—the most important weeks of the year.

      'Today you work the south field,' he says without looking up.
      'The oxen team arrives at midday. Don't be late.'

      You're sixteen now. Old enough to work alone. Old enough to
      start thinking about your own future.
    immediate_pressures:
      - "Family expectations"
      - "Work to do today"
      - "Stable but constrained"

  landowner_new:
    scene: |
      The surveyor's rope lies coiled at your feet. The Sa-gid has
      marked the boundaries of your land—YOUR land—with clay pegs.

      It looks smaller than you imagined. The irrigation channel is
      silted. The storehouse roof sags. The two workers assigned to
      you look skeptical of their new master.

      'The Temple tax assessor comes in thirty days,' the surveyor
      says. 'I suggest you have something to show him.'

      You own land. Now you must learn what that means.
    immediate_pressures:
      - "30-day deadline for first tax"
      - "Property needs work"
      - "Must earn workers' respect"
      - "Don't know how to farm/craft yet"
```

### 10.2 Tutorial Integration

```yaml
tutorial_by_background:
  marginalized:
    focus: "Immediate survival"
    lessons:
      - "Finding food and water"
      - "Identifying shelter options"
      - "Building first relationships"
      - "Earning first SILA"
    tone: "Desperate, scrappy, resourceful"

  commoner:
    focus: "Skill development"
    lessons:
      - "Performing your trade"
      - "Understanding the economy"
      - "Building reputation"
      - "Planning advancement"
    tone: "Steady, hopeful, hardworking"

  artisan_professional:
    focus: "Mastery and growth"
    lessons:
      - "Advanced craft techniques"
      - "Business relationships"
      - "Taking on apprentices"
      - "Temple contracts"
    tone: "Ambitious, skilled, competitive"

  landowner:
    focus: "Management and survival"
    lessons:
      - "Property maintenance"
      - "NPC delegation"
      - "Tax obligations"
      - "Still need to learn the actual skills"
    tone: "Overwhelmed, responsible, learning fast"
```

---

## 11. Training Data Value

### 11.1 What Character Creation Captures

```yaml
training_data_from_creation:
  identity_choices:
    - "What names do players choose? Why?"
    - "How do they customize appearance?"
    - "Do they embrace or resist their assigned background?"

  economic_decisions:
    - "Who pays for better starting conditions?"
    - "What's the conversion rate of money → advantage?"
    - "Do landowners succeed or fail more often?"

  social_behavior:
    - "How do marginalized players build relationships?"
    - "How do elite players treat commoners?"
    - "Do players help their starting class or leave it behind?"

  risk_assessment:
    - "Do players re-roll for better backgrounds?"
    - "How many re-rolls before acceptance?"
    - "Do landowners understand their obligations?"
```

### 11.2 Longitudinal Tracking

```yaml
longitudinal_value:
  question: "Does starting position determine outcomes?"
  tracking:
    - "Survival rates by starting class"
    - "Wealth accumulation curves"
    - "Social mobility patterns"
    - "Player satisfaction by background"
  insight: |
    Real-world AI applications need to understand how initial
    conditions affect long-term outcomes. Our game provides
    millions of data points on exactly this question.
```

---

## 12. Implementation Notes

### 12.1 MVP Scope

```yaml
mvp_character_creation:
  included:
    backgrounds:
      - "5 commoner backgrounds"
      - "3 marginalized backgrounds"
      - "2 artisan backgrounds (SILA purchase)"
      - "1 professional background (SILA purchase)"

    customization:
      - "Basic face/body sliders"
      - "Hair style selection"
      - "Name generator"

    entry_paths:
      - "Free random (commoner/marginalized pool)"
      - "SILA background purchase"
      - "Land purchase (1 type: small farm)"

    tutorial:
      - "Background-specific opening scenes"
      - "First 30 minutes guided by background"

  deferred:
    - "All professional backgrounds"
    - "Workshop and estate land purchases"
    - "Advanced customization"
    - "Family creation (spouse, children)"
```

### 12.2 Database Schema Considerations

```yaml
character_data:
  persistent:
    - "account_id (bloodline link)"
    - "character_id"
    - "name"
    - "background_type"
    - "entry_path (free/sila/land)"
    - "creation_timestamp"
    - "starting_conditions (snapshot)"

  tracked_for_training:
    - "re_roll_count"
    - "customization_time_spent"
    - "name_generation_attempts"
    - "tutorial_completion_rate"
    - "first_24h_survival"
    - "first_7d_progression"
```

---

## Appendix: The Cast of Eridu Quick Reference

### By Social Tier

| Tier | Sumerian Title | English | Playable Start? |
|------|----------------|---------|-----------------|
| **Elite** | Ensi/Lugal | Priest-King | No (attainable) |
| **Elite** | Sanga | Temple Administrator | No (attainable) |
| **Elite** | Nin | Queen/High Priestess | No (attainable) |
| **Temple** | En | High Priest/Priestess | No (attainable) |
| **Temple** | Gala | Lamentation Priest | No (attainable) |
| **Temple** | Asipu | Exorcist | No (attainable) |
| **Temple** | Asu | Physician | SILA (1,000) |
| **Professional** | Dub-sar | Scribe | SILA (1,000) |
| **Professional** | Dam-gar | Merchant | SILA (1,000) |
| **Professional** | Ugula | Foreman | No (attainable) |
| **Professional** | Sa-gid | Surveyor | No (attainable) |
| **Commoner** | Engar | Farmer | Free |
| **Commoner** | Shu-ku | Fisherman | Free |
| **Commoner** | Ush-bar | Weaver | Free |
| **Commoner** | Simug | Smith | SILA (500) |
| **Commoner** | Nagar | Carpenter | SILA (500) |
| **Commoner** | Lungaa | Brewer | Free |
| **Commoner** | Bahar | Potter | SILA (500) |
| **Marginalized** | Wardu | Slave | Free |
| **Marginalized** | Debtor | Debt-servant | Free |
| **Marginalized** | Igi-nu-du | Blind Worker | Free |
| **Marginalized** | Kar-kid | Tavern Worker | Free |
| **Marginalized** | Marsh Dweller | Outsider | Free |

---

*"You were not born a hero. You were born a human. What you become is your choice—and your struggle."*
