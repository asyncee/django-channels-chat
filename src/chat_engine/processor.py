from django.dispatch import receiver

from . import events
from .utils import parse_message


class EventProcessor:
    pass


class WebsocketEventProcessor(EventProcessor):

    def handle_connect(self, message):
        pass

    def handle_receive(self, message):
        payload = parse_message(message)
        action = payload['type']

        if action == "connect":
            r = events.user_joined.send_robust(
                sender=self.__class__, message=message, payload=payload)
            print(r)

        elif action == 'message':
            if payload['text'].startswith('/'):
                # chat command
                r = events.chat_command.send_robust(
                    sender=self.__class__, message=message, payload=payload)
                print(r)
            else:
                # chat message
                r = events.chat_message.send_robust(
                    sender=self.__class__, message=message, payload=payload)
                print(r)

    def handle_disconnect(self, message):
        r = events.user_left.send_robust(sender=self.__class__, message=message)
        print(r)


processor = WebsocketEventProcessor()
