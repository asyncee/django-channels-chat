import json


def parse_message(message):
    return json.loads(message.content['text'])
