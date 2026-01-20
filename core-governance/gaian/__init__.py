"""
Gaian Governance Engine

The proprietary governance layer that maintains balance between
probabilistic AI systems and deterministic rules.

Copyright (c) 2026 Analog Economy. All rights reserved.
This code is proprietary and confidential.
"""

__version__ = "0.1.0"
__author__ = "Analog Economy"

from .core.policy_engine import PolicyEngine
from .core.ethics_filter import EthicsFilter
from .core.novelty_scorer import NoveltyScorer
from .core.anti_cheat import AntiCheat
from .core.data_gate import DataGate

__all__ = [
    "PolicyEngine",
    "EthicsFilter",
    "NoveltyScorer",
    "AntiCheat",
    "DataGate",
]
