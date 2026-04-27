---

## 🚀 How To Run Locally

### Prerequisites
- Python 3.11+
- Google Gemini API key from [ai.google.dev](https://ai.google.dev)

### Steps

```bash
# 1. Clone the repo
git clone https://github.com/Vigneshyadala/civicguide-election-edu
cd civicguide-election-edu

# 2. Install dependencies
cd backend
pip install -r requirements.txt

# 3. Set Gemini API key
set GEMINI_API_KEY=your-key-here

# 4. Run backend
python app.py
```

Then open `frontend/index.html` in your browser.

---

## ☁️ Deploy to Google Cloud Run

```bash
./deploy.sh YOUR_GCP_PROJECT_ID YOUR_GEMINI_API_KEY
```

---

## 🌐 Google Services Used

| Service | Usage |
|---|---|
| **Google Gemini 1.5 Flash** | Powers the AI chat assistant |
| **Google Cloud Run** | Serverless deployment |
| **Google Cloud Build** | Container build and push |

---

## 🔐 Security

- XSS prevention with `bleach` input sanitization
- HTML escaping on all user content
- Non-root Docker container
- Gemini safety filters enabled
- CORS configurable via environment variable

---

## 🧪 Testing

```bash
pip install pytest
pytest
```

20+ tests covering chat, sanitization, security, and API endpoints.

---

## 👨‍💻 Developer

**Vignesh Yadala**  
🔗 [github.com/Vigneshyadala](https://github.com/Vigneshyadala)
👨‍💻 Author
Vignesh Yadala
Email:vignesh.yadala@gmail.com

---

## 📄 License

MIT License © 2025 Vignesh Yadala

---

*Built with ❤️ for civic education. Democracy works better when citizens understand it.*  
