##  Introduction
Hack 20 Bot is a discord bot that takes code and a specified language as input and outputs the result. Format your command in the form:



------------------------------------------
!run
\`\`\`{language (case insensitive)}
//CODE
\`\`\`
------------------------------------------
Supported languages:
Java

## Requirements
All dependencies are listed within `requirements.txt`. Install them with

```
pip install -r requirements.txt
```

## Instructions
### Local
To start the bot locally, install the required dependencies and run the following:

```
python bot.py
```

### Google Cloud
To deploy the bot on Google Cloud:

* [Download the Google Cloud SDK](https://cloud.google.com/sdk/docs)
* Create a Google Cloud project

```
gcloud projects create [YOUR_PROJECT_ID] --set-as-default
```

* Create the application

```
gcloud app create --project=[YOUR_PROJECT_ID]
```

* [Enable billing for the project](https://console.cloud.google.com/projectselector2/billing)
* Deploy the bot

```
gcloud app deploy
```

