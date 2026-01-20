"""
Biome IDs - Canonical biome identifiers.

This is the source of truth for biome identification across all components.
"""

# Biome identifiers
BIOME_ABYSS = "abyss"
BIOME_SCORCH = "scorch"
BIOME_RUINS = "ruins"
BIOME_AQUA = "aqua"
BIOME_BOTANY = "botany"
BIOME_THEATER = "theater"
BIOME_EXODUS = "exodus"
BIOME_BRINK = "brink"
BIOME_VECTOR = "vector"
BIOME_UPRISING = "uprising"

# All biome IDs
ALL_BIOMES = [
    BIOME_ABYSS,
    BIOME_SCORCH,
    BIOME_RUINS,
    BIOME_AQUA,
    BIOME_BOTANY,
    BIOME_THEATER,
    BIOME_EXODUS,
    BIOME_BRINK,
    BIOME_VECTOR,
    BIOME_UPRISING,
]

# Biome classifications
STANDARD_BIOMES = [BIOME_ABYSS, BIOME_SCORCH, BIOME_RUINS, BIOME_AQUA, BIOME_BOTANY]
SENSITIVE_BIOMES = [BIOME_EXODUS]
RESTRICTED_BIOMES = [BIOME_THEATER, BIOME_BRINK, BIOME_VECTOR]
CRITICAL_BIOMES = [BIOME_UPRISING]

# Biome display names
BIOME_NAMES = {
    BIOME_ABYSS: "The Abyss",
    BIOME_SCORCH: "The Scorch",
    BIOME_RUINS: "The Ruins",
    BIOME_AQUA: "The Aqua",
    BIOME_BOTANY: "The Botany",
    BIOME_THEATER: "The Theater",
    BIOME_EXODUS: "The Exodus",
    BIOME_BRINK: "The Brink",
    BIOME_VECTOR: "The Vector",
    BIOME_UPRISING: "The Uprising",
}

# Biome themes
BIOME_THEMES = {
    BIOME_ABYSS: "Deep Ocean",
    BIOME_SCORCH: "High Desert / Mars",
    BIOME_RUINS: "Disaster / Rubble",
    BIOME_AQUA: "Water Scarcity",
    BIOME_BOTANY: "Food Security",
    BIOME_THEATER: "Geopolitics",
    BIOME_EXODUS: "Migration",
    BIOME_BRINK: "Nuclear Escalation",
    BIOME_VECTOR: "Bio-Warfare",
    BIOME_UPRISING: "Man vs. Machine",
}
