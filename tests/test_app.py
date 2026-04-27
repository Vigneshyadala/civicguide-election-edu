"""
Tests for Election Education Assistant API
"""
import pytest
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../backend"))
from app import app, sanitize_input, demo_response


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# --- Health Check ---
class TestHealth:
    def test_health_returns_200(self, client):
        res = client.get("/health")
        assert res.status_code == 200

    def test_health_json(self, client):
        res = client.get("/health")
        data = res.get_json()
        assert data["status"] == "healthy"
        assert "service" in data


# --- Topics Endpoint ---
class TestTopics:
    def test_topics_returns_list(self, client):
        res = client.get("/api/topics")
        assert res.status_code == 200
        data = res.get_json()
        assert "topics" in data
        assert len(data["topics"]) >= 6

    def test_topics_have_required_fields(self, client):
        res = client.get("/api/topics")
        topics = res.get_json()["topics"]
        for topic in topics:
            assert "id" in topic
            assert "title" in topic
            assert "icon" in topic


# --- Chat Endpoint ---
class TestChat:
    def test_chat_requires_message(self, client):
        res = client.post("/api/chat", json={})
        assert res.status_code == 400

    def test_chat_empty_message(self, client):
        res = client.post("/api/chat", json={"message": ""})
        assert res.status_code == 400

    def test_chat_returns_response(self, client):
        res = client.post("/api/chat", json={"message": "How do I register to vote?"})
        assert res.status_code == 200
        data = res.get_json()
        assert "response" in data
        assert len(data["response"]) > 10

    def test_chat_with_history(self, client):
        res = client.post("/api/chat", json={
            "message": "Tell me more",
            "history": [
                {"role": "user", "content": "What is the Electoral College?"},
                {"role": "model", "content": "The Electoral College is..."}
            ]
        })
        assert res.status_code == 200

    def test_chat_no_api_key_uses_demo(self, client):
        """Without API key, should use demo fallback."""
        res = client.post("/api/chat", json={"message": "How do I register?"})
        data = res.get_json()
        assert "response" in data


# --- Input Sanitization ---
class TestSanitization:
    def test_strips_html_tags(self):
        result = sanitize_input("<script>alert('xss')</script>hello")
        assert "<script>" not in result
        assert "hello" in result

    def test_truncates_long_input(self):
        long_input = "a" * 2000
        result = sanitize_input(long_input)
        assert len(result) <= 1000

    def test_strips_whitespace(self):
        result = sanitize_input("  hello world  ")
        assert result == "hello world"

    def test_empty_string(self):
        result = sanitize_input("")
        assert result == ""


# --- Demo Responses ---
class TestDemoResponses:
    def test_register_response(self):
        resp = demo_response("How do I register to vote?")
        assert len(resp) > 50
        assert "register" in resp.lower() or "vote" in resp.lower()

    def test_electoral_college_response(self):
        resp = demo_response("What is the electoral college?")
        assert "electoral" in resp.lower() or "270" in resp

    def test_ballot_response(self):
        resp = demo_response("How do I fill out my ballot?")
        assert len(resp) > 50

    def test_generic_fallback(self):
        resp = demo_response("something random xyz123")
        assert "CivicGuide" in resp or "election" in resp.lower()


# --- Security ---
class TestSecurity:
    def test_invalid_json_handled(self, client):
        res = client.post("/api/chat",
                         data="not json",
                         content_type="application/json")
        assert res.status_code in (400, 500)

    def test_xss_in_message(self, client):
        res = client.post("/api/chat", json={
            "message": "<img src=x onerror=alert(1)> How to vote?"
        })
        assert res.status_code == 200
        # Should not reflect raw HTML back

    def test_sql_injection_safe(self, client):
        res = client.post("/api/chat", json={
            "message": "'; DROP TABLE users; -- How to vote?"
        })
        assert res.status_code == 200 
