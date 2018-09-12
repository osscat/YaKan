from django.urls import path
from . import consumers
from django.conf.urls import url

websocket_urlpatterns = [
    # 元のコードは→url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
    path('Django/ws/chat/echo/', consumers.EchoConsumer),
    path('ws/chat/echo/', consumers.EchoConsumer),
]
