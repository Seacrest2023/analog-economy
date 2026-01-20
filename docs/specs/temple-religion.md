# Temple Service & Religious Life

> *"The gods do not need us. We need them. Service is not burden—it is survival."*

## Overview

Religious participation in Eridu is not optional flavor content—it is the primary mechanism for sanity restoration and karma maintenance. The Temple of Enki (E-Abzu) operates as a living household for the god, requiring constant service from priests and lay worshippers alike. Players who neglect the gods face mounting sanity penalties; those who serve faithfully gain protection, community standing, and inner peace.

---

## Design Philosophy

### Core Principles

1. **Service for Serenity**: Temple activities restore sanity—the gods provide mental stability
2. **Structured Access**: Social class determines what temple activities are available
3. **Seasonal Rhythm**: Festivals create natural gameplay peaks throughout the year
4. **Mutual Exchange**: "I give so that you may give" (do ut des) - offerings yield tangible benefits
5. **Training Data Value**: Religious reasoning, ethical decisions, ritual knowledge

### The Neglect Penalty

```yaml
temple_neglect:
  tracking: "Days since last temple interaction"

  thresholds:
    7_days:
      effect: "Uneasy dreams"
      sanity_drain: "-1/day"

    14_days:
      effect: "Divine disfavor whispers"
      sanity_drain: "-2/day"
      npc_reaction: "Priests express concern"

    30_days:
      effect: "Marked by absence"
      sanity_drain: "-5/day"
      npc_reaction: "Community suspicion"
      karma: "-1/day"

    60_days:
      effect: "Godless one"
      sanity_drain: "-10/day"
      karma: "-3/day"
      social_penalty: "Temple services refused"
```

---

## Daily Temple Practices

### The God's Schedule

The E-Abzu follows a strict domestic routine to keep Enki comfortable:

```yaml
daily_schedule:
  dawn_awakening:
    time: "First light"
    activities:
      - "Priests enter inner sanctum"
      - "Hymns sung to awaken the statue"
      - "Incense lit throughout temple"
    player_participation:
      allowed: "Temple workers and above"
      role: "Incense bearer, hymn chorus"
      karma: "+2"
      sanity: "+5"

  morning_washing:
    time: "After dawn"
    activities:
      - "Mis-Pi (Mouth-Washing) ritual"
      - "Opens statue's senses symbolically"
      - "Fresh garments and jewels applied"
    player_participation:
      allowed: "Priests only"
      role: "Garment handler, jewel bearer"
      karma: "+5"
      sanity: "+8"

  sunrise_meal:
    time: "Mid-morning"
    activities:
      - "Food laid on gold/silver dishes"
      - "Curtain drawn for privacy"
      - "Music played throughout"
    player_participation:
      allowed: "Temple workers and above"
      role: "Food preparer, musician, curtain attendant"
      karma: "+3"
      sanity: "+6"

  midday_rest:
    time: "Noon to afternoon"
    activities:
      - "Temple quiet period"
      - "Priests attend to administration"
    player_participation:
      allowed: "Limited - cleaning, maintenance"

  sunset_meal:
    time: "Evening"
    activities:
      - "Second feeding ceremony"
      - "Evening hymns"
    player_participation:
      allowed: "Temple workers and above"
      role: "Same as sunrise meal"
      karma: "+3"
      sanity: "+6"

  night_watch:
    time: "After dark"
    activities:
      - "Lamps lit throughout temple"
      - "Night guards posted"
      - "Quiet prayers"
    player_participation:
      allowed: "Temple guards, dedicated worshippers"
      role: "Lamp tender, night vigil"
      karma: "+2"
      sanity: "+10 (peaceful meditation)"
```

### Temple Service Tiers

Access to temple activities depends on social standing and dedication:

| Service Level | Who Can Participate | Karma | Sanity | Payment |
|---------------|---------------------|-------|--------|---------|
| **Festival Attendance** | Anyone | +2 | +10 | None (time cost only) |
| **Outer Court Prayer** | Anyone | +1 | +3 | Small offering expected |
| **Offering Delivery** | Commoners+ | +3 | +5 | Small SILA tip possible |
| **Meal Preparation** | Temple workers | +5 | +8 | Daily rations |
| **Music Performance** | Trained musicians | +5 | +15 | Rations + tips |
| **Curtain Duty** | Trusted servants | +8 | +10 | Steady wage |
| **Washing Ritual Assist** | Priests only | +15 | +20 | Temple stipend |
| **Inner Sanctum Access** | High priests only | +25 | +30 | Elite status |

