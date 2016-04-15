from channels.routing import route, include

from chat_engine.routing import routing as chat_routing


routing = [
    include(chat_routing, path=r"^/chat"),
]
