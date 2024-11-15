# api/slack.py
import os
from slack_bolt import App
from slack_bolt.adapter.vercel import VercelRequestHandler
from dotenv import load_dotenv
from flask import Flask

# Load environment variables
load_dotenv()

# Initialize your Slack bot app
app = App(
    token=os.getenv("SLACK_BOT_TOKEN"),
    signing_secret=os.getenv("SLACK_SIGNING_SECRET")
)

# Define a simple event listener for mentions
@app.event("app_mention")
def handle_app_mention(event, say):
    user = event.get("user")
    say(f"Hello, <@{user}>! 👋")

# Define a simple slash command
@app.command("/hello")
def handle_hello_command(ack, respond, command):
    ack()
    user = command.get("user_name")
    respond(f"Hello, {user}!")

# Setup Vercel handler
flask_app = Flask(__name__)
handler = VercelRequestHandler(app)

@flask_app.route("/api/slack", methods=["POST"])
def slack_events():
    return handler.handle(flask_app.request)

# For Vercel, we expose the Flask app
def app(event, context):
    return flask_app(event, context)