---

## Offering System

### The Philosophy: Do Ut Des

"I give so that you may give" - offerings are transactions with the divine.

```yaml
offering_types:
  daily_offerings:
    bread:
      quality_tiers: ["common", "fine", "temple-grade"]
      karma_by_tier: [1, 2, 3]
      notes: "Freshly baked preferred"

    beer:
      quality_tiers: ["common", "quality", "ceremonial"]
      karma_by_tier: [1, 2, 4]
      notes: "The god's preferred drink"

    dates:
      karma: 1
      notes: "Sweet offerings please Enki"

    milk:
      karma: 2
      notes: "Fresh, not soured"

  animal_sacrifices:
    goat:
      karma: 5
      cost: "Significant"
      occasions: "Minor festivals, personal requests"

    lamb:
      karma: 10
      cost: "High"
      occasions: "Major festivals, serious petitions"

    ox:
      karma: 25
      cost: "Very high"
      occasions: "Temple consecration, city emergencies"

  votive_offerings:
    description: "Permanent gifts left for the god"
    examples:
      inscribed_jewelry:
        karma: 15-50
        effect: "Permanent temple reputation boost"

      decorated_bowls:
        karma: 10-30
        effect: "Name recorded in temple records"

      ceremonial_weapons:
        karma: 20-75
        effect: "Displayed in temple, legacy recognition"
```

### Offering Disposal

After the god "absorbs" the spiritual essence:

```yaml
offering_redistribution:
  hierarchy:
    1: "High priest receives finest portions"
    2: "Priests receive quality portions"
    3: "Temple workers receive standard portions"
    4: "Surplus sold at temple market"

  player_benefit:
    temple_workers: "Free meals (survival need met)"
    priests: "Quality food + wine rations"

  economic_note: "Temple food is why temple jobs are coveted"
```

---

## Festival Calendar

### The Annual Cycle

Festivals are the only times common citizens see the god directly:

```yaml
major_festivals:
  akitu_spring:
    timing: "Spring equinox"
    duration: "12 days"
    significance: "New Year, barley sowing"

    daily_events:
      day_1_3: "Purification rituals"
      day_4: "Creation myth recitation"
      day_5: "Royal Humiliation ceremony"
      day_6_8: "Processions through city"
      day_9: "Boat of Heaven voyage"
      day_10_11: "Sacred marriage rites"
      day_12: "Blessing of the fields"

    player_activities:
      watching_procession:
        karma: "+5"
        sanity: "+15"
        cost: "Time only"

      participating_in_procession:
        requirements: "Temple worker or invited"
        karma: "+15"
        sanity: "+25"
        payment: "Special rations"

      boat_of_heaven_crew:
        requirements: "Sailor skill + temple favor"
        karma: "+20"
        sanity: "+20"
        payment: "Significant SILA bonus"
        special: "Rare honor, major reputation"

    special_events:
      royal_humiliation:
        description: "High priest strips king, slaps him"
        player_role: "Witness only"
        outcome: "If king cries = good omen for harvest"
        karma_witness: "+3"

  akitu_autumn:
    timing: "Autumn equinox"
    duration: "12 days"
    significance: "Harvest thanksgiving"

    player_activities:
      harvest_offerings:
        karma: "+10"
        sanity: "+20"
        requirement: "Bring portion of your harvest"

      communal_feasting:
        karma: "+5"
        sanity: "+15"
        benefit: "Network with community"

  lunar_feasts:
    timing: "7th and 15th of each month"
    duration: "1 day each"
    significance: "New and full moon observances"

    player_activities:
      moon_offerings:
        karma: "+3"
        sanity: "+8"

      night_markets:
        benefit: "Special goods available"
        social: "Prime networking time"

  kispu_ceremony:
    timing: "End of each month"
    duration: "1 evening"
    significance: "Ancestor remembrance"

    player_activities:
      ancestral_libations:
        karma: "+5"
        sanity: "+10"
        special: "Legacy Point bonus if notable ancestors"

      family_gathering:
        sanity: "+8"
        benefit: "Strengthen household bonds"
```

