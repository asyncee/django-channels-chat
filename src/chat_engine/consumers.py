import json
import random

from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels.sessions import channel_session

from .processor import processor


@channel_session
def ws_connect(message):
    processor.handle_connect(message)


@channel_session
def ws_receive(message):
    processor.handle_receive(message)


@channel_session
def ws_disconnect(message):
    processor.handle_disconnect(message)
