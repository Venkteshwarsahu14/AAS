import os
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from aas import consumers

from django.urls import re_path,path
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ezcom_backend.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket":AuthMiddlewareStack(
URLRouter(
[path('aas/notification_testing/',consumers.NotificationConsumer)]
))
    
    
    
})