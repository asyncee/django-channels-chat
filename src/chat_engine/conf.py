from django.conf import settings


CHAT_ROUTER = getattr(settings, 'ROUTER', 'chat_engine.message_router.MessageRouter')
CHAT_ENGINE = getattr(settings, 'ENGINE', 'chat_engine.engine')
