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


