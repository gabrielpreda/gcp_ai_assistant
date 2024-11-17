#!/bin/bash

# Purpose: To deploy the App to Cloud Run.


# Check if correct parameters were provided
if [ "$#" -ne 2 ]; then
    echo "Error: Invalid number of arguments."
    echo "Usage: $0 <PROJECT> <LOCATION>"
    exit 1
fi

# Google Cloud Project
PROJECT=$1 

# Google Cloud Region
LOCATION=$2 

echo "Deployment with parameters:"
echo "Project: $PROJECT"
echo "Location: $LOCATION"


# Depolying app from source code
sudo ~/google-cloud-sdk/bin/gcloud run deploy gemini-ai-assistant --source . --region=$LOCATION --project=$PROJECT --allow-unauthenticated