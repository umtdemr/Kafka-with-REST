from channels.generic.websocket import AsyncJsonWebsocketConsumer


class LogConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("gossip", self.channel_name)
        print(f"Added {self.channel_name} channel to gossip")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("gossip", self.channel_name)
        print(f"Removed {self.channel_name} channel to gossip")

    async def receive(self, text_data=None, bytes_data=None):
        # await self.send("Connected")
        await self.channel_layer.group_send(
            "gossip",
            {
                "type": "log.gossip",
                "message": "msg from websocket",
            },
        )

    async def log_gossip(self, event):
        print("------------------------")
        await self.send_json(event)
        print(f"Got message at {self.channel_name}")
