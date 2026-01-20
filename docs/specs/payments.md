# The Analog Economy: Payments & Economic System Specification

> **Version:** 1.1
> **Last Updated:** 2026-01-19
> **Status:** Vision Complete

---

## Executive Summary

The Analog Economy implements a **dual-economy model** that separates problem-solving tools (free, abundant) from collectible assets (scarce, tradeable). Unlike traditional games where players buy power, our economy rewards players for solving real problems while creating a self-sustaining barter system tied to cryptocurrency.

**Core Principle:** No one is locked out of solving humanity's problems due to lack of funds.

> **Related Documentation:** For technical blockchain implementation details including smart contracts, chain selection, and NFT architecture, see [Blockchain Economy](blockchain-economy.md).

---

## Table of Contents

1. [Economic Philosophy](#economic-philosophy)
2. [The Dual Economy Model](#the-dual-economy-model)
3. [Player Income Streams](#player-income-streams)
4. [The Collectible Layer](#the-collectible-layer)
5. [The Barter System](#the-barter-system)
6. [Free-to-Play Pathways](#free-to-play-pathways)
7. [The Creator Economy](#the-creator-economy)
8. [Token Economics](#token-economics)
9. [Technical Implementation](#technical-implementation)
10. [Bootstrap Phase](#bootstrap-phase)

---

## Economic Philosophy

### What We Reject

| Traditional Gaming | Why It's Wrong |
|-------------------|----------------|
| Pay-to-win | Locks out players from core content |
| Artificial scarcity on essential tools | Creates frustration, not engagement |
| Grinding for basic progression | Wastes human potential |
| Closed economies | Value trapped inside game |

### What We Embrace

| Our Approach | Why It Works |
|--------------|--------------|
| Free problem-solving tools | Everyone can contribute to solutions |
| Scarcity only on collectibles | Trading card economics - rare = valuable |
| Earn through contribution | Real problems solved = real rewards |
| Open economy (crypto-backed) | Value flows in AND out of game |
| Barter system | Human negotiation, AI-facilitated |

---

## The Dual Economy Model

### Layer 1: Utility Tools (FREE & Abundant)

**Purpose:** Enable players to solve problems without barriers.

```
┌─────────────────────────────────────────────────────────────┐
│                    UTILITY LAYER                            │
│                   (No Scarcity)                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Problem-Solving Tools                                      │
│  ├── Water filtration equipment (The Aqua)                  │
│  ├── Search & rescue gear (The Ruins)                       │
│  ├── Mining/pipeline tools (The Abyss)                      │
│  ├── Agricultural implements (The Botany)                   │
│  └── [Biome-specific essentials]                            │
│                                                             │
│  Spawn Behavior:                                            │
│  • Given at biome entry, OR                                 │
│  • Rendered when player reaches destination, OR             │
│  • Found abundantly in environment                          │
│                                                             │
│  Cost: FREE (Always)                                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Rules:**
- Tools required to solve the current problem = always available
- No grinding required to access essential equipment
- Cannot be traded (utility items are soulbound)
- Disappear when no longer needed for active problem

### Layer 2: Collectibles & Assets (SCARCE & Tradeable)

**Purpose:** Create real economic value through scarcity and player ownership.

```
┌─────────────────────────────────────────────────────────────┐
│                  COLLECTIBLE LAYER                          │
│              (Scarce, NFT-Backed)                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Legendary Items (Ultra-Rare)                               │
│  ├── Excalibur Swords: 1,000 total supply                   │
│  ├── Gaian Coins: 100 total supply                          │
│  └── [Mythic artifacts]                                     │
│                                                             │
│  Rare Items                                                 │
│  ├── Magical Potions: 5,000 total supply                    │
│  ├── Ancient Maps: 2,500 total supply                       │
│  └── [Collectible gear]                                     │
│                                                             │
│  Player-Built Assets                                        │
│  ├── Shelters & Sheds (rentable to other players)           │
│  ├── Workshops (crafting stations)                          │
│  ├── Waypoints (fast travel)                                │
│  └── [Infrastructure]                                       │
│                                                             │
│  Backing: ERC-721 (unique) or ERC-1155 (semi-fungible)      │
│  Value: In-game utility + Real-world exchangeability        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Rules:**
- Fixed supply - no inflation
- Tradeable between players
- Crypto-backed (real ownership)
- Can be sold outside the game
- Permadeath can burn items (deflationary pressure)

---

## Player Income Streams

### Tier 1: Problem Solving (Highest Payouts)

**Source:** Enterprise/government buyers of training data

```
Player solves complex problem
        ↓
Gaian validates solution (ethics, anti-cheat)
        ↓
NoveltyScorer evaluates creativity
        ↓
SILA awarded (in-game) + ANALOG for exceptional work
        ↓
Value exchangeable for:
├── Collectible items (in-game with SILA)
├── NFTs and premium items (with ANALOG)
└── Fiat currency (ANALOG via exchanges)
```

**Payout Factors:**
| Factor | Multiplier | Description |
|--------|------------|-------------|
| Baseline | 1.0x | Any valid solution |
| Efficiency | 1.5x | Faster than average |
| Creativity | 3.0x | Unexpected approach |
| Collaboration | 1.2x | Team solution |
| First Solution | 5.0x | Novel problem type |
| Biome Priority | Variable | Water (2.5x), SAR (1.5x), etc. |

### Tier 2: Asset Rental (Passive Income)

**Source:** Other players renting your built assets

```
Player builds shed in The Ruins
        ↓
Other players need shelter before reaching Level 5
        ↓
Traveler negotiates with Landlord's AI Bot
        ↓
Rental agreement = SILA or ANALOG transaction
        ↓
Landlord receives rent (SILA for short-term, ANALOG for premium)
```

**Rentable Assets:**
- Shelters (rest points)
- Workshops (crafting)
- Waypoints (fast travel)
- Storage (inventory expansion)
- Training grounds (skill practice)

### Tier 3: Trading & Bartering

**Source:** Buying low, selling high; arbitrage; negotiation

```
Player finds rare Ancient Map
        ↓
Another player needs map for their quest
        ↓
Negotiation (direct or via AI broker)
        ↓
Trade: Map ↔ Magical Potions + SILA
        ↓
Both parties receive assets
```

### Tier 4: Discovery & Contribution

**Source:** Found items, bug bounties, feedback

| Activity | Reward Type | Notes |
|----------|-------------|-------|
| Finding items in-world | Items/SILA | Zelda-style exploration |
| Reporting glitches | SILA/ANALOG | "Glitches in the matrix" |
| Quality feedback | SILA/ANALOG | Improving the simulation |
| Survey completion | SILA | Advertiser-funded |
| Tutorial completion | Items | Onboarding rewards |

---

## The Barter System

### AI-Powered NPCs (Landlords, Merchants)

Every player-owned rentable asset can have an **AI Bot** assigned to negotiate on their behalf.

**Landlord Bot Configuration:**
```yaml
landlord_bot:
  owner: "player_wallet_address"
  asset: "shelter_ruins_042"

  pricing:
    minimum_rent: 5              # Won't accept less than 5 SILA
    preferred_rent: 8            # Will accept immediately at 8+
    negotiation_range: [5, 12]   # Will negotiate within this range

  barter_accepts:
    - item: "magical_potion"
      value: 3                   # Equivalent to 3 SILA
    - item: "ancient_map"
      value: 10

  personality:
    style: "friendly_but_firm"
    max_negotiation_rounds: 5

  availability:
    hours: "always"              # Or specific time windows
```

**Negotiation Flow:**
```
Traveler: "I need to rest. How much for the shed?"
Bot: "8 SILA per night. Fair price for safe shelter."
Traveler: "I only have 4 SILA, but I have potions."
Bot: "Potions? I could use those. 4 SILA + 2 potions?"
Traveler: "Deal."
Bot: "Welcome. The shed is yours for the night."
        ↓
    [Transaction executes - SILA off-chain, instant]
```

### Direct Player-to-Player Trading

Players can also negotiate directly:
- In-game chat with trade UI
- Escrow smart contract holds both sides
- Trade executes atomically (both or neither)

---

## Free-to-Play Pathways

**Principle:** A player with zero money can still progress, earn, and eventually thrive.

### Path 1: Exploration (Zelda Model)

```
Explore the world
        ↓
Find items in:
├── Abandoned structures
├── Hidden caches
├── Environmental puzzles
├── Quest rewards
└── Random spawns
        ↓
Trade items for what you need
```

### Path 2: Contribution Rewards

| Contribution | Reward |
|--------------|--------|
| Report a bug/glitch | 10-100 SILA (severity-based) |
| Suggest improvement | 5-50 SILA (if implemented) |
| Complete survey | 2-10 SILA |
| Watch sponsor content | 1-5 SILA |
| Refer new player | 20 SILA (on their first solve) |

### Path 3: Community Support

- Veteran players can tip/gift new players
- Guild systems for resource sharing
- "Scholarship" programs for promising players

### Path 4: Skill-Based Earning

Even without rare items, skilled players can:
- Solve problems efficiently (higher multipliers)
- Help others (collaboration bonuses)
- Speedrun for leaderboard rewards

---

## The Creator Economy

**Vision:** Players become entrepreneurs—designing, building, and selling their own tools and magical items within the game. The best creations take off organically; creators earn ongoing revenue.

### The Tool Forge

Players can create custom tools with unique abilities:

```
┌─────────────────────────────────────────────────────────────┐
│                    THE TOOL FORGE                           │
│              (Player Creation System)                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  What Players Can Create:                                   │
│  ├── Magical Tools (enhanced abilities)                     │
│  ├── Potions & Consumables                                  │
│  ├── Weapons & Armor                                        │
│  ├── Utility Items (maps, compasses, keys)                  │
│  ├── Cosmetics (skins, effects, trails)                     │
│  └── Structures (shelters, workshops, waypoints)            │
│                                                             │
│  Creation Question: "If you could create any magical        │
│  power, what would you want?"                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Creator Licensing Tiers

**To create and sell tools, players must purchase rights:**

| License Tier | Cost (SILA) | What You Can Create | Revenue Share |
|--------------|------------|---------------------|---------------|
| **Apprentice** | 100 | Basic tools, cosmetics | 70% to creator |
| **Artisan** | 500 | Enhanced tools, consumables | 75% to creator |
| **Master** | 2,000 | Magical items, structures | 80% to creator |
| **Legendary** | 10,000 | Mythic items, unique abilities | 85% to creator |

**Revenue flows:**
- Creator gets their share
- Platform (us) gets the remainder
- Transaction fees on secondary sales

### Creation Process

```
1. DESIGN
   Player uses Tool Forge UI to design item
        ↓
2. INVEST
   Pay license fee + material costs
        ↓
3. MINT
   Item is minted as NFT (limited or unlimited supply)
        ↓
4. GAIAN REVIEW
   Ethics filter checks for prohibited content
        ↓
5. DISTRIBUTE
   ├── Hide in world (treasure hunt)
   ├── Sell in marketplace
   ├── Gift to other players
   └── Use personally
        ↓
6. MARKET VALIDATION
   See if the tool "takes off" organically
        ↓
7. EARN
   Ongoing royalties from sales/usage
```

### Distribution Channels

#### 1. Hidden Treasures (Discovery Model)

Creators can hide their tools throughout the world:

```yaml
hidden_item:
  item_id: "phoenix_feather_042"
  creator: "player_wallet_address"

  location:
    biome: "the_scorch"
    coordinates: [x, y, z]
    visibility: "hidden"           # Must be discovered

  discovery_conditions:
    - type: "proximity"
      radius: 10                   # Within 10 meters
    - type: "time_of_day"
      window: "dawn"               # Only visible at dawn
    - type: "prerequisite"
      requires: "ancient_compass"  # Need specific item

  finder_cost: 0                   # Free to find
  creator_reward: 5                # Creator gets 5 SILA when found
```

**Why hide items?**
- Organic discovery = word of mouth marketing
- Creates treasure hunting gameplay
- Finders tell others → demand grows
- Creator builds reputation

#### 2. Marketplace (Direct Sales)

```yaml
marketplace_listing:
  item_id: "phoenix_feather"
  creator: "player_wallet_address"

  pricing:
    type: "fixed"                  # or "auction"
    price: 50                      # 50 SILA (or ANALOG for NFTs)

  supply:
    type: "limited"                # or "unlimited"
    total: 500                     # Only 500 will ever exist
    minted: 127                    # 127 sold so far

  royalties:
    creator_share: 0.80            # 80% to creator
    platform_share: 0.20           # 20% to platform
    secondary_royalty: 0.05        # 5% on resales
```

#### 3. NPC Vendors (Passive Sales)

Creators can set up NPC vendors to sell on their behalf:

```yaml
creator_vendor:
  owner: "player_wallet_address"
  location: "marketplace_district_ruins"

  inventory:
    - item: "phoenix_feather"
      stock: 50
      price: 50
    - item: "healing_salve"
      stock: unlimited
      price: 10

  vendor_personality:
    style: "enthusiastic_merchant"
    pitch: "Finest phoenix feathers in all the Ruins!"
```

### Quality Control & Curation

#### Gaian Ethics Filter

All created items pass through Gaian before distribution:

```python
class CreatorItemFilter:
    """Ethics and quality filter for player-created items."""

    def evaluate(self, item: CreatedItem) -> FilterResult:
        # Check for prohibited content
        # - No real-world weapon designs
        # - No hate symbols
        # - No exploitative mechanics
        # - No copyright infringement

        # Check for game balance
        # - Not game-breaking overpowered
        # - Fits within power curve
        # - Doesn't bypass intended progression

        return FilterResult(
            approved=True,
            warnings=[],
            required_changes=[]
        )
```

#### Community Curation

- **Upvote/Downvote** - Players rate items
- **Featured Creator** - Highlighted on marketplace
- **Creator Reputation** - Track record visible
- **Verified Creator** - Badge for consistent quality

### Creator Economics

#### Revenue Streams for Creators

| Source | When | Amount |
|--------|------|--------|
| Initial sale | Item first purchased | 70-85% of price |
| Secondary sale | Item resold by owner | 5% royalty |
| Hidden discovery | Someone finds hidden item | Flat fee (5 SILA) |
| Rental | Item rented out | % of rental fee |
| Usage fee | Consumable used | Per-use micro-payment |

#### Example: Successful Creator Journey

```
Week 1: Buy Apprentice License (100 SILA)
        Create "Traveler's Lucky Charm"
        Hide 20 in The Ruins

Week 2: First discoveries, word spreads
        Players want more → list on marketplace
        Price: 25 SILA, sell 50 units
        Revenue: 50 × 25 × 0.70 = 875 SILA

Week 4: Upgrade to Artisan License (500 SILA)
        Create "Phoenix Feather" (enhanced)
        Limited edition: 200 total
        Price: 100 SILA
        Revenue: 200 × 100 × 0.75 = 15,000 SILA

Week 8: Items trading on secondary market
        100 resales at avg 150 SILA
        Royalty: 100 × 150 × 0.05 = 750 SILA

Total: Invested 600 SILA → Earned 16,625 SILA
```

### Platform Revenue (Developer Income)

The game developer (Mault) earns revenue through multiple automated streams. Smart contracts make percentage collection automatic and transparent.

#### Revenue Stream 1: Direct Sales (Primary Market)

**We sell official items directly to players:**

| Category | Examples | Price Range (USD equivalent) |
|----------|----------|------------------------------|
| **Reincarnation Tickets** | Entry to game, era access | $10-50 |
| **Land Deeds** | City plots, farm plots, workshops | $25-500 |
| **Premium Tools** | Legendary weapons, blessed items | $5-100 |
| **Cosmetics** | Clothing, jewelry, housing decor | $1-25 |
| **Starter Packs** | Bundled items for new players | $15-75 |

**Revenue:** 100% to developer (minus blockchain gas costs)

#### Revenue Stream 2: Transaction Fees (Secondary Market)

**We take a percentage of ALL player-to-player trades:**

```yaml
marketplace_fees:
  nft_trades:
    platform_fee: "2.5%"          # Goes to Mault treasury
    creator_royalty: "2.5%"       # Goes to original item creator
    total_cut: "5%"

  how_it_works:
    smart_contract: "EIP-2981 royalty standard"
    enforcement: "Built into NFT contract—cannot be bypassed"
    automatic: "Fees deducted at transaction time"

  example:
    sale_price: 100 ANALOG
    buyer_pays: 100 ANALOG
    seller_receives: 95 ANALOG
    platform_receives: 2.5 ANALOG
    creator_receives: 2.5 ANALOG
```

**This is standard and simple to implement.** OpenSea, Rarible, and all major NFT marketplaces do this.

#### Revenue Stream 3: Royalties on Resales (Forever)

**Every time an NFT we created is resold, we get paid:**

```yaml
developer_royalties:
  official_items:
    land_deeds: "5% on every resale"
    reincarnation_tickets: "5% on every resale"
    legendary_items: "5% on every resale"

  smart_contract_enforcement:
    standard: "EIP-2981"
    visibility: "Royalty % stored on-chain, visible to all"
    execution: "Automatic payment on compliant marketplaces"

  example_scenario:
    initial_sale: "We sell Land Deed for $100 → We get $100"
    resale_1: "Player sells for $200 → We get $10 (5%)"
    resale_2: "New owner sells for $500 → We get $25 (5%)"
    resale_3: "Sold again for $1000 → We get $50 (5%)"
    total_from_one_item: "$185 from one $100 initial sale"
```

#### Revenue Stream 4: Land Sales (Major Revenue)

**Land is scarce and valuable:**

```yaml
land_economics:
  eridu_ancient_era:
    total_city_plots: 500          # Fixed supply, never more
    total_farm_plots: 2000         # Fixed supply
    total_workshop_plots: 300      # Fixed supply

  pricing_tiers:
    prime_location:                # Temple district, market center
      initial_price: "$200-500"
      expected_resale: "2-10x"
    standard_location:             # Residential areas
      initial_price: "$50-150"
      expected_resale: "1.5-3x"
    edge_location:                 # City outskirts, wilderness
      initial_price: "$25-75"
      expected_resale: "1-2x"

  revenue_projection:
    if_500_city_plots_at_avg_100: "$50,000"
    if_2000_farm_plots_at_avg_50: "$100,000"
    plus_5%_on_all_resales: "Ongoing passive income"
```

#### Revenue Stream 5: Premium Features

| Feature | Price | Description |
|---------|-------|-------------|
| Name reservation | $5 | Reserve character/business name before launch |
| Early access | $25 | Play in alpha/beta |
| Founder status | $100 | Special badge, early access, bonus items |
| Premium listing | $1-5 | Featured spot in marketplace |
| Express minting | $2-10 | Skip queue for NFT minting |

#### Summary: How We Make Money

```
┌─────────────────────────────────────────────────────────────┐
│                 DEVELOPER REVENUE STREAMS                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  DIRECT SALES (One-time)                                    │
│  ├── Reincarnation Tickets                                  │
│  ├── Land Deeds (fixed supply, valuable)                    │
│  ├── Premium/Legendary Items                                │
│  ├── Cosmetics                                              │
│  └── Starter Packs                                          │
│                                                             │
│  TRANSACTION FEES (Ongoing, automatic)                      │
│  ├── 2.5% of ALL NFT marketplace trades                     │
│  └── Smart contract enforced—no way to skip                 │
│                                                             │
│  ROYALTIES (Forever, automatic)                             │
│  ├── 5% every time our NFTs resell                          │
│  └── Land, tickets, official items                          │
│                                                             │
│  PREMIUM FEATURES (Optional)                                │
│  ├── Early access, founder packs                            │
│  └── Convenience features                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Key Point:** Smart contracts make the percentage collection automatic. Once an NFT is minted with royalty settings, every resale automatically sends us our cut. No invoicing, no chasing payments—it's built into the transaction.

### Anti-Spam & Quality Measures

**Problem:** Prevent flooding the market with garbage items.

**Solutions:**

1. **License Cost Barrier** - Creating costs real tokens
2. **Material Costs** - Better items = more materials needed
3. **Reputation System** - Low-rated creators get deprioritized
4. **Gaian Filter** - Blocks low-effort/prohibited content
5. **Minting Limits** - Max items per creator per week
6. **Curation Tax** - Unlimited items cost more to list

### Creator Tools (Technical)

```
┌─────────────────────────────────────────────────────────────┐
│                  TOOL FORGE UI                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [DESIGN TAB]                                               │
│  ├── Visual Editor (3D model, textures)                     │
│  ├── Ability Designer (drag-drop effects)                   │
│  ├── Stats Configuration (power, durability)                │
│  └── Rarity & Supply Settings                               │
│                                                             │
│  [PREVIEW TAB]                                              │
│  ├── In-game preview                                        │
│  ├── Balance analysis                                       │
│  └── Similar items comparison                               │
│                                                             │
│  [PUBLISH TAB]                                              │
│  ├── Set pricing                                            │
│  ├── Choose distribution method                             │
│  ├── Submit for Gaian review                                │
│  └── Track sales & analytics                                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Token Economics

> **Note:** For detailed technical specifications of ANALOG and SILA tokens, including smart contract architecture and chain selection, see [Blockchain Economy](blockchain-economy.md).

### Two-Token System

The Analog Economy uses a dual-token system designed for both seamless gameplay and real-world value:

| Token | Type | Purpose |
|-------|------|---------|
| **SILA** | Off-chain (Database) | Daily gameplay, NPC trades, small transactions |
| **ANALOG** | ERC-20 (On-chain) | Governance, NFT minting, premium features, real value |

### SILA (Gameplay Currency)

**Type:** Off-chain database currency (NOT a cryptocurrency)

**Flow Model:**
```
┌─────────────────────────────────────────────────────────────┐
│                    SILA FLOW                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  INFLOW (Earning)                                           │
│  ├── Work wages (farming, crafting, labor)                  │
│  ├── Selling goods to NPCs/players                          │
│  ├── Quest rewards                                          │
│  └── Contribution rewards                                   │
│                                                             │
│  OUTFLOW (Sinks)                                            │
│  ├── NPC purchases                                          │
│  ├── Service fees                                           │
│  ├── Death/respawn costs                                    │
│  ├── NFT minting fees (SILA portion)                        │
│  └── Taxes and tithes                                       │
│                                                             │
│  CIRCULATION                                                │
│  ├── Player-to-player trades                                │
│  ├── Rental payments                                        │
│  └── NPC transactions                                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### ANALOG (Governance Token)

**Type:** ERC-20 (Fungible, on Polygon)

**Supply:** 1,000,000,000 ANALOG (Fixed cap)

**Utility:**
- Governance voting on game development
- Mint NFTs from craftables
- Premium marketplace features
- Staking for fee reductions

**Anti-Inflation Mechanisms:**
1. **Fixed supply** - No additional minting after initial distribution
2. **NFT minting costs** - ANALOG burned when minting NFTs
3. **Staking locks** - Tokens locked for governance participation
4. **Quality gates** - Cannot grind ANALOG (earned through achievements)

### Collectible NFTs

**Types:**

| Standard | Use Case | Examples |
|----------|----------|----------|
| ERC-721 | Unique items | Excalibur #42, Gaian Coin #7 |
| ERC-1155 | Semi-fungible | Magical Potion (batch of identical) |

**Supply Caps (Examples):**
| Item | Total Supply | Rarity Tier |
|------|--------------|-------------|
| Gaian Coin | 100 | Mythic |
| Excalibur Sword | 1,000 | Legendary |
| Ancient Map | 2,500 | Epic |
| Magical Potion | 5,000 | Rare |
| Traveler's Cloak | 25,000 | Uncommon |

---

## Technical Implementation

### Smart Contracts Required

```
economy-contracts/
├── contracts/
│   ├── token/
│   │   └── NoveltyToken.sol        # ERC-20 with mint/burn
│   ├── items/
│   │   ├── LegendaryItems.sol      # ERC-721 for uniques
│   │   └── CollectibleItems.sol    # ERC-1155 for batches
│   ├── land/
│   │   └── PlayerAssets.sol        # ERC-721 for built structures
│   ├── marketplace/
│   │   ├── TradeEscrow.sol         # Atomic swaps
│   │   └── RentalAgreement.sol     # Time-locked rentals
│   ├── creator/
│   │   ├── CreatorLicense.sol      # License NFTs (Apprentice→Legendary)
│   │   ├── CreatedItems.sol        # Player-created item registry
│   │   └── RoyaltyDistributor.sol  # Automatic creator royalties
│   └── governance/
│       └── TreasuryDAO.sol         # Community treasury
```

### Backend Services

```
core-governance/
├── app/
│   ├── services/
│   │   ├── payout_calculator.py    # Orchestrates token minting
│   │   ├── rental_service.py       # Manages rental agreements
│   │   ├── trade_service.py        # Facilitates trades
│   │   ├── npc_negotiator.py       # AI bot logic
│   │   ├── creator_service.py      # Tool Forge backend
│   │   └── hidden_item_service.py  # Treasure placement & discovery
│   └── api/
│       └── v1/
│           ├── payouts.py          # Claim rewards
│           ├── marketplace.py      # List/buy items
│           ├── rentals.py          # Rent/lease assets
│           ├── wallet.py           # Balance, history
│           ├── creator.py          # Tool Forge API
│           └── discovery.py        # Hidden item mechanics
```

### Creator Tools Infrastructure

```
client-simulation/
├── Source/
│   └── ToolForge/                  # UE5 Creator UI
│       ├── ToolForgeUI.cpp         # Main forge interface
│       ├── ItemDesigner.cpp        # Visual item editor
│       ├── AbilityComposer.cpp     # Drag-drop ability system
│       └── PreviewRenderer.cpp     # In-game preview

core-governance/
├── gaian/
│   └── creator/
│       ├── item_filter.py          # Ethics check for created items
│       ├── balance_checker.py      # Game balance validation
│       └── copyright_scanner.py    # Detect prohibited content
```

### AI Bot Architecture

```python
class LandlordBot:
    """AI-powered negotiator for player-owned assets."""

    def __init__(self, config: LandlordConfig):
        self.min_price = config.minimum_rent
        self.preferred_price = config.preferred_rent
        self.barter_values = config.barter_accepts
        self.personality = config.personality

    def negotiate(self, offer: TradeOffer) -> NegotiationResponse:
        """Evaluate offer and respond."""
        # Calculate total value of offer
        # Compare to minimum threshold
        # Generate personality-appropriate response
        # Accept, counter, or reject
```

---

## Bootstrap Phase

**Problem:** Before we have enterprise buyers, how do players earn?

### Phase 1: Internal Economy (Launch)

```
No external buyers yet
        ↓
Players solve problems anyway
        ↓
Rewarded with:
├── Novelty Tokens (from treasury allocation)
├── Collectible items (limited supply)
└── Player-built asset rights
        ↓
Value comes from:
├── Scarcity (fixed NFT supply)
├── Utility (items help progression)
└── Speculation (future buyer interest)
```

**Treasury Allocation:**
- X% of tokens reserved for early player rewards
- Distributed through problem-solving, not airdrops
- Decreasing emission rate over time

### Phase 2: First Buyers (Growth)

```
First enterprise buyer signs
        ↓
Training data sales begin
        ↓
Revenue flows to:
├── Player rewards (increased payouts)
├── Treasury (sustainability)
└── Development (growth)
        ↓
Token gains real backing
```

### Phase 3: Mature Economy (Scale)

```
Multiple biomes, multiple buyers
        ↓
Diversified revenue streams
        ↓
Self-sustaining economy
        ↓
Player-owned, player-governed (DAO)
```

---

## Summary

| Aspect | Traditional Games | The Analog Economy |
|--------|------------------|-------------------|
| Problem tools | Buy or grind | Free, always |
| Collectibles | Loot boxes, RNG | Fixed supply NFTs |
| Trading | Closed or banned | Open, crypto-backed |
| Income sources | 1 (maybe) | 5+ tiers |
| Value portability | None | Full (crypto) |
| Free players | Second-class | Full access to core |
| User creation | Limited/none | Full creator economy |
| Platform revenue | Upfront purchase | Ongoing from activity |

**The Vision:** A world where solving humanity's problems is the most profitable activity, where no one is locked out due to lack of funds, and where players can become entrepreneurs within the game economy.

---

## Related Documentation

- [Blockchain Economy](blockchain-economy.md) - Technical blockchain implementation, smart contracts, NFT architecture
- [Project Overview](../guides/concepts/project-overview.md)
- [Gaian Configuration](../../core-governance/gaian/config.yaml)
- [Directory Structure](../guides/architecture/directory-structure.md)