### Festival Benefits Summary

| Festival | Frequency | Max Karma | Max Sanity | Special Rewards |
|----------|-----------|-----------|------------|-----------------|
| Akitu (Spring) | 1x/year | +40 | +50 | Blessing of Enki (7-day buff) |
| Akitu (Autumn) | 1x/year | +30 | +40 | Harvest bonus |
| Lunar Feasts | 2x/month | +6 | +16 | Night market access |
| Kispu | 1x/month | +10 | +18 | Legacy Point bonus |

---

## Priestly Paths

### Temple Hierarchy

```yaml
temple_hierarchy:
  en_priest:
    title: "En (High Priest/Priestess)"
    description: "Supreme religious authority"
    player_accessible: false
    note: "NPC role, player influence target"

  sanga:
    title: "Sanga (Temple Administrator)"
    description: "Manages temple economy and staff"
    player_accessible: "Late game, exceptional reputation"
    requirements:
      - "Literacy (cuneiform)"
      - "Accounting skills"
      - "Years of temple service"
      - "Divine favor demonstrated"
    income: "Elite stipend + housing"

  gala:
    title: "Gala (Lamentation Priest)"
    description: "Specialist in mourning songs"
    player_accessible: true
    requirements:
      - "Music skill (Journeyman+)"
      - "Specific vocal training"
      - "Temple initiation"
    duties:
      - "Funeral lamentations"
      - "Calming angry gods"
      - "City mourning ceremonies"
    income: "Per-ceremony fees + rations"
    karma_per_service: "+8"
    sanity_cost: "-3 (emotionally draining)"

  gudug:
    title: "Gudug (Purification Priest)"
    description: "Specialist in cleansing rituals"
    player_accessible: true
    requirements:
      - "Ritual knowledge (Journeyman+)"
      - "Clean karma record"
      - "Temple training"
    duties:
      - "Purifying sacred spaces"
      - "Cleansing worshippers"
      - "Preparing ritual materials"
    income: "Steady temple wage"
    karma_per_duty: "+3"

  temple_musician:
    title: "Nar (Temple Musician)"
    description: "Sacred music performer"
    player_accessible: true
    requirements:
      - "Instrument skill (Apprentice+)"
      - "Temple audition passed"
    duties:
      - "Daily meal music"
      - "Festival performances"
      - "Hymn accompaniment"
    income: "Rations + performance bonuses"
    sanity_benefit: "+15 per performance"
```

### Path to Priesthood

```yaml
priestly_progression:
  entry_requirements:
    - "Clean karma (no major crimes)"
    - "Basic literacy recommended"
    - "Temple favor (regular attendance)"

  progression_path:
    stage_1_lay_worshipper:
      duration: "Immediate"
      activities: "Outer court prayer, festival attendance"

    stage_2_temple_helper:
      duration: "Weeks of regular attendance"
      activities: "Offering delivery, basic cleaning"
      benefit: "Access to temple meals"

    stage_3_temple_worker:
      duration: "Months of service"
      activities: "Meal preparation, curtain duty"
      benefit: "Steady employment, housing possible"

    stage_4_specialized_training:
      duration: "Varies by path"
      paths:
        musician: "Instrument mastery + audition"
        purification: "Ritual knowledge + initiation"
        lamentation: "Vocal training + emotional endurance"

    stage_5_ordained_priest:
      requirements: "Demonstrated skill + divine favor"
      benefits: "Full priestly privileges, elite status"
```

---

## Sacred Spaces

### Temple Zones and Access

```yaml
temple_zones:
  outer_courtyard:
    access: "Public"
    activities:
      - "General prayer"
      - "Waiting for audiences"
      - "Market transactions"
    atmosphere: "Busy, commercial"

  inner_courtyard:
    access: "Worshippers with offerings"
    activities:
      - "Formal offerings"
      - "Petition submission"
      - "Festival gathering"
    atmosphere: "Reverent, structured"

  temple_workshops:
    access: "Temple workers"
    activities:
      - "Textile production"
      - "Food preparation"
      - "Administrative work"
    benefit: "Employment, skill learning"

  priest_quarters:
    access: "Temple staff only"
    activities:
      - "Rest, study"
      - "Private rituals"

  inner_sanctum:
    access: "High priests only"
    contents: "The statue of Enki"
    player_access: "Never (maintains mystery)"
    note: "Players may petition for messages to be delivered"
```

