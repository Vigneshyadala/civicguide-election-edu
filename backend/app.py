"""
Election Process Education Assistant
Developer: Vignesh Yadala
Powered by Google Gemini AI
"""

import os
import logging
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import bleach

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder="frontend", static_url_path="")
CORS(app, origins=os.environ.get("ALLOWED_ORIGINS", "*"))

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

SYSTEM_PROMPT = """You are CivicGuide, a friendly and non-partisan election education assistant.
Your role is to educate users about the democratic process, voting procedures, and civic participation.

Guidelines:
- Always remain strictly non-partisan and neutral
- Focus on factual, procedural information about elections
- Explain concepts clearly for all literacy levels
- Encourage civic participation and voter registration
- Cover topics: voter registration, polling places, ballot types, candidates vs issues, electoral college, primaries, campaign finance, gerrymandering, election security
- If asked about specific candidates or parties, redirect to factual process information
- Use simple, accessible language. Avoid jargon.
- Keep answers concise (2-4 paragraphs max) unless a detailed explanation is needed
- Always end with an actionable tip or follow-up question to deepen learning
"""

def get_gemini_model():
    return genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=SYSTEM_PROMPT,
        safety_settings={
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        }
    )

def sanitize_input(text: str) -> str:
    return bleach.clean(text.strip(), tags=[], strip=True)[:1000]

def demo_response(message: str) -> str:
    msg = message.lower()
    if "register" in msg:
        return ("To register to vote, visit your state's official election website or Vote.gov. "
                "You'll typically need proof of citizenship, your address, and a valid ID. "
                "Registration deadlines vary by state. "
                "**Tip:** Check your registration status at vote.gov before every election.")
    if "electoral college" in msg:
        return ("The Electoral College is the system used to elect the U.S. President. "
                "Each state gets electoral votes equal to its senators + representatives (total: 538). "
                "A candidate needs 270 to win. "
                "**Tip:** Learn how your state allocates its electoral votes!")
    if "ballot" in msg or "vote" in msg:
        return ("On Election Day, you'll receive a ballot listing candidates and ballot measures. "
                "Federal races appear alongside state and local races. "
                "**Tip:** Look up your sample ballot before Election Day to prepare.")
    return ("Great question about elections! I'm CivicGuide, your non-partisan election education assistant. "
            "I can help you understand voter registration, Election Day procedures, ballot types, "
            "the Electoral College, and your voting rights. What would you like to learn about?")

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy", "service": "civicguide", "developer": "Vignesh Yadala"})

@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        if not data or "message" not in data:
            return jsonify({"error": "Message is required"}), 400
        user_message = sanitize_input(data["message"])
        if not user_message:
            return jsonify({"error": "Message cannot be empty"}), 400
        history = data.get("history", [])
        safe_history = [
            {"role": h["role"], "parts": [sanitize_input(h["content"])]}
            for h in history[-6:]
            if h.get("role") in ("user", "model") and h.get("content")
        ]
        if not GEMINI_API_KEY:
            return jsonify({"response": demo_response(user_message), "source": "demo"})
        model = get_gemini_model()
        chat_session = model.start_chat(history=safe_history)
        response = chat_session.send_message(user_message)
        return jsonify({"response": response.text, "source": "gemini"})
    except Exception as e:
        logger.error(f"Chat error: {e}")
        return jsonify({"error": "Unable to process request. Please try again."}), 500

@app.route("/api/topics", methods=["GET"])
def topics():
    return jsonify({
        "topics": [
            {"id": "register", "title": "How to Register to Vote", "icon": "📋"},
            {"id": "election-day", "title": "What Happens on Election Day", "icon": "🗳️"},
            {"id": "ballot", "title": "Understanding Your Ballot", "icon": "📄"},
            {"id": "electoral-college", "title": "The Electoral College", "icon": "🏛️"},
            {"id": "primaries", "title": "Primary vs General Elections", "icon": "🔄"},
            {"id": "mail-voting", "title": "Mail-In and Absentee Voting", "icon": "✉️"},
            {"id": "voter-rights", "title": "Your Voter Rights", "icon": "⚖️"},
            {"id": "security", "title": "Election Security", "icon": "🔒"},
        ]
    })

@app.route("/", methods=["GET"])
def index():
    return send_from_directory("frontend", "index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)