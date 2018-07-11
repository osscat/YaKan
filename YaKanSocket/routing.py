from django.urls import path
from . import consumers


websocket_urlpatterns = [
    # 元のコードは→url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
    path('ws/chat/echo/', consumers.EchoConsumer),
]