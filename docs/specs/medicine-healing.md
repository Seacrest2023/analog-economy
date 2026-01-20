# Medicine & Healing

> *"The body breaks. The spirit cracks. One healer mends flesh. The other mends fate. Wisdom knows when to call each."*

## Overview

Healing in Eridu operates through two complementary professions: the Asu (physician-surgeon) who treats physical symptoms with practical medicine, and the Ashipu (exorcist-priest) who addresses spiritual causes through ritual. Neither is superior—complex cases require both. This dual system creates rich gameplay, meaningful profession choices, and valuable training data about diagnostic reasoning and treatment decisions.

---

## Design Philosophy

### Core Principles

1. **Dual Causation**: Every illness has both physical symptoms AND spiritual cause
2. **Complementary Expertise**: Asu and Ashipu work together, not against each other
3. **Learn Real Knowledge**: The pharmacopeia uses historically accurate ingredients
4. **Consequence of Failure**: Wrong treatments can worsen conditions
5. **Training Data Value**: Diagnostic reasoning, treatment selection, outcome analysis

### The Healer's Dilemma

```yaml
diagnostic_challenge:
  presenting_symptom: "Fever and weakness"

  asu_interpretation:
    diagnosis: "Imbalance of humors, possible infection"
    treatment: "Willow bark tea, cool compresses, rest"
    focus: "Reduce fever, restore strength"

  ashipu_interpretation:
    diagnosis: "God's displeasure or demonic possession"
    treatment: "Identify sin, perform purification ritual"
    focus: "Appease divine anger, expel spirit"

  synergy:
    process:
      - "Ashipu diagnoses spiritual cause"
      - "Asu manages physical symptoms"
      - "Both treatments applied together"
    outcome: "Fastest, most complete recovery"

  failure_scenario:
    asu_only: "Symptoms managed but keep returning"
    ashipu_only: "Spiritual peace but body still suffering"
    neither: "Condition worsens, possible death"
```

---

## The Asu (Physician-Surgeon)

### Philosophy

"The body is a vessel. When it leaks, we patch. When it burns, we cool. When it starves, we feed. Practical problems require practical solutions."

### Skill Tree

```yaml
asu_skill_tree:
  tier_1_novice:
    skills:
      wound_cleaning:
        description: "Clean wounds with salt water or sour wine"
        sila_reward: 15
        unlocks: "Basic wound treatment"

      basic_bandaging:
        description: "Apply cloth wrappings to injuries"
        sila_reward: 15
        unlocks: "Injury stabilization"

      burn_treatment:
        description: "Apply ghee and honey to burns"
        sila_reward: 20
        unlocks: "Burn care"

    earnings: "10-30 SILA per treatment"
    reputation: "Helpful neighbor"

  tier_2_apprentice:
    requirements: "Tier 1 complete + 10 successful treatments"
    skills:
      bone_setting:
        description: "Align and splint broken bones"
        sila_reward: 30
        risk: "Improper setting = permanent disability"

      fever_reduction:
        description: "Prepare willow bark tea"
        sila_reward: 25
        knowledge: "Willow bark = ancient aspirin"

      digestive_remedies:
        description: "Mint, fenugreek for stomach ailments"
        sila_reward: 25
        common_use: "Food poisoning, parasites"

      poultice_preparation:
        description: "Mix herbs into healing paste"
        sila_reward: 30
        ingredients: "Mustard, garlic, honey base"

    earnings: "30-75 SILA per treatment"
    reputation: "Sought-after healer"

  tier_3_journeyman:
    requirements: "Tier 2 complete + 25 successful treatments + mentor"
    skills:
      minor_surgery:
        description: "Lance boils, remove splinters, drain abscesses"
        sila_reward: 50
        tools: "Bronze knife, clean cloth, honey"

      pain_management:
        description: "Prepare opium-based remedies"
        sila_reward: 50
        restriction: "Temple-controlled substance"
        risk: "Addiction if overused"

      respiratory_treatment:
        description: "Myrrh steam inhalation, thyme tea"
        sila_reward: 40
        common_use: "Cough, chest congestion"

      antidote_basics:
        description: "Counter common poisons"
        sila_reward: 60
        knowledge: "Requires knowing poison types"

    earnings: "75-150 SILA per treatment"
    reputation: "Respected physician"

  tier_4_master:
    requirements: "Tier 3 complete + 50 treatments + temple recognition"
    skills:
      complex_surgery:
        description: "Major wound repair, tumor removal"
        sila_reward: 100
        risk: "Death if failed"
        tools: "Specialized bronze instruments"

      veterinary_medicine:
        description: "Treat livestock diseases"
        sila_reward: 75
        market: "Temple flocks, merchant animals"

      teaching:
        description: "Train apprentice Asu"
        sila_reward: 100
        benefit: "Passive income from students"

      pharmacopeia_mastery:
        description: "Create any known medicine"
        sila_reward: 150
        status: "Elite healer"

    earnings: "150-500 SILA per treatment"
    reputation: "Famous physician"
```

