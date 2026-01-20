# SRP_EXEMPT: evaluate() is 79 LOC - needs refactoring in future PR
"""
Data Gate - Final checkpoint before data exits the system.

This module is the last line of defense, ensuring that only
properly vetted and approved data is exported to buyers.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any

import pendulum
from pendulum import DateTime


class ExportDecision(Enum):
    """Possible outcomes of export evaluation."""

    APPROVED = "approved"
    PENDING_REVIEW = "pending_review"
    REJECTED = "rejected"
    QUARANTINED = "quarantined"


@dataclass
class ExportRequest:
    """A request to export data to a buyer."""

    buyer_id: str
    biome_id: str
    record_count: int
    data_hash: str
    requested_at: DateTime
    classification: str


@dataclass
class ExportResult:
    """Result of export gate evaluation."""

    decision: ExportDecision
    request: ExportRequest
    reasons: list[str]
    requires_human_review: bool
    audit_id: str | None


class DataGate:
    """
    Final checkpoint for data export.

    Responsibilities:
    - Verify buyer authorization
    - Check biome access permissions
    - Enforce batch size limits
    - Trigger human review when required
    - Generate audit logs
    """

    def __init__(self, config: dict[str, Any]):
        """Initialize data gate with configuration."""
        self.config = config.get("exports", {})
        self.human_review_threshold = self.config.get("require_human_review_above", 1000)
        self.max_batch_size = self.config.get("max_batch_size", 10000)
        self.allowed_buyers = self._load_allowed_buyers()

        # Audit log
        self._audit_log: list[dict[str, Any]] = []

    def _load_allowed_buyers(self) -> dict[str, dict[str, Any]]:
        """Load allowed buyer configurations."""
        buyers = {}
        for buyer in self.config.get("allowed_buyers", []):
            buyers[buyer["id"]] = buyer
        return buyers

    def evaluate(self, request: ExportRequest) -> ExportResult:
        """
        Evaluate an export request.

        Args:
            request: The export request to evaluate

        Returns:
            ExportResult with decision and audit information
        """
        # Check batch size
        if request.record_count > self.max_batch_size:
            return ExportResult(
                decision=ExportDecision.REJECTED,
                request=request,
                reasons=[
                    f"Batch size {request.record_count} exceeds maximum {self.max_batch_size}"
                ],
                requires_human_review=False,
                audit_id=self._create_audit_entry(request, "rejected_batch_size"),
            )

        # Check buyer authorization
        buyer_config = self.allowed_buyers.get(request.buyer_id)
        if buyer_config is None:
            return ExportResult(
                decision=ExportDecision.REJECTED,
                request=request,
                reasons=[f"Buyer '{request.buyer_id}' is not authorized"],
                requires_human_review=False,
                audit_id=self._create_audit_entry(request, "rejected_unauthorized"),
            )

        # Check biome access
        allowed_biomes = buyer_config.get("biomes", [])
        if request.biome_id not in allowed_biomes:
            return ExportResult(
                decision=ExportDecision.REJECTED,
                request=request,
                reasons=[f"Buyer not authorized for biome '{request.biome_id}'"],
                requires_human_review=False,
                audit_id=self._create_audit_entry(request, "rejected_biome_access"),
            )

        # Check classification level
        buyer_clearance = buyer_config.get("classification_level", "UNCLASSIFIED")
        if not self._clearance_sufficient(buyer_clearance, request.classification):
            return ExportResult(
                decision=ExportDecision.REJECTED,
                request=request,
                reasons=[
                    f"Buyer clearance '{buyer_clearance}' insufficient for '{request.classification}' data"
                ],
                requires_human_review=False,
                audit_id=self._create_audit_entry(request, "rejected_clearance"),
            )

        # Check if human review required
        requires_review = request.record_count > self.human_review_threshold or buyer_config.get(
            "ethics_board_approval", False
        )

        if requires_review:
            return ExportResult(
                decision=ExportDecision.PENDING_REVIEW,
                request=request,
                reasons=["Human review required for this export"],
                requires_human_review=True,
                audit_id=self._create_audit_entry(request, "pending_review"),
            )

        # Approved
        return ExportResult(
            decision=ExportDecision.APPROVED,
            request=request,
            reasons=[],
            requires_human_review=False,
            audit_id=self._create_audit_entry(request, "approved"),
        )

    def _clearance_sufficient(self, buyer_clearance: str, data_classification: str) -> bool:
        """Check if buyer clearance is sufficient for data classification."""
        clearance_levels = {
            "UNCLASSIFIED": 0,
            "RESTRICTED": 1,
            "SECRET": 2,
            "TOP_SECRET": 3,
        }

        buyer_level = clearance_levels.get(buyer_clearance, 0)
        data_level = clearance_levels.get(data_classification, 0)

        return buyer_level >= data_level

    def _create_audit_entry(self, request: ExportRequest, status: str) -> str:
        """Create an audit log entry and return the audit ID."""
        audit_id = f"AUDIT-{pendulum.now('UTC').format('YYYYMMDDHHmmss')}-{len(self._audit_log)}"

        entry = {
            "audit_id": audit_id,
            "timestamp": pendulum.now("UTC").to_iso8601_string(),
            "buyer_id": request.buyer_id,
            "biome_id": request.biome_id,
            "record_count": request.record_count,
            "data_hash": request.data_hash,
            "status": status,
        }

        self._audit_log.append(entry)

        return audit_id

    def get_audit_log(self) -> list[dict[str, Any]]:
        """Get the full audit log."""
        return self._audit_log.copy()
