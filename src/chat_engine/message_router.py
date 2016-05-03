import json

from django.dispatch import receiver
from django.utils.module_loading import import_string

from channels import Channel

from . import conf


class MessageRouter:

    def handle_receive(self, message):
        message, payload = self.decode_message(message)
        action = payload['type']

        if action == "connect":
            self.route('chat.connect', message)

        elif action == 'message':
            if payload['text'].startswith('/'):
                self.route('chat.command', message)
            else:
                self.route('chat.message', message)

    def handle_disconnect(self, message):
        self.route('chat.disconnect', message)

    def decode_message(self, message):
        payload = json.loads(message.content['text'])
        message.content['text'] = payload
        return message, payload

    def route(self, channel, message):
        Channel(channel).send(message.content)


def get_router(*args, **kwargs):
    return import_string(conf.CHAT_ROUTER)(*args, **kwargs)