### The Asu's Pharmacopeia

```yaml
pharmacopeia:
  herbs_and_botanicals:
    willow_bark:
      effect: "Pain relief, fever reduction"
      preparation: "Boil in water, drink as tea"
      historical_note: "Source of salicylic acid (aspirin)"
      sila_to_learn: 25

    garlic:
      effect: "Vitality boost, antiseptic"
      preparation: "Eat raw or crush into poultice"
      common_use: "Given to workers for strength"
      sila_to_learn: 15

    opium:
      effect: "Severe pain relief, sedation"
      preparation: "Extract from poppy, mix with wine"
      restriction: "Temple-controlled"
      risk: "Addiction"
      sila_to_learn: 50

    myrrh:
      effect: "Respiratory relief, wound care"
      preparation: "Burn for steam or mix into salve"
      sila_to_learn: 30

    mint:
      effect: "Digestive aid, cooling"
      preparation: "Tea or chewed fresh"
      sila_to_learn: 15

    thyme:
      effect: "Respiratory, antiseptic"
      preparation: "Tea or steam inhalation"
      sila_to_learn: 20

    honey:
      effect: "Natural antiseptic, wound healing"
      preparation: "Apply directly to wounds"
      historical_note: "Still used in modern medicine"
      sila_to_learn: 15

    fenugreek:
      effect: "Stomach cleansing, respiratory"
      preparation: "Seeds boiled in water"
      sila_to_learn: 25

    licorice:
      effect: "Soothing, flavor for medicines"
      preparation: "Root chewed or boiled"
      sila_to_learn: 20

  bases_and_vehicles:
    beer:
      use: "Most common medicine base"
      reason: "Alcohol preserves, aids absorption"

    wine:
      use: "Luxury medicines, disinfectant"
      reason: "Higher alcohol, cleaner"

    milk:
      use: "Soothing applications"
      reason: "Gentle delivery for children"

    ghee:
      use: "Burn treatment, salve base"
      reason: "Moisture barrier, healing fats"

  minerals_and_compounds:
    salt:
      use: "Wound cleaning, preservation"
      preparation: "Dissolve in water"

    potassium_nitrate:
      use: "Astringent"
      source: "Collected from urine deposits"

    sodium_bicarbonate:
      use: "Stomach acid relief"
      preparation: "Dissolve in water"
      historical_note: "Ancient antacid"
```

### Treatment Outcomes

```yaml
treatment_success_factors:
  diagnosis_accuracy:
    weight: 30%
    description: "Did you identify the correct condition?"

  treatment_selection:
    weight: 25%
    description: "Did you choose appropriate medicine?"

  preparation_quality:
    weight: 20%
    description: "Was the medicine properly prepared?"

  timing:
    weight: 15%
    description: "Was treatment applied early enough?"

  patient_compliance:
    weight: 10%
    description: "Did patient follow instructions?"

outcome_matrix:
  excellent: "Full recovery, patient gratitude, reputation boost"
  good: "Recovery with minor lasting effects"
  partial: "Symptoms managed but underlying issue remains"
  poor: "No improvement, reputation damage"
  failure: "Patient worsens or dies, possible legal action"

liability:
  negligence:
    definition: "Obvious incompetence or carelessness"
    consequence: "Fines, reputation destruction"
  honest_failure:
    definition: "Correct treatment, unlucky outcome"
    consequence: "No legal penalty, minor reputation hit"
```

---

## The Ashipu (Exorcist-Priest)

### Philosophy

"All suffering flows from disruption of divine order. A god's anger. A demon's intrusion. A forgotten sin. Find the cause, perform the cure, restore the balance."

### Skill Tree

