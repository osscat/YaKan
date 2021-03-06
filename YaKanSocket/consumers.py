from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


class EchoConsumer(WebsocketConsumer):

    def connect(self):
        self.room_group_name = 'Yakan'


        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data, **kwargs):
        text_data_json = json.loads(text_data)
        text_data_json['type'] = 'yakan_message'

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            text_data_json
        )

    # Receive message from room group
    def yakan_message(self, event):
        # Send message to WebSocket
        self.send(text_data=json.dumps(event))
