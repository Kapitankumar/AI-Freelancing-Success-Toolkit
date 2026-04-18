"""
AI Freelancing Success Toolkit
Domain: Freelancing / Gig Economy
API: Google Gemini
Framework: Flask
"""

from flask import Flask, render_template, request, jsonify, session
from google import genai
from dotenv import load_dotenv
import os
from datetime import datetime

# **********************************************************
# Load environment variables from .env file
# **********************************************************

load_dotenv()   # <-- This loads variables from .env into environment

# **********************************************************
# Flask Setup
# **********************************************************

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "freelance-ai-secret-2024")

# **********************************************************
# Gemini Client Setup
# **********************************************************

# Get API key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

MODEL_NAME = "gemini-3-flash-preview"

# **********************************************************
# Routes
# **********************************************************

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/proposal")
def proposal_page():
    return render_template("proposal.html")


@app.route("/chatbot")
def chatbot_page():
    session.setdefault("chat_history", [])
    return render_template("chatbot.html")


# **********************************************************
# Generate Proposal
# **********************************************************

@app.route("/api/generate-proposal", methods=["POST"])
def generate_proposal():

    data = request.get_json()

    project_title = data.get("project_title", "")
    client_name = data.get("client_name", "Client")
    project_desc = data.get("project_desc", "")
    skills = data.get("skills", "")
    budget = data.get("budget", "")
    timeline = data.get("timeline", "")
    tone = data.get("tone", "professional")

    if not project_title or not project_desc:
        return jsonify({"error": "Project title and description required"}), 400

    prompt = f"""
Generate a {tone} freelance project proposal.

Project Title: {project_title}
Client Name: {client_name}

Project Description:
{project_desc}

Skills: {skills}
Budget: {budget}
Timeline: {timeline}

Structure the proposal with:
1. Opening
2. Understanding the project
3. Proposed solution
4. Why choose me
5. Deliverables
6. Timeline
7. Closing call to action

Limit response to 350 words.
"""

    try:

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        proposal_text = response.text

        session.setdefault("proposals", [])
        session["proposals"].append({
            "title": project_title,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "text": proposal_text
        })

        session.modified = True

        return jsonify({"proposal": proposal_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# **********************************************************
# Chatbot API
# **********************************************************

@app.route("/api/chat", methods=["POST"])
def chat():

    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    history = session.get("chat_history", [])

    try:

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=user_message
        )

        bot_reply = response.text

        history.append({"role": "user", "content": user_message})
        history.append({"role": "bot", "content": bot_reply})

        session["chat_history"] = history[-20:]
        session.modified = True

        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# **********************************************************
# Clear Chat
# **********************************************************

@app.route("/api/clear-chat", methods=["POST"])
def clear_chat():

    session["chat_history"] = []
    session.modified = True

    return jsonify({"status": "cleared"})


# **********************************************************
# Run Server
# **********************************************************

if __name__ == "__main__":
    app.run(debug=True, port=5000)