```yaml
ashipu_skill_tree:
  tier_1_novice:
    skills:
      basic_incantations:
        description: "Recite protective prayers (shiptu)"
        sila_reward: 20
        use: "Minor spiritual cleansing"

      purification_water:
        description: "Prepare and apply holy water"
        sila_reward: 15
        use: "Cleanse spaces and persons"

      incense_preparation:
        description: "Blend sacred smoke mixtures"
        sila_reward: 15
        use: "Attract gods, repel demons"

    earnings: "Temple rations + 15-40 SILA per ritual"
    status: "Temple initiate"

  tier_2_apprentice:
    requirements: "Tier 1 complete + temple service"
    skills:
      sin_identification:
        description: "Question patient to find transgression"
        sila_reward: 30
        method: "Structured interview, observation"

      substitute_figurine:
        description: "Create clay figure to absorb evil"
        sila_reward: 35
        process: "Shape, consecrate, transfer, destroy"

      basic_divination:
        description: "Read simple omens"
        sila_reward: 40
        types: "Oil on water, smoke patterns"

    earnings: "Temple rations + 40-80 SILA per ritual"
    status: "Practicing exorcist"

  tier_3_journeyman:
    requirements: "Tier 2 complete + 20 successful rituals + priest sponsor"
    skills:
      liver_reading:
        description: "Haruspicy - divine from sheep liver"
        sila_reward: 75
        cost: "Requires sacrificial animal"
        accuracy: "Considered most reliable divination"

      demon_identification:
        description: "Name the specific spirit causing illness"
        sila_reward: 60
        importance: "Named demons are easier to expel"

      ritual_prescription:
        description: "Design custom purification ritual"
        sila_reward: 70
        creativity: "Each case may need unique approach"

    earnings: "Temple stipend + 80-150 SILA per ritual"
    status: "Respected exorcist"

  tier_4_master:
    requirements: "Tier 3 complete + 50 rituals + temple ordination"
    skills:
      major_exorcism:
        description: "Full demon expulsion ceremony"
        sila_reward: 150
        duration: "Hours to days"
        drama: "Intense, dangerous, powerful"

      divine_intercession:
        description: "Petition gods directly on patient's behalf"
        sila_reward: 200
        requires: "Excellent temple standing"

      teaching:
        description: "Train apprentice Ashipu"
        sila_reward: 100
        legacy: "Create next generation"

    earnings: "Elite temple position + 150-400 SILA per major ritual"
    status: "Master exorcist"
```

### Spiritual Diagnosis

```yaml
cause_identification:
  divine_anger:
    symptoms:
      - "Sudden illness after temple neglect"
      - "Dreams of angry gods"
      - "Misfortune in temple-related matters"
    treatment: "Appeasement offerings, public confession"

  demonic_possession:
    symptoms:
      - "Personality changes"
      - "Speaking in strange voices"
      - "Unexplained violence"
    treatment: "Exorcism ritual, substitute figurine"

  ancestral_curse:
    symptoms:
      - "Family pattern of illness"
      - "Nightmares about dead relatives"
      - "Illness around Kispu neglect"
    treatment: "Ancestral offerings, family reconciliation"

  sorcery:
    symptoms:
      - "Illness after conflict with enemy"
      - "Finding ritual objects near home"
      - "Unnaturally targeted misfortune"
    treatment: "Counter-ritual, purification, legal action"

  forgotten_sin:
    symptoms:
      - "Guilt-related dreams"
      - "Illness with no apparent trigger"
      - "Feeling of divine displeasure"
    treatment: "Confession, penance, offerings"
```

### Ritual Types

```yaml
ritual_catalog:
  namburbi:
    type: "Preventive ritual"
    purpose: "Avert predicted misfortune"
    trigger: "Bad omen observed"
    process: "Counter-ritual before disaster strikes"

  maqlû:
    type: "Anti-witchcraft"
    purpose: "Break curses and spells"
    process: "Burning effigies, incantations"
    duration: "Night-long ceremony"

  shurpu:
    type: "Purification from sin"
    purpose: "Cleanse accumulated transgressions"
    process: "Confession, symbolic burning of sins"
    outcome: "Restored relationship with gods"

  mis_pi:
    type: "Mouth-washing"
    purpose: "Activate/purify sacred objects"
    use: "Temple statues, amulets"
    restriction: "Priest-only ritual"

  bit_rimki:
    type: "House of bathing"
    purpose: "Major purification"
    process: "Ritual bathing over multiple days"
    use: "Severe pollution, preparation for important events"
```

---

## The Synergy System

### Combined Treatment Protocol

