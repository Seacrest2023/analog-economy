# Inventory System Specification

> "Every object tells a story. Every possession has weight."

## Table of Contents

1. [Inventory Philosophy](#1-inventory-philosophy)
2. [Item Categories](#2-item-categories)
3. [Rarity Tiers](#3-rarity-tiers)
4. [Official Store Items](#4-official-store-items)
5. [Weapons Inventory](#5-weapons-inventory)
6. [Tools Inventory](#6-tools-inventory)
7. [Artifacts & Household Goods](#7-artifacts--household-goods)
8. [Jewelry Inventory](#8-jewelry-inventory)
9. [Craftable Items](#9-craftable-items)
10. ["Learn the Ways" Crafting System](#10-learn-the-ways-crafting-system)
11. [Loot & Found Items](#11-loot--found-items)
12. [Land & Property](#12-land--property)
13. [City Store Distribution](#13-city-store-distribution)
14. [Marketplace & Trading](#14-marketplace--trading)
15. [Metalworking & Crafting Processes](#15-metalworking--crafting-processes)
16. [NPC Conversion & Passive Income](#16-npc-conversion--passive-income)
17. [Item Properties](#17-item-properties)
18. [Inventory Management](#18-inventory-management)
19. [Item Lifecycle](#19-item-lifecycle)
20. [Pricing Guidelines](#20-pricing-guidelines)

---

## 1. Inventory Philosophy

### 1.1 Core Principles

```yaml
inventory_philosophy:
  realism_first:
    description: "Items should feel historically grounded"
    implication: "No magical glowing swords—but exceptional craftsmanship exists"

  scarcity_matters:
    description: "Valuable things are actually rare"
    implication: "Fixed supplies, no infinite spawns of good items"

  everything_has_weight:
    description: "Carrying capacity is limited"
    implication: "Strategic choices about what to carry"

  items_degrade:
    description: "Nothing lasts forever"
    implication: "Maintenance creates ongoing economy, repair skills matter"

  ownership_is_real:
    description: "Key items can be truly owned (NFT)"
    implication: "Trade outside game, real value"
```

### 1.2 Historical Grounding

All items in the Ancient Era are based on actual Mesopotamian artifacts and materials:

- **Materials available:** Clay, reed, mud brick, copper, bitumen, wool, linen, leather, wood, stone, obsidian, lapis lazuli, carnelian, gold, silver
- **Materials NOT available:** Iron (rare meteoric only), glass (primitive), paper, silk

---

## 2. Item Categories

### 2.1 Category Overview

```yaml
item_categories:
  tools:
    description: "Items used for work"
    examples: "Sickle, hoe, fishing net, spindle"
    tradeable: true
    craftable: true

  weapons:
    description: "Items for combat and hunting"
    examples: "Copper dagger, spear, bow, sling"
    tradeable: true
    craftable: true

  clothing:
    description: "Wearable items"
    examples: "Wool kilt, linen robe, leather sandals"
    tradeable: true
    craftable: true

  jewelry:
    description: "Decorative items with status value"
    examples: "Lapis beads, gold earrings, cylinder seal"
    tradeable: true
    craftable: true

  food:
    description: "Consumable sustenance"
    examples: "Bread, beer, fish, dates"
    tradeable: true
    craftable: true
    perishable: true

  materials:
    description: "Raw crafting components"
    examples: "Copper ingot, wool bundle, clay"
    tradeable: true
    craftable: false

  furniture:
    description: "Household items"
    examples: "Reed mat, wooden stool, storage jar"
    tradeable: true
    craftable: true

  religious:
    description: "Temple and worship items"
    examples: "Votive statue, offering bowl, incense"
    tradeable: "Limited"
    craftable: true

  documents:
    description: "Written records"
    examples: "Clay tablet, contract, receipt"
    tradeable: true
    craftable: true

  land:
    description: "Property deeds"
    examples: "City plot, farm plot, workshop"
    tradeable: true
    craftable: false
    nft_only: true

  special:
    description: "Meta-game items"
    examples: "Reincarnation ticket, legacy token"
    tradeable: true
    craftable: false
    nft_only: true
```

---

## 3. Rarity Tiers

### 3.1 Tier Definitions

```yaml
rarity_tiers:
  common:
    color: "Gray"
    drop_rate: "60%"
    description: "Everyday items anyone can make"
    examples:
      - "Reed basket"
      - "Clay cup"
      - "Wool cloth (basic)"
      - "Barley bread"
    nft_eligible: false

  uncommon:
    color: "Green"
    drop_rate: "25%"
    description: "Quality items requiring skill"
    examples:
      - "Copper sickle"
      - "Woven mat (decorated)"
      - "Beer (quality)"
      - "Leather sandals"
    nft_eligible: false

  rare:
    color: "Blue"
    drop_rate: "10%"
    description: "Expert craftsmanship or scarce materials"
    examples:
      - "Bronze dagger"
      - "Linen robe (fine)"
      - "Lapis bead necklace"
      - "Cylinder seal (personal)"
    nft_eligible: true
    nft_threshold: "Top 10% quality"

  epic:
    color: "Purple"
    drop_rate: "4%"
    description: "Exceptional items, master crafters only"
    examples:
      - "Gold earrings"
      - "Ceremonial copper axe"
      - "Embroidered priest robe"
      - "Master cylinder seal"
    nft_eligible: true
    nft_threshold: "Top 5% quality"

  legendary:
    color: "Orange"
    drop_rate: "1%"
    description: "One-of-a-kind or divine-touched items"
    examples:
      - "Blessed weapon (temple)"
      - "Royal jewelry"
      - "Ancient heirloom"
      - "Innovation blueprint"
    nft_eligible: true
    nft_required: true
    supply: "Strictly limited"
```

### 3.2 Quality Levels

Within each rarity tier, items have a quality score (1-100):

```yaml
quality_scoring:
  factors:
    materials: "30% - Quality of inputs"
    craftsmanship: "40% - Crafter skill level"
    tools_used: "15% - Quality of crafting tools"
    conditions: "10% - Workshop, lighting, time taken"
    luck: "5% - Random variance"

  quality_effects:
    durability: "+1% per quality point"
    effectiveness: "+0.5% per quality point"
    appearance: "Visual differences at 25/50/75/100"
    value: "Exponential increase with quality"

  nft_threshold:
    rare_items: "Quality 90+ can be minted"
    epic_items: "Quality 85+ can be minted"
    legendary_items: "Always NFT"
```

---

## 4. Official Store Items

Items sold directly by the developer (Mault).

### 4.1 Reincarnation Tickets

```yaml
reincarnation_tickets:
  description: "Permission to begin a new life"

  tiers:
    basic_ticket:
      price: "$10"
      features:
        - "Start as commoner"
        - "Random family placement"
        - "Basic era access"
      supply: "Unlimited"
      nft: true
      royalty: "5%"

    heritage_ticket:
      price: "$25"
      features:
        - "Choose profession family"
        - "Small starting bonus"
        - "Era selection"
      supply: "Limited waves (10,000 per wave)"
      nft: true
      royalty: "5%"

    noble_ticket:
      price: "$50"
      features:
        - "Born into elite family"
        - "Significant starting advantages"
        - "All eras unlocked"
        - "Bloodline bonus active"
      supply: "Very limited (1,000 per era)"
      nft: true
      royalty: "5%"

    founder_ticket:
      price: "$100"
      features:
        - "All noble benefits"
        - "Founder badge (permanent)"
        - "Early access to new eras"
        - "Exclusive cosmetics"
      supply: "500 total (never more)"
      nft: true
      royalty: "5%"
```

### 4.2 Land Deeds

```yaml
land_deeds:
  description: "Ownership of in-game property"

  eridu_ancient_era:
    city_plots:
      temple_district:
        total_supply: 50
        price_range: "$300-500"
        benefits:
          - "Prime location for business"
          - "High foot traffic"
          - "Religious event access"
        rental_potential: "High"

      market_district:
        total_supply: 100
        price_range: "$150-300"
        benefits:
          - "Trading bonus"
          - "Merchant NPC proximity"
          - "Storage facilities"
        rental_potential: "High"

      residential_district:
        total_supply: 200
        price_range: "$50-150"
        benefits:
          - "Build home"
          - "Family housing"
          - "Quiet area"
        rental_potential: "Medium"

      craftsman_district:
        total_supply: 150
        price_range: "$75-200"
        benefits:
          - "Workshop space"
          - "Crafting bonus"
          - "Apprentice housing"
        rental_potential: "Medium"

    farm_plots:
      irrigated_fields:
        total_supply: 500
        price_range: "$75-150"
        benefits:
          - "Reliable water"
          - "High crop yield"
          - "Near city"
        rental_potential: "High"

      rain_fed_fields:
        total_supply: 1000
        price_range: "$25-75"
        benefits:
          - "Lower maintenance"
          - "Larger plots"
          - "Grazing rights"
        rental_potential: "Medium"

      orchard_plots:
        total_supply: 300
        price_range: "$100-200"
        benefits:
          - "Date palms, fruit trees"
          - "Multi-year investment"
          - "Premium products"
        rental_potential: "Medium"

    special_plots:
      workshop_plots:
        total_supply: 200
        price_range: "$100-300"
        benefits:
          - "Industrial zoning"
          - "Kiln/forge permitted"
          - "Apprentice capacity"

      tavern_plots:
        total_supply: 50
        price_range: "$150-400"
        benefits:
          - "Alcohol service license"
          - "Entertainment venue"
          - "High traffic"

  nft_properties:
    all_land: true
    royalty: "5% on all resales"
    rental_income: "Owner sets rates"
```

### 4.3 Premium Items (Store-Only)

```yaml
premium_items:
  legendary_tools:
    blessed_sickle:
      price: "$25"
      supply: 500
      benefits:
        - "+20% harvest speed"
        - "Never breaks (self-repairs)"
        - "Unique visual effect"
      nft: true

    temple_craftsman_kit:
      price: "$50"
      supply: 200
      benefits:
        - "+15% crafting quality"
        - "Full tool set"
        - "Blessed by Enki"
      nft: true

  legendary_weapons:
    kings_guard_spear:
      price: "$40"
      supply: 300
      benefits:
        - "+25% combat effectiveness"
        - "Intimidation aura"
        - "Slow degradation"
      nft: true

    hunter_compound_bow:
      price: "$35"
      supply: 400
      benefits:
        - "+30% hunting success"
        - "Extended range"
        - "Quiet shot"
      nft: true

  cosmetics:
    royal_jewelry_set:
      price: "$15"
      supply: "Unlimited"
      items:
        - "Gold circlet"
        - "Lapis collar"
        - "Carnelian bracelet"
      nft: false

    priest_vestments:
      price: "$20"
      supply: 1000
      items:
        - "Ceremonial robe"
        - "Temple sandals"
        - "Sacred sash"
      nft: true

    merchant_finery:
      price: "$10"
      supply: "Unlimited"
      items:
        - "Quality wool robe"
        - "Leather belt with pouches"
        - "Cylinder seal (decorative)"
      nft: false
```

### 4.4 Starter Packs

```yaml
starter_packs:
  farmers_beginning:
    price: "$15"
    contents:
      - "Copper sickle (uncommon)"
      - "Seed grain (50 sila)"
      - "Wool clothing set"
      - "100 SILA currency"
    value: "~$25 worth"

  craftsmans_toolkit:
    price: "$20"
    contents:
      - "Basic tool set (profession-appropriate)"
      - "Raw materials bundle"
      - "Workshop access token (1 month)"
      - "150 SILA currency"
    value: "~$35 worth"

  merchants_fortune:
    price: "$25"
    contents:
      - "Trade goods assortment"
      - "Donkey (transport animal)"
      - "Quality clothing"
      - "200 SILA currency"
      - "Marketplace stall token (1 week)"
    value: "~$45 worth"

  warriors_arsenal:
    price: "$30"
    contents:
      - "Copper spear (rare)"
      - "Leather armor"
      - "Shield (reed/leather)"
      - "150 SILA currency"
    value: "~$50 worth"

  founders_collection:
    price: "$75"
    contents:
      - "Heritage Reincarnation Ticket"
      - "City plot deed (residential)"
      - "Full profession toolkit"
      - "500 SILA currency"
      - "Founder cosmetic set"
    value: "~$150 worth"
    supply: "Limited (1000)"
```

### 4.5 SILA-Only Developer Store

> Items purchasable with earned SILA tokens only—not crypto. These provide essential gameplay benefits without pay-to-win.

```yaml
sila_store:
  description: |
    SILA tokens earned through gameplay can ONLY be spent on these items from the developer.
    This creates a reward loop: Learn → Craft → Earn SILA → Buy essentials from developer.

  currency_note:
    sila_accepted: true
    analog_accepted: false
    crypto_accepted: false
    purpose: "Ensure free-to-play players can access essential items"

  survival_essentials:
    fire_starter_kit:
      name: "Premium Fire Striker Kit"
      description: "High-quality flint and pyrite set with prepared tinder"
      price: "25 SILA"
      supply: "Unlimited"
      contents:
        - "Quality flint nodule"
        - "Large iron pyrite chunk"
        - "Dried horse hoof fungus"
        - "Cattail fluff bundle"
        - "Sealed clay container"
      benefits:
        - "+20% fire-starting success rate"
        - "Longer-lasting components"
        - "Waterproof container"
      durability: "50 uses before replacement needed"
      nft_eligible: false

    ember_carrier:
      name: "Temple-Blessed Fire Safe"
      description: "Keeps embers alive longer during travel"
      price: "15 SILA"
      supply: "Unlimited"
      duration: "Embers last 8 hours"
      blessing: "+5% warmth bonus"
      nft_eligible: false

    basic_ration_pack:
      name: "Week's Provisions"
      description: "Barley bread, dried dates, beer"
      price: "10 SILA"
      supply: "Unlimited"
      contents:
        - "7 days of basic food"
        - "Water skin"
        - "Salt portion"
      prevents: "Starvation for 1 week"
      nft_eligible: false

    first_aid_bundle:
      name: "Healer's Pouch"
      description: "Basic medicinal supplies"
      price: "20 SILA"
      supply: "Unlimited"
      contents:
        - "Wound binding cloths"
        - "Antiseptic herbs"
        - "Pain-dulling willow bark"
        - "Honey (wound treatment)"
      uses: 5
      nft_eligible: false

  tool_sets:
    basic_tool_set:
      name: "Laborer's Essential Tools"
      description: "Starting tool kit for any profession"
      price: "30 SILA"
      supply: "Unlimited"
      contents:
        - "Flint knife"
        - "Wooden mallet"
        - "Rope (10 cubits)"
        - "Carrying basket"
      quality: "Common"
      nft_eligible: false

    farmers_seed_pack:
      name: "Seasonal Seed Packet"
      description: "Enough seeds to plant a small field"
      price: "15 SILA"
      supply: "Unlimited"
      contents:
        - "Barley seeds (enough for 1/4 acre)"
        - "Onion sets"
        - "Date palm seedling"
      note: "Varies by season"
      nft_eligible: false

    fishing_starter:
      name: "Fisherman's Basics"
      description: "Everything needed to start fishing"
      price: "20 SILA"
      supply: "Unlimited"
      contents:
        - "Simple casting net"
        - "Reed fish trap"
        - "Bone hooks (10)"
        - "Line (flax fiber)"
      nft_eligible: false

  clothing_bundles:
    basic_wardrobe:
      name: "Commoner's Clothing Set"
      description: "Modest but functional attire"
      price: "15 SILA"
      supply: "Unlimited"
      contents:
        - "Wool kilt"
        - "Linen tunic"
        - "Reed sandals"
        - "Rope belt"
      protection: "Basic weather protection"
      nft_eligible: false

    cold_weather_bundle:
      name: "Northern Traveler's Gear"
      description: "For mountain or winter journeys"
      price: "35 SILA"
      supply: "Unlimited"
      contents:
        - "Wool cloak (thick)"
        - "Leather boots"
        - "Head wrap"
        - "Wool mittens"
      benefit: "+30% cold resistance"
      nft_eligible: false

  consumables:
    lamp_oil_supply:
      name: "Month's Lamp Oil"
      description: "Sesame oil for clay lamps"
      price: "8 SILA"
      supply: "Unlimited"
      provides: "30 nights of light"
      nft_eligible: false

    writing_supplies:
      name: "Scribe's Pack"
      description: "Basic writing materials"
      price: "12 SILA"
      supply: "Unlimited"
      contents:
        - "Blank clay tablets (20)"
        - "Reed stylus (5)"
        - "Water vessel"
        - "Smoothing stone"
      nft_eligible: false

    repair_materials:
      name: "Tool Maintenance Kit"
      description: "Materials to repair worn tools"
      price: "18 SILA"
      supply: "Unlimited"
      contents:
        - "Leather strips"
        - "Bitumen (waterproofing)"
        - "Wood binding resin"
        - "Sharpening stone"
      uses: "Repair 5 items"
      nft_eligible: false

  purchase_limits:
    purpose: "Prevent hoarding/resale abuse"
    daily_limit: "3 of each item type"
    weekly_limit: "10 of each item type"
    exception: "Consumables have no limit"

  value_proposition:
    for_new_players: "Get essential gear without grinding"
    for_craftsmen: "Focus crafting on sellable items, buy basics"
    for_economy: "SILA has real utility—demand stays stable"
```

### 4.6 Payment Methods Summary

```yaml
payment_summary:
  crypto_only_items:
    description: "These require ANALOG or real currency (USD via crypto)"
    items:
      - "Reincarnation Tickets (all tiers)"
      - "Land Deeds (all types)"
      - "NFT Premium Tools"
      - "NFT Legendary Weapons"
      - "Founder/Limited Edition items"
    reason: "Scarcity and real ownership require blockchain"

  sila_only_items:
    description: "These can ONLY be purchased with earned SILA"
    items:
      - "Fire Starter Kits"
      - "Ration Packs"
      - "Basic Tool Sets"
      - "Seed Packets"
      - "Clothing Bundles"
      - "Consumables"
    reason: "Essential gameplay items must be accessible to free players"

  either_currency:
    description: "These can be purchased with SILA or from player merchants"
    items:
      - "Common crafted goods"
      - "Food and beverages"
      - "Basic materials"
      - "Services"
    note: "Market prices vary; dev store provides price floor"

  transaction_flow:
    learn_the_ways: "Craft items → Earn SILA"
    spend_sila: "Buy essentials from developer store"
    value_creation: "Items bought with SILA only have value when used or traded in-game"
    nft_path: "Exceptional items → Mint to NFT with ANALOG"
```

---

## 5. Weapons Inventory

> The Sumerian military relied heavily on simple, effective, short-range bronze and copper weapons.

### 5.1 Melee Weapons

```yaml
melee_weapons:
  spears:
    description: "Primary weapon of infantry formations"
    construction: "Leaf-shaped or socketed copper/bronze heads on wooden shafts"
    variants:
      - name: "Wooden Spear"
        tip: "Fire-hardened wood"
        rarity: "Common"
        damage: "Low"
        price: "5 SILA"

      - name: "Flint-Tipped Spear"
        tip: "Knapped flint"
        rarity: "Common"
        damage: "Low-Medium"
        price: "15 SILA"

      - name: "Copper Spear"
        tip: "Cast copper head, socketed"
        rarity: "Uncommon"
        damage: "Medium"
        price: "40 SILA"

      - name: "Bronze Spear"
        tip: "Bronze head, leaf-shaped"
        rarity: "Rare"
        damage: "High"
        price: "100 SILA"
        nft_eligible: true

  battle_axes:
    description: "Essential for close combat"
    evolution: "Early polished stone heads → copper/bronze heads"
    variants:
      - name: "Stone Battle Axe"
        head: "Polished stone"
        rarity: "Common"
        damage: "Medium"
        price: "20 SILA"

      - name: "Copper Battle Axe"
        head: "Cast copper"
        rarity: "Uncommon"
        damage: "High"
        price: "60 SILA"

      - name: "Bronze Battle Axe"
        head: "Cast bronze, socketed"
        rarity: "Rare"
        damage: "Very High"
        price: "150 SILA"
        nft_eligible: true

  daggers:
    description: "Short-bladed secondary weapons or tools"
    variants:
      - name: "Flint Knife"
        blade: "Knapped flint"
        rarity: "Common"
        damage: "Low"
        price: "8 SILA"

      - name: "Copper Dagger"
        blade: "Cast copper, decorated handle"
        rarity: "Uncommon"
        damage: "Medium"
        price: "35 SILA"

      - name: "Bronze Dagger"
        blade: "Bronze, ornamental handle"
        rarity: "Rare"
        damage: "Medium-High"
        price: "80 SILA"
        nft_eligible: true

      - name: "Ceremonial Dagger"
        blade: "Gold-inlaid bronze"
        rarity: "Epic"
        damage: "Medium"
        special: "Status symbol, +reputation"
        price: "500 SILA"
        nft_eligible: true

  maces:
    description: "Status weapons for officers and temple guards"
    variants:
      - name: "Wooden Club"
        head: "Hardwood"
        rarity: "Common"
        damage: "Low"
        price: "3 SILA"

      - name: "Stone Mace"
        head: "Carved stone, wooden shaft"
        rarity: "Uncommon"
        damage: "High"
        price: "45 SILA"

      - name: "Ceremonial Mace"
        head: "Copper-bound stone"
        rarity: "Rare"
        damage: "High"
        special: "Symbol of authority"
        price: "200 SILA"
        nft_eligible: true
```

### 5.2 Ranged Weapons

```yaml
ranged_weapons:
  slingshots:
    description: "Simple but effective long-range weapons for light infantry"
    ammunition: "Clay bullets or river stones"
    variants:
      - name: "Simple Sling"
        construction: "Woven leather"
        rarity: "Common"
        range: "30m effective"
        price: "5 SILA"

      - name: "Military Sling"
        construction: "Braided leather, longer pouch"
        rarity: "Uncommon"
        range: "50m effective"
        price: "15 SILA"

    ammunition_types:
      clay_bullets:
        description: "Mass-produced, sometimes inscribed with curses"
        price: "1 SILA per 20"
      stone_projectiles:
        description: "Smooth river stones"
        price: "Free (foraged)"

  bows:
    description: "Wooden self-bows common; composite bows imported/rare"
    variants:
      - name: "Simple Self-Bow"
        construction: "Single piece of wood"
        rarity: "Uncommon"
        range: "40m effective"
        price: "25 SILA"

      - name: "Recurve Bow"
        construction: "Curved wooden bow"
        rarity: "Rare"
        range: "60m effective"
        price: "75 SILA"

      - name: "Composite Bow"
        construction: "Sinew, horn, and wood layered"
        rarity: "Epic"
        range: "100m+ effective"
        damage: "Very High"
        price: "300 SILA"
        note: "Imported from eastern lands or requires revolutionary innovation"
        nft_eligible: true

    arrows:
      flint_arrow:
        price: "2 SILA per 10"
      copper_arrow:
        price: "10 SILA per 10"
      bronze_arrow:
        price: "25 SILA per 10"
```

### 5.3 Armor & Protection

```yaml
armor:
  body_armor:
    leather_cloak:
      description: "Basic protection, leather or felt"
      rarity: "Uncommon"
      protection: "Light"
      price: "30 SILA"

    studded_cloak:
      description: "Leather/felt studded with small copper/bronze discs"
      rarity: "Rare"
      protection: "Medium"
      price: "100 SILA"
      note: "Standard military issue for trained soldiers"

    scale_armor:
      description: "Overlapping bronze scales on leather backing"
      rarity: "Epic"
      protection: "High"
      price: "400 SILA"
      note: "Officers and elite troops only"
      nft_eligible: true

  helmets:
    leather_cap:
      description: "Hardened leather head protection"
      rarity: "Uncommon"
      protection: "Light"
      price: "20 SILA"

    copper_helmet:
      description: "Beaten copper, basic design"
      rarity: "Rare"
      protection: "Medium"
      price: "80 SILA"

    golden_wig_helmet:
      description: "Elaborate helmet mimicking hair, gold or copper"
      rarity: "Legendary"
      protection: "Medium"
      special: "Extreme status symbol, like those found at Ur"
      price: "2000+ SILA"
      nft_required: true
      supply: "50 total"

  shields:
    reed_shield:
      description: "Woven reeds with leather backing"
      rarity: "Common"
      protection: "Light (directional)"
      price: "15 SILA"

    leather_shield:
      description: "Hardened leather over wooden frame"
      rarity: "Uncommon"
      protection: "Medium (directional)"
      price: "40 SILA"

    copper_faced_shield:
      description: "Wood/leather with copper sheet facing"
      rarity: "Rare"
      protection: "High (directional)"
      price: "120 SILA"
      nft_eligible: true
```

---

## 6. Tools Inventory

> Tools were predominantly made of flint, obsidian, or copper, catering to farming, construction, and craft production.

### 6.1 Agricultural Tools

```yaml
agricultural_tools:
  plows:
    description: "Heavy wooden plows for preparing fields"
    variants:
      - name: "Wooden Plow"
        construction: "Hardwood beam and share"
        rarity: "Common"
        efficiency: "Base"
        price: "25 SILA"
        requires: "Ox or donkey team"

      - name: "Stone-Tipped Plow"
        construction: "Wooden frame, stone point"
        rarity: "Uncommon"
        efficiency: "+25%"
        price: "50 SILA"

      - name: "Copper-Tipped Plow"
        construction: "Wooden frame, copper share"
        rarity: "Rare"
        efficiency: "+50%"
        price: "120 SILA"
        nft_eligible: true

  sickles:
    description: "Curved blades for harvesting barley"
    variants:
      - name: "Flint Sickle"
        construction: "Curved flint blades set into wooden handle"
        rarity: "Common"
        efficiency: "Base"
        price: "10 SILA"

      - name: "Clay Sickle"
        construction: "Fired clay blade, wooden handle"
        rarity: "Common"
        efficiency: "Base"
        price: "8 SILA"
        durability: "Low"

      - name: "Copper Sickle"
        construction: "Cast copper blade"
        rarity: "Uncommon"
        efficiency: "+30%"
        price: "35 SILA"

      - name: "Bronze Sickle"
        construction: "Bronze blade, hardwood handle"
        rarity: "Rare"
        efficiency: "+50%"
        price: "80 SILA"
        nft_eligible: true

  irrigation_tools:
    shaduf:
      description: "Water-lifting lever device"
      rarity: "Uncommon"
      function: "Lifts water from canal to field"
      price: "60 SILA"

    irrigation_basket:
      description: "For manual water carrying"
      rarity: "Common"
      price: "5 SILA"

    canal_tools:
      description: "Shovels, hoes for canal maintenance"
      rarity: "Common"
      price: "15-30 SILA"
```

### 6.2 Craftsman Tools

```yaml
craftsman_tools:
  pottery:
    potters_wheel:
      description: "Massive innovation for mass-producing pottery"
      rarity: "Uncommon"
      function: "10x faster pottery production"
      price: "100 SILA"
      note: "Requires trained skill to operate"

    kiln:
      description: "Large structure for firing pottery and bricks"
      rarity: "Rare"
      function: "Required for quality ceramics"
      price: "300 SILA"
      installation: "Fixed to workshop plot"

    forming_tools:
      description: "Paddles, ribs, cutting wires"
      rarity: "Common"
      price: "10 SILA set"

  metalworking:
    forge:
      description: "Charcoal-fired furnace for metalworking"
      rarity: "Rare"
      function: "Required for metal tools/weapons"
      price: "400 SILA"
      installation: "Fixed to workshop plot"

    crucibles:
      description: "Clay vessels for melting metal"
      rarity: "Uncommon"
      price: "15 SILA each"

    bellows:
      description: "Leather air pumps for forge"
      rarity: "Uncommon"
      price: "30 SILA"

    hammer_and_tongs:
      description: "Basic smithing tools"
      rarity: "Uncommon"
      price: "25 SILA set"

    chisels_and_razors:
      description: "Copper cutting tools"
      rarity: "Uncommon"
      price: "20 SILA set"

  woodworking:
    adzes:
      description: "Shaping tools for wood"
      rarity: "Uncommon"
      price: "20 SILA"

    gouges:
      description: "Carving tools"
      rarity: "Uncommon"
      price: "15 SILA"

    saw:
      description: "Copper-toothed saw for cutting"
      rarity: "Rare"
      price: "50 SILA"

  weaving:
    loom:
      description: "Wooden frame for textile production"
      variants:
        - name: "Simple Loom"
          rarity: "Common"
          output: "Basic"
          price: "40 SILA"
        - name: "Professional Loom"
          rarity: "Uncommon"
          output: "Quality textiles"
          price: "100 SILA"

    spindle:
      description: "For spinning wool/flax into thread"
      rarity: "Common"
      price: "5 SILA"

    combs:
      description: "For preparing wool fibers"
      rarity: "Common"
      price: "8 SILA"
```

### 6.3 Fishing Tools

```yaml
fishing_tools:
  nets:
    cast_net:
      description: "Woven net for throwing"
      rarity: "Common"
      price: "15 SILA"

    seine_net:
      description: "Large net for group fishing"
      rarity: "Uncommon"
      price: "50 SILA"
      requires: "Multiple people"

  traps:
    reed_trap:
      description: "Woven reed fish trap"
      rarity: "Common"
      price: "8 SILA"

    basket_trap:
      description: "Large wicker trap for marshes"
      rarity: "Uncommon"
      price: "20 SILA"

  boats:
    reed_bundle_raft:
      description: "Simple reed bundle boat"
      rarity: "Common"
      capacity: "1-2 people"
      price: "30 SILA"

    bitumen_sealed_boat:
      description: "Reed boat with bitumen waterproofing"
      rarity: "Uncommon"
      capacity: "3-4 people"
      price: "80 SILA"

    wooden_fishing_boat:
      description: "Planked wooden vessel"
      rarity: "Rare"
      capacity: "5-6 people"
      price: "200 SILA"
      nft_eligible: true
```

### 6.4 Fire Starting Equipment

> Starting fire from scratch was labor-intensive. Most households maintained existing embers rather than starting fresh.

```yaml
fire_starting:
  note: "Fire was precious—maintaining embers was easier than starting new fires"

  percussion_method:
    description: "Strike-a-light using natural minerals"
    how_it_works:
      - "Strike flint against iron pyrite (fool's gold)"
      - "Tiny pyrite fragments shear off and oxidize"
      - "Creates shower of low-temperature 'cold' sparks"
      - "Must land on highly flammable prepared tinder"

    fire_striker_kit:
      name: "Flint and Pyrite Fire Striker"
      contents:
        - "Flint nodule (knapped edge)"
        - "Iron pyrite chunk"
        - "Dried horse hoof fungus tinder"
        - "Fluffed plant fiber bundle"
        - "Small clay container"
      rarity: "Uncommon"
      price: "25 SILA"
      durability: "Medium (pyrite wears down)"
      skill_required: 10
      success_rate:
        novice: "40% (many attempts needed)"
        skilled: "80%"
        master: "95%"

    materials_separate:
      flint_nodule:
        price: "3 SILA"
        source: "Found in riverbeds, traded"
      iron_pyrite:
        price: "8 SILA"
        source: "Imported, rare locally"
        note: "Called 'fool's gold' for its appearance"
      prepared_tinder:
        price: "2 SILA"
        types:
          - "Dried tree fungus (horse hoof fungus)"
          - "Fluffed cattail fibers"
          - "Dried grass bundles"
          - "Charred cloth scraps"

  friction_method:
    description: "Fire drill using kinetic energy"
    how_it_works:
      - "Bow with string wrapped around vertical spindle"
      - "Saw bow back and forth"
      - "Spindle spins rapidly against wooden hearth board"
      - "Friction creates hot wood dust"
      - "Dust coalesces into glowing coal"

    bow_drill_kit:
      name: "Bow Drill Fire Set"
      contents:
        - "Small wooden bow with leather string"
        - "Hardwood spindle"
        - "Softwood hearth board"
        - "Bearing block (holds spindle top)"
        - "Tinder nest"
      rarity: "Uncommon"
      price: "20 SILA"
      durability: "Low (parts wear out quickly)"
      skill_required: 15
      effort: "High—physically demanding"
      success_rate:
        novice: "25% (exhausting, frustrating)"
        skilled: "70%"
        master: "90%"
      note: "Reserved for when primary fire has died completely"

    hand_drill_kit:
      name: "Hand Drill (Simple)"
      contents:
        - "Hardwood spindle"
        - "Softwood hearth board"
      rarity: "Common"
      price: "8 SILA"
      durability: "Very Low"
      skill_required: 20
      effort: "Very High—blisters common"
      success_rate:
        novice: "10% (extremely difficult)"
        skilled: "50%"
        master: "80%"

  fire_maintenance:
    description: "The 'Keeper of the Flame' method—most common daily practice"
    importance: "Starting fire was so labor-intensive that most households banked coals"

    banking_coals:
      description: "Cover hearth coals with thick ash layers to insulate"
      duration: "Coals stay alive 8-12 hours"
      skill_required: 5
      cost: "Free (uses existing fire)"

    ember_containers:
      clay_tinderbox:
        name: "Clay Fire Safe"
        description: "Hollow clay container for transporting embers"
        contents: "Glowing embers wrapped in fresh leaves, packed in tinder"
        duration: "Embers last 4-6 hours"
        rarity: "Common"
        price: "5 SILA"

      birch_bark_safe:
        name: "Bark Fire Carrier"
        description: "Imported birch bark container (birch rare in Sumer)"
        duration: "Embers last 6-8 hours"
        rarity: "Uncommon"
        price: "15 SILA"
        note: "Bark must be imported from northern regions"

      bronze_ember_pot:
        name: "Bronze Fire Vessel"
        description: "Metal container with ventilation holes"
        duration: "Embers last 8-12 hours"
        rarity: "Rare"
        price: "50 SILA"
        nft_eligible: true

    borrowing_fire:
      description: "Common practice—borrow a lit coal from neighbor"
      cost: "Social (favor owed)"
      note: "Refusing to share fire was considered extremely rude"

  fire_starting_services:
    temple_eternal_flame:
      description: "Temples maintained perpetual sacred fires"
      service: "Obtain blessed coal for small offering"
      cost: "1-2 SILA donation"
      benefit: "Guaranteed fire + religious blessing"

    tavern_hearth:
      description: "Taverns always had fire burning"
      service: "Take coal with drink purchase"
      cost: "Included with drink"

  gameplay_mechanics:
    fire_is_essential:
      warmth: "Required in cold/night for health"
      cooking: "Required to prepare most foods"
      crafting: "Required for pottery, metalwork, etc."
      light: "Required for nighttime activities"

    fire_death:
      consequence: "Health degrades without warmth at night"
      emergency_options:
        - "Borrow from neighbor"
        - "Go to tavern"
        - "Go to temple"
        - "Use fire starting kit (time + skill)"
```

---

## 7. Artifacts & Household Goods

> Life revolved around the mud-brick home, utilizing readily available clay.

### 7.1 Pottery & Vessels

```yaml
pottery:
  beveled_rim_bowls:
    description: "Ubiquitous, mass-produced, standardized clay bowls"
    historical_note: "Theorized to measure daily rations for workers"
    rarity: "Common"
    price: "0.5 SILA"
    uses:
      - "Ration measurement"
      - "Food serving"
      - "Currency alternative"
    supply: "Unlimited (mass-produced)"

  storage_jars:
    small_jar:
      description: "For liquids and dry goods"
      rarity: "Common"
      capacity: "5 liters"
      price: "3 SILA"

    large_storage_vessel:
      description: "For grain storage"
      rarity: "Uncommon"
      capacity: "50+ liters"
      price: "15 SILA"

    decorated_vessel:
      description: "Painted or incised pottery"
      rarity: "Rare"
      price: "50-200 SILA"
      nft_eligible: true

  specialized_vessels:
    beer_jar:
      description: "Pointed bottom for fermentation"
      rarity: "Common"
      price: "5 SILA"

    oil_jar:
      description: "Narrow neck for pouring"
      rarity: "Uncommon"
      price: "8 SILA"

    ritual_vessel:
      description: "Temple use, fine craftsmanship"
      rarity: "Epic"
      price: "100-500 SILA"
      nft_eligible: true
```

### 7.2 Writing & Administration

```yaml
writing_materials:
  cylinder_seals:
    description: "Small stone cylinders rolled over wet clay as signatures"
    importance: "Crucial for identifying ownership of goods and documents"
    variants:
      - name: "Simple Cylinder Seal"
        material: "Common stone"
        rarity: "Uncommon"
        price: "50 SILA"

      - name: "Personal Cylinder Seal"
        material: "Quality stone, unique design"
        rarity: "Rare"
        price: "200 SILA"
        function: "Personal signature, identity"
        nft_eligible: true

      - name: "Master Cylinder Seal"
        material: "Lapis lazuli, gold caps"
        rarity: "Epic"
        price: "1000+ SILA"
        function: "High official/merchant signature"
        nft_eligible: true

      - name: "Royal/Temple Seal"
        material: "Precious materials, divine imagery"
        rarity: "Legendary"
        price: "5000+ SILA"
        nft_required: true
        supply: "Limited (10 per city)"

  clay_tablets:
    description: "Primary medium for cuneiform records"
    types:
      blank_tablet:
        price: "0.5 SILA"
        rarity: "Common"

      administrative_record:
        description: "Receipts, inventories, worker lists"
        rarity: "Common"
        value: "Depends on content"

      contract_tablet:
        description: "Legal agreements"
        rarity: "Uncommon"
        function: "Legally binding"
        price: "5-20 SILA (scribe fee)"

      literary_tablet:
        description: "Myths, hymns, wisdom texts"
        rarity: "Rare"
        price: "50-500 SILA"
        nft_eligible: true

  stylus:
    description: "Reed writing implement for cuneiform"
    rarity: "Common"
    price: "1 SILA"
```

### 7.3 Household Items

```yaml
household_goods:
  reed_mats:
    description: "Used for flooring, sleeping, and constructing mudhifs"
    variants:
      - name: "Simple Reed Mat"
        rarity: "Common"
        price: "2 SILA"

      - name: "Woven Sleeping Mat"
        rarity: "Common"
        price: "5 SILA"

      - name: "Decorated Mat"
        rarity: "Uncommon"
        price: "15 SILA"

  furniture:
    wooden_stool:
      rarity: "Uncommon"
      price: "20 SILA"

    wooden_table:
      rarity: "Uncommon"
      price: "30 SILA"

    bed_frame:
      rarity: "Rare"
      price: "75 SILA"

    storage_chest:
      rarity: "Uncommon"
      price: "40 SILA"

    chair_with_back:
      description: "Status item"
      rarity: "Rare"
      price: "100 SILA"

  lighting:
    clay_oil_lamp:
      rarity: "Common"
      price: "3 SILA"

    bronze_lamp:
      rarity: "Rare"
      price: "50 SILA"
```

### 7.4 Musical Instruments

```yaml
musical_instruments:
  lyres:
    description: "Elaborate stringed instruments"
    variants:
      - name: "Simple Lyre"
        construction: "Wood, gut strings"
        rarity: "Rare"
        price: "100 SILA"

      - name: "Decorated Lyre"
        construction: "Wood with inlay"
        rarity: "Epic"
        price: "500 SILA"
        nft_eligible: true

      - name: "Bull-Head Lyre"
        construction: "Gold and lapis lazuli bull head"
        rarity: "Legendary"
        price: "5000+ SILA"
        historical_note: "Like those found in Royal Tombs of Ur"
        nft_required: true
        supply: "5 total"

  harps:
    simple_harp:
      rarity: "Rare"
      price: "80 SILA"

    temple_harp:
      rarity: "Epic"
      price: "400 SILA"
      nft_eligible: true

  drums:
    frame_drum:
      rarity: "Common"
      price: "15 SILA"

    ceremonial_drum:
      rarity: "Rare"
      price: "100 SILA"

  wind_instruments:
    reed_pipe:
      rarity: "Common"
      price: "5 SILA"

    double_pipe:
      rarity: "Uncommon"
      price: "20 SILA"
```

---

## 8. Jewelry Inventory

> Jewelry indicated wealth and status, using rare, highly valued imported materials not found locally.

### 8.1 Imported Materials

```yaml
jewelry_materials:
  note: "All precious materials are imported from distant lands"

  lapis_lazuli:
    source: "Afghanistan (Badakhshan)"
    color: "Deep blue"
    value: "Extremely high"
    uses: "Beads, inlay, cylinder seals"

  carnelian:
    source: "Indus Valley (Meluhha)"
    color: "Red-orange"
    value: "High"
    uses: "Beads, pendants"

  gold:
    source: "Egypt, Asia Minor"
    value: "Highest"
    uses: "All fine jewelry"

  silver:
    source: "Asia Minor (Anatolia)"
    value: "Very high"
    uses: "Jewelry, currency"

  agate:
    source: "Various"
    value: "Medium-high"
    uses: "Beads"

  shell:
    source: "Persian Gulf, Red Sea"
    value: "Low-medium"
    uses: "Beads, inlay"
```

### 8.2 Jewelry Types

```yaml
jewelry_items:
  headdresses:
    description: "Intricate gold leaf and ribbon arrangements"
    worn_by: "Noblewomen for formal occasions or burial"
    variants:
      - name: "Simple Hair Ribbon"
        material: "Woven gold thread"
        rarity: "Rare"
        price: "200 SILA"

      - name: "Gold Leaf Headdress"
        material: "Beaten gold leaves"
        rarity: "Epic"
        price: "1000 SILA"
        nft_eligible: true

      - name: "Royal Headdress"
        material: "Gold, lapis, carnelian"
        rarity: "Legendary"
        price: "5000+ SILA"
        historical_note: "Like Queen Puabi's headdress"
        nft_required: true
        supply: "3 total"

  necklaces:
    description: "Multi-layered strands of beads"
    variants:
      - name: "Shell Bead Necklace"
        rarity: "Common"
        price: "10 SILA"

      - name: "Carnelian Bead Necklace"
        rarity: "Rare"
        price: "100 SILA"
        nft_eligible: true

      - name: "Lapis Lazuli Necklace"
        rarity: "Epic"
        price: "300 SILA"
        nft_eligible: true

      - name: "Gold and Lapis Collar"
        rarity: "Legendary"
        price: "2000+ SILA"
        nft_required: true
        supply: "20 total"

  earrings:
    description: "Large, elaborate designs popular among elite"
    variants:
      - name: "Copper Earrings"
        rarity: "Uncommon"
        price: "15 SILA"

      - name: "Silver Earrings"
        rarity: "Rare"
        price: "80 SILA"

      - name: "Gold Crescent Earrings"
        description: "Large crescent-shaped"
        rarity: "Epic"
        price: "400 SILA"
        nft_eligible: true

  bracelets:
    description: "Metal bands or beaded strands"
    variants:
      - name: "Copper Bracelet"
        rarity: "Uncommon"
        price: "20 SILA"

      - name: "Silver Bracelet"
        rarity: "Rare"
        price: "100 SILA"

      - name: "Gold Bracelet"
        rarity: "Epic"
        price: "500 SILA"
        nft_eligible: true

      - name: "Beaded Ankle Bracelet"
        rarity: "Uncommon"
        price: "25 SILA"

  rings:
    description: "Finger rings of various metals"
    variants:
      - name: "Copper Ring"
        rarity: "Common"
        price: "5 SILA"

      - name: "Bronze Ring"
        rarity: "Uncommon"
        price: "15 SILA"

      - name: "Silver Ring"
        rarity: "Rare"
        price: "60 SILA"

      - name: "Gold Ring"
        rarity: "Epic"
        price: "250 SILA"
        nft_eligible: true

      - name: "Signet Ring"
        description: "With personal seal"
        rarity: "Epic"
        price: "400 SILA"
        nft_eligible: true

  pins:
    description: "Used to fasten clothing, often with cylinder seal holders"
    variants:
      - name: "Copper Cloak Pin"
        rarity: "Common"
        price: "8 SILA"

      - name: "Bronze Pin with Ornament"
        rarity: "Uncommon"
        price: "25 SILA"

      - name: "Gold Pin with Seal"
        rarity: "Epic"
        price: "300 SILA"
        function: "Holds cylinder seal"
        nft_eligible: true
```

---

## 9. Craftable Items

Items players can create through gameplay.

### 9.1 Tools by Profession

```yaml
craftable_tools:
  farming:
    items:
      - name: "Flint sickle"
        materials: "Flint, wood handle, leather binding"
        skill_required: 5
        rarity: "Common"

      - name: "Copper sickle"
        materials: "Copper blade, wood handle"
        skill_required: 20
        rarity: "Uncommon"

      - name: "Bronze sickle"
        materials: "Bronze blade, hardwood handle"
        skill_required: 50
        rarity: "Rare"

      - name: "Irrigation tool set"
        materials: "Wood, copper, leather"
        skill_required: 30
        rarity: "Uncommon"

  fishing:
    items:
      - name: "Reed fishing trap"
        materials: "Reeds, rope"
        skill_required: 5
        rarity: "Common"

      - name: "Woven net"
        materials: "Flax fiber, weights"
        skill_required: 15
        rarity: "Uncommon"

      - name: "Fishing boat"
        materials: "Reeds, bitumen, rope"
        skill_required: 40
        rarity: "Rare"
        note: "Requires boat builder skill"

  pottery:
    items:
      - name: "Storage jar"
        materials: "Clay"
        skill_required: 10
        rarity: "Common"

      - name: "Decorated vessel"
        materials: "Clay, pigments"
        skill_required: 30
        rarity: "Uncommon"

      - name: "Ritual vessel"
        materials: "Fine clay, gold leaf"
        skill_required: 60
        rarity: "Rare"

  weaving:
    items:
      - name: "Basic loom"
        materials: "Wood, rope"
        skill_required: 15
        rarity: "Common"

      - name: "Wool cloth"
        materials: "Wool yarn"
        skill_required: 10
        rarity: "Common"

      - name: "Linen cloth"
        materials: "Flax fiber"
        skill_required: 25
        rarity: "Uncommon"

      - name: "Embroidered textile"
        materials: "Cloth, colored thread"
        skill_required: 50
        rarity: "Rare"

  metallurgy:
    items:
      - name: "Copper ingot"
        materials: "Copper ore, charcoal"
        skill_required: 20
        rarity: "Uncommon"

      - name: "Bronze ingot"
        materials: "Copper, tin ore"
        skill_required: 40
        rarity: "Rare"

      - name: "Copper dagger"
        materials: "Copper ingot, wood"
        skill_required: 30
        rarity: "Uncommon"

      - name: "Bronze sword"
        materials: "Bronze ingot, leather"
        skill_required: 60
        rarity: "Rare"

      - name: "Gold jewelry piece"
        materials: "Gold, gems"
        skill_required: 70
        rarity: "Epic"
```

### 9.2 Weapons

```yaml
craftable_weapons:
  melee:
    - name: "Wooden club"
      materials: "Hardwood"
      skill: 5
      damage: "Low"
      rarity: "Common"

    - name: "Flint knife"
      materials: "Flint, leather grip"
      skill: 10
      damage: "Low-Medium"
      rarity: "Common"

    - name: "Copper dagger"
      materials: "Copper, wood/bone handle"
      skill: 25
      damage: "Medium"
      rarity: "Uncommon"

    - name: "Copper spear"
      materials: "Copper point, wood shaft"
      skill: 30
      damage: "Medium-High"
      rarity: "Uncommon"

    - name: "Bronze sword"
      materials: "Bronze blade, leather grip"
      skill: 55
      damage: "High"
      rarity: "Rare"

    - name: "Ceremonial mace"
      materials: "Stone head, copper binding, wood"
      skill: 45
      damage: "High"
      rarity: "Rare"
      note: "Status weapon"

  ranged:
    - name: "Sling"
      materials: "Leather, rope"
      skill: 5
      damage: "Low"
      rarity: "Common"

    - name: "Simple bow"
      materials: "Wood, sinew string"
      skill: 20
      damage: "Medium"
      rarity: "Uncommon"

    - name: "Throwing spear"
      materials: "Wood, flint/copper point"
      skill: 15
      damage: "Medium"
      rarity: "Common"

  armor:
    - name: "Leather vest"
      materials: "Tanned leather"
      skill: 20
      protection: "Light"
      rarity: "Uncommon"

    - name: "Studded leather"
      materials: "Leather, copper studs"
      skill: 35
      protection: "Medium"
      rarity: "Rare"

    - name: "Reed shield"
      materials: "Reeds, leather binding"
      skill: 15
      protection: "Light (directional)"
      rarity: "Common"

    - name: "Copper-faced shield"
      materials: "Wood, copper sheet, leather"
      skill: 40
      protection: "Medium (directional)"
      rarity: "Rare"
```

### 9.3 Clothing

```yaml
craftable_clothing:
  basic:
    - name: "Wool kilt"
      materials: "Wool cloth"
      skill: 10
      rarity: "Common"

    - name: "Linen tunic"
      materials: "Linen cloth"
      skill: 20
      rarity: "Uncommon"

    - name: "Leather sandals"
      materials: "Leather"
      skill: 15
      rarity: "Uncommon"

  quality:
    - name: "Embroidered robe"
      materials: "Fine linen, colored thread"
      skill: 45
      rarity: "Rare"

    - name: "Priest vestments"
      materials: "Fine linen, wool trim, dyes"
      skill: 55
      rarity: "Rare"
      requirement: "Temple commission"

    - name: "Merchant outfit"
      materials: "Quality wool, leather belt"
      skill: 35
      rarity: "Uncommon"

  accessories:
    - name: "Wool cap"
      materials: "Wool"
      skill: 10
      rarity: "Common"

    - name: "Leather belt"
      materials: "Leather, copper buckle"
      skill: 20
      rarity: "Uncommon"

    - name: "Woven sash"
      materials: "Colored wool/linen"
      skill: 25
      rarity: "Uncommon"
```

### 9.4 Jewelry

```yaml
craftable_jewelry:
  beads:
    - name: "Clay beads"
      materials: "Painted clay"
      skill: 10
      rarity: "Common"
      value: "5 SILA"

    - name: "Carnelian beads"
      materials: "Carnelian stones"
      skill: 35
      rarity: "Rare"
      value: "50-100 SILA"

    - name: "Lapis lazuli beads"
      materials: "Lapis lazuli"
      skill: 40
      rarity: "Rare"
      value: "100-200 SILA"

  metalwork:
    - name: "Copper bracelet"
      materials: "Copper"
      skill: 25
      rarity: "Uncommon"
      value: "20-40 SILA"

    - name: "Silver ring"
      materials: "Silver"
      skill: 45
      rarity: "Rare"
      value: "100-200 SILA"

    - name: "Gold earrings"
      materials: "Gold"
      skill: 60
      rarity: "Epic"
      value: "500-1000 SILA"

    - name: "Gold collar necklace"
      materials: "Gold, gems"
      skill: 75
      rarity: "Legendary"
      value: "2000+ SILA"

  seals:
    - name: "Personal cylinder seal"
      materials: "Stone, copper"
      skill: 50
      rarity: "Rare"
      value: "200-500 SILA"
      note: "Unique to owner, signature item"

    - name: "Master cylinder seal"
      materials: "Lapis lazuli, gold caps"
      skill: 80
      rarity: "Epic"
      value: "1000+ SILA"
```

---

## 10. "Learn the Ways" Crafting System

> Players who learn to craft their own items instead of buying receive token rewards. Knowledge is power.

### 10.1 Core Philosophy

```yaml
learn_the_ways:
  principle: "Knowledge rewards those who seek it"

  concept:
    description: |
      Instead of buying tools from merchants, players can:
      1. Find the specifications (blueprints/recipes)
      2. Source the raw materials
      3. Negotiate with community members for help
      4. Craft the item themselves

    rewards:
      - "Get the tool/item for FREE (materials cost only)"
      - "Earn SILA tokens for completing the learning process"
      - "Gain permanent knowledge (can craft again anytime)"
      - "Higher crafting skill over time"

  why_this_matters:
    for_gameplay: "Creates exploration, social interaction, skill progression"
    for_training_data: "Captures human problem-solving, negotiation, learning"
    for_economy: "Multiple paths to acquire items—not just purchase"
```

### 10.2 The Learning Process

```yaml
learning_process:
  step_1_find_specifications:
    description: "Discover how the item is made"
    sources:
      elder_knowledge:
        how: "Ask elderly NPCs or players about traditional methods"
        cost: "Time + social reputation"
        example: "The old potter knows how to make a kiln..."

      observation:
        how: "Watch craftsmen work, study their techniques"
        cost: "Time + sometimes permission"
        example: "Spend 3 days apprenticing with the blacksmith"

      written_records:
        how: "Find clay tablets with craft instructions"
        cost: "Exploration + reading skill"
        example: "Ancient tablet describes bronze alloy ratios"

      experimentation:
        how: "Trial and error (historically accurate)"
        cost: "Materials + time + failures"
        example: "Your first 5 pots crack in the kiln..."

      trade_secrets:
        how: "Negotiate with master craftsmen"
        cost: "Significant payment or favor"
        example: "The smith will teach you for 50 SILA or a month of labor"

  step_2_source_materials:
    description: "Gather all required components"
    methods:
      forage:
        description: "Find in the wild"
        items: "Clay, reeds, flint, wood, fibers"
        cost: "Time + knowledge of where to look"

      mine_extract:
        description: "Extract from deposits"
        items: "Copper ore, stone, bitumen"
        cost: "Tools + labor + access to site"

      trade:
        description: "Purchase or barter from others"
        items: "Metals, rare materials, imports"
        cost: "SILA or trade goods"

      process:
        description: "Transform raw into usable"
        examples:
          - "Smelt ore into copper"
          - "Spin fiber into thread"
          - "Tan hides into leather"

  step_3_community_negotiation:
    description: "Get help from others when needed"
    scenarios:
      borrow_tools:
        example: "Need a kiln? Negotiate with potter to use theirs"
        payment: "SILA, labor, or share of output"

      hire_expertise:
        example: "Need metalwork? Pay a smith to assist"
        payment: "Wages or apprenticeship agreement"

      cooperative_crafting:
        example: "Pool resources with other players"
        structure: "Share costs, share output"

      guild_access:
        example: "Join a craft guild for facilities"
        requirements: "Dues, labor, loyalty"

  step_4_crafting:
    description: "Actually make the item"
    factors:
      skill_level: "Affects quality and success rate"
      tool_quality: "Better tools = better results"
      material_quality: "Better inputs = better outputs"
      time_invested: "Rushing = lower quality"
      guidance: "Help from experts improves odds"
```

### 10.3 SILA Token Rewards

```yaml
crafting_rewards:
  principle: "Learning earns tokens; buying does not"

  reward_structure:
    first_time_craft:
      description: "First time you successfully craft an item type"
      base_reward: "Item's shop price × 0.5 in SILA"
      examples:
        flint_sickle:
          shop_price: "10 SILA"
          first_craft_reward: "5 SILA"
        copper_dagger:
          shop_price: "35 SILA"
          first_craft_reward: "17 SILA"
        bronze_spear:
          shop_price: "100 SILA"
          first_craft_reward: "50 SILA"
        fire_striker_kit:
          shop_price: "25 SILA"
          first_craft_reward: "12 SILA"

    learning_milestones:
      description: "Bonus rewards for acquiring knowledge"
      spec_discovered:
        reward: "5-20 SILA (based on item complexity)"
        note: "Awarded when you find/learn the recipe"

      material_mastery:
        reward: "10 SILA per new material source discovered"
        example: "Finding a clay deposit = 10 SILA"

      technique_learned:
        reward: "15-50 SILA for mastering a technique"
        examples:
          - "Fire starting: 15 SILA"
          - "Pottery wheel: 25 SILA"
          - "Bronze smelting: 50 SILA"

    quality_bonuses:
      description: "Exceptional crafts earn extra"
      good_quality: "+10% bonus SILA"
      excellent_quality: "+25% bonus SILA"
      masterwork: "+50% bonus SILA + reputation"

    teaching_rewards:
      description: "Earn SILA for teaching others"
      teach_another_player:
        reward: "10% of their first-craft reward"
        note: "Passive income from your knowledge"

  sila_usage:
    where_sila_can_be_spent:
      developer_store:
        description: "Official items sold by Mault"
        items:
          - "Fire Starter Kits"
          - "Basic tool sets"
          - "Seed packets"
          - "Clothing bundles"
          - "Consumables"
        note: "SILA only—not ANALOG"

      npc_merchants:
        description: "Buy from in-game NPCs"
        items: "Common and uncommon goods"

      player_merchants:
        description: "Trade with other players"
        items: "Anything they're selling"

      services:
        description: "Pay for services"
        examples:
          - "Scribe services"
          - "Healing"
          - "Tool rental"
          - "Workshop access"

    what_sila_cannot_buy:
      - "Land deeds (ANALOG/crypto only)"
      - "NFT items (ANALOG required)"
      - "Legendary official items (crypto only)"
      - "Reincarnation tickets (crypto only)"
```

### 10.4 Example: Learning to Make Fire

```yaml
fire_making_example:
  scenario: "New player wants to start their own fires"

  option_a_buy:
    action: "Purchase fire striker kit from merchant"
    cost: "25 SILA"
    result: "Have kit immediately"
    sila_reward: "0"
    knowledge_gained: "None (can use kit, but not make one)"

  option_b_learn_the_ways:
    step_1:
      action: "Ask elder about fire-starting methods"
      time: "1 hour conversation"
      result: "Learn about flint/pyrite method"
      sila_reward: "15 SILA (technique learned)"

    step_2:
      action: "Find flint in riverbed"
      time: "2-3 hours searching"
      result: "Obtain flint nodule"
      sila_reward: "10 SILA (material source discovered)"

    step_3:
      action: "Trade with merchant for iron pyrite"
      cost: "8 SILA (or barter goods)"
      result: "Obtain pyrite"

    step_4:
      action: "Gather tinder materials (cattails, dried fungus)"
      time: "1 hour foraging"
      result: "Prepared tinder bundle"

    step_5:
      action: "Assemble kit with help from potter (clay container)"
      negotiation: "Offer to help carry clay in exchange"
      result: "Complete fire striker kit"
      sila_reward: "12 SILA (first craft bonus)"

    totals:
      time_invested: "~5 hours gameplay"
      sila_spent: "8 SILA (pyrite)"
      sila_earned: "37 SILA"
      net_gain: "+29 SILA AND free fire kit"
      knowledge: "Can now craft fire kits anytime"

  comparison:
    buying: "Costs 25 SILA, instant, no knowledge"
    learning: "Earns 29 SILA, takes time, permanent knowledge"
    conclusion: "Learning is always more valuable long-term"
```

### 10.5 Knowledge Persistence

```yaml
knowledge_system:
  learned_recipes:
    description: "Once learned, always known"
    storage: "Saved to character permanently"
    transfer: "Knowledge carries to new incarnations"
    value: "Most valuable character asset"

  knowledge_tiers:
    novice:
      description: "Know the basic method"
      quality_cap: "Common items only"
      success_rate: "Variable"

    journeyman:
      description: "Consistent technique"
      quality_cap: "Up to Uncommon"
      success_rate: "Good"

    expert:
      description: "Refined methods"
      quality_cap: "Up to Rare"
      success_rate: "High"

    master:
      description: "Peak skill"
      quality_cap: "Up to Epic"
      success_rate: "Very High"
      special: "Can teach others, create innovations"

  knowledge_trading:
    can_teach: "Players can teach other players"
    cannot_sell: "Knowledge itself isn't an item"
    benefit: "Teacher earns SILA when student succeeds"
```

---

## 11. Loot & Found Items

Items discovered through exploration and gameplay.

### 11.1 Environmental Finds

```yaml
found_items:
  wilderness:
    common:
      - "Edible plants"
      - "Flint stones"
      - "Bird eggs"
      - "Reed bundles"
      - "Clay deposits"
    uncommon:
      - "Obsidian fragments"
      - "Turtle shells"
      - "Medicinal herbs"
      - "Wild honey"
    rare:
      - "Gold nugget (river)"
      - "Lapis lazuli rough"
      - "Ancient bones"
      - "Meteor fragment"

  ruins:
    common:
      - "Pottery shards"
      - "Broken tools"
      - "Clay tablets (damaged)"
    uncommon:
      - "Intact pottery"
      - "Copper items (corroded)"
      - "Textile fragments"
    rare:
      - "Jewelry piece"
      - "Readable tablet"
      - "Intact weapon"
    legendary:
      - "Ancient heirloom"
      - "Lost innovation blueprint"
      - "Royal artifact"

  water:
    common:
      - "Fish"
      - "Shells"
      - "Reeds"
    uncommon:
      - "Large fish"
      - "Pearls (river)"
      - "Bitumen deposits"
    rare:
      - "Sunken cargo"
      - "Ancient jewelry"
```

### 11.2 Hunting & Animal Products

```yaml
animal_products:
  from_hunting:
    gazelle:
      - "Meat (8-12 portions)"
      - "Hide (1)"
      - "Bones"
      - "Horns (uncommon)"

    wild_boar:
      - "Meat (15-20 portions)"
      - "Hide (1, thick)"
      - "Tusks (rare, valuable)"

    wild_onager:
      - "Meat (20-25 portions)"
      - "Hide (1, large)"
      - "Bones (tool material)"

    lion:
      - "Meat (10 portions, tough)"
      - "Pelt (rare, very valuable)"
      - "Teeth (trophy)"
      - "Claws (trophy)"
      note: "Extremely dangerous, high prestige"

    birds:
      - "Meat (2-4 portions)"
      - "Feathers"
      - "Eggs (if nest found)"

  from_livestock:
    sheep:
      - "Wool (regular shearing)"
      - "Milk"
      - "Meat (if slaughtered)"
      - "Hide"

    goat:
      - "Milk"
      - "Hair (for rope/cloth)"
      - "Meat (if slaughtered)"
      - "Hide"

    cattle:
      - "Milk"
      - "Meat (large quantity)"
      - "Hide (large, valuable)"
      - "Bones"
      - "Horn"
      - "Dung (fuel, building material)"
```

### 11.3 Quest Rewards

```yaml
quest_rewards:
  temple_quests:
    minor:
      - "SILA (10-50)"
      - "Food rations"
      - "Common item"
      - "Reputation increase"

    major:
      - "SILA (100-500)"
      - "Rare item"
      - "Temple blessing (buff)"
      - "Access to restricted areas"

    legendary:
      - "SILA (1000+)"
      - "Epic/Legendary item"
      - "Land grant"
      - "Divine favor (permanent)"

  community_quests:
    - "Building materials"
    - "Tool rewards"
    - "Community reputation"
    - "Shared resources"

  innovation_quests:
    - "Blueprint NFT"
    - "ANALOG tokens"
    - "Legacy points"
    - "Unique crafting recipe"
```

---

## 12. Land & Property

### 12.1 Property Types

```yaml
property_types:
  city_residential:
    description: "Living space within city walls"
    features:
      - "Build house"
      - "Family residence"
      - "Small storage"
    can_build:
      - "Reed hut"
      - "Mud brick house"
      - "Multi-room home"
    rental_use: "Housing for other players"

  city_commercial:
    description: "Business location"
    features:
      - "Storefront"
      - "Workshop space"
      - "Customer access"
    can_build:
      - "Market stall"
      - "Shop"
      - "Tavern/food service"
    rental_use: "Business rental"

  farm_land:
    description: "Agricultural plot outside city"
    features:
      - "Crop cultivation"
      - "Animal grazing"
      - "Storage structures"
    can_build:
      - "Field irrigation"
      - "Storage shed"
      - "Simple dwelling"
    rental_use: "Sharecropping"

  workshop_plot:
    description: "Industrial/craft production space"
    features:
      - "Heavy craft allowed"
      - "Fire/kiln permitted"
      - "Noise tolerance"
    can_build:
      - "Pottery kiln"
      - "Metal forge"
      - "Large loom"
      - "Brewery"
    rental_use: "Workshop rental"
```

### 12.2 Property Improvements

```yaml
property_improvements:
  residential:
    basic:
      - name: "Reed hut"
        cost: "50 SILA"
        capacity: "2 people"
        durability: "Low (needs maintenance)"

      - name: "Mud brick house"
        cost: "200 SILA"
        capacity: "4-6 people"
        durability: "Medium"

    advanced:
      - name: "Courtyard house"
        cost: "500 SILA"
        capacity: "8-10 people"
        durability: "High"
        features: "Private courtyard, multiple rooms"

      - name: "Two-story house"
        cost: "1000 SILA"
        capacity: "10+ people"
        durability: "High"
        features: "Storage, servant quarters"

  commercial:
    - name: "Market stall"
      cost: "30 SILA"
      function: "Basic selling"

    - name: "Shop building"
      cost: "200 SILA"
      function: "Enclosed store, storage"

    - name: "Tavern"
      cost: "400 SILA"
      function: "Drink service, social hub"
      requires: "Tavern license plot"

  agricultural:
    - name: "Irrigation canal"
      cost: "100 SILA"
      function: "+50% crop yield"

    - name: "Storage barn"
      cost: "150 SILA"
      function: "Crop storage, animal shelter"

    - name: "Granary"
      cost: "300 SILA"
      function: "Large storage, pest protection"

  industrial:
    - name: "Pottery kiln"
      cost: "200 SILA"
      function: "Fire pottery, higher quality"

    - name: "Metal forge"
      cost: "400 SILA"
      function: "Smelt ore, forge metal"

    - name: "Large loom"
      cost: "150 SILA"
      function: "Textile production, higher output"
```

### 12.3 Land Rental System

```yaml
land_rental:
  description: "All land can be rented to other players for passive income"

  rental_types:
    short_term:
      duration: "1 day to 1 week"
      payment: "SILA only"
      use_case: "Travelers, temporary workers"

    long_term:
      duration: "1 month to 1 year"
      payment: "SILA or ANALOG"
      use_case: "Established businesses, farmers"

    permanent_lease:
      duration: "Indefinite (can be canceled)"
      payment: "ANALOG (monthly)"
      use_case: "Major investments"

  rental_mechanics:
    owner_sets_terms:
      - "Price per period"
      - "Acceptable uses"
      - "Minimum rental duration"
      - "Deposit requirements"

    tenant_rights:
      - "Use of land during rental"
      - "Keep improvements (unless specified)"
      - "Right to renew (if terms met)"

    owner_rights:
      - "Collect rent automatically"
      - "Evict for non-payment"
      - "Reclaim after lease expires"
      - "Take percentage of tenant profits (optional)"

  passive_income_example:
    scenario: "Player owns 3 city commercial plots"
    rental_rate: "50 SILA/month each"
    monthly_income: "150 SILA"
    annual_income: "1,800 SILA"
    note: "Income continues even when player is offline"

  npc_tenant_option:
    description: "If no player rents, NPCs can be assigned"
    npc_rental_rate: "70% of player rate"
    benefit: "Guaranteed income, no vacancies"
    drawback: "Lower income than player tenants"
```

---

## 13. City Store Distribution

> Of the 500 city plots in Eridu, stores are distributed by type to create a realistic marketplace.

### 13.1 Fixed Store Allocations

```yaml
city_store_distribution:
  total_commercial_plots: 150  # Out of 500 city plots

  store_types:
    pottery_shops:
      count: 25
      sells:
        - "Beveled-rim bowls"
        - "Storage jars"
        - "Decorated vessels"
        - "Ritual vessels"
      always_stocked: true
      owner_type: "Player or NPC"

    weapons_armory:
      count: 10
      sells:
        - "Spears"
        - "Daggers"
        - "Battle axes"
        - "Armor"
        - "Shields"
      always_stocked: true
      note: "Regulated by temple/palace"

    jewelry_shops:
      count: 8
      sells:
        - "Necklaces"
        - "Earrings"
        - "Bracelets"
        - "Rings"
        - "Cylinder seals"
      luxury: true
      owner_type: "Wealthy players"

    textile_merchants:
      count: 20
      sells:
        - "Wool cloth"
        - "Linen"
        - "Clothing"
        - "Reed mats"
      always_stocked: true

    food_vendors:
      count: 30
      sells:
        - "Bread"
        - "Beer"
        - "Fish"
        - "Dates"
        - "Vegetables"
      perishable: true
      high_turnover: true

    tool_shops:
      count: 15
      sells:
        - "Farming tools"
        - "Craftsman tools"
        - "Fishing equipment"
      always_stocked: true

    metal_merchants:
      count: 8
      sells:
        - "Copper ingots"
        - "Bronze"
        - "Metal tools"
        - "Imported metals"
      import_dependent: true

    wood_timber:
      count: 5
      sells:
        - "Imported timber"
        - "Wooden items"
        - "Construction materials"
      rare: true
      import_only: true

    luxury_imports:
      count: 5
      sells:
        - "Lapis lazuli"
        - "Carnelian"
        - "Gold"
        - "Ivory"
        - "Exotic goods"
      very_expensive: true
      rare_stock: true

    taverns:
      count: 12
      sells:
        - "Beer"
        - "Wine (imported)"
        - "Food"
        - "Entertainment"
      social_hub: true
      information_exchange: true

    scribe_services:
      count: 6
      sells:
        - "Contract writing"
        - "Administrative records"
        - "Clay tablets"
        - "Cylinder seal engraving"
      professional_service: true

    general_merchants:
      count: 6
      sells:
        - "Mixed goods"
        - "Traded items"
        - "Secondhand goods"
      variety: true
```

### 13.2 Temple & Palace Stores

```yaml
temple_stores:
  ziggurat_of_enki:
    description: "Massive warehouse and redistribution center—city's largest 'store'"
    functions:
      - "Grain storage and distribution"
      - "Wool collection and processing"
      - "Ration distribution to workers"
      - "Temple goods exchange"

    what_temple_sells:
      - "Blessed items"
      - "Ritual vessels"
      - "Temple surplus grain"
      - "Wool and textiles"
      - "Beer rations"

    what_temple_buys:
      - "Offerings"
      - "Tithes (grain, livestock)"
      - "Craft goods for temple use"
      - "Labor (work for rations)"

    player_interaction:
      can_sell_to_temple: true
      can_buy_from_temple: true
      fixed_prices: true
      note: "Temple is always available—price floor/ceiling"

  palace_stores:
    description: "Royal warehouses for military and administration"
    sells:
      - "Military equipment"
      - "Quality textiles"
      - "Imported luxury goods"
    restricted: "Must have status/permission"
```

### 13.3 Import/Export Goods

```yaml
trade_goods:
  eridu_exports:
    description: "What Eridu produces and sells"
    goods:
      agricultural:
        - "Barley and grain"
        - "Dates"
        - "Onions, herbs, spices"
      manufactured:
        - "Wool textiles (major industry)"
        - "Leather products"
        - "Beer"
        - "Mass-produced ceramics"
      fish_products:
        - "Dried fish"
        - "Palm/vegetable oils"

  imported_goods:
    description: "What merchants bring in from distant lands"
    precious:
      gold_silver:
        source: "Egypt, Asia Minor"
        price: "Very high"
      lapis_lazuli:
        source: "Afghanistan (Badakhshan)"
        price: "Extremely high"
      carnelian_ivory:
        source: "Indus Valley (Meluhha)"
        price: "High"
      gemstones_pearls:
        source: "Various"
        price: "High"

    metals:
      copper:
        source: "Anatolia (Turkey)"
        essential: true
        price: "High"
      tin:
        source: "Iran, Afghanistan"
        essential: "For bronze"
        price: "Very high"

    building_materials:
      timber:
        source: "Levant/Lebanon, Elam"
        essential: "No local trees"
        price: "High"

    other:
      slaves:
        source: "War captives, debt"
        price: "Variable"
      wine:
        source: "Northern regions"
        luxury: true
      obsidian:
        source: "Anatolia"
        use: "Tools"
```

---

## 14. Marketplace & Trading

> Vibrant marketplaces were dynamic social hubs where merchants, pilgrims, and locals gathered.

### 14.1 Marketplace Structure

```yaml
marketplace:
  types:
    main_market:
      location: "Central market district"
      description: "Primary trading hub"
      features:
        - "Permanent stall spaces"
        - "Daily trading hours"
        - "Temple oversight"
        - "Weight/measure standards"

    harbor_market:
      location: "River docks"
      description: "Import/export trading"
      features:
        - "Ship arrivals = excitement"
        - "Rare goods available"
        - "Merchant caravan access"

    temple_market:
      location: "Outside ziggurat"
      description: "Religious goods, offerings"
      features:
        - "Ritual items"
        - "Votive statues"
        - "Blessed goods"

  trading_hours:
    dawn: "Market opens, freshest goods"
    midday: "Peak activity"
    afternoon: "Bargains on perishables"
    dusk: "Market closes"

  social_functions:
    - "News and gossip exchange"
    - "Business negotiations"
    - "Meeting place"
    - "Entertainment (musicians, storytellers)"
```

### 14.2 Merchant Types

```yaml
merchant_types:
  local_vendors:
    description: "City residents selling own goods"
    operates: "Fixed stall or shop"
    inventory: "Local products"
    always_present: true

  caravan_merchants:
    description: "Long-distance traders"
    operates: "Temporary when caravan arrives"
    inventory: "Imported goods"
    arrival: "Event-based (exciting!)"
    travel_methods:
      - "Donkey caravan"
      - "River barges"
      - "Seagoing ships"
    role: "Independent businesspeople or temple/palace agents"

  temple_merchants:
    description: "Agents of the temple economy"
    operates: "Temple district"
    inventory: "Temple surplus, blessed items"
    special: "Fixed prices, always available"

  itinerant_traders:
    description: "Traveling vendors, peddlers"
    operates: "Moves through city"
    inventory: "Small goods, trinkets"
    bargaining: "Aggressive"
```

### 14.3 Price Standards

```yaml
trade_standards:
  weights_measures:
    description: "Government-established systems for fair trade"
    managed_by: "Temple administration"

    weight_units:
      talent: "~30 kg"
      mina: "~500 g (60 per talent)"
      shekel: "~8 g (60 per mina)"

    volume_units:
      gur: "~300 liters"
      bariga: "~60 liters"
      ban: "~10 liters"
      sila: "~1 liter (base unit)"

    enforcement:
      - "Official weights kept at temple"
      - "Merchants must use standard measures"
      - "Cheating = legal punishment"

  price_posting:
    temple_prices: "Posted publicly—reference point"
    market_prices: "Negotiated, but temple sets floor/ceiling"
    haggling: "Expected for most transactions"
```

### 14.4 Farmers Market (Daily Event)

> Once per day, Eridu comes alive with the farmers market—a timed event that rewards active players.

```yaml
farmers_market:
  description: "Daily open-air market where ALL players can sell, not just shop owners"
  purpose: "Encourage daily login, create social gathering, level playing field"

  schedule:
    frequency: "Once per day"
    duration: "1 hour real-time"
    timing:
      morning_market: "10:00-11:00 AM server time"
      note: "Same time daily for predictability"
    announcement: "Town criers announce 15 minutes before opening"

  location:
    main_plaza: "Central market square"
    capacity: "100 temporary stalls"
    layout:
      - "Inner ring: Food vendors (perishables priority)"
      - "Middle ring: Craftsmen (pottery, textiles, tools)"
      - "Outer ring: Specialty goods (imports, rare items)"

  who_can_participate:
    any_player:
      requirement: "Own goods to sell"
      stall_cost: "0 SILA (free during market hour)"
      limit: "1 stall per player"

    shop_owners:
      benefit: "Can run shop AND have market stall"
      advantage: "Established reputation draws buyers"

    new_players:
      opportunity: "Sell foraged/crafted items without owning shop"
      reason: "Democratizes commerce"

  market_mechanics:
    setup:
      arrives: "Players arrive early to claim stall spots"
      first_come: "Best locations go to early birds"
      display: "Arrange goods on stall"

    selling:
      direct_negotiation: "Face-to-face haggling"
      bulk_discounts: "Common practice"
      barter_allowed: "Trade goods directly"

    advantages_over_shops:
      - "No shop rental costs"
      - "Direct customer interaction"
      - "Impulse buying atmosphere"
      - "Social connections"

    when_market_closes:
      unsold_goods: "Player keeps inventory"
      stall_disappears: "Space returns to plaza"
      next_opportunity: "Tomorrow's market"

  special_market_days:
    festival_markets:
      frequency: "Monthly (religious festivals)"
      duration: "3 hours"
      features:
        - "Double capacity (200 stalls)"
        - "Temple goods available"
        - "Special blessing for purchases"
        - "Entertainment (musicians, dancers)"

    harvest_market:
      timing: "End of barley harvest"
      specialty: "Agricultural goods abundant, prices low"
      duration: "2 hours"

  player_benefits:
    encourages_login:
      reason: "Miss the market = miss opportunities"
      fomo: "Limited window creates urgency"

    social_hub:
      reason: "Best place to meet other players"
      networking: "Find customers, suppliers, partners"

    price_discovery:
      reason: "See what things actually sell for"
      market_research: "Inform your crafting/farming choices"
```

### 14.5 Caravan Events

> When merchant caravans arrive, the city transforms. Exotic goods, foreign news, and rare opportunities.

```yaml
caravan_events:
  description: "Periodic arrival of long-distance traders bringing imports"
  importance: "Primary source of materials not available in Eridu"

  caravan_types:
    donkey_caravan:
      origin: "Overland routes (Anatolia, Persia, India)"
      frequency: "Every 3-5 days"
      duration: "2-3 days in city"
      capacity: "Medium (20-50 donkey loads)"
      goods:
        - "Copper and tin ingots"
        - "Lapis lazuli from Afghanistan"
        - "Carnelian from Indus Valley"
        - "Timber from Lebanon"
        - "Obsidian from Anatolia"

    river_barge:
      origin: "Upstream cities (Ur, Uruk, Nippur)"
      frequency: "Every 2-3 days"
      duration: "1-2 days in city"
      capacity: "Large (heavy goods)"
      goods:
        - "Grain surplus from other cities"
        - "Finished goods from specialized cities"
        - "Temple redistribution items"
        - "Slaves and livestock"

    seagoing_ship:
      origin: "Persian Gulf, Dilmun (Bahrain), Meluhha (Indus)"
      frequency: "Every 7-14 days (seasonal)"
      duration: "3-5 days in city"
      capacity: "Very large"
      goods:
        - "Pearls and shells"
        - "Ivory from Africa/India"
        - "Exotic spices"
        - "Gold from Egypt"
        - "Unique crafted items"
      event_status: "Major city event"

  arrival_mechanics:
    announcement:
      scouts: "Scouts spot caravan 1 day before arrival"
      town_criers: "Announce to city"
      player_notification: "In-game alert"

    arrival_event:
      location: "Harbor market or city gates"
      crowd: "NPCs and players gather"
      unloading: "Goods revealed over time (excitement)"

    trading_window:
      first_hour: "Premium prices (eager buyers pay more)"
      main_period: "Standard negotiation"
      final_day: "Discounts on remaining stock"

  caravan_inventory:
    randomized:
      base_goods: "Always have trade staples"
      rare_goods: "Random chance of exceptional items"
      unique_items: "Very rare (1-5% chance per caravan)"

    supply_limits:
      each_good: "Limited quantity available"
      first_come: "Early buyers get best selection"
      price_increase: "Scarcity drives up price"

    example_caravan:
      type: "Donkey caravan from Anatolia"
      goods:
        copper_ingots:
          quantity: 50
          price: "15 SILA each"
        tin_ingots:
          quantity: 10
          price: "50 SILA each (rare!)"
        obsidian_chunks:
          quantity: 30
          price: "8 SILA each"
        timber_logs:
          quantity: 20
          price: "25 SILA each"
        rare_item:
          item: "Anatolian bronze dagger (masterwork)"
          quantity: 1
          price: "Auction starting at 200 SILA"

  player_opportunities:
    buyer:
      action: "Purchase imports before they sell out"
      advantage: "Get materials unavailable locally"
      strategy: "Save SILA for caravan days"

    seller:
      action: "Sell local goods to caravan merchants"
      exports: "Textiles, grain, dried fish, pottery"
      advantage: "Caravan pays good prices for trade goods"

    information:
      action: "Talk to caravan traders"
      news: "Learn about distant lands, prices, events"
      quests: "Caravans may offer delivery quests"

    investment:
      action: "Fund caravan expeditions"
      risk: "Caravans can be attacked, delayed, lost"
      reward: "Share of profits if successful"

  caravan_guild:
    description: "Organization of long-distance traders"
    player_membership:
      requirements:
        - "Merchant reputation 50+"
        - "Complete 5 trade quests"
        - "500 SILA membership fee"
      benefits:
        - "Early access to caravan goods (30 min head start)"
        - "Wholesale prices (10% discount)"
        - "Can join caravan expeditions"
        - "Access to guild warehouse"
```

### 14.6 Merchant Production Limits

> Shop owners can't mass-produce items. Each craft takes real time, limiting supply and creating value.

```yaml
merchant_production:
  philosophy: "Time is the ultimate cost—just like real life"
  principle: "Complex items take longer. No instant gratification."

  shop_type_limits:
    metalworking_forge:
      city_limit: 3
      description: "Smelting furnaces and smithing workshops"
      daily_production_cap: "Based on fuel/ore supply"

    pottery_kiln:
      city_limit: 5
      description: "Firing kilns for ceramics"
      daily_production_cap: "Based on kiln capacity"

    textile_workshop:
      city_limit: 8
      description: "Looms and weaving operations"
      daily_production_cap: "Based on loom count"

    jewelry_workshop:
      city_limit: 3
      description: "Fine metalwork and gem setting"
      daily_production_cap: "Based on craftsman skill"

    weapons_armory:
      city_limit: 2
      description: "Specialized weapon smithing"
      daily_production_cap: "Regulated by temple/palace"

  production_times:
    note: "Times assume skilled craftsman with proper tools"

    weapons_military:
      bronze_spearhead:
        time: "2 hours"
        materials: "Bronze ingot, charcoal"
        furnace_required: true
      bronze_sword:
        time: "4 hours"
        materials: "2 bronze ingots, charcoal, wood handle"
        furnace_required: true
        skill_minimum: 40
      bronze_dagger:
        time: "1.5 hours"
        materials: "Bronze ingot, charcoal"
        furnace_required: true
      copper_helmet:
        time: "3 hours"
        materials: "2 copper ingots, charcoal, leather padding"
        furnace_required: true
        skill_minimum: 50
        note: "Requires beating and annealing process"
      bronze_arrowheads:
        time: "30 minutes per 10"
        materials: "Bronze ingot"
        furnace_required: true
      battle_axe_head:
        time: "2.5 hours"
        materials: "Bronze ingot, charcoal"
        furnace_required: true
      mace_head:
        time: "1 hour"
        materials: "Stone or bronze"
        note: "Stone is faster, bronze requires furnace"

    tools_implements:
      copper_sickle:
        time: "1 hour"
        materials: "Copper ingot, wood handle"
        furnace_required: true
      bronze_chisel:
        time: "45 minutes"
        materials: "Bronze"
        furnace_required: true
      copper_adze:
        time: "1.5 hours"
        materials: "Copper, wood handle"
        furnace_required: true
      bronze_razor:
        time: "1 hour"
        materials: "Bronze"
        furnace_required: true
        skill_minimum: 35
      harpoon_point:
        time: "1 hour"
        materials: "Bronze or copper"
        furnace_required: true
      plow_tip:
        time: "2 hours"
        materials: "Bronze, wood fitting"
        furnace_required: true

    pottery_ceramics:
      beveled_rim_bowl:
        time: "10 minutes (mass production)"
        materials: "Clay"
        kiln_required: true
        batch_size: "20 per firing"
      storage_jar_small:
        time: "30 minutes + firing"
        materials: "Clay"
        kiln_required: true
      storage_jar_large:
        time: "1 hour + firing"
        materials: "Clay (large quantity)"
        kiln_required: true
      decorated_vessel:
        time: "2-4 hours + firing"
        materials: "Clay, pigments"
        kiln_required: true
        skill_minimum: 40
      kiln_firing_cycle:
        time: "8-12 hours"
        note: "Multiple items fired together"

    jewelry_fine_work:
      copper_ring:
        time: "30 minutes"
        materials: "Copper scrap"
      bronze_bracelet:
        time: "1 hour"
        materials: "Bronze"
      gold_earrings:
        time: "2 hours"
        materials: "Gold"
        skill_minimum: 50
      lapis_bead_necklace:
        time: "4 hours"
        materials: "Lapis lazuli, cord"
        skill_minimum: 45
      cylinder_seal:
        time: "8-16 hours"
        materials: "Stone (lapis, agate, etc.)"
        skill_minimum: 60
        note: "Intricate carving work"

    statues_sculptures:
      small_votive_figure:
        time: "4 hours (lost-wax)"
        materials: "Wax, clay, bronze"
        skill_minimum: 55
      large_statue:
        time: "3-7 days"
        materials: "Large quantity bronze, wax, clay"
        skill_minimum: 70
        note: "Major commission work"

    construction_materials:
      mud_brick:
        time: "5 minutes forming + sun drying"
        batch_size: "50 per day (1 worker)"
      fired_brick:
        time: "5 minutes + kiln firing"
        kiln_required: true
        note: "Premium, waterproof"
      foundation_cone:
        time: "1 hour + inscription time"
        materials: "Clay or copper"
        note: "Temple commissions only"

  production_modifiers:
    skill_level:
      novice: "150% time (slower)"
      journeyman: "100% time (standard)"
      expert: "80% time"
      master: "60% time"

    tool_quality:
      poor_tools: "125% time"
      standard_tools: "100% time"
      quality_tools: "85% time"
      masterwork_tools: "70% time"

    workshop_quality:
      basic_workshop: "110% time"
      proper_workshop: "100% time"
      advanced_workshop: "85% time"

    assistance:
      alone: "100% time"
      with_apprentice: "80% time"
      with_journeyman: "65% time"

  daily_limits_example:
    master_bronze_smith:
      skill: "Master (60% time modifier)"
      tools: "Quality (85% modifier)"
      workshop: "Advanced (85% modifier)"
      combined_modifier: "~44% of base time"
      daily_output_8hrs:
        - "4 bronze swords OR"
        - "8 spearheads OR"
        - "2 helmets OR"
        - "Mix of smaller items"
      note: "Still limited by material supply"

    journeyman_potter:
      skill: "Journeyman (100%)"
      tools: "Standard (100%)"
      workshop: "Proper (100%)"
      daily_output_8hrs:
        - "1 kiln firing cycle"
        - "40-60 beveled-rim bowls OR"
        - "8-10 storage jars OR"
        - "2-3 decorated vessels"

  material_constraints:
    bronze_production:
      requires: "Copper + Tin (9:1 ratio)"
      tin_scarcity: "Limits bronze production regardless of time"
      import_dependent: "Must buy from caravans"

    fuel_requirements:
      charcoal: "Required for all metalwork"
      production: "1 charcoal load = 3-4 hours smithing"
      source: "Imported or made from local brush"

  player_implications:
    time_investment:
      note: "Cost of the game is TIME, just like real life"
      meaning: "You have until death—not infinite time"
      strategy: "Choose what to craft carefully"

    shop_value:
      reason: "Limited production = limited supply"
      result: "Shop ownership is valuable"
      competition: "Only 3 forge owners in city = monopoly-ish"

    crafting_vs_buying:
      craft_yourself: "Takes your time, but keeps SILA"
      buy_from_shop: "Costs SILA, but saves time"
      economic_choice: "What is your time worth?"
```

---

## 15. Metalworking & Crafting Processes

> Bronze was the pinnacle of Sumerian technology. Understanding the process reveals why metalworkers were elite.

### 15.1 Bronze vs. Brass

```yaml
metals_clarification:
  bronze:
    composition: "Copper + Tin (typically 90:10 ratio)"
    properties:
      hardness: "Hard enough for weapons and tools"
      durability: "Long-lasting, holds edge"
      color: "Golden-brown"
    status: "THE metal of the Bronze Age"
    availability: "Tin is rare—imported from Afghanistan or beyond"

  arsenic_bronze:
    composition: "Copper + Arsenic (natural or added)"
    properties:
      hardness: "Similar to tin bronze"
      danger: "Toxic fumes when working"
    status: "Earlier/cheaper alternative to tin bronze"
    note: "Smiths who work it often suffer health problems"

  brass:
    composition: "Copper + Zinc"
    status: "ACCIDENTAL in this era"
    how_it_happened:
      - "Some copper ores contain zinc naturally"
      - "Smelting produces 'yellow copper'"
      - "Not understood or intentionally produced"
    treatment: "Curiosity or inferior bronze, not valued"
    historical_note: "True brass production comes much later (Romans)"

  copper:
    composition: "Pure copper"
    properties:
      softness: "Too soft for most weapons"
      workability: "Easy to shape"
      color: "Reddish"
    uses: "Jewelry, simple tools, decorative items"
    status: "Common but limited utility"

  gold:
    composition: "Pure gold"
    properties:
      softness: "Very soft"
      beauty: "Highly prized for appearance"
      rarity: "Imported, extremely valuable"
    uses: "Jewelry, royal items, temple decorations"
    working: "Beaten into thin sheets, no furnace needed"

  silver:
    composition: "Pure silver"
    properties:
      hardness: "Harder than gold"
      value: "Currency standard"
    uses: "Jewelry, currency, fine objects"
    status: "Imported from Anatolia"
```

### 15.2 Furnaces and Kilns

```yaml
heat_sources:
  smelting_furnace:
    purpose: "Extract metal from ore"
    construction:
      material: "Heat-resistant mud brick"
      shape: "Vertical stacking structure"
      height: "1-2 meters (sometimes taller)"
      design: "Air channels at base for bellows"

    operation:
      fuel: "Charcoal (wood won't reach temperature)"
      temperature: "1,100-1,200°C for copper"
      process:
        1: "Layer ore and charcoal"
        2: "Light fire, work bellows continuously"
        3: "Molten metal collects at bottom"
        4: "Tap off slag, retrieve metal"
      time: "4-8 hours per smelt"
      labor: "2-3 workers (bellows is exhausting)"

    output:
      copper_from_ore: "~5-10% yield (ore is mostly rock)"
      ingot_result: "Raw metal ingot for further working"

  crucible_furnace:
    purpose: "Melt metal for casting"
    construction:
      crucible: "Small ceramic pot"
      furnace: "Small charcoal fire with bellows"

    operation:
      temperature: "1,085°C for copper, ~950°C for bronze"
      process:
        1: "Place metal pieces in crucible"
        2: "Heat with bellows-driven fire"
        3: "Metal becomes liquid"
        4: "Pour into molds"
      time: "30-60 minutes to melt"

  shop_furnace:
    purpose: "Heating metal for shaping"
    construction: "Smaller, portable charcoal fire"
    operation:
      use: "Heat metal to make it workable"
      annealing: "Reheat metal between hammering sessions"
      note: "Metal becomes brittle if worked cold too long"

  pottery_kiln:
    purpose: "Fire clay items"
    construction:
      design: "Dual-chamber (fuel separate from items)"
      material: "Mud brick, insulated"
      age: "Technology 8,000+ years old"

    operation:
      temperature: "900-1,100°C"
      process:
        1: "Load items in upper chamber"
        2: "Build fire in lower chamber"
        3: "Slowly increase heat (cracking prevention)"
        4: "Maintain peak temperature for hours"
        5: "Slow cooling (overnight)"
      time: "8-12 hours firing + 12 hours cooling"
      capacity: "20-100 items depending on size"

  bread_oven:
    purpose: "Cooking, not crafting"
    temperature: "200-300°C"
    note: "Cannot be used for metalwork or quality pottery"
```

### 15.3 Casting Techniques

```yaml
casting_methods:
  open_mold_casting:
    description: "Pour metal into open stone or clay mold"
    used_for: "Simple shapes—ingots, axe heads, flat items"
    process:
      1: "Carve negative shape in stone/clay"
      2: "Pour molten metal"
      3: "Let cool, remove"
    quality: "Rough, one-sided items"
    skill_required: 20

  two_piece_mold:
    description: "Two halves create complete shape"
    used_for: "Spearheads, tools, simple objects"
    process:
      1: "Create two mold halves that fit together"
      2: "Clamp or tie halves"
      3: "Pour metal through channel"
      4: "Cool, separate, finish"
    quality: "Better detail, complete shapes"
    skill_required: 35

  lost_wax_casting:
    description: "Wax model encased in clay, burned out"
    used_for: "Intricate jewelry, statues, decorative items"
    process:
      1: "Sculpt detailed wax model"
      2: "Cover in layers of fine clay"
      3: "Fire to melt/burn out wax"
      4: "Pour metal into resulting hollow"
      5: "Break clay to reveal metal object"
    quality: "Highest detail possible"
    skill_required: 55
    time: "Many hours of work"

  beating_and_annealing:
    description: "Shape metal by hammering"
    used_for: "Bowls, helmets, shields, vessels"
    process:
      1: "Heat metal sheet to workable state"
      2: "Hammer over wooden form"
      3: "Metal work-hardens (becomes brittle)"
      4: "Reheat (anneal) to restore workability"
      5: "Repeat until shape achieved"
    quality: "Strong, seamless vessels"
    skill_required: 40
    note: "Helmets require many annealing cycles"
```

### 15.4 Items Produced by Metalworking

```yaml
metalwork_items:
  weapons_military:
    spearheads:
      description: "Pointed metal tips for infantry weapons"
      production: "Open mold or two-piece casting"
      time: "2 hours"
    arrowheads:
      description: "Small fired tips for projectile weapons"
      production: "Open mold casting (batch)"
      time: "30 min per 10"
    battle_axes_mace_heads:
      description: "Crushing and cutting weapons for close combat"
      production: "Two-piece mold casting"
      time: "2-3 hours"
    daggers_swords:
      description: "Blades for close-quarters fighting"
      production: "Casting + extensive hammering/grinding"
      time: "1.5-4 hours"
    helmets:
      description: "Beaten metal head protection for elite soldiers"
      production: "Beating and annealing (gold or copper/bronze)"
      time: "3+ hours"
      note: "Status items for officers/royalty"

  tools_agricultural:
    chisels:
      description: "Tools for shaping wood, stone, other materials"
      production: "Casting + edge hardening"
      time: "45 min"
    adzes_gouges:
      description: "Woodworking tools for carving and shaping"
      production: "Casting + fitting to handle"
      time: "1.5 hours"
    razors:
      description: "Metal blades for personal grooming"
      production: "Careful casting, fine edge"
      time: "1 hour"
    harpoons:
      description: "Barbed poles for fishing"
      production: "Casting barbed point"
      time: "1 hour"
    vessels_jugs:
      description: "Metal containers for liquids"
      production: "Beating and annealing"
      time: "2-4 hours"
    plow_tips:
      description: "Durable points for agricultural plows"
      production: "Heavy casting"
      time: "2 hours"

  artifacts_household:
    statues_sculptures:
      description: "Votive figures and royal statues"
      production: "Lost-wax casting"
      time: "4 hours to multiple days"
    jewelry:
      description: "Necklaces, earrings, pins"
      production: "Fine casting, beating, wire work"
      time: "30 min to 16 hours"
    foundation_cones:
      description: "Inscribed pegs for temple dedication"
      production: "Casting + inscription"
      time: "1-2 hours"
    weights:
      description: "Standardized trade weights"
      production: "Precise casting (often stone, sometimes metal)"
      time: "1 hour"
      note: "Must match temple standards exactly"

  construction:
    nails_rivets:
      description: "Fasteners for construction"
      production: "Simple casting"
      time: "15 min per batch"
    door_fittings:
      description: "Hinges, handles, locks"
      production: "Casting + assembly"
      time: "2-4 hours"
    clamps_brackets:
      description: "Structural supports"
      production: "Casting or beating"
      time: "1 hour"
```

---

## 16. NPC Conversion & Passive Income

> When players are offline, their characters convert to NPCs that continue operating.

### 16.1 Offline Character Behavior

```yaml
offline_npc_conversion:
  trigger: "Player logs off or is inactive for 30+ minutes"

  what_happens:
    character_becomes_npc: true
    retains:
      - "All inventory"
      - "Property ownership"
      - "Shop/business"
      - "Reputation"
    controlled_by: "AI Director (simplified)"

  npc_activities:
    shop_owner:
      behavior: "Continues selling at set prices"
      income: "Accumulates while offline"
      limitations:
        - "Won't negotiate complex deals"
        - "Fixed prices only"
        - "Won't accept barter"

    farmer:
      behavior: "Maintains fields, basic harvesting"
      income: "Crops continue growing"
      limitations:
        - "No innovations"
        - "Basic maintenance only"

    craftsman:
      behavior: "Continues producing at set rate"
      income: "Goods accumulate for sale"
      limitations:
        - "Only items already known"
        - "No quality improvements"

    landlord:
      behavior: "Collects rent from tenants"
      income: "Rent accumulates automatically"
      limitations:
        - "Can't evict"
        - "Can't change terms"
```

### 16.2 Passive Income Sources

```yaml
passive_income:
  shop_sales:
    description: "Your store keeps selling while you're offline"
    how_it_works:
      - "Set prices before logging off"
      - "NPC version serves customers"
      - "Income accumulates in your account"
    income_rate: "50-80% of active rate"
    limitations:
      - "Can't restock (sells until empty)"
      - "Fixed prices (no haggling)"

  rental_income:
    description: "Collect rent from property tenants"
    how_it_works:
      - "Set rental terms while online"
      - "Rent collected automatically"
      - "Works for land, buildings, equipment"
    income_rate: "100% (fully passive)"
    note: "Best passive income source"

  crop_growth:
    description: "Crops continue growing while offline"
    how_it_works:
      - "Plant crops while online"
      - "Growth continues offline"
      - "NPC harvests when ready"
    income_rate: "70% (some spoilage)"
    limitations:
      - "Fields may need irrigation"
      - "Pests may cause losses"

  investment_returns:
    description: "Business partnerships continue operating"
    how_it_works:
      - "Invest in merchant ventures"
      - "Partner manages operations"
      - "Share profits automatically"
    income_rate: "Variable (based on venture)"
    risk: "Ventures can fail"

  temple_stipends:
    description: "If you work for temple, stipend continues"
    how_it_works:
      - "Employment agreement"
      - "Regular payment schedule"
    income_rate: "100% (guaranteed)"
```

### 16.3 Returning from Offline

```yaml
return_from_offline:
  when_you_log_in:
    summary_provided:
      - "Total income earned"
      - "Items sold"
      - "Rent collected"
      - "Crops harvested"
      - "Events that occurred"

    potential_issues:
      - "Stock depleted (need to restock)"
      - "Tenant complaints"
      - "Crop losses"
      - "Market price changes"

  npc_log:
    description: "Record of what your NPC did"
    includes:
      - "All transactions"
      - "Visitors to your property"
      - "Any problems encountered"

  seamless_transition:
    note: "Other players don't know you were offline"
    npc_appearance: "Same as your character"
    personality: "Simplified version of your character"
```

### 16.4 Passive Income Limits

```yaml
passive_income_limits:
  purpose: "Prevent pure AFK farming"

  daily_caps:
    shop_sales: "100 transactions/day offline"
    rental_income: "No cap (fully passive)"
    crop_harvest: "Fields you own only"

  quality_degradation:
    description: "Long offline periods reduce efficiency"
    after_1_day: "95% efficiency"
    after_3_days: "85% efficiency"
    after_7_days: "70% efficiency"
    after_30_days: "50% efficiency"
    reason: "Business relationships need maintenance"

  reactivation:
    how_to_restore: "Log in and actively participate"
    recovery_time: "1 hour online = 1 day recovery"
```

---

## 17. Item Properties

### 17.1 Common Properties

```yaml
item_properties:
  durability:
    description: "How long item lasts before breaking"
    range: "1-100"
    degradation: "Use reduces durability"
    repair: "Skill + materials restore durability"
    at_zero: "Item breaks, may be repairable or lost"

  quality:
    description: "Craftsmanship level"
    range: "1-100"
    affects:
      - "Effectiveness"
      - "Durability rate"
      - "Sale value"
      - "NFT eligibility"

  weight:
    description: "Carrying burden"
    unit: "Talent (30kg) / Mina (500g) / Shekel (8g)"
    affects: "Inventory capacity, travel speed"

  condition:
    states:
      - "Pristine (100%)"
      - "Good (75-99%)"
      - "Worn (50-74%)"
      - "Damaged (25-49%)"
      - "Broken (1-24%)"
      - "Destroyed (0%)"
```

### 17.2 Special Properties

```yaml
special_properties:
  blessed:
    source: "Temple ritual"
    effect: "+10% effectiveness, slower degradation"
    duration: "Permanent until item breaks"
    visual: "Subtle glow/aura"

  cursed:
    source: "Negative events, stolen temple items"
    effect: "Bad luck, faster degradation"
    removal: "Exorcism (Asipu), high cost"

  heirloom:
    source: "Passed through 3+ generations"
    effect: "Legacy points, family bonding"
    special: "Tracks history, previous owners"
    nft: "Automatic NFT eligibility"

  innovation_marked:
    source: "First of its kind created"
    effect: "Blueprint rights"
    nft: "Required NFT"
    royalties: "Creator earns on copies"

  named:
    source: "Player names the item"
    effect: "Personal connection, easier tracking"
    requirement: "Rare+ quality"
```

---

## 18. Inventory Management

### 18.1 Carrying Capacity

```yaml
carrying_capacity:
  base_capacity:
    adult_human: "30kg (1 talent)"
    with_pack: "40kg"
    with_donkey: "+60kg"
    with_cart: "+200kg"

  overweight_effects:
    110%: "Slower movement"
    125%: "Very slow, stamina drain"
    150%: "Cannot move"

  storage_options:
    personal_home:
      capacity: "Varies by house size"
      security: "Locked (can be broken into)"

    warehouse_rental:
      capacity: "Large"
      cost: "5 SILA/month per unit"
      security: "Guarded"

    temple_deposit:
      capacity: "Limited"
      cost: "Offering-based"
      security: "Very high (divine protection)"
```

### 18.2 Inventory UI

```yaml
inventory_interface:
  categories:
    equipped: "Currently worn/held items"
    tools: "Work implements"
    weapons: "Combat items"
    materials: "Crafting resources"
    food: "Consumables"
    valuables: "Jewelry, currency, documents"
    misc: "Everything else"

  sorting:
    - "By category"
    - "By rarity"
    - "By weight"
    - "By value"
    - "By condition"

  features:
    stack_similar: "Identical items stack"
    quick_access: "Hotbar for frequently used"
    search: "Find items by name"
    compare: "Side-by-side comparison"
```

---

## 19. Item Lifecycle

### 19.1 Creation to Destruction

```yaml
item_lifecycle:
  creation:
    crafted: "Made by player/NPC"
    found: "Discovered in world"
    purchased: "Bought from store/player/NPC"
    rewarded: "Quest/achievement reward"

  ownership:
    possessed: "In player inventory/storage"
    equipped: "Currently in use"
    displayed: "Placed in world (decorative)"
    listed: "For sale in marketplace"
    escrowed: "In trade transaction"

  transfer:
    trade: "Player to player exchange"
    gift: "Given freely"
    sale: "Sold for SILA/ANALOG"
    inheritance: "Passed to heir on death"
    theft: "Stolen (if caught, legal consequences)"

  end_of_life:
    broken: "Durability reaches 0"
    consumed: "Food/consumable used"
    burned: "Destroyed by fire/disaster"
    sacrificed: "Temple offering"
    lost: "Dropped, never recovered"
    nft_burned: "Special destruction process"
```

### 19.2 Degradation & Repair

```yaml
degradation:
  use_degradation:
    tools: "1-5% per use session"
    weapons: "2-10% per combat"
    clothing: "0.5-2% per day worn"
    armor: "5-15% per combat"

  environmental:
    rain: "+50% degradation for non-waterproof"
    sun: "Slow degradation for organics"
    storage: "Minimal degradation if proper"

  repair:
    requirements:
      - "Appropriate skill (20% of creation skill)"
      - "Materials (10-30% of original)"
      - "Tools"

    limits:
      - "Max quality decreases with each repair"
      - "Eventually item cannot be repaired"
      - "Pristine → can only reach 95% → 90% → etc."

  special_items:
    blessed_items: "50% slower degradation"
    legendary_items: "Self-repair or very slow degradation"
    cursed_items: "200% degradation rate"
```

---

## 20. Pricing Guidelines

### 20.1 SILA Pricing Reference

```yaml
sila_pricing:
  note: "1 SILA ≈ 1 liter of barley, daily unskilled wage = 2-3 SILA"

  materials:
    clay_bundle: 1
    reed_bundle: 2
    wool_raw_kg: 5
    flax_bundle: 8
    copper_ingot: 50
    silver_shekel: 300
    gold_shekel: 3000
    lapis_chunk: 200

  common_items:
    bread_loaf: 0.5
    beer_jar: 1
    wool_cloth_meter: 10
    pottery_jar: 5
    reed_basket: 3
    wooden_stool: 15

  uncommon_items:
    copper_tool: 25-50
    leather_goods: 20-40
    quality_clothing: 30-60
    decorated_pottery: 15-30

  rare_items:
    bronze_weapon: 100-200
    fine_jewelry: 50-200
    cylinder_seal: 200-500
    quality_furniture: 50-100

  epic_items:
    gold_jewelry: 500-2000
    master_crafted: 200-500
    rare_materials: 300-1000

  legendary_items:
    unique_artifacts: 1000+
    innovation_blueprints: 5000+
    blessed_items: 500-5000
```

### 20.2 Real Money Equivalents

```yaml
real_money_guidelines:
  conversion_target: "1 USD ≈ 100 SILA at launch"

  store_pricing:
    micro_transaction: "$1-5"
    small_purchase: "$5-15"
    medium_purchase: "$15-50"
    large_purchase: "$50-100"
    major_purchase: "$100+"

  nft_floor_prices:
    basic_craftable: "$5-20"
    rare_item: "$20-50"
    epic_item: "$50-200"
    legendary_item: "$200+"
    land_deed: "$25-500"
    reincarnation_ticket: "$10-100"
```

---

## Appendix: Quick Reference

### Item Category Summary

| Category | Tradeable | NFT Eligible | Degrades | Stackable |
|----------|-----------|--------------|----------|-----------|
| Tools | Yes | Rare+ | Yes | No |
| Weapons | Yes | Rare+ | Yes | No |
| Clothing | Yes | Rare+ | Yes | No |
| Jewelry | Yes | Rare+ | Slow | No |
| Food | Yes | No | Fast | Yes |
| Materials | Yes | No | Some | Yes |
| Furniture | Yes | Rare+ | Slow | No |
| Documents | Yes | Some | Slow | No |
| Land | Yes | Always | No | No |
| Special | Yes | Always | No | No |

### Store Item Summary

| Item Type | Price Range | Supply | NFT |
|-----------|-------------|--------|-----|
| Basic Ticket | $10 | Unlimited | Yes |
| Heritage Ticket | $25 | 10k waves | Yes |
| Noble Ticket | $50 | 1k/era | Yes |
| Founder Ticket | $100 | 500 total | Yes |
| City Plot | $50-500 | Fixed | Yes |
| Farm Plot | $25-200 | Fixed | Yes |
| Premium Tools | $25-50 | Limited | Yes |
| Cosmetics | $1-25 | Varies | Varies |
| Starter Pack | $15-75 | Varies | Varies |

---

*"In Eridu, a man is measured not by what he has, but by what he has made."*
