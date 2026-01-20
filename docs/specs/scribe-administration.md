# Scribe & Administration

> *"The stylus is mightier than the spear. While the soldier conquers cities, the scribe conquers time itself—for what is written in clay endures when memory fails and heroes are forgotten."*

## Overview

The Dubsar (scribe) is the operating system of Eridu. In a largely illiterate society, scribes hold immense power by controlling the flow of information. They record transactions, draft contracts, manage temple accounts, and preserve knowledge. This spec covers the Edubba (scribal school), career paths, document types, and the economics of literacy.

---

## Design Philosophy

### Core Principles

1. **Literacy as Power**: Reading and writing are rare, valuable skills
2. **Multi-Year Training**: Becoming a scribe is a significant investment
3. **Career Diversity**: From village notary to palace administrator
4. **Document Mastery**: Different documents require different expertise
5. **Training Data Value**: Record-keeping, administrative reasoning, knowledge preservation

### The Literacy Gap

```yaml
literacy_reality:
  population: "95%+ cannot read or write"

  literate_classes:
    scribes: "Professional writers"
    some_priests: "Temple administration"
    some_merchants: "Basic numeracy"
    royalty: "Variable"

  consequence:
    power: "Scribes mediate all written transactions"
    trust: "Society depends on scribe honesty"
    value: "Literate skills command premium prices"
```

---

## The Edubba (Scribal School)

### Overview

```yaml
edubba:
  translation: "Tablet House"
  type: "Private institution"
  funding: "Tuition from wealthy families"
  purpose: "Train professional scribes"

  admission:
    age: "5-8 years old typical"
    gender: "Primarily male (some female exceptions)"
    class: "Wealthy families only (tuition expensive)"
    selection: "Father's decision and ability to pay"
```

### Curriculum

```yaml
edubba_curriculum:
  stage_1_elementary:
    duration: "1-2 years"
    focus: "Physical skills and basics"

    skills:
      clay_preparation:
        description: "Knead clay to proper consistency"
        sila_reward: 10

      stylus_handling:
        description: "Hold and control reed stylus"
        sila_reward: 10

      basic_wedges:
        description: "Form fundamental cuneiform shapes"
        sila_reward: 15

      copying_simple:
        description: "Reproduce basic signs"
        sila_reward: 15

  stage_2_intermediate:
    duration: "2-3 years"
    focus: "Vocabulary and mathematics"

    skills:
      lexical_lists:
        description: "Memorize thousands of nouns"
        content: "Animals, plants, minerals, tools, gods"
        sila_reward: 40

      mathematical_tables:
        description: "Multiplication, division, reciprocals"
        sila_reward: 35

      metrological_lists:
        description: "Weights, measures, capacities"
        sila_reward: 30

      proverbs:
        description: "Wisdom literature"
        sila_reward: 25

  stage_3_advanced:
    duration: "2-4 years"
    focus: "Literature and professional skills"

    skills:
      sumerian_literature:
        description: "Copy major literary works"
        content: "Gilgamesh, myths, hymns"
        sila_reward: 75

      model_contracts:
        description: "Learn legal formulas"
        sila_reward: 60

      mathematical_problems:
        description: "Complex calculations, surveying"
        sila_reward: 50

      specialized_vocabulary:
        description: "Professional terminology"
        sila_reward: 50
```

### School Life

```yaml
school_discipline:
  strictness: "Severe"

  punishments:
    caning: "For errors in penmanship"
    beating: "For speaking without permission"
    extra_work: "For sloppiness"
    humiliation: "For laziness"

  schedule:
    dawn: "Arrive, prepare materials"
    morning: "Instruction and copying"
    midday: "Brief rest, meal"
    afternoon: "More copying, recitation"
    evening: "Dismissed"

  bribes_and_gifts:
    practice: "Students invite teachers to dinner"
    purpose: "Better grades, lenient treatment"
    frequency: "Common and expected"

  graduation:
    examination: "Demonstrate competence"
    ceremony: "Recognition as Dubsar"
    title: "Tablet Writer"
```

### Tuition and Costs

