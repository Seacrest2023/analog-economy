# Legal & Justice System

> *"The tablet speaks truth. The oath binds the soul. The river knows guilt from innocence. In Eridu, justice is not opinion—it is procedure."*

## Overview

The Sumerian legal system predates Hammurabi by nearly 300 years and is notably more humane—favoring fines over mutilation. This spec covers the court hierarchy, evidence and procedures, the sacred oath system, the dramatic River Ordeal, and the pre-Hammurabi Code of Ur-Nammu that governs Eridu.

---

## Design Philosophy

### Core Principles

1. **Restorative Justice**: Fines and compensation over punishment
2. **Written Evidence**: Clay tablets as binding truth
3. **Divine Witness**: Oaths before gods carry weight
4. **Procedural Fairness**: Established processes protect all
5. **Training Data Value**: Legal reasoning, evidence evaluation, ethical judgment

### The Sumerian Difference

```yaml
legal_philosophy:
  hammurabi_later:
    famous_for: "Eye for an eye"
    era: "1754 BCE (later)"
    approach: "Talion (matching punishment)"

  ur_nammu_earlier:
    our_era: "2100-2050 BCE inspiration"
    approach: "Monetary compensation"
    principle: "Pay for damage, don't suffer it"

  gameplay_implication:
    injured_eye: "Attacker pays silver, keeps own eye"
    theft: "Return goods + penalty payment"
    murder: "Death penalty (exception)"
```

---

## Court Hierarchy

### The Three Levels

```yaml
court_system:
  level_1_local_assembly:
    name: "Ukkin"
    composition: "Council of elders (7-12 citizens)"
    jurisdiction:
      - "Property disputes"
      - "Contract disagreements"
      - "Minor injuries"
      - "Family matters"
    procedure: "Oral testimony, community standards"
    binding: "Yes, for local matters"
    appeal: "To temple court"

  level_2_temple_court:
    name: "Di-Kud (Temple Judges)"
    composition: "Priests of Utu/Shamash (sun god of justice)"
    jurisdiction:
      - "Cases requiring divine witness"
      - "Oaths and sacred contracts"
      - "Serious property disputes"
      - "Appeals from local assembly"
    procedure: "Formal process, divine elements"
    binding: "Yes, with religious sanction"
    appeal: "To royal court (rare)"

  level_3_royal_court:
    name: "King's Justice"
    composition: "King or appointed official"
    jurisdiction:
      - "Capital crimes"
      - "Appeals from lower courts"
      - "Official misconduct"
      - "Interstate disputes"
    procedure: "Formal hearing, written records"
    binding: "Absolute"
    appeal: "None"
```

### Court Personnel

```yaml
court_roles:
  di_kud:
    title: "Judge"
    qualification: "Appointed by temple or king"
    duties: "Hear cases, render judgment"
    status: "High respect"

  mashkim:
    title: "Bailiff/Court Officer"
    duties: "Summon parties, maintain order"
    authority: "Enforce attendance"

  dub_sar:
    title: "Court Scribe"
    duties: "Record proceedings, verdicts"
    importance: "Creates binding documentation"

  witnesses:
    role: "Provide testimony"
    requirement: "Oath before speaking"
    liability: "Perjury is punishable"
```

---

## Evidence and Procedure

### The Tablet as Truth

```yaml
written_evidence:
  principle: "A valid contract on clay is binding law"

  requirements:
    tablet: "Proper clay document"
    witnesses: "2-3 named individuals"
    seal: "Cylinder seal impression"
    content: "Clear terms"

  evidentiary_weight:
    with_tablet: "Presumed valid"
    without_tablet: "Must rely on witnesses"
    conflicting_tablets: "Examine seals, witnesses"

  lost_tablet:
    process: "Court decree based on witness testimony"
    requirement: "Multiple witnesses agree"
    result: "Court creates replacement record"
```

### Witness Testimony

```yaml
witness_rules:
  requirements:
    oath: "Must swear before gods first"
    standing: "Generally free citizens"
    number: "More witnesses = stronger case"

  credibility_factors:
    status: "Higher status = more weight"
    reputation: "Known honest = more weight"
    consistency: "Matching testimony = more weight"
    relationship: "Neutral parties preferred"

  limitations:
    slaves: "Limited testimony rights"
    women: "Context dependent"
    children: "Generally not accepted"
    enemies: "Suspect testimony"
```

### Divine Oath

```yaml
oath_system:
  process:
    location: "Before divine symbol (sun disk, water vessel)"
    words: "Standardized oath formula"
    action: "Touch sacred object"
    witness: "Priest and parties present"

  power:
    belief: "Gods will punish liars"
    effectiveness: "Extremely high deterrent"
    consequence: "Divine wrath for perjury"

  oath_types:
    assertory:
      purpose: "Swear something is true"
      example: "I did not steal the grain"

    promissory:
      purpose: "Swear to future action"
      example: "I will repay by harvest"

    purgatory:
      purpose: "Clear accusation"
      example: "I had no part in this crime"

  gameplay:
    karma_impact:
      true_oath: "No effect"
      false_oath: "-25 karma + divine disfavor"
    detection: "Random bad events increase after false oath"
```

