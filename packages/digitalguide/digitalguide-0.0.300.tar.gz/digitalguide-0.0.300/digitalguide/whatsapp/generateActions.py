import asyncio
from collections import defaultdict
from digitalguide.whatsapp.WhatsAppUpdate import WhatsAppUpdate
import yaml

from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')

import os

def read_action_yaml(filename, action_functions={}):
    with open(filename) as file:
        yaml_dict = yaml.load(file, Loader=yaml.FullLoader)

    actions_dict = {}

    for key, value in yaml_dict.items():
        actions_dict[key] = Action(value, action_functions=action_functions)

    return actions_dict

class Action():
    def __init__(self, actions, action_functions={}, log_user=True, log_interaction=True):
        self.actions = actions
        self.action_functions = action_functions
        self.log_user = log_user
        self.log_interaction = log_interaction
        if log_user or log_interaction:
            import mongoengine
            dbname = config["bot"]["bot_name"]
            if os.getenv('DATABASE_CERT', None):
                # This can be remove in the future
                with open("ca-certificate.crt", "w") as text_file:
                    text_file.write(os.getenv('DATABASE_CERT'))
                mongoengine.connect(alias=dbname, host="mongodb+srv://" + os.getenv("DATABASE_USERNAME")+":" + os.getenv("DATABASE_PASSWORD") +
                                    "@" + os.getenv("DATABASE_HOST") + "/"+dbname+"?authSource=admin&tls=true&tlsCAFile=ca-certificate.crt")
            else:
                mongoengine.connect(alias=dbname, host="mongodb+srv://" + os.getenv("DATABASE_USERNAME")+":" + os.getenv("DATABASE_PASSWORD") +
                                    "@" + os.getenv("DATABASE_HOST") + "/"+dbname+"?authSource=admin&tls=true")
            


    async def __call__(self, client, update: WhatsAppUpdate, context):
        if self.log_user and not ("user_id" in context.keys()):
            from digitalguide.twilio.db_objects import TwilioUser
            db_user = TwilioUser(ProfileName=update.ProfileName,
                           WaId=update.WaId)
            db_user.save()
            context["user_id"] = db_user

        if self.log_interaction:
            from digitalguide.twilio.db_objects import TwilioInteraction

            TwilioInteraction(user=context["user_id"],
                            Latitude = update.Latitude,
                            Longitude = update.Longitude,
                            SmsMessageSid = update.SmsMessageSid,
                            NumMedia = update.NumMedia,
                            ProfileName = update.ProfileName,
                            SmsSid = update.SmsSid,
                            WaId = update.WaId,
                            SmsStatus = update.SmsStatus,
                            Body = update.Body,
                            To = update.To,
                            NumSegments = update.NumSegments,
                            MessageSid = update.MessageSid,
                            AccountSid = update.AccountSid,
                            From = update.From,
                            ApiVersion = update.ApiVersion,
                            MediaContentType0 = update.MediaContentType0,
                            MediaUrl0 = update.MediaUrl0,
                            MessagingServiceSid = update.MessagingServiceSid,
                            ReferralNumMedia = update.ReferralNumMedia
                            ).save()




        for item in self.actions:
            if item["type"] == "return":
                return item["state"]

            if item["type"] == "message":
                client.send_message(item["text"].format(
                        **{"profileName": update.ProfileName, "echo": update.Body, **context}), update.get_from())
                
            elif item["type"] == "venue":
                client.send_location(
                    name=item["title"],
                    lat=item["latitude"],
                    long=item["longitude"],
                    address=item["address"],
                    recipient_id=update.get_from()
                )
            elif item["type"] == "photo":
                client.send_image(
                    item["url"],
                    update.get_from()
                )
            elif item["type"] == "video":
                client.send_video(
                    item["url"],
                    update.get_from()
                )
            elif item["type"] == "media_group":
                pass
                #message = client.messages.create(
                #    media_url=item["urls"],
                #    from_=update.To,
                #    to=update.From
                #)
            elif item["type"] == "audio" or item["type"] == "voice":
                client.send_audio(
                    [item["url"]],
                    update.get_from()
                )
            elif item["type"] == "poll":
                message = item["question"] + "\n"
                for option in item["options"]:
                    message += option + "\n"
                client.send_message(message, update.get_from())

            elif item["type"] == "function":
                arguments = {i: item[i]
                             for i in item if i != 'type' and i != 'func'}
                self.action_functions[item["func"]](
                    client, update, context, **arguments)