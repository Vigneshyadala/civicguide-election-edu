# 🏛️ CivicGuide — Election Process Education Assistant

<div align="center">

![Election Education](https://img.shields.io/badge/Election-Education-blue?style=for-the-badge&logo=googlechrome)
![AI Powered](https://img.shields.io/badge/AI-Powered-orange?style=for-the-badge&logo=google)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge)

### 🚀 AI-Powered Civic Education Platform

*Empowering citizens with non-partisan, factual information about the democratic process*

[🌐 Live Demo](https://civicguide-election-edu-185024642346.us-central1.run.app) • [📖 Documentation](#tech-stack) • [🐙 GitHub](https://github.com/Vigneshyadala/civicguide-election-edu)

---

**Built for Google Antigravity Challenge 2026**

[![GitHub Stars](https://img.shields.io/github/stars/Vigneshyadala/civicguide-election-edu?style=social)](https://github.com/Vigneshyadala/civicguide-election-edu)
[![GitHub Forks](https://img.shields.io/github/forks/Vigneshyadala/civicguide-election-edu?style=social)](https://github.com/Vigneshyadala/civicguide-election-edu/fork)

</div>

---

## 🎯 Problem Statement

Many citizens lack basic knowledge about the democratic process, leading to lower civic participation:

| Challenge | Impact |
|-----------|--------|
| 🗳️ **Voter Confusion** | Citizens don't know how to register or where to vote |
| 📄 **Ballot Complexity** | Ballots are hard to understand without guidance |
| 🏛️ **Civic Ignorance** | Electoral College and primaries are widely misunderstood |
| ⚖️ **Rights Unawareness** | Many don't know their voting rights |
| 📉 **Low Participation** | Lack of knowledge leads to disengagement from democracy |

> **Result:** Lower voter turnout, uninformed decisions, and weakened democratic participation.

---

## 💡 The Solution

A **smart AI-powered civic education assistant** that provides non-partisan, factual information about elections — making democracy accessible to everyone.

<div align="center">

### 🎨 From Confusion to Civic Confidence

```
❓ Ask Any Election Question  →  🤖 AI Analysis  →  📚 Clear Explanation  →  🗳️ Informed Citizen
```

</div>

---

## ✨ Core Capabilities

### 🤖 1. AI-Powered Chat Assistant
- Powered by **Google Gemini 2.5 Flash**
- Non-partisan, factual election information
- Covers voter registration, ballots, Electoral College, and more
- Context-aware conversation history

### 📋 2. Curated Election Topics
- 8 key civic education topics
- One-click topic shortcuts
- Structured, easy-to-understand answers

### 🧠 3. Interactive Knowledge Quiz
- Test your election knowledge
- Instant feedback with explanations
- Covers key civic concepts

### 🗳️ 4. Voter Registration CTA
- Direct link to vote.gov
- State-specific guidance
- Registration deadline reminders

### ♿ 5. Fully Accessible Design
- WCAG 2.1 AA compliant
- Screen reader support
- Keyboard navigation
- High contrast mode

### 🔒 6. Secure Backend
- XSS prevention with bleach sanitization
- Input length limits
- Non-root Docker container
- Gemini safety filters enabled

---

## 🛠️ Tech Stack

<div align="center">

### Frontend
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

### Backend
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-22.0-499848?style=for-the-badge&logo=gunicorn&logoColor=white)

### AI & Google Services
![Gemini](https://img.shields.io/badge/Google_Gemini-2.5_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Cloud Run](https://img.shields.io/badge/Cloud_Run-Serverless-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)
![Cloud Build](https://img.shields.io/badge/Cloud_Build-CI/CD-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)

</div>

---

## 🚀 Features

<table>
<tr>
<td width="50%">

### 💬 Smart AI Chat
- ✅ Ask any election question
- ✅ Non-partisan responses
- ✅ Conversation history
- ✅ Fallback demo mode

</td>
<td width="50%">

### 📚 Topic Shortcuts
- ✅ Voter Registration
- ✅ Election Day Guide
- ✅ Ballot Explained
- ✅ Electoral College

</td>
</tr>
<tr>
<td width="50%">

### 🧠 Knowledge Quiz
- ✅ Interactive questions
- ✅ Instant explanations
- ✅ Civic facts
- ✅ Score tracking

</td>
<td width="50%">

### 🔐 Security & Access
- ✅ Input sanitization
- ✅ ARIA labels
- ✅ Skip links
- ✅ Mobile responsive

</td>
</tr>
</table>

---

## 🌐 Live Demo

<div align="center">

### 🔗 Try it Now!

**Live App:** [https://civicguide-election-edu-185024642346.us-central1.run.app](https://civicguide-election-edu-185024642346.us-central1.run.app)

**Health Check:** [/health](https://civicguide-election-edu-185024642346.us-central1.run.app/health)

**GitHub Repo:** [https://github.com/Vigneshyadala/civicguide-election-edu](https://github.com/Vigneshyadala/civicguide-election-edu)

</div>

---

## 💻 Running Locally

### Prerequisites
```bash
- Python 3.11+
- Google Gemini API key from ai.google.dev
- Git
```

### Setup

```bash
# Clone the repository
git clone https://github.com/Vigneshyadala/civicguide-election-edu
cd civicguide-election-edu

# Install dependencies
cd backend
pip install -r requirements.txt

# Set Gemini API key (Windows)
set GEMINI_API_KEY=your-key-here

# Run backend
python app.py
```

Then open `frontend/index.html` in your browser.

**Backend will be available at:** `http://localhost:8080`

---

## ☁️ Deploy to Google Cloud Run

```bash
./deploy.sh YOUR_GCP_PROJECT_ID YOUR_GEMINI_API_KEY
```

Or manually:

```bash
gcloud run deploy civicguide-election-edu \
  --source backend \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GEMINI_API_KEY=your-key
```

---

## 📁 Project Structure

```
civicguide-election-edu/
│
├── 📂 backend/
│   ├── app.py              # Flask API + Gemini AI
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile          # Cloud Run container
│   └── 📂 frontend/
│       └── index.html      # Served by Flask
│
├── 📂 frontend/
│   └── index.html          # Single-page web app
│
├── 📂 tests/
│   └── test_app.py         # 20+ pytest tests
│
├── deploy.sh               # GCP deployment script
├── pytest.ini              # Test configuration
├── .gitignore              # Git ignore rules
└── README.md               # Project documentation
```

---

## 🧪 Testing

```bash
pip install pytest
pytest
```

20+ tests covering:
- Health endpoint
- Chat API
- Input sanitization
- Security headers
- Topic endpoints

---

## 🌐 Google Services Used

| Service | Usage |
|---------|-------|
| **Google Gemini 2.5 Flash** | Powers the AI chat assistant |
| **Google Cloud Run** | Serverless deployment |
| **Google Cloud Build** | Container build and CI/CD |

---

## 🔐 Security

| Feature | Implementation |
|---------|---------------|
| XSS Prevention | `bleach` input sanitization |
| HTML Escaping | All user content escaped |
| Container Security | Non-root Docker user |
| AI Safety | Gemini safety filters enabled |
| CORS | Configurable via environment variable |
| Input Limits | 1000 character max per message |

---

## 📈 Performance

| Metric | Value |
|--------|-------|
| ⚡ Response Time | < 2 seconds |
| 📦 Repo Size | < 10 MB |
| 🧪 Test Coverage | 20+ tests |
| ♿ Accessibility | WCAG 2.1 AA |
| 🌿 Branch | Single (main) |

---

## 🔮 Future Enhancements

### 📅 Phase 1
- [ ] State-specific election information
- [ ] Multi-language support
- [ ] Voter registration deadline alerts

### 📅 Phase 2
- [ ] Integration with official election APIs
- [ ] Ballot measure explainer
- [ ] Polling location finder

### 📅 Phase 3
- [ ] Mobile app (iOS/Android)
- [ ] Push notifications for election dates
- [ ] Multilingual AI responses

---

## 📄 License

This project is licensed under the **MIT License** © 2026 Vignesh Yadala

---

## 👨‍💻 Developer

<div align="center">

### **Vignesh Yadala**

[![GitHub](https://img.shields.io/badge/GitHub-Vigneshyadala-181717?style=for-the-badge&logo=github)](https://github.com/Vigneshyadala)
[![Email](https://img.shields.io/badge/Email-vignesh.yadala@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:vignesh.yadala@gmail.com)

**🏆 Google Antigravity Challenge 2026**

*Built with ❤️ for civic education. Democracy works better when citizens understand it.*

</div>

---

## 🙏 Acknowledgments

- 🤖 [Google Gemini](https://ai.google.dev/) for the AI API
- ☁️ [Google Cloud Run](https://cloud.google.com/run) for serverless hosting
- 🏆 Google Antigravity Challenge organizers
- 🗳️ [Vote.gov](https://vote.gov) for voter registration resources

---

<div align="center">

### 🌟 If this helped you learn about elections, give it a star! 🌟

**Built for Google Antigravity Challenge 2026**

---

**© 2026 Vignesh Yadala. All rights reserved.**

</div>
