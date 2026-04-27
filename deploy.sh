#!/bin/bash
# deploy.sh — Deploy Election Education Assistant to Google Cloud Run
# Usage: ./deploy.sh YOUR_PROJECT_ID YOUR_GEMINI_API_KEY

set -e

PROJECT_ID=${1:-"your-gcp-project-id"}
GEMINI_API_KEY=${2:-""}
SERVICE_NAME="election-edu-assistant"
REGION="us-central1"
IMAGE="gcr.io/$PROJECT_ID/$SERVICE_NAME"

echo "🗳️  Deploying CivicGuide Election Education Assistant"
echo "Project: $PROJECT_ID | Region: $REGION"

# Build & push container
gcloud builds submit ./backend --tag "$IMAGE" --project "$PROJECT_ID"

# Deploy to Cloud Run
gcloud run deploy "$SERVICE_NAME" \
  --image "$IMAGE" \
  --platform managed \
  --region "$REGION" \
  --allow-unauthenticated \
  --memory 512Mi \
  --cpu 1 \
  --max-instances 10 \
  --set-env-vars "GEMINI_API_KEY=$GEMINI_API_KEY" \
  --project "$PROJECT_ID"

SERVICE_URL=$(gcloud run services describe "$SERVICE_NAME" \
  --platform managed --region "$REGION" \
  --format 'value(status.url)' --project "$PROJECT_ID")

echo ""
echo "✅ Deployment successful!"
echo "🌐 Service URL: $SERVICE_URL"
echo ""
echo "Next steps:"
echo "  1. Update API_BASE in frontend/index.html to: $SERVICE_URL"
echo "  2. Host frontend/index.html via Firebase Hosting or Cloud Storage"
echo "  3. Test: curl $SERVICE_URL/health" 
