# Introduction  

Gemini Chatbot demonstrate how to quickly build and deploy a chatbot powered with Gemini.  

The user interface is developed using Streamlit.  

The application is deployed with Cloud Run.

![](images/gemini_ai_assistant.jpg)


# Deployment using Google Cloud SDK


To deploy  the application, run the command:

```.\deploy.sh```

This will result in runing the deployment for the chatbot app.

```gcloud run deploy simple-app --source . --region=$LOCATION --project=$PROJECT --allow-unauthenticated```

# Start app

The application will run when Cloud Run instance will start.