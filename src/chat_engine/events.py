from django.dispatch import Signal


chat_event = Signal(providing_args=["message"])

user_joined = Signal(providing_args=["message", "payload"])
user_left = Signal(providing_args=["message"])
chat_message = Signal(providing_args=["message", "payload"])
chat_command = Signal(providing_args=["message", "payload"])
