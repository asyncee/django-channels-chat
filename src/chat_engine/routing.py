from channels.routing import route
from channels.sessions import channel_session

from .message_router import get_router
from .engine import get_engine


router = get_router()
engine = get_engine()


routing = [
    route("websocket.receive", channel_session(router.handle_receive)),
    route("websocket.disconnect", channel_session(router.handle_disconnect)),

    route("chat.connect", engine.on_connect),
    route("chat.message", engine.on_message),
    route("chat.command", engine.on_command),
    route("chat.disconnect", engine.on_disconnect),
]
