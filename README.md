# 🤖 AI Freelancing Success Toolkit

**Domain:** Freelancing / Gig Economy  
**API Used:** Google Gemini 1.5 Flash (Free Tier)  
**Framework:** Flask (Python)  
**Course:** INT428 – Domain-Specific Generative AI Chatbot  

---

## 📋 Project Overview

A web application that helps freelancers:
1. **Generate professional client proposals** using AI (Gemini API)
2. **Get real-time guidance** on client communication via an AI chatbot

### Features
- ✅ Proposal Generator (3 tone options: Professional / Friendly / Bold)
- ✅ Copy & Download proposals as .txt
- ✅ AI Chatbot with session memory (last 20 turns)
- ✅ Quick-prompt buttons for common freelancing questions
- ✅ Clean dark-mode responsive UI

### Model Configuration
| Parameter | Value | Reason |
|-----------|-------|--------|
| Temperature | 0.7 | Balanced creativity for proposals |
| Top-p | 0.9 | Broad but focused vocabulary |
| Max Tokens | 1024 | Full proposal length |
| Model | gemini-1.5-flash | Free tier, fast responses |

---

## 🚀 Step-by-Step Setup Guide (For Beginners)

### Prerequisites
- A computer with Windows / macOS / Linux
- Internet connection

---

### STEP 1 — Install Python

1. Go to https://www.python.org/downloads/
2. Download **Python 3.11** (or newer)
3. Run the installer — **IMPORTANT:** check the box ✅ "Add Python to PATH"
4. Click Install
5. Verify: open Terminal (or Command Prompt) and type:
   ```
   python --version
   ```
   You should see something like `Python 3.11.x`

---

### STEP 2 — Install VS Code

1. Go to https://code.visualstudio.com/
2. Download and install for your OS
3. Open VS Code
4. Install the **Python extension**:
   - Click the Extensions icon (left sidebar, looks like 4 squares)
   - Search "Python" → click Install on the one by Microsoft

---

### STEP 3 — Install Git

1. Go to https://git-scm.com/downloads
2. Download and install for your OS
3. Verify: open Terminal and type:
   ```
   git --version
   ```

---

### STEP 4 — Get Your FREE Gemini API Key

1. Go to https://aistudio.google.com/app/apikey
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy the key — it looks like `AIzaSy...`
5. Keep it safe — you'll need it in Step 7

---

### STEP 5 — Create a GitHub Account & Repository

1. Go to https://github.com and sign up (free)
2. Click the **"+"** → **"New repository"**
3. Name it: `ai-freelancing-toolkit`
4. Check "Public" (or Private)
5. Click **"Create repository"**
6. Copy the repository URL (e.g., `https://github.com/yourusername/ai-freelancing-toolkit.git`)

---

### STEP 6 — Open the Project in VS Code

1. Download or clone this project folder
2. Open VS Code → **File → Open Folder** → select `ai-freelancing-toolkit`
3. Open the integrated terminal: **Terminal → New Terminal**

---

### STEP 7 — Set Up Environment Variables

1. In the project folder, find the file `.env.example`
2. Make a copy and rename it to `.env`
3. Open `.env` and replace the placeholders:
   ```
   GEMINI_API_KEY=AIzaSy_YOUR_ACTUAL_KEY_HERE
   SECRET_KEY=any_random_string_like_abc123xyz
   ```
4. Save the file — **never share this file or commit it to GitHub**

---

### STEP 8 — Create a Virtual Environment

In the VS Code terminal, run these commands one by one:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` appear at the start of your terminal line — this means the virtual environment is active.

---

### STEP 9 — Install Required Libraries

With the virtual environment active, run:
```bash
pip install -r requirements.txt
```

This installs Flask, Google Generative AI, and all other dependencies.

---

### STEP 10 — Run the App Locally

```bash
python app.py
```

You should see:
```
* Running on http://127.0.0.1:5000
```

Open your browser and go to: **http://localhost:5000**

Your app is running! 🎉

---

### STEP 11 — Commit & Push to GitHub

In VS Code terminal (make sure you're in the project folder):

```bash
# Initialize git (first time only)
git init

# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/ai-freelancing-toolkit.git

# Stage all files
git add .

# Commit with a message
git commit -m "Initial commit: AI Freelancing Toolkit"

# Push to GitHub
git push -u origin main
```

If it asks for login, use your GitHub username and a **Personal Access Token** (not your password):
- Go to GitHub → Settings → Developer Settings → Personal Access Tokens → Generate new token

---

### STEP 12 — Making Changes & Committing Again

Every time you edit files:
```bash
git add .
git commit -m "Your description of what changed"
git push
```

---

## 📁 Project Structure

```
ai-freelancing-toolkit/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template
├── .env                    # Your actual keys (NOT committed to GitHub)
├── .gitignore              # Files to ignore in git
├── README.md               # This file
├── templates/
│   ├── base.html           # Navigation & layout
│   ├── index.html          # Home page
│   ├── proposal.html       # Proposal generator page
│   └── chatbot.html        # AI chat guide page
└── static/
    ├── css/style.css       # All styling
    └── js/
        ├── main.js         # Shared JS
        ├── proposal.js     # Proposal logic
        └── chatbot.js      # Chat logic
```

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError` | Make sure venv is active and `pip install -r requirements.txt` was run |
| `API key invalid` | Double-check your `.env` file has the correct key |
| Port already in use | Run `python app.py` on a different port: change `port=5000` to `port=5001` in app.py |
| `git push` fails | Make sure you created the GitHub repo and used the correct remote URL |

---

## 📊 Evaluation Criteria Mapping (INT428)

| Criteria | How this project addresses it |
|----------|-------------------------------|
| Problem Identification | Freelancer proposal & communication challenge |
| Domain Specificity | Freelancing domain, prompt-engineered responses |
| API Integration | Google Gemini 1.5 Flash via official SDK |
| Prompt Engineering | Structured prompt with tone, sections, word limits |
| Model Config (Temp/Top-p) | Temperature=0.7, Top-p=0.9, documented in code |
| Working Prototype | Full web app with UI |
| Societal Impact | Helps gig workers compete more effectively |

---

## 👨‍💻 Author
INT428 Project — AI Freelancing Success Toolkit
