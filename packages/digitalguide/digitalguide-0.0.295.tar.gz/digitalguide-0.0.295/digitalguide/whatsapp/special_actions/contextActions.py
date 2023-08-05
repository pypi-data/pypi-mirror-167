from digitalguide.whatsapp.WhatsAppUpdate import WhatsAppUpdate


def whatsapp_default_name(client, update: WhatsAppUpdate, context):
    context["name"] = update.ProfileName


def whatsapp_save_text_to_context(client, update: WhatsAppUpdate, context, key):
    context[key] = update.Body


def whatsapp_save_value_to_context(client, update: WhatsAppUpdate, context, key, value):
    context[key] = value


twilio_action_functions = {"default_name": whatsapp_default_name,
                           "save_text_to_context": whatsapp_save_text_to_context,
                           "save_value_to_context": whatsapp_save_value_to_context
                           }
