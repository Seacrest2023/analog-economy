# Blockchain Economy & Smart Contracts

> "Your labor has value. Your creations have ownership. Your legacy persists beyond the game."

> **Related Documentation:** For player-facing economic design including the creator economy, free-to-play pathways, and AI-powered NPC trading, see [Payments & Economic System](payments.md).

## Table of Contents

1. [Philosophy](#1-philosophy)
2. [Chain Selection](#2-chain-selection)
3. [Token Architecture](#3-token-architecture)
4. [NFT System](#4-nft-system)
5. [In-Game Currency](#5-in-game-currency)
6. [Player-to-Player Trading](#6-player-to-player-trading)
7. [NPC Economy](#7-npc-economy)
8. [Earning Real Value](#8-earning-real-value)
9. [Smart Contract Architecture](#9-smart-contract-architecture)
10. [Wallet Integration](#10-wallet-integration)
11. [Marketplace](#11-marketplace)
12. [Anti-Exploitation](#12-anti-exploitation)
13. [Gas & Transaction Costs](#13-gas--transaction-costs)
14. [Legal Considerations](#14-legal-considerations)
15. [Implementation Roadmap](#15-implementation-roadmap)

---

## 1. Philosophy

### 1.1 Core Economic Principles

```yaml
economic_philosophy:
  primary_goal: "Real value for real contribution"

  principles:
    labor_has_value:
      statement: "Time and skill invested should create tradeable value"
      implementation: "Crafted items, innovations, and contributions are NFTs"

    ownership_is_real:
      statement: "If you own it in-game, you own it for real"
      implementation: "Key assets backed by blockchain"

    economy_serves_gameplay:
      statement: "Blockchain enhances, never obstructs gameplay"
      implementation: "Seamless integration, optional engagement depth"

    scarcity_is_meaningful:
      statement: "Rare things are actually rare"
      implementation: "On-chain supply caps, verifiable scarcity"

  what_we_avoid:
    pay_to_win: "Cannot buy gameplay advantages with real money"
    infinite_inflation: "Token supplies are controlled"
    extraction_focus: "Game must be fun regardless of earning"
    complexity_barrier: "Non-crypto users can play fully"
```

### 1.2 The Two-Layer Economy

```yaml
two_layer_economy:
  layer_1_gameplay:
    description: "Traditional in-game economy"
    currency: "Sila (barley equivalent)"
    transactions: "Off-chain, instant, free"
    use: "Daily gameplay, NPC trades, small transactions"

  layer_2_ownership:
    description: "Blockchain-backed assets"
    tokens: "NFTs, ANALOG token"
    transactions: "On-chain, verified, tradeable"
    use: "Major assets, cross-player trades, real-world value"

  bridge:
    description: "Convert between layers"
    game_to_chain: "Mint craftables as NFTs"
    chain_to_game: "Import owned NFTs into gameplay"
    friction: "Intentional—prevents constant speculation"
```

---

## 2. Chain Selection

### 2.1 Requirements

```yaml
chain_requirements:
  technical:
    throughput: "High TPS for marketplace activity"
    finality: "Fast confirmation for trading"
    cost: "Low gas for accessibility"
    smart_contracts: "Full programmability"

  ecosystem:
    nft_standards: "Established NFT infrastructure"
    marketplace: "Existing secondary markets"
    wallets: "User-friendly wallet options"
    bridges: "Cross-chain interoperability"

  business:
    adoption: "Large user base familiar with chain"
    stability: "Proven, not experimental"
    developer_tools: "Good SDK, documentation"
```

### 2.2 Chain Recommendation

```yaml
recommended_chain:
  primary: "Polygon (MATIC)"

  rationale:
    cost: "Sub-cent transactions"
    speed: "2-second finality"
    ecosystem: "OpenSea, major marketplace support"
    ethereum_compatible: "ERC standards, wide wallet support"
    proven: "Used by major games (Aavegotchi, Sunflower Land)"

  alternative_considerations:
    immutable_x:
      pros: "Gas-free NFT minting, gaming-focused"
      cons: "Smaller ecosystem, less flexibility"

    solana:
      pros: "Very fast, low cost"
      cons: "Different ecosystem, past stability issues"

    arbitrum:
      pros: "Ethereum security, growing ecosystem"
      cons: "Higher costs than Polygon"

  future_proofing:
    strategy: "Abstract chain layer for potential migration"
    bridges: "Enable cross-chain asset movement"
```

---

## 3. Token Architecture

### 3.1 Token Types Overview

```yaml
token_types:
  ANALOG:
    type: "ERC-20 (Fungible)"
    purpose: "Governance, premium transactions, staking"
    supply: "Fixed cap"

  SILA:
    type: "Off-chain (Database)"
    purpose: "Daily gameplay currency"
    supply: "Inflationary (controlled)"

  NFTs:
    type: "ERC-721 / ERC-1155"
    purpose: "Unique assets, ownership"
    categories:
      - "Reincarnation Tickets"
      - "Land Deeds"
      - "Heirlooms"
      - "Blueprints/Innovations"
      - "Crafted Items (rare)"
```

### 3.2 ANALOG Token (Governance Token)

```yaml
ANALOG_token:
  standard: "ERC-20"

  tokenomics:
    total_supply: "1,000,000,000 ANALOG"
    distribution:
      gameplay_rewards: "40% (400M) - Earned through play"
      treasury: "25% (250M) - Development, operations"
      team: "15% (150M) - 4-year vesting"
      early_supporters: "10% (100M) - Early access sales"
      liquidity: "10% (100M) - DEX liquidity"

    vesting:
      team: "4 years, 1 year cliff, monthly thereafter"
      early_supporters: "1 year, quarterly unlocks"
      gameplay: "Released based on milestone achievements"

  utility:
    governance:
      - "Vote on game development priorities"
      - "Vote on economic parameters"
      - "Propose community features"

    premium_features:
      - "Mint NFTs from craftables"
      - "List on premium marketplace slots"
      - "Access exclusive cosmetics"

    staking:
      - "Stake for governance weight"
      - "Stake for marketplace fee reduction"
      - "Stake for priority access to limited items"

  earning_ANALOG:
    methods:
      innovation_codex: "Major contributions earn ANALOG"
      community_achievements: "Server-wide milestones"
      tournament_prizes: "Competitive events"
      bug_bounties: "Testing and feedback"
    note: "NOT earnable through grinding—prevents bot farms"
```

### 3.3 SILA (In-Game Currency)

```yaml
SILA:
  type: "Off-chain database currency"
  NOT_a_cryptocurrency: true

  purpose:
    - "Daily transactions"
    - "NPC trades"
    - "Services and wages"
    - "Small player trades"

  characteristics:
    instant: "No blockchain confirmation needed"
    free: "No gas costs"
    flexible: "Game can adjust for balance"
    non_tradeable: "Cannot sell SILA for real money directly"

  conversion:
    sila_to_analog: "NOT directly convertible"
    indirect_value: "Craft items → Mint NFT → Sell for ANALOG"
    design_intent: "Prevents pure currency farming"

  inflation_control:
    sinks:
      - "NPC purchases"
      - "Service fees"
      - "Death/respawn costs"
      - "NFT minting fees (SILA portion)"
    faucets:
      - "Work wages"
      - "Selling goods to NPCs"
      - "Quest rewards"
    balance: "Monitored and adjusted by game systems"
```

---

## 4. NFT System

### 4.1 NFT Categories

```yaml
nft_categories:
  reincarnation_tickets:
    description: "Right to play as new character"
    standard: "ERC-721"
    supply: "Limited, released in waves"
    traits:
      era_access: "Which eras unlocked"
      bloodline_level: "Starting advantages"
      legacy_points: "Accumulated across lives"
    transferable: true
    use_case: "Entry to game, tradeable value"

  land_deeds:
    description: "Ownership of in-game property"
    standard: "ERC-721"
    supply: "Fixed per era/region"
    traits:
      location: "Specific coordinates"
      size: "Plot dimensions"
      resources: "Available resources on land"
      improvements: "Buildings, infrastructure"
    transferable: true
    rental: "Can rent to other players (control vs ownership)"

  heirlooms:
    description: "Items passed through generations"
    standard: "ERC-721"
    supply: "Created through gameplay, limited minting"
    traits:
      history: "Previous owners, events witnessed"
      bonuses: "Gameplay benefits"
      rarity: "Based on history and age"
    transferable: true
    creation: "Items gain heirloom status over multiple generations"

  blueprints:
    description: "Innovations and recipes"
    standard: "ERC-721"
    supply: "Each innovation can be minted once by discoverer"
    traits:
      innovation_type: "What it creates/enables"
      efficiency: "Quality of the discovery"
      era: "When discovered"
    transferable: true
    royalties: "Original discoverer gets % on uses"

  craftables:
    description: "High-quality crafted items"
    standard: "ERC-1155 (semi-fungible)"
    supply: "Unlimited minting, natural scarcity through effort"
    traits:
      quality: "Craftsmanship level"
      materials: "What it's made from"
      maker: "Who crafted it"
    transferable: true
    threshold: "Only exceptional items (top 10% quality) mintable"
```

### 4.2 NFT Minting Process

```yaml
minting_process:
  requirements:
    must_exist_in_game: "Item/asset must be created through gameplay first"
    quality_threshold: "Must meet minimum quality standards"
    minting_cost:
      sila: "In-game currency portion"
      analog: "Token portion (small)"
      gas: "Blockchain transaction fee"

  workflow:
    1_creation: "Player creates/earns asset in-game"
    2_evaluation: "System evaluates mint eligibility"
    3_request: "Player requests minting"
    4_payment: "Pay minting costs"
    5_minting: "Smart contract creates NFT"
    6_linking: "NFT linked to in-game asset"

  cooldowns:
    per_player: "Max 5 NFT mints per week"
    per_item_type: "Prevents flooding market"
    reason: "Maintain scarcity, prevent exploitation"

  reverse_process:
    nft_to_game: "Import NFT back into active gameplay"
    requirements: "Must own NFT, compatible with current era"
    result: "NFT locked while in active use"
```

### 4.3 NFT Metadata & Traits

```yaml
nft_metadata:
  on_chain:
    owner: "Current wallet address"
    token_id: "Unique identifier"
    contract_address: "Collection address"
    creation_date: "Block timestamp"

  off_chain_ipfs:
    visual: "Image/3D model"
    description: "Item lore and history"
    traits:
      static:
        - "Type"
        - "Era of creation"
        - "Original creator"
      dynamic:
        - "Current condition"
        - "Usage history"
        - "Owners list"

  trait_rarity:
    calculation: "Based on actual distribution"
    display: "Percentage rarity shown"
    updates: "Dynamic as more items created"
```

---

## 5. In-Game Currency

### 5.1 SILA Economy

```yaml
sila_economy:
  earning_sila:
    work:
      farming: "2-5 sila/hour (depending on skill)"
      crafting: "5-20 sila/hour (depending on trade)"
      fishing: "3-8 sila/hour"
      labor: "2-3 sila/hour"

    selling:
      to_npcs: "Fixed prices, always available"
      to_players: "Negotiated prices"
      marketplace: "Auction/listing"

    quests:
      temple_tasks: "5-20 sila"
      community_tasks: "10-50 sila"
      innovation_rewards: "50-500 sila"

  spending_sila:
    necessities:
      food: "2-5 sila/day"
      housing: "5-100 sila/month"
      tools: "10-100 sila"

    services:
      healing: "5-50 sila"
      training: "20-100 sila"
      legal: "10-200 sila"

    luxury:
      jewelry: "20-1000 sila"
      fine_goods: "50-500 sila"

    meta:
      nft_minting: "100-1000 sila (portion of cost)"
      marketplace_fees: "5% of transaction"

  economic_balance:
    target_inflation: "2-5% annual"
    adjustment_mechanisms:
      - "NPC price adjustments"
      - "Sink event creation"
      - "Faucet rate tuning"
```

### 5.2 Historical Accuracy

```yaml
historical_pricing:
  reference_system:
    base_unit: "1 sila = ~1 liter of barley"
    silver_equivalent: "1 shekel silver = ~300 sila"
    daily_wage: "Unskilled laborer = 2-3 sila/day"

  price_examples:
    food:
      barley_1_sila: 1
      bread_loaf: 0.5
      fish_fresh: 2
      beer_jar: 1
      mutton_portion: 8

    goods:
      basic_tunic: 10
      copper_sickle: 25
      pottery_jar: 5
      wooden_stool: 15

    luxury:
      lapis_bead: 50
      gold_earring: 500
      linen_garment: 100

    property:
      reed_hut_rent_month: 10
      small_house_purchase: 1000
      field_plot: 5000
```

---

## 6. Player-to-Player Trading

### 6.1 Trade Types

```yaml
p2p_trade_types:
  direct_trade:
    description: "Face-to-face exchange in-game"
    location: "Must be physically near each other"
    currency: "SILA only"
    items: "Any in-game items"
    blockchain: "Off-chain"
    fees: "None"
    disputes: "In-game legal system"

  marketplace_trade:
    description: "List items for sale to any player"
    location: "Accessible from marketplaces in cities"
    currency: "SILA or ANALOG"
    items: "Any items, NFTs"
    blockchain: "On-chain for NFTs, off-chain for regular items"
    fees: "5% to game treasury"
    disputes: "Automated escrow"

  nft_trade:
    description: "Direct NFT exchange"
    location: "In-game or external marketplaces"
    currency: "ANALOG, ETH, or other NFTs"
    items: "NFTs only"
    blockchain: "Always on-chain"
    fees: "2.5% royalty to original creator, 2.5% to treasury"
    disputes: "Smart contract enforced"

  barter:
    description: "Item-for-item exchange"
    location: "In-game, face-to-face"
    currency: "None—pure trade"
    items: "Any in-game items"
    blockchain: "Off-chain"
    fees: "None"
    disputes: "In-game legal system"
```

### 6.2 Trading Interface

```yaml
trading_interface:
  direct_trade_ui:
    trigger: "Approach player, initiate trade"
    display:
      - "Your offer (items, SILA)"
      - "Their offer (items, SILA)"
      - "Confirm buttons for both"
    security:
      - "Both must confirm"
      - "3-second delay after changes"
      - "Clear display of all items"

  marketplace_ui:
    browse:
      - "Search by item type"
      - "Filter by price, era, quality"
      - "Sort by newest, cheapest, rarest"

    sell:
      - "Select item from inventory"
      - "Set price (fixed or auction)"
      - "Set duration"
      - "Pay listing fee"

    buy:
      - "View item details"
      - "Verify authenticity (for NFTs)"
      - "Confirm purchase"
      - "Automatic delivery"

  nft_marketplace:
    internal: "In-game NFT trading"
    external: "OpenSea, etc. integration"
    display:
      - "Full trait breakdown"
      - "Price history"
      - "Ownership history"
      - "Rarity ranking"
```

### 6.3 Escrow System

```yaml
escrow:
  purpose: "Secure trades between untrusting parties"

  for_sila_trades:
    mechanism: "Game server holds items/currency"
    process:
      1: "Seller lists item"
      2: "Buyer pays to escrow"
      3: "Item transferred to buyer"
      4: "SILA released to seller"
    dispute: "Support ticket, evidence review"

  for_nft_trades:
    mechanism: "Smart contract escrow"
    process:
      1: "Seller approves NFT to escrow contract"
      2: "Buyer sends payment to escrow contract"
      3: "Contract atomically swaps"
    dispute: "None possible—atomic swap"

  for_complex_deals:
    mechanism: "Multi-sig escrow"
    use_case: "Large land deals, business sales"
    process:
      1: "Both parties agree to terms"
      2: "Both deposit to escrow"
      3: "Conditions verified"
      4: "Release to both parties"
    arbiter: "Optional third party for disputes"
```

---

## 7. NPC Economy

### 7.1 NPC Trading

```yaml
npc_trading:
  buy_from_npcs:
    availability: "Always available"
    prices: "Fixed, slightly above player market"
    purpose: "Price ceiling, consistent supply"
    examples:
      tool_merchant: "Sells basic tools at set prices"
      food_vendor: "Sells food staples"
      temple_shop: "Sells religious items"

  sell_to_npcs:
    availability: "Always available"
    prices: "Fixed, slightly below player market"
    purpose: "Price floor, guaranteed liquidity"
    examples:
      grain_buyer: "Buys crops at base prices"
      scrap_dealer: "Buys damaged goods"
      temple_offering: "Accepts donations"

  price_dynamics:
    static_base: "Core prices don't change"
    supply_adjustment: "Bulk sales may reduce price temporarily"
    seasonal: "Some prices vary by season"
    event_driven: "Festivals, disasters affect prices"
```

### 7.2 NPC Services

```yaml
npc_services:
  paid_services:
    healing:
      asu_physician: "10-50 sila depending on ailment"
      asipu_exorcist: "20-100 sila"
      temple_healing: "Offering-based"

    training:
      craft_master: "50-200 sila for skill advancement"
      combat_trainer: "30-100 sila"
      scribe_lessons: "100-500 sila (literacy)"

    legal:
      contract_writing: "10-50 sila"
      court_representation: "50-200 sila"
      property_registration: "20-100 sila"

    transport:
      boat_passage: "5-20 sila"
      caravan_join: "10-50 sila"
      messenger: "5-30 sila"

  free_services:
    temple_public: "Basic religious services"
    information: "Gossip, directions"
    emergency: "Disaster response"
```

### 7.3 Economic Sinks

```yaml
economic_sinks:
  purpose: "Remove SILA from circulation to prevent inflation"

  sinks:
    npc_purchases:
      description: "Buying from NPCs removes SILA"
      impact: "Major sink"

    service_fees:
      description: "Paying for services"
      impact: "Moderate sink"

    death_costs:
      description: "Funeral expenses, restart costs"
      impact: "Moderate sink"

    taxes_and_tithes:
      description: "Temple obligations, property taxes"
      impact: "Consistent sink"

    item_degradation:
      description: "Repair costs for worn items"
      impact: "Ongoing sink"

    minting_fees:
      description: "SILA portion of NFT minting"
      impact: "Variable sink"

    luxury_consumption:
      description: "Cosmetics, decorations, feasts"
      impact: "Voluntary sink"

  monitoring:
    metrics:
      - "Total SILA in circulation"
      - "Daily SILA created vs destroyed"
      - "Average player wealth"
      - "Price index stability"
    adjustment: "Tune sink/faucet rates to maintain balance"
```

---

## 8. Earning Real Value

### 8.1 Value Extraction Pathways

```yaml
earning_pathways:
  pathway_1_crafting:
    description: "Create valuable items, mint as NFT, sell"
    steps:
      1: "Master a craft through gameplay"
      2: "Create exceptional quality items"
      3: "Mint best items as NFTs"
      4: "Sell NFTs for ANALOG or ETH"
      5: "Convert to fiat via exchanges"
    skill_required: "High crafting skill"
    time_investment: "Significant"
    earning_potential: "Variable, based on market demand"

  pathway_2_innovation:
    description: "Discover innovations, earn royalties"
    steps:
      1: "Discover new innovation through gameplay"
      2: "Mint innovation as Blueprint NFT"
      3: "Other players use your innovation"
      4: "Earn royalty on each use"
    skill_required: "Problem-solving, experimentation"
    time_investment: "Very significant"
    earning_potential: "Passive income stream"

  pathway_3_land:
    description: "Own land, develop it, earn rent"
    steps:
      1: "Acquire Land Deed NFT"
      2: "Develop property (buildings, farms)"
      3: "Rent to other players"
      4: "Collect rent in ANALOG"
    skill_required: "Capital investment"
    time_investment: "Management ongoing"
    earning_potential: "Steady passive income"

  pathway_4_tournament:
    description: "Compete in events, win prizes"
    steps:
      1: "Enter competitive events"
      2: "Win or place highly"
      3: "Receive ANALOG prizes"
    skill_required: "Gameplay mastery"
    time_investment: "Event-based"
    earning_potential: "High variance"

  pathway_5_contribution:
    description: "Contribute to game development"
    steps:
      1: "Create content (art, lore, guides)"
      2: "Submit to official programs"
      3: "Approved content earns ANALOG"
    skill_required: "Creative skills"
    time_investment: "Variable"
    earning_potential: "Based on contribution quality"
```

### 8.2 Cash Out Process

```yaml
cash_out:
  analog_to_fiat:
    pathway: "ANALOG → DEX → ETH/USDC → CEX → Bank"
    steps:
      1: "Have ANALOG in wallet"
      2: "Swap on DEX (Uniswap, QuickSwap)"
      3: "Receive ETH or stablecoin"
      4: "Transfer to centralized exchange"
      5: "Sell for fiat"
      6: "Withdraw to bank"
    fees: "DEX swap fees, CEX fees, withdrawal fees"
    time: "Minutes to days depending on exchange"

  nft_to_fiat:
    pathway: "NFT → Marketplace → ETH → CEX → Bank"
    steps:
      1: "List NFT on marketplace"
      2: "Buyer purchases with ETH/MATIC"
      3: "Receive payment minus fees"
      4: "Convert to fiat via exchange"
    fees: "Marketplace fees (2.5-5%), conversion fees"
    time: "Depends on sale speed"

  important_notes:
    tax_implications: "Players responsible for tax reporting"
    regional_restrictions: "Some regions may restrict crypto"
    exchange_requirements: "KYC may be required for large amounts"
```

### 8.3 Earning Caps and Limits

```yaml
earning_limits:
  purpose: "Prevent exploitation, maintain game integrity"

  daily_limits:
    nft_minting: "5 per day per account"
    marketplace_listings: "50 per day"
    reason: "Prevent flooding, maintain quality"

  anti_bot_measures:
    captcha: "For high-value transactions"
    behavior_analysis: "Flag suspicious patterns"
    account_verification: "For large withdrawals"

  minimum_thresholds:
    nft_minting: "Item must meet quality threshold"
    withdrawal: "Minimum ANALOG to withdraw"
    reason: "Prevent dust transactions"
```

---

## 9. Smart Contract Architecture

### 9.1 Contract Overview

```yaml
smart_contracts:
  core_contracts:
    ANALOG_token:
      type: "ERC-20"
      functions:
        - "transfer"
        - "approve"
        - "stake"
        - "governance_vote"

    NFT_collection:
      type: "ERC-721"
      functions:
        - "mint"
        - "burn"
        - "transfer"
        - "update_metadata"

    marketplace:
      type: "Custom"
      functions:
        - "list_item"
        - "buy_item"
        - "cancel_listing"
        - "make_offer"
        - "accept_offer"

    escrow:
      type: "Custom"
      functions:
        - "create_escrow"
        - "deposit"
        - "release"
        - "dispute"

    royalty_splitter:
      type: "Custom"
      functions:
        - "register_creator"
        - "distribute_royalties"
        - "claim_earnings"

    governance:
      type: "Custom"
      functions:
        - "propose"
        - "vote"
        - "execute"
        - "cancel"
```

### 9.2 Contract Security

```yaml
security_measures:
  audits:
    requirement: "Full audit before mainnet"
    auditors: "Top-tier firms (OpenZeppelin, Trail of Bits)"
    scope: "All deployed contracts"
    frequency: "Before major upgrades"

  patterns:
    reentrancy: "ReentrancyGuard on all external calls"
    access_control: "Role-based permissions"
    upgradability: "Proxy pattern for future fixes"
    pausability: "Emergency pause mechanism"

  testing:
    unit_tests: "100% function coverage"
    integration_tests: "Full flow testing"
    fuzzing: "Automated edge case discovery"
    formal_verification: "For critical functions"

  monitoring:
    alerts: "Unusual transaction patterns"
    rate_limits: "Per-address transaction limits"
    circuit_breakers: "Automatic pause on anomalies"
```

### 9.3 Upgradability

```yaml
upgradability:
  pattern: "Transparent Proxy (OpenZeppelin)"

  governance:
    who_can_upgrade: "Multisig + timelock"
    timelock: "48 hours minimum"
    notification: "Community announcement required"

  migration:
    data_preservation: "State maintained across upgrades"
    user_action: "None required for upgrades"
    rollback: "Emergency rollback procedure documented"
```

---

## 10. Wallet Integration

### 10.1 Supported Wallets

```yaml
wallet_support:
  primary:
    metamask:
      type: "Browser extension, mobile"
      support: "Full integration"

    walletconnect:
      type: "Protocol (many wallets)"
      support: "Full integration"

  secondary:
    coinbase_wallet:
      type: "Mobile, browser"
      support: "Via WalletConnect"

    rainbow:
      type: "Mobile"
      support: "Via WalletConnect"

  embedded:
    game_wallet:
      type: "Custodial option for beginners"
      features:
        - "Created with email"
        - "No seed phrase management"
        - "Can export to self-custody later"
      limitations:
        - "Lower withdrawal limits"
        - "Requires identity verification for large amounts"
```

### 10.2 Wallet UX

```yaml
wallet_ux:
  non_crypto_users:
    goal: "Play without knowing it's blockchain"
    implementation:
      - "Email login creates embedded wallet"
      - "All transactions abstracted"
      - "SILA shown, not ANALOG/gas"
      - "NFT ownership invisible unless exported"

  crypto_users:
    goal: "Full control and transparency"
    implementation:
      - "Connect external wallet"
      - "See all on-chain assets"
      - "Direct marketplace access"
      - "Export/import NFTs freely"

  hybrid:
    goal: "Gradual onboarding"
    implementation:
      - "Start with embedded wallet"
      - "Tutorial on self-custody"
      - "Easy migration path"
      - "Incentives for self-custody"
```

### 10.3 Transaction Signing

```yaml
transaction_signing:
  visible_transactions:
    when:
      - "Minting NFT"
      - "Trading NFT"
      - "Withdrawing ANALOG"
    ux: "Clear explanation of what's being signed"

  invisible_transactions:
    when:
      - "Daily gameplay"
      - "SILA trades"
      - "NPC interactions"
    ux: "No wallet interaction needed"

  batch_transactions:
    when: "Multiple NFT operations"
    ux: "Single signature for multiple actions"
```

---

## 11. Marketplace

### 11.1 Internal Marketplace

```yaml
internal_marketplace:
  location: "Accessible from in-game market areas"

  features:
    listings:
      - "Fixed price"
      - "Auction (timed)"
      - "Accepting offers"

    search:
      - "By item type"
      - "By era"
      - "By price range"
      - "By seller"

    filters:
      - "NFT only / SILA only"
      - "Verified sellers"
      - "Price history"

  fees:
    listing_fee: "Free"
    sale_fee: "5% of sale price"
    royalty: "2.5% to original creator (NFTs)"

  settlement:
    sila_trades: "Instant"
    nft_trades: "On-chain confirmation (~30 seconds)"
```

### 11.2 External Marketplace Integration

```yaml
external_marketplaces:
  opensea:
    integration: "Full metadata support"
    royalties: "Enforced via contract"
    benefits: "Exposure to wider audience"

  rarible:
    integration: "Supported"
    royalties: "Honored"

  custom_trades:
    support: "Direct wallet-to-wallet supported"
    warning: "Recommend using escrow"
```

### 11.3 Price Discovery

```yaml
price_discovery:
  mechanisms:
    auction: "True price discovery for rare items"
    fixed_price: "Seller sets, market responds"
    offers: "Buyers propose prices"

  price_history:
    display: "Last 10 sales of similar items"
    chart: "Price trend over time"
    floor_price: "Lowest current listing"

  recommendations:
    to_sellers: "Suggested price based on comparables"
    to_buyers: "Fair value estimate"
```

---

## 12. Anti-Exploitation

### 12.1 Bot Prevention

```yaml
bot_prevention:
  detection:
    behavior_analysis:
      - "Inhuman click patterns"
      - "Repetitive exact actions"
      - "24/7 activity without breaks"
      - "Impossible reaction times"

    network_analysis:
      - "Multiple accounts same IP"
      - "VPN/proxy detection"
      - "Device fingerprinting"

  prevention:
    captcha: "On high-value actions"
    rate_limits: "Actions per time period"
    cooldowns: "Between similar actions"
    verification: "For suspicious accounts"

  penalties:
    warning: "First offense"
    restriction: "Limited functionality"
    ban: "Repeat offenders"
    asset_freeze: "Pending investigation"
```

### 12.2 Multi-Accounting

```yaml
multi_accounting:
  policy: "One primary account per person"

  detection:
    - "Device fingerprinting"
    - "Behavioral similarity"
    - "Transaction patterns"
    - "IP correlation"

  allowed_exceptions:
    - "Family members (different devices)"
    - "Content creators (disclosed)"

  enforcement:
    - "Linked accounts flagged"
    - "Earnings consolidated"
    - "Abuse = all accounts banned"
```

### 12.3 Economic Exploits

```yaml
exploit_prevention:
  duplication:
    prevention: "Atomic transactions, idempotency keys"
    detection: "Balance monitoring"
    response: "Automatic rollback"

  market_manipulation:
    wash_trading:
      detection: "Same-wallet trades flagged"
      prevention: "Fees make it unprofitable"

    price_manipulation:
      detection: "Unusual price movements"
      prevention: "Circuit breakers on extreme moves"

    insider_trading:
      prevention: "No advance info on game changes"
      policy: "Team cannot trade during sensitive periods"
```

---

## 13. Gas & Transaction Costs

### 13.1 Gas Strategy

```yaml
gas_strategy:
  player_pays:
    when:
      - "Minting NFT"
      - "Trading on external marketplace"
      - "Withdrawing to external wallet"
    mitigation: "Show gas estimate before action"

  game_pays:
    when:
      - "Distributing rewards"
      - "Updating NFT metadata"
      - "System operations"
    funding: "Treasury allocation"

  gas_optimization:
    batching: "Combine multiple operations"
    off_peak: "Suggest low-gas times"
    layer2: "Polygon for low costs"
```

### 13.2 Fee Structure

```yaml
fees:
  marketplace:
    sale_fee: "5% of sale price"
    split:
      treasury: "2.5%"
      creator_royalty: "2.5%"

  minting:
    sila_cost: "100-1000 SILA (varies by item)"
    analog_cost: "1-10 ANALOG (varies by item)"
    gas: "Player pays (minimal on Polygon)"

  withdrawal:
    minimum: "100 ANALOG"
    fee: "1% or 5 ANALOG (whichever greater)"

  staking:
    deposit: "Free"
    withdrawal: "Free"
    rewards: "Distributed automatically"
```

---

## 14. Legal Considerations

### 14.1 Regulatory Compliance

```yaml
compliance:
  token_classification:
    analog: "Utility token (governance, access)"
    nfts: "Digital collectibles"
    sila: "In-game currency (not security)"

  jurisdictions:
    prohibited: "List of restricted countries"
    restricted: "Limited functionality regions"
    full_access: "Most jurisdictions"

  kyc_aml:
    when_required:
      - "Large withdrawals (>$10K equivalent)"
      - "Suspicious activity flags"
      - "Regulatory requirement"
    provider: "Third-party KYC service"
    data: "Minimized, securely stored"

  terms_of_service:
    ownership: "Clear IP rights"
    liability: "Market risks disclosed"
    taxation: "User responsibility stated"
```

### 14.2 User Protections

```yaml
user_protections:
  transparency:
    - "Clear fee disclosure"
    - "Transaction confirmation screens"
    - "Price history available"

  dispute_resolution:
    - "Internal appeals process"
    - "Arbitration for significant disputes"
    - "Smart contract is final for on-chain"

  data_privacy:
    - "Wallet addresses pseudonymous"
    - "Personal data (if collected) protected"
    - "GDPR compliance where applicable"
```

---

## 15. Implementation Roadmap

### 15.1 Phase 1: Foundation

```yaml
phase_1:
  timeline: "Months 1-3 of development"

  deliverables:
    - "ANALOG token contract (testnet)"
    - "Basic NFT contract (testnet)"
    - "Embedded wallet integration"
    - "SILA database system"
    - "Basic marketplace (SILA only)"

  testing:
    - "Internal testing"
    - "Small closed alpha"
```

### 15.2 Phase 2: NFT Integration

```yaml
phase_2:
  timeline: "Months 4-6"

  deliverables:
    - "Full NFT minting system"
    - "NFT marketplace (internal)"
    - "External wallet support"
    - "Royalty system"

  testing:
    - "Expanded alpha"
    - "Security audit"
```

### 15.3 Phase 3: Full Economy

```yaml
phase_3:
  timeline: "Months 7-9"

  deliverables:
    - "ANALOG mainnet launch"
    - "External marketplace integration"
    - "Staking system"
    - "Governance launch"

  testing:
    - "Open beta"
    - "Economic stress testing"
```

### 15.4 Phase 4: Maturity

```yaml
phase_4:
  timeline: "Post-launch"

  deliverables:
    - "Advanced trading features"
    - "Cross-chain bridges"
    - "Developer API"
    - "Third-party integrations"

  ongoing:
    - "Economic monitoring"
    - "Feature iteration"
    - "Regulatory adaptation"
```

---

## Appendix: Quick Reference

### Token Summary

| Token | Type | Supply | On-Chain | Tradeable |
|-------|------|--------|----------|-----------|
| ANALOG | ERC-20 | 1B fixed | Yes | Yes |
| SILA | Database | Inflationary | No | In-game only |
| Tickets | ERC-721 | Limited waves | Yes | Yes |
| Land | ERC-721 | Fixed per region | Yes | Yes |
| Heirlooms | ERC-721 | Player-created | Yes | Yes |
| Blueprints | ERC-721 | 1 per innovation | Yes | Yes |
| Craftables | ERC-1155 | Unlimited (quality gate) | Yes | Yes |

### Fee Summary

| Action | Cost |
|--------|------|
| Marketplace sale | 5% (2.5% treasury, 2.5% creator) |
| NFT minting | 100-1000 SILA + 1-10 ANALOG + gas |
| ANALOG withdrawal | 1% or 5 ANALOG minimum |
| SILA trades | Free |
| NPC transactions | Free |

---

*"What you create, you own. What you own, you can trade. What you trade, has value."*