```yaml
synergy_protocol:
  initial_assessment:
    step_1: "Patient describes symptoms"
    step_2: "Asu examines physical condition"
    step_3: "Ashipu inquires about spiritual state"

  diagnosis_sharing:
    asu_reports: "Physical findings, suspected illness"
    ashipu_reports: "Spiritual cause, divine displeasure signs"

  treatment_plan:
    physical_track: "Asu prescribes medicines, care"
    spiritual_track: "Ashipu designs appropriate ritual"
    timing: "Both treatments proceed simultaneously"

  outcome_interpretation:
    success: "Physical + spiritual healing complete"
    partial_physical: "Asu treatment works, ritual may have helped"
    partial_spiritual: "Patient feels peace, body still suffering"
    failure_physical: "Proves spiritual cause is primary"
    failure_spiritual: "Indicates physical cause is primary"
```

### Referral System

```yaml
referral_mechanics:
  asu_to_ashipu:
    trigger: "Physical treatment repeatedly fails"
    interpretation: "Spiritual cause confirmed"
    protocol: "Asu recommends temple visit"
    reputation: "No penalty for appropriate referral"

  ashipu_to_asu:
    trigger: "Ritual complete but symptoms persist"
    interpretation: "Physical treatment needed"
    protocol: "Ashipu recommends physician"
    reputation: "No penalty for appropriate referral"

  joint_consultation:
    trigger: "Complex or serious cases"
    protocol: "Both healers examine patient together"
    benefit: "Most accurate diagnosis, fastest healing"
    cost: "Patient pays both"
```

---

## Common Ailments and Treatments

### Condition Catalog

```yaml
common_conditions:
  fever:
    physical_cause: "Infection, heat exposure"
    spiritual_cause: "Divine punishment, demon Asakku"
    asu_treatment: "Willow bark tea, cool cloths"
    ashipu_treatment: "Prayer to Ninurta, demon expulsion"
    synergy_benefit: "+50% recovery speed"

  wound_infection:
    physical_cause: "Contaminated injury"
    spiritual_cause: "Curse or pollution"
    asu_treatment: "Clean, honey dressing, garlic poultice"
    ashipu_treatment: "Purification ritual, protective amulet"
    synergy_benefit: "Prevents recurrence"

  digestive_illness:
    physical_cause: "Bad food, parasites, stress"
    spiritual_cause: "Angered Enki (water god)"
    asu_treatment: "Fasting, mint tea, sodium bicarbonate"
    ashipu_treatment: "Offerings to Enki, river purification"
    synergy_benefit: "Addresses root cause"

  respiratory_problems:
    physical_cause: "Dust, smoke, infection"
    spiritual_cause: "Demon Lamashtu attack"
    asu_treatment: "Myrrh steam, thyme tea, rest"
    ashipu_treatment: "Lamashtu amulet, protective incantation"
    synergy_benefit: "Long-term protection"

  broken_bone:
    physical_cause: "Trauma"
    spiritual_cause: "Bad luck, forgotten offering"
    asu_treatment: "Set bone, splint, immobilize"
    ashipu_treatment: "Blessing for healing, luck restoration"
    synergy_benefit: "Faster mending"

  mental_disturbance:
    physical_cause: "Trauma, stress, substance"
    spiritual_cause: "Demonic possession, divine punishment"
    asu_treatment: "Sedatives, rest, nutrition"
    ashipu_treatment: "Exorcism, sin confession, purification"
    synergy_benefit: "Essential for full recovery"

  infertility:
    physical_cause: "Health issues, age"
    spiritual_cause: "Divine disfavor, curse"
    asu_treatment: "Fertility herbs, health optimization"
    ashipu_treatment: "Fertility rituals, Inanna prayers"
    synergy_benefit: "Both approaches recommended"

  snakebite:
    physical_cause: "Venom injection"
    spiritual_cause: "Sent by enemy sorcerer"
    asu_treatment: "Antidote, wound care, tourniquet"
    ashipu_treatment: "Counter-curse, snake-god appeasement"
    synergy_benefit: "Time-critical, use both immediately"
```

---

## Economics of Healing

### Asu Payment Structure

```yaml
asu_economics:
  payment_model: "Success-based with upfront costs"

  fee_schedule:
    minor_treatment: "10-30 SILA"
    moderate_treatment: "30-80 SILA"
    major_treatment: "80-200 SILA"
    surgery: "150-500 SILA"

  material_costs:
    herbs: "5-20 SILA depending on rarity"
    instruments: "50-200 SILA (one-time investment)"
    supplies: "10-30 SILA per major treatment"

  liability_risk:
    negligence_fine: "10x treatment fee"
    reputation_damage: "Loss of future patients"
    legal_defense: "Time and social capital"

  profit_potential:
    novice: "Barely sustainable"
    apprentice: "Modest living"
    journeyman: "Comfortable income"
    master: "Wealthy professional"
```

### Ashipu Payment Structure