### False Accusation

```yaml
false_accusation:
  principle: "Prevent frivolous lawsuits"

  rule:
    failure_to_prove:
      consequence: "Accuser pays proposed penalty"
      rationale: "Risk deters false claims"

  example:
    scenario: "A accuses B of theft (10 silver penalty)"
    if_proven: "B pays 10 silver to A"
    if_not_proven: "A pays 10 silver to B"

  gameplay:
    consideration: "Think carefully before accusing"
    evidence: "Gather proof before court"
    risk: "Losing costs you"
```

---

## The River Ordeal

### The Ultimate Test

```yaml
river_ordeal:
  trigger: "No witnesses, word against word"
  purpose: "Divine judgment when humans cannot decide"
  rarity: "Last resort only"

  process:
    preparation:
      step_1: "Both parties go to sacred canal"
      step_2: "Priests invoke river god"
      step_3: "Accused prepared for ordeal"

    execution:
      step_4: "Accused thrown into water"
      step_5: "River god judges"
      step_6: "Outcome determines guilt"

    outcomes:
      survived:
        meaning: "River god declares innocent"
        result: "Accuser pays fine to defendant"
        reputation: "Vindication"

      drowned:
        meaning: "River god declares guilty"
        result: "Case closed, property to accuser"
        note: "Death is the punishment"
```

### Gameplay Mechanics

```yaml
ordeal_mechanics:
  factors_affecting_survival:
    karma:
      high: "Significant survival bonus"
      neutral: "Standard odds"
      low: "Survival penalty"

    swimming_skill:
      effect: "Helps but not guaranteed"
      note: "Divine will overrides skill"

    divine_favor:
      temple_service: "Improves odds"
      neglect: "Worsens odds"

    truth:
      innocent: "Hidden bonus"
      guilty: "Hidden penalty"
      note: "System knows the truth"

  dramatic_elements:
    crowd: "Spectators gather"
    tension: "Life or death moment"
    priests: "Officiating, praying"
    aftermath: "Major reputation event"

  refusing_ordeal:
    allowed: "Yes, but..."
    consequence: "Presumed guilty"
    alternative: "Heavy fine or confession"

  sila_reward:
    survive_ordeal: 100
    proven_innocent: "Major karma boost"
```

---

## The Code of Ur-Nammu

### Penalty Structure

```yaml
penalty_schedule:
  physical_injuries:
    eye_injury:
      penalty: "Half-mina silver (~250g)"
      comparison: "NOT losing your own eye"

    broken_bone:
      penalty: "10 shekels silver"
      note: "Compensation, not retaliation"

    knocked_out_tooth:
      penalty: "2 shekels silver"

    cut_off_nose:
      penalty: "Two-thirds mina silver"

    severed_foot:
      penalty: "10 shekels silver"

  property_crimes:
    theft:
      penalty: "Return goods + 2x value"
      repeat: "Increased penalty"

    damage_to_property:
      penalty: "Full replacement value"

    trespass:
      penalty: "Fine based on damage"

  contract_violations:
    breach:
      penalty: "Fulfill contract + penalty"

    fraud:
      penalty: "Return value + multiple fine"
```

### Capital Crimes

```yaml
capital_offenses:
  murder:
    penalty: "Death"
    exception: "Self-defense (no penalty)"
    process: "Royal court judgment"

  robbery:
    penalty: "Death"
    definition: "Violent theft"
    note: "Theft without violence = fines"

  rape:
    penalty: "Death"
    process: "Temple or royal court"

  adultery:
    female_adultery:
      penalty: "Death for woman"
      historical: "Gendered law"
      gameplay: "Reflects historical reality"

    male_adultery:
      penalty: "Fine to husband"
      note: "Less severe (historical)"

  treason:
    penalty: "Death"
    scope: "Against king or city"

  sorcery:
    penalty: "Death or severe punishment"
    proof: "Difficult to establish"
```

### Marriage and Family

```yaml
marriage_law:
  divorce:
    husband_initiated:
      without_cause:
        penalty: "Pay wife mina silver"
        property: "Wife keeps dowry"

      with_cause:
        causes: "Adultery, childlessness, dereliction"
        penalty: "Reduced or none"

    wife_initiated:
      rare: "Difficult but possible"
      grounds: "Abuse, neglect, impotence"

  inheritance:
    sons: "Primary heirs"
    daughters: "Dowry portion"
    widow: "Usufruct rights (use, not own)"

  adoption:
    process: "Formal contract"
    rights: "Equal to birth children"

  bride_price:
    payer: "Groom's family"
    purpose: "Compensation to bride's family"
    return: "If marriage fails without cause"
```

