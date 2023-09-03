from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack, AuthMiddleware


application = ProtocolTypeRouter({
        'websocket': AuthMiddlewareStack(
            URLRouter(
            
            )
        )
})
