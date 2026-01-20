"""
Golden Spike Tests - Phase 1

Tests the core observability infrastructure:
- /health endpoint returns valid JSON with ORJSONResponse
- X-Trace-ID header is present on all responses
- Timestamps use UTC (pendulum)

Architecture Rules:
- NEVER use datetime. ALWAYS use pendulum.
- NEVER use json. ALWAYS use orjson.
- ALWAYS use create_autospec() for mocks (not needed here - pure integration tests).
"""

import re

import pendulum
import pytest
from fastapi.testclient import TestClient
from gaian.main import app


@pytest.fixture
def client() -> TestClient:
    """Create a test client for the Gaian API."""
    return TestClient(app)


class TestHealthEndpoint:
    """Tests for the /health endpoint."""

    def test_health_returns_200(self, client: TestClient) -> None:
        """Health endpoint should return HTTP 200 OK."""
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_returns_valid_json(self, client: TestClient) -> None:
        """Health endpoint should return valid JSON with expected fields."""
        response = client.get("/health")

        # Should be valid JSON (orjson handles serialization)
        data = response.json()

        # Check required fields exist
        assert "status" in data
        assert "version" in data
        assert "environment" in data
        assert "timestamp" in data
        assert "checks" in data

        # Check values are correct types
        assert data["status"] == "healthy"
        assert isinstance(data["version"], str)
        assert isinstance(data["environment"], str)
        assert isinstance(data["timestamp"], str)
        assert isinstance(data["checks"], dict)

    def test_health_timestamp_is_utc_iso_format(self, client: TestClient) -> None:
        """Health endpoint timestamp should be in UTC ISO format (pendulum)."""
        # Get time before request
        before = pendulum.now("UTC")

        response = client.get("/health")
        data = response.json()

        # Get time after request
        after = pendulum.now("UTC")

        # Parse the timestamp - should be valid ISO format
        timestamp_str = data["timestamp"]
        timestamp = pendulum.parse(timestamp_str)

        # Should be between before and after (within reasonable bounds)
        assert timestamp >= before.subtract(seconds=1)
        assert timestamp <= after.add(seconds=1)

        # Should be UTC timezone
        assert timestamp.timezone_name == "UTC" or "+00:00" in timestamp_str


class TestTraceIDMiddleware:
    """Tests for the X-Trace-ID middleware."""

    def test_trace_id_header_present_in_response(self, client: TestClient) -> None:
        """All responses should include X-Trace-ID header."""
        response = client.get("/health")

        assert "X-Trace-ID" in response.headers
        assert response.headers["X-Trace-ID"] is not None
        assert len(response.headers["X-Trace-ID"]) > 0

    def test_trace_id_is_valid_uuid4_format(self, client: TestClient) -> None:
        """Generated trace ID should be a valid UUID4 format."""
        response = client.get("/health")

        trace_id = response.headers["X-Trace-ID"]

        # UUID4 format: 8-4-4-4-12 hex characters
        uuid_pattern = re.compile(
            r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
            re.IGNORECASE,
        )
        assert uuid_pattern.match(trace_id), f"Trace ID '{trace_id}' is not valid UUID4"

    def test_trace_id_echoes_client_provided_id(self, client: TestClient) -> None:
        """If client provides X-Trace-ID, server should echo it back."""
        client_trace_id = "test-trace-id-12345"

        response = client.get("/health", headers={"X-Trace-ID": client_trace_id})

        assert response.headers["X-Trace-ID"] == client_trace_id

    def test_trace_id_unique_per_request(self, client: TestClient) -> None:
        """Each request without client trace ID should get a unique ID."""
        response1 = client.get("/health")
        response2 = client.get("/health")

        trace_id_1 = response1.headers["X-Trace-ID"]
        trace_id_2 = response2.headers["X-Trace-ID"]

        assert trace_id_1 != trace_id_2


class TestPingEndpoint:
    """Tests for the /ping endpoint."""

    def test_ping_returns_pong(self, client: TestClient) -> None:
        """Ping endpoint should return pong."""
        response = client.get("/ping")

        assert response.status_code == 200
        assert response.json() == {"ping": "pong"}

    def test_ping_has_trace_id(self, client: TestClient) -> None:
        """Ping endpoint should also have trace ID."""
        response = client.get("/ping")

        assert "X-Trace-ID" in response.headers


class TestRootEndpoint:
    """Tests for the root endpoint."""

    def test_root_returns_service_info(self, client: TestClient) -> None:
        """Root endpoint should return service information."""
        response = client.get("/")

        assert response.status_code == 200
        data = response.json()

        assert "service" in data
        assert "version" in data
        assert "status" in data
        assert data["service"] == "Gaian Governance Service"

    def test_root_has_trace_id(self, client: TestClient) -> None:
        """Root endpoint should also have trace ID."""
        response = client.get("/")

        assert "X-Trace-ID" in response.headers