### Ziggurat Significance

```yaml
ziggurat:
  description: "The great stepped pyramid beside E-Abzu"

  symbolic_meaning:
    - "Bridge between earth and heaven"
    - "Mountain of the gods"
    - "Visible proof of divine presence"

  player_interaction:
    climbing: "Not permitted (sacred)"
    viewing: "Awe-inspiring (+sanity from beauty)"
    festival_use: "Processions ascend during Akitu"

  gameplay_function:
    - "Navigation landmark"
    - "Symbol of civilization"
    - "Reminder of divine order"
```

---

## Petitions and Divine Favor

### Requesting Divine Aid

```yaml
petition_system:
  process:
    step_1: "Bring offering to inner courtyard"
    step_2: "State petition to attending priest"
    step_3: "Priest evaluates and records"
    step_4: "Petition delivered to god during meal"
    step_5: "Wait for divine response (signs)"

  petition_types:
    healing:
      offering_minimum: "Goat or equivalent"
      success_factors: ["karma", "offering quality", "temple standing"]
      outcome: "Blessing that aids recovery"

    business_success:
      offering_minimum: "Quality offerings over time"
      success_factors: ["consistent worship", "honest dealings"]
      outcome: "Minor luck bonus on transactions"

    fertility:
      offering_minimum: "Significant (lamb+)"
      success_factors: ["karma", "marital status", "dedication"]
      outcome: "Blessing for conception"

    protection:
      offering_minimum: "Variable by threat"
      success_factors: ["karma", "temple service"]
      outcome: "Temporary protection buff"

  divine_response:
    positive_signs:
      - "Favorable omen in divination"
      - "Dream message"
      - "Unexpected good fortune"

    negative_signs:
      - "Bad omens"
      - "Continued misfortune"
      - "Priest reports god's silence"
```

---

## Implementation Notes

### Database Schema

```yaml
player_temple_record:
  player_id: uuid
  last_temple_visit: datetime
  temple_standing: integer  # 0-100
  lifetime_offerings: integer  # total value
  priestly_rank: enum
  festival_participations: array
  petitions_pending: array
  divine_favor_score: integer  # hidden, affects luck
```

### Director AI Integration

```yaml
director_hooks:
  festival_reminder:
    trigger: "3 days before major festival"
    action: "NPC mentions upcoming event"

  neglect_warning:
    trigger: "7 days without temple visit"
    action: "Dreams become disturbing, NPCs comment"

  divine_intervention:
    trigger: "High karma + petition + good standing"
    action: "Small 'miracle' events (found items, avoided danger)"

  punishment_signs:
    trigger: "Very low karma + temple neglect"
    action: "Minor misfortunes increase"
```

### Training Data Capture

```yaml
training_data_points:
  religious_reasoning:
    - "Why did player choose this offering?"
    - "What petition did they make and why?"
    - "How did they interpret omens?"

  ethical_decisions:
    - "Service vs. personal time trade-offs"
    - "Offering quality choices"
    - "Response to divine silence"

  ritual_knowledge:
    - "Correct ritual procedures learned"
    - "Festival participation patterns"
    - "Understanding of religious calendar"
```

---

## Appendix: Sumerian Religious Terms

| Term | Meaning | Gameplay Role |
|------|---------|---------------|
| **E-Abzu** | "House of the Abyss" - Enki's temple | Main temple in Eridu |
| **Mis-Pi** | "Mouth-Washing" ritual | Key priestly duty |
| **Akitu** | New Year festival | Major seasonal event |
| **Kispu** | Ancestor offering ceremony | Monthly family event |
| **En** | High Priest/Priestess | Temple leadership |
| **Sanga** | Temple administrator | Economic management |
| **Gala** | Lamentation singer | Mourning specialist |
| **Nar** | Musician | Temple performer |
| **Gudug** | Purification priest | Cleansing specialist |

---

*"The temple does not judge your wealth. It judges your presence. Show up. Serve. The gods remember."*
