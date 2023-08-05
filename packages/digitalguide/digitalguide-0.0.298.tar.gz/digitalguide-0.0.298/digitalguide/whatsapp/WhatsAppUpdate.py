class WhatsAppUpdate:

    def __init__(self, object, entry) -> None:
        self._object = object
        self.entry = [WhatsAppEntry(**e) for e in entry]


class WhatsAppEntry:
    def __init__(self, id, changes) -> None:
        self.id = id
        self.changes = [WhatsAppChange(**change) for change in changes]


class WhatsAppChange:
    def __init__(self, value, field):
        self.value = [WhatsAppValue(**v) for v in value]
        self.field = field


class WhatsAppValue:
    def __init__(self, contacts, errors, messaging_product, messages, metadata, statuses):
        self.contacts = [WhatsAppContact(**contact) for contact in contacts]
        self.errors = [WhatsAppError(**error) for error in errors]
        self.messaging_product = messaging_product
        self.messages = [WhatsAppMessage(**message) for message in messages]
        metadata = WhatsAppMetadata(metadata)
        statuses = [WhatsAppStatus(**status) for status in statuses]


class WhatsAppContact:
    def __init__(self, wa_id, profile) -> None:
        self.wa_id = wa_id
        self.profile_name = profile.name


class WhatsAppError:
    def __init__(self, code, title) -> None:
        self.code = code
        self.title = title


class WhatsAppMessage:
    def __init__(self, audio, button, context, document, errors, _from, id, identity, image, interactive, order, referral, sticker, system, text, timestamp, type, video) -> None:
        self.audio = WhatsAppAudio(**audio)
        self.button = WhatsAppButton(**button)
        self.context = context
        self.document = document
        self.errors = errors
        self._from = _from
        self.id = id
        self.identity = identity
        self.image = image
        self.interactive = interactive
        self.order = order
        self.referral = referral
        self.sticker = sticker
        self.system = system
        self.text = text
        self.timestamp = timestamp
        self._type = type
        self.video = video


class WhatsAppAudio:
    def __init__(self, id, mime_type) -> None:
        self.id = id
        self.mime_type = mime_type


class WhatsAppButton:
    def __init__(self, payload, text) -> None:
        self.payload = payload
        self.text = text


class WhatsAppMetadata:
    def __init__(self, display_phone_number, phone_number_id) -> None:
        self.display_phone_number = display_phone_number
        self.phone_number_id = phone_number_id


class WhatsAppStatus:
    def __init__(self, conversation, id, pricing, recipient_id, status, timestamp) -> None:
        self.conversation = WhatsAppConversation(**conversation)
        self.id = id
        self.pricing_category = pricing.category
        self.pricing_model = pricing.model
        self.recipient_id = recipient_id
        self.status = status
        self.timestamp = timestamp


class WhatsAppConversation:
    def __init__(self, id, origin, expiration_timestamp) -> None:
        self.id = id
        self.origin_type = origin.type
        self.expiration_timestamp = expiration_timestamp
