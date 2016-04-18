import json

from django.dispatch import receiver
from django.utils.translation import ugettext as _
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
        self.send(
            message.reply_channel, messages.system(_('Welcome to the chat!')))
        self.broadcast(
            messages.system(_('User %(username)s joined chat') % payload))
        self.group.add(message.reply_channel)

    def on_user_left(self, message, **kwargs):
        self.group.discard(message.reply_channel)
        self.broadcast(messages.system(
            _('User %(user)s left chat') % message.channel_session))

    def on_chat_message(self, message, payload, **kwargs):
        user = message.channel_session['user']
        message = messages.info(payload['text'], user)
        self.broadcast(message)

    def on_chat_command(self, message, payload, **kwargs):
        user = message.channel_session['user']
        command = payload['text']

        if command.startswith('/me') and len(command.split()) > 1:
            text = ' '.join(command.split()[1:])
            message = messages.system('{} {}'.format(user, text))
            self.broadcast(message)

        else:
            msg = messages.system(
                _('Error: no such command %(command)') % {'command': command})
            self.send(message.reply_channel, msg)


chat = Chat()
