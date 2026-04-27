# CivicGuide - Election Process Education Assistant

Developer: Vignesh Yadala
GitHub: https://github.com/Vigneshyadala
Email: Vignesh.yadala@gmail.com
Powered by: Google Gemini AI + Google Cloud Run

## About

CivicGuide is a smart AI-powered election education assistant built to help citizens understand the democratic process. It provides non-partisan, factual information about voting, registration, ballots, and civic participation.

Built by Vignesh Yadala for the Google Antigravity Challenge.

## Features

- AI Chat powered by Google Gemini
- 8 curated election topics
- Interactive knowledge quiz
- Voter registration link to vote.gov
- WCAG 2.1 AA accessible design
- Secure backend with input sanitization

## Project Structure

- backend/app.py - Flask API + Gemini AI
- backend/requirements.txt - Python dependencies
- backend/Dockerfile - Cloud Run container
- frontend/index.html - Single page web app
- tests/test_app.py - 20 pytest tests
- deploy.sh - GCP deployment script

## How To Run Locally

1. Clone the repo
   git clone https://github.com/Vigneshyadala/civicguide-election-edu

2. Install dependencies
   cd backend
   pip install -r requirements.txt

3. Set Gemini API key
   set GEMINI_API_KEY=your-key-here

4. Run backend
   python app.py

5. Open frontend/index.html in your browser

## Deploy to Google Cloud Run

deploy.sh YOUR_GCP_PROJECT_ID YOUR_GEMINI_API_KEY

## Google Services Used

- Google Gemini 1.5 Flash - Powers the AI chat
- Google Cloud Run - Serverless deployment
- Google Cloud Build - Container build and push

## Security

- XSS prevention with bleach sanitization
- HTML escaping on all user content
- Non-root Docker container
- Gemini safety filters enabled
- CORS configurable via environment variable

## Testing

Run pytest
20 tests covering chat, sanitization, security, and API endpoints.

## Developer

Vignesh Yadala
GitHub: https://github.com/Vigneshyadala
Email: Vignesh.yadala@gmail.com

## License

MIT License 2025 Vignesh Yadala

Built with love for civic education. Democracy works better when citizens understand it.