```yaml
edubba_economics:
  tuition:
    cost: "Significant (elite families only)"
    payment: "To school headmaster"
    duration: "Throughout training"

  materials:
    clay: "Student provides or purchases"
    stylus: "Student provides"
    reference_texts: "School provides (borrowed)"

  total_investment:
    duration: "5-10 years"
    opportunity_cost: "Child not working"
    social_cost: "Family sacrifice"

  return_on_investment:
    income: "Scribes earn well"
    status: "Respected profession"
    security: "Always demand for literacy"
```

---

## The Dubsar (Scribe)

### Career Paths

```yaml
scribe_careers:
  temple_administrator:
    description: "Manage temple economy"
    duties:
      - "Track offerings and expenditures"
      - "Manage worker rations"
      - "Record temple property"
      - "Handle correspondence"
    employer: "Temple of Enki"
    income: "Temple salary + rations"
    status: "High"
    sila_reward: 100

  palace_administrator:
    description: "Serve royal household"
    duties:
      - "Royal correspondence"
      - "Tax collection records"
      - "Military logistics"
      - "Diplomatic messages"
    employer: "City ruler"
    income: "Royal salary"
    status: "Highest"
    sila_reward: 150

  private_notary:
    description: "Write contracts for citizens"
    duties:
      - "Sales contracts"
      - "Marriage agreements"
      - "Loan documents"
      - "Letters for hire"
    employer: "Self (fees from clients)"
    income: "Per-document fees"
    status: "Middle"
    location: "Karum, public spaces"
    sila_reward: 75

  specialized_scholar:
    description: "Expert in specific field"
    fields:
      mathematics: "Surveying, accounting"
      medicine: "Medical texts, diagnosis"
      astronomy: "Calendar, omens"
      law: "Legal expertise"
    employer: "Various"
    income: "Consultation fees"
    status: "Respected expert"
    sila_reward: 125

  village_scribe:
    description: "Serve rural community"
    duties:
      - "Land deeds"
      - "Agricultural records"
      - "Letters for farmers"
      - "Simple contracts"
    employer: "Village fees"
    income: "Lower but steady"
    status: "Local important person"
    sila_reward: 50
```

### Scribe Skill Tree

```yaml
scribe_skills:
  tier_1_graduate:
    skills:
      basic_cuneiform:
        description: "Read and write standard texts"
        sila_reward: 50

      simple_contracts:
        description: "Write basic agreements"
        sila_reward: 40

      arithmetic:
        description: "Basic calculations"
        sila_reward: 30

    role: "Junior scribe, copyist"
    earnings: "20-50 SILA/day"

  tier_2_professional:
    requirements: "2 years practice"
    skills:
      complex_contracts:
        description: "Legal documents, loans, sales"
        sila_reward: 60

      administrative_records:
        description: "Accounts, inventories, lists"
        sila_reward: 50

      correspondence:
        description: "Official letters"
        sila_reward: 45

    role: "Working scribe"
    earnings: "50-100 SILA/day"

  tier_3_senior:
    requirements: "5 years + specialization"
    skills:
      legal_expertise:
        description: "Complex legal matters"
        sila_reward: 100

      literary_copying:
        description: "Preserve major texts"
        sila_reward: 80

      mathematical_surveying:
        description: "Land measurement, calculations"
        sila_reward: 90

    role: "Senior scribe, department head"
    earnings: "100-200 SILA/day"

  tier_4_master:
    requirements: "10+ years + reputation"
    skills:
      archive_management:
        description: "Maintain institutional records"
        sila_reward: 150

      teaching:
        description: "Train new scribes"
        sila_reward: 100

      advisory:
        description: "Counsel rulers and priests"
        sila_reward: 150

    role: "Chief scribe, school head"
    earnings: "Elite status + salary"
```

---

## Document Types

### Economic Documents

