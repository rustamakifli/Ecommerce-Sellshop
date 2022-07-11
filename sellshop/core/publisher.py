from django.conf import settings
import json

class Publish:
    channel_name = 'events'

    def __init__(self, data, event_type):
        self.data = data
        self.event_type = event_type
        self._publish()

    def _stringfy(self):
        return str({
            "data": self.data,
            "event_type": self.event_type
        })

    def _publish(self):
        settings.REDIS_CLIENT.publish(self.channel_name,self._stringfy())