---

## Court Procedures

### Initiating a Case

```yaml
case_initiation:
  step_1_complaint:
    action: "Plaintiff states grievance"
    location: "Court or official"
    record: "Scribe documents"

  step_2_summons:
    action: "Mashkim summons defendant"
    deadline: "Appear by set date"
    failure: "Default judgment possible"

  step_3_response:
    action: "Defendant answers charges"
    options:
      - "Admit (negotiate penalty)"
      - "Deny (proceed to trial)"
      - "Counter-claim"

  step_4_evidence:
    action: "Both sides present proof"
    types:
      - "Tablets/contracts"
      - "Witnesses"
      - "Oaths"
      - "Physical evidence"

  step_5_judgment:
    action: "Court renders decision"
    record: "Written verdict"
    appeal: "To higher court if grounds exist"

  step_6_enforcement:
    action: "Ensure compliance"
    methods:
      - "Voluntary compliance"
      - "Seizure of property"
      - "Community enforcement"
```

### Representation

```yaml
representation:
  self_representation:
    norm: "Most people represent themselves"
    skill: "Speaking ability matters"

  advocates:
    existence: "No formal lawyers"
    informal: "Knowledgeable friends may help"
    scribes: "Can explain procedures"

  interpreters:
    when: "Foreign parties"
    role: "Translate testimony"
```

---

## Player Paths in Law

### Legal Careers

```yaml
legal_paths:
  court_scribe:
    requirements: "Literacy (cuneiform)"
    duties: "Record proceedings"
    income: "Per-case fees + reputation"
    progression: "To senior positions"

  witness_for_hire:
    caution: "Ethical concerns"
    legitimate: "Witness contracts you observed"
    problematic: "False testimony"
    karma: "False witness = severe penalty"

  elder_council:
    requirements: "Age, reputation, land ownership"
    duties: "Decide local disputes"
    status: "Community respect"
    income: "Prestige + small fees"

  mashkim:
    requirements: "Physical ability, reputation"
    duties: "Court enforcement"
    authority: "Official power"
    income: "Salary + fees"
```

### Using the Courts

```yaml
player_litigation:
  as_plaintiff:
    prepare: "Gather evidence first"
    risk: "False accusation penalty"
    cost: "Court fees"
    reward: "Compensation if win"

  as_defendant:
    prepare: "Counter-evidence"
    options: "Settlement, trial, ordeal"
    risk: "Penalty if lose"

  as_witness:
    duty: "Truthful testimony"
    oath: "Before speaking"
    risk: "Perjury punishment"
```

---

## Karma Integration

```yaml
karma_legal_actions:
  positive:
    honest_testimony: "+3"
    help_innocent: "+10"
    fair_judgment: "+5"
    settle_fairly: "+3"

  negative:
    false_accusation: "-15"
    perjury: "-25"
    bribery: "-20"
    false_oath: "-25"
    obstruction: "-10"

  neutral:
    use_legal_system: "No karma effect"
    win_legitimate_case: "No karma effect"
    pay_legitimate_fine: "No karma effect"
```

---

## Training Data Value

### Knowledge Capture

```yaml
training_data:
  legal_reasoning:
    - "Evidence evaluation"
    - "Witness credibility assessment"
    - "Penalty proportionality"

  ethical_judgment:
    - "Fairness in disputes"
    - "Truth vs. self-interest"
    - "Justice vs. mercy"

  procedural_knowledge:
    - "Court processes"
    - "Documentation requirements"
    - "Appeal procedures"

  conflict_resolution:
    - "Negotiation strategies"
    - "Settlement terms"
    - "Relationship preservation"
```

---

## Implementation Notes

### Database Schema

```yaml
legal_records:
  case_record:
    case_id: uuid
    plaintiff_id: uuid
    defendant_id: uuid
    court_level: enum
    charges: array
    evidence: array
    witnesses: array
    verdict: object
    status: enum
    timestamp: datetime

  verdict_record:
    verdict_id: uuid
    case_id: uuid
    outcome: enum
    penalties: array
    enforced: boolean

  oath_record:
    oath_id: uuid
    swearer_id: uuid
    content: text
    truthful: boolean  # Hidden, affects karma
    timestamp: datetime
```

---

## Appendix: Sumerian Legal Terms

| Term | Meaning | Gameplay Role |
|------|---------|---------------|
| **Di-Kud** | Judge | Court authority |
| **Ukkin** | Assembly | Local court |
| **Mashkim** | Bailiff | Court officer |
| **Dub-Sar** | Scribe | Record keeper |
| **Nam-Erim** | Oath | Sacred testimony |
| **Kislah** | Ordeal | Divine judgment |

---

*"Justice in Eridu is not vengeance wearing a mask. It is the restoration of balance—what was taken, returned; what was broken, mended; what was violated, acknowledged. Only for the gravest sins does the city demand a life."*
