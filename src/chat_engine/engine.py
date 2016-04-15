import json

from django.dispatch import receiver
from channels import Group

from . import events
from . import messages


class Chat:

    def __init__(self):
        events.user_joined.connect(self.on_user_joined)
        events.user_left.connect(self.on_user_left)
        events.chat_message.connect(self.on_chat_message)
        events.chat_command.connect(self.on_chat_command)

    @property
    def group(self):
        return Group('chat')

    def broadcast(self, message):
        self.group.send(message)

    def send(self, channel, message):
        channel.send(message)

    def on_user_joined(self, message, payload, **kwargs):
        message.channel_session['user'] = payload['username']
        self.send(message.reply_channel, messages.system('Добро пожаловать в чат!'))
        self.broadcast(messages.system('Пользователь {} вошёл в чат'.format(payload['username'])))
        self.group.add(message.reply_channel)

    def on_user_left(self, message, **kwargs):
        self.group.discard(message.reply_channel)
        user = message.channel_session['user']
        self.broadcast(messages.system('Пользователь {} покинул чат'.format(user)))

    def on_chat_message(self, message, payload, **kwargs):
        user = message.channel_session['user']
        message = messages.info(payload['text'], user)
        self.broadcast(message)

    def on_chat_command(self, message, payload, **kwargs):
        pass


chat = Chat()
