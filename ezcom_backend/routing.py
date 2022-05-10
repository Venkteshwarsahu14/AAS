from channels.routing import ProtocolTypeRouter, URLRouter
from my_proj.game.routing import websockets
application = ProtocolTypeRouter({
    "websocket": websockets,
})