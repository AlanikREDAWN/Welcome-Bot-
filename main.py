from slack_bolt import App
# from slack_bolt import WebClient
from dotenv import load_dotenv
import time
import os

load_dotenv()


# Initialize your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

@app.command("/hello-world-lilia1")
def hello_world_lilia1(ack, say, body, client):
    ack()
    say("testing")
    
@app.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(f"Hey there <@{message['user']}>!")


# New functionality
@app.event("app_home_opened")
def update_home_tab(client, event, logger, ack, say):
  ack()
  try:
    # views.publish is the method that your app uses to push a view to the Home tab
    client.views_publish(
      # the user that opened your app's app home
      user_id=event["user"],
      # the view object that appears in the app home
      view={
        "type": "home",
        "callback_id": "home_view",

        # body of the view
        "blocks": [
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "*Welcome to your _App's Home tab_* :tada:"
            }
          },
          {
            "type": "divider"
          },
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "This button won't do much for now but you can set up a listener for it using the `actions()` method and passing its unique `action_id`. See an example in the `examples` folder within your Bolt app."
            }
          },
          {
            "type": "actions",
            "elements": [
              {
                "type": "button",
                "text": {
                  "type": "plain_text",
                  "text": "Click me!"
                }
              }
            ]
          }
        ]
      }
    )

  except Exception as e:
    logger.error(f"Error publishing home tab: {e}")

@app.event("member_joined_channel")
def member_joined_channel(client, event, logger, body, ack, say):
    # logger.info(body)
    ack()
    try:
        message_blocks = [
          {
            "type": "section",
            "text": {
              "type": "plain_text",
              "text": "KittyCat also had a pet bird named Oly, in case you were wondering",
            }
          },
          {
            "type": "actions",
            "elements": [
              {
                "type": "button",
                "text": {
                  "type": "plain_text",
                  "text": "Hello! Nice to meet you!"
                },
                "value": "click_me_123",
                "action_id": "actionId-0"
              }
            ]
          }
        ]

        message_blocks1 = [
          {
            "type": "section",
            "text": {
              "type": "plain_text",
              "text": "Meow",
            }
          },
          {
            "type": "image",
            "image_url": "https://cloud-l5rmdnp6x-hack-club-bot.vercel.app/0img_7625.jpg",
            "alt_text": "Carly kitty"
          }
        ]
        userInfo = client.users_info(
           user=event["user"]
        )
        print(userInfo)
        result = client.chat_postMessage(
            channel="C07MYBDLBGU",
            text=f"Meow! <@{event['user']}> has joined the cattery!",
            username="Alex",
            icon_url="https://cloud-7tyr8vl40-hack-club-bot.vercel.app/0img_4717.jpeg",
            link_names=True
        )
        print(result)

        global ts
        ts = result["ts"]
        
        print(ts)
        client.chat_postMessage(
           channel="C07MYBDLBGU",
           text="Meow! A new guest! Welcome, my name is Alex",
           username="Alex",
           icon_url="https://cloud-7tyr8vl40-hack-club-bot.vercel.app/0img_4717.jpeg",
           thread_ts=ts
        )
        time.sleep(3)
        client.chat_postMessage(
           channel="C07MYBDLBGU",
           text="And mine is Carly. We're KittyCat's cats, and this is KittyCat's Cattery",
           username="Carly",
           icon_url="https://cloud-l5rmdnp6x-hack-club-bot.vercel.app/0img_7625.jpg",
           thread_ts=ts,
        )
        time.sleep(3)
        client.chat_postMessage(
           channel="C07MYBDLBGU",
           text="KittyCat also had a pet bird named Oly, in case you were wondering",
           username="Alex",
           icon_url="https://cloud-7tyr8vl40-hack-club-bot.vercel.app/0img_4717.jpeg",
           thread_ts=ts,
           blocks=message_blocks
        )

        # client.chat_postMessage(
        #    channel="C07MYBDLBGU",
        #    text="Meow meow",
        #    username="Carly",
        #    icon_url="https://cloud-l5rmdnp6x-hack-club-bot.vercel.app/0img_7625.jpg",
        #    thread_ts=ts,
        #    blocks=message_blocks1
        # )
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")

# @app.event("member_joined_channel")
# def member_joined_channel(client, event, logger, ack):
#     ack()
#     try:
#         # Send a message to the channel the user joined
#         client.chat_postMessage(
#             channel=event["channel"],
#             text=f"Hello <@{event['user']}>! Welcome to the channel! 🎉"
#         )
#     except Exception as e:
#         logger.error(f"Error in 'member_joined_channel' handler: {e}")