```yaml
economic_documents:
  receipts:
    purpose: "Proof of payment/delivery"
    format: "Simple statement with date and seal"
    fee: "5-10 SILA"

  account_ledgers:
    purpose: "Track ongoing transactions"
    format: "Columnar lists"
    complexity: "High"
    fee: "Based on scope"

  payroll_records:
    purpose: "Track worker rations/wages"
    format: "Lists with amounts"
    employer: "Temple, palace"
    fee: "Institutional salary"

  inventories:
    purpose: "List holdings"
    format: "Categorized lists"
    use: "Warehouses, temples, estates"
    fee: "Based on size"

  trade_accounts:
    purpose: "Track commercial ventures"
    format: "Voyage records, profit calculations"
    user: "Damgar, investors"
    fee: "20-50 SILA"
```

### Legal Documents

```yaml
legal_documents:
  sales_contracts:
    purpose: "Transfer ownership"
    subjects: "Land, slaves, animals, goods"
    elements:
      - "Parties named"
      - "Item described"
      - "Price stated"
      - "Witnesses listed"
      - "Seals applied"
    fee: "10-50 SILA (based on value)"

  loan_contracts:
    purpose: "Document debt"
    elements:
      - "Lender and borrower"
      - "Amount and interest rate"
      - "Repayment terms"
      - "Collateral if any"
    fee: "15-30 SILA"

  marriage_contracts:
    purpose: "Establish marriage terms"
    elements:
      - "Bride and groom"
      - "Bride price"
      - "Dowry"
      - "Divorce provisions"
    fee: "20-40 SILA"

  divorce_documents:
    purpose: "Dissolve marriage"
    elements:
      - "Cause stated"
      - "Property division"
      - "Child custody"
    fee: "20-50 SILA"

  adoption_documents:
    purpose: "Create legal parent-child relationship"
    elements:
      - "Parties"
      - "Rights granted"
      - "Inheritance terms"
    fee: "15-30 SILA"

  wills:
    purpose: "Distribute property after death"
    elements:
      - "Testator"
      - "Heirs"
      - "Specific bequests"
    fee: "30-100 SILA"
```

### Administrative Documents

```yaml
administrative_documents:
  land_surveys:
    purpose: "Measure and record property"
    elements:
      - "Boundaries"
      - "Area calculation"
      - "Owner"
    skill: "Mathematical expertise"
    fee: "50-200 SILA"

  census_records:
    purpose: "Population tracking"
    elements:
      - "Households"
      - "Occupations"
      - "Tax obligations"
    employer: "Palace, temple"

  tax_records:
    purpose: "Track Bala obligations"
    elements:
      - "Taxpayer"
      - "Amount owed"
      - "Payment status"
    employer: "Tax authority"

  ration_lists:
    purpose: "Distribute temple/palace food"
    elements:
      - "Recipients"
      - "Amounts"
      - "Dates"
    employer: "Institution"
```

### Letters and Correspondence

```yaml
letters:
  personal_letters:
    purpose: "Private communication"
    format: "Greeting, message, closing"
    fee: "5-15 SILA"
    service: "Scribe writes, courier delivers"

  official_letters:
    purpose: "Institutional communication"
    format: "Formal structure"
    fee: "Institutional salary"

  diplomatic_messages:
    purpose: "Inter-city communication"
    format: "Highly formal"
    scribe: "Specialized, trusted"
```

### Model Contracts (Training)

```yaml
model_contracts:
  purpose: "Training documents in schools"
  content: "Standard legal formulas"
  use: "Students copy to learn"
  preservation: "Establishes consistent practice"
```

---

## Writing Technology

### Materials

```yaml
writing_materials:
  clay:
    type: "Fine alluvial clay"
    preparation: "Washed, kneaded, shaped"
    format: "Tablets (various sizes)"
    wet: "Write while soft"
    drying: "Sun-dry for temporary records"
    firing: "Kiln-fire for permanent records"

  stylus:
    material: "Cut reed"
    shape: "Triangular tip"
    technique: "Press wedge shapes"
    maintenance: "Cut fresh regularly"

  clay_envelopes:
    purpose: "Seal documents"
    use: "Contracts, secure messages"
    feature: "Break to read"
```

### Cuneiform Basics

```yaml
cuneiform:
  name: "Wedge-shaped writing"
  signs: "600+ in common use"
  types:
    logograms: "One sign = one word"
    syllables: "One sign = one syllable"
    determinatives: "Category markers"

  reading_difficulty:
    issue: "Same sign can have multiple readings"
    solution: "Context determines meaning"

  learning_curve:
    basic_literacy: "2-3 years"
    professional: "5-7 years"
    mastery: "10+ years"
```