```yaml
ashipu_economics:
  payment_model: "Temple stipend + ritual fees + offerings"

  fee_schedule:
    minor_ritual: "20-50 SILA"
    moderate_ritual: "50-100 SILA"
    major_ritual: "100-300 SILA"
    exorcism: "200-500 SILA"

  temple_benefits:
    housing: "Often provided"
    food: "Temple rations"
    status: "Religious authority"
    materials: "Temple provides ritual supplies"

  additional_income:
    divination: "30-100 SILA per reading"
    amulets: "25-75 SILA each"
    teaching: "Percentage of student fees"

  profit_potential:
    novice: "Subsistence via temple"
    apprentice: "Comfortable within temple"
    journeyman: "Well-off, respected"
    master: "Elite status, significant wealth"
```

---

## Player Path Considerations

### Choosing Your Healing Path

```yaml
path_comparison:
  asu_path:
    playstyle: "Practical, hands-on, scientific"
    skills_needed: "Botany, preparation, anatomy"
    income_source: "Patient fees (variable)"
    risk: "Liable for failures"
    freedom: "Independent practice possible"
    synergy: "Works well with farming (herb growing)"

  ashipu_path:
    playstyle: "Ritual, spiritual, mysterious"
    skills_needed: "Religious knowledge, performance, divination"
    income_source: "Temple + fees (stable)"
    risk: "Temple politics, divine displeasure"
    freedom: "Tied to temple structure"
    synergy: "Works well with priestly career"

  dual_path:
    possibility: "Learn both (rare, time-intensive)"
    benefit: "Handle any case alone"
    drawback: "Master of neither quickly"
    prestige: "Extremely high if achieved"
```

### Career Milestones

```yaml
healer_milestones:
  first_cure:
    description: "Successfully treat first patient"
    reward: "Unlock healing reputation"
    sila: 25

  tenth_cure:
    description: "Establish track record"
    reward: "Patients seek you out"
    sila: 50

  save_a_life:
    description: "Cure potentially fatal condition"
    reward: "Major reputation boost"
    sila: 100
    karma: +15

  community_healer:
    description: "Recognized as neighborhood's healer"
    reward: "Steady patient flow"
    sila: 75

  temple_recognition:
    description: "Temple acknowledges your skill"
    reward: "Access to rare materials"
    sila: 150

  train_successor:
    description: "Successfully train an apprentice"
    reward: "Legacy establishment"
    sila: 100
    legacy_points: +5
```

---

## Implementation Notes

### Database Schema

```yaml
healer_record:
  player_id: uuid
  healer_type: enum["asu", "ashipu", "both"]
  skill_tier: integer
  treatments_attempted: integer
  treatments_successful: integer
  success_rate: float
  specializations: array
  reputation_score: integer
  known_recipes: array
  known_rituals: array

treatment_log:
  treatment_id: uuid
  healer_id: uuid
  patient_id: uuid
  condition: string
  diagnosis: string
  treatment_applied: string
  outcome: enum["success", "partial", "failure"]
  reasoning_captured: text  # Training data
  timestamp: datetime
```

### Training Data Capture

```yaml
training_data_points:
  diagnostic_reasoning:
    - "What symptoms did player observe?"
    - "How did they reach diagnosis?"
    - "What alternatives did they consider?"

  treatment_selection:
    - "Why this treatment over alternatives?"
    - "What was the expected outcome?"
    - "How did they prepare the medicine?"

  outcome_analysis:
    - "Did treatment work? Why/why not?"
    - "What would they do differently?"
    - "Lessons learned?"

  referral_decisions:
    - "When did they refer to other healer?"
    - "Why was referral appropriate?"
    - "How did collaboration work?"
```

---

## Appendix: Sumerian Medical Terms

| Term | Meaning | Gameplay Role |
|------|---------|---------------|
| **Asu** | Physician-surgeon | Physical healing profession |
| **Ashipu** | Exorcist-priest | Spiritual healing profession |
| **Shiptu** | Incantation | Ashipu tool |
| **Sakikku** | "All Diseases" diagnostic manual | Knowledge source |
| **Gidim** | Ghost/demon | Cause of illness |
| **Lamashtu** | Female demon | Targets mothers/children |
| **Asakku** | Fever demon | Common illness cause |
| **Pišāšū** | Salve/ointment | Asu medicine type |
| **Namburbi** | Preventive ritual | Ashipu specialty |

---

*"The wounded man who finds only an Asu may live. The possessed man who finds only an Ashipu may find peace. But the wise man seeks both—for we are flesh AND spirit, and both must heal."*