@app.action("actionId-0")
def second_button(client, event, logger, body, ack):
    ack()
    try:
      message_blocks2 = [
        {
          "type": "section",
          "text": {
            "type": "plain_text",
            "text": "We're so happy you joined the cattery, we love having new faces. Would you like to get to know us better?",
          }
        },
        {
          "type": "actions",
          "elements": [
            {
              "type": "button",
              "text": {
                "type": "plain_text",
                "text": "Sure!"
              },
              "value": "click_me_123",
              "action_id": "actionId-1"
            }
          ]
        }
      ]
      client.chat_postMessage(
          channel="C07MYBDLBGU",
          text="We're so happy you joined the cattery, we love having new faces. Would you like to get to know us better?",
          username="Alex",
          icon_url="https://cloud-7tyr8vl40-hack-club-bot.vercel.app/0img_4717.jpeg",
          thread_ts=ts,
          blocks=message_blocks2
      )
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")


@app.action("actionId-1")
def first_button(client, event, logger, body, ack):
    ack()
    try:
      message_blocks3 = [
        {
          "type": "section",
          "text": {
            "type": "plain_text",
            "text": "Yeah! We even have our own treadmill, and plently of toys, but my favorite is the food. What about you, Carly?... Carly? Carly? Oh, great, she's doing it again"
          }
        },
        {
          "type": "actions",
          "elements": [
            {
              "type": "button",
              "text": {
                "type": "plain_text",
                "text": "Doing what?"
              },
              "value": "click_me_123",
              "action_id": "actionId-2"
            }
          ]
        }
      ]
      client.chat_postMessage(
           channel="C07MYBDLBGU",
           text="Okay then! As for breed, we're cornish rex cats, a very playful breed",
           username="Carly",
           icon_url="https://cloud-l5rmdnp6x-hack-club-bot.vercel.app/0img_7625.jpg",
           thread_ts=ts,
        )
      time.sleep(3)
      client.chat_postMessage(
          channel="C07MYBDLBGU",
          text="Yeah! We even have our own treadmill, and plently of toys, but my favorite is the food. What about you, Carly?... Carly? Carly? Oh, great, she's doing it again",
          username="Alex",
          icon_url="https://cloud-7tyr8vl40-hack-club-bot.vercel.app/0img_4717.jpeg",
          thread_ts=ts,
          blocks=message_blocks3
      )

    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")

@app.action("actionId-2")
def first_button(client, event, logger, body, ack):
    ack()
    try:
      message_blocks4 = [
        {
          "type": "section",
          "text": {
            "type": "plain_text",
            "text": "Staring at the wall. She does it all the time. I have no idea why... I promise you, she is a really smart cat...most of the time..."
          }
        },
        {
          "type": "image",
          "image_url": "https://cloud-790dmg8j3-hack-club-bot.vercel.app/0untitled_design.png",
          "alt_text": "Carly staring at the wall"
        }
      ]

      client.chat_postMessage(
          channel="C07MYBDLBGU",
          text="Staring at the wall. She does it all the time. I have no idea why... I promise you, she is a really smart cat...most of the time...",
          username="Alex",
          icon_url="https://cloud-7tyr8vl40-hack-club-bot.vercel.app/0img_4717.jpeg",
          thread_ts=ts,
          blocks=message_blocks4
      )
      time.sleep(3)
      client.chat_postMessage(
           channel="C07MYBDLBGU",
           text="Meow...hey guys, what's up?",
           username="Carly",
           icon_url="https://cloud-l5rmdnp6x-hack-club-bot.vercel.app/0img_7625.jpg",
           thread_ts=ts,
        )
      time.sleep(3)
      client.chat_postMessage(
          channel="C07MYBDLBGU",
          text="You were staring at the wall again",
          username="Alex",
          icon_url="https://cloud-7tyr8vl40-hack-club-bot.vercel.app/0img_4717.jpeg",
          thread_ts=ts,
      )
      time.sleep(3)
      client.chat_postMessage(
           channel="C07MYBDLBGU",
           text="No I wasn't. Anyways, welcome again to the cattery! Feel free to take a look around the channel. Meow!",
           username="Carly",
           icon_url="https://cloud-l5rmdnp6x-hack-club-bot.vercel.app/0img_7625.jpg",
           thread_ts=ts,
        )

    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")
    # channel_name = "kittycats-cattery"
    # conversation_id = None
    # try:
    #     # Call the conversations.list method using the WebClient
    #     for result in client.conversations_list():
    #         if conversation_id is not None:
    #             break
    #         for channel in result["channels"]:
    #             if channel["name"] == channel_name:
    #                 conversation_id = channel["id"]
    #                 #Print result
    #                 print(f"Found conversation ID: {conversation_id}")
    #                 break

    #     # ID of channel you want to post message to
    #     channel_id = conversation_id


    #     # Call the conversations.list method using the WebClient
    #     result = client.chat_postMessage(
    #         channel=channel_id,
    #         text="Hello world!"
    #         # You could also use a blocks[] array to send richer content
    #     )
    #     # Print result, which includes information about the message (like TS)
    #     print(result)

    # except Exception as e:
    #     logger.error(f"Error: {e}")
        
        


   

# Ready? Start your app!
if __name__ == "__main__":
   app.start(port=int(os.environ.get("PORT", 3000)))