---

## Economics of Scribal Services

### Fee Structure

```yaml
scribal_fees:
  simple_receipt: "5-10 SILA"
  basic_contract: "10-25 SILA"
  complex_contract: "25-100 SILA"
  personal_letter: "5-15 SILA"
  official_document: "Based on complexity"
  land_survey: "50-200 SILA"
  legal_consultation: "20-50 SILA"

  factors:
    length: "More text = higher fee"
    complexity: "Legal expertise = premium"
    urgency: "Rush jobs cost more"
    copies: "Each copy has fee"
```

### Employment Options

```yaml
employment:
  institutional:
    employers: "Temple, palace"
    benefits: "Steady salary, rations, housing"
    drawbacks: "Fixed income, obligations"

  freelance:
    location: "Karum, public spaces"
    benefits: "Variable income, independence"
    drawbacks: "No guaranteed work"

  mixed:
    arrangement: "Part-time institutional + private"
    benefits: "Stability + extra income"
    common: "Many scribes do this"
```

---

## Special Roles

### Archive Keeper

```yaml
archive_keeper:
  description: "Maintain institutional records"

  duties:
    organization: "Systematic storage"
    retrieval: "Find documents on request"
    preservation: "Protect from damage"
    copying: "Replace deteriorating tablets"

  skills:
    cataloging: "Know what exists and where"
    memory: "Recall document locations"
    judgment: "What to keep, what to discard"

  importance: "Institutional memory depends on them"
```

### School Teacher

```yaml
edubba_teacher:
  description: "Train next generation"

  roles:
    ummia: "School headmaster"
    dubsar_tur: "Assistant teacher"
    shesh_gal: "Big brother (advanced student helper)"

  income:
    tuition: "From students' families"
    gifts: "From students seeking favor"

  status: "Respected, influential"
```

### Specialized Expert

```yaml
expert_scribes:
  mathematician:
    specialty: "Complex calculations, surveying"
    clients: "Temple, merchants, government"
    sila_reward: 100

  medical_scribe:
    specialty: "Medical texts, diagnosis records"
    clients: "Asu, Ashipu, temple"
    sila_reward: 100

  astronomer:
    specialty: "Calendar, omens, predictions"
    clients: "Temple, rulers"
    sila_reward: 125

  legal_expert:
    specialty: "Complex legal matters"
    clients: "Courts, wealthy individuals"
    sila_reward: 100
```

---

## Training Data Value

### Knowledge Capture

```yaml
training_data:
  administrative_reasoning:
    - "Record organization decisions"
    - "Accuracy verification"
    - "Information retrieval"

  legal_thinking:
    - "Contract interpretation"
    - "Term selection"
    - "Dispute documentation"

  knowledge_preservation:
    - "What to record and why"
    - "How to organize information"
    - "Teaching methods"

  mathematical_reasoning:
    - "Calculation methods"
    - "Measurement techniques"
    - "Problem-solving"
```

---

## Implementation Notes

### Database Schema

```yaml
scribe_records:
  scribe_profile:
    player_id: uuid
    skill_level: integer
    specializations: array
    documents_written: integer
    employer: string
    reputation: integer
    known_texts: array

  document_record:
    document_id: uuid
    scribe_id: uuid
    type: enum
    parties: array
    content_summary: text
    fee: integer
    date: datetime
    witnesses: array
    status: enum
```

---

## Appendix: Sumerian Scribal Terms

| Term | Meaning | Gameplay Role |
|------|---------|---------------|
| **Dubsar** | Scribe | Writing profession |
| **Edubba** | Tablet House (school) | Training institution |
| **Ummia** | School headmaster | Teacher role |
| **Dub** | Tablet | Writing medium |
| **Gi-dub-ba** | Stylus (reed pen) | Writing tool |

---

*"What the tongue speaks, the wind carries away. What the stylus writes, the clay preserves. This is why the scribe sits at the right hand of power—for memory itself bows to the tablet."*
