# rock_n_roll/apps.py

from django.apps import AppConfig

class DefaultConfig(AppConfig):
    name = 'chat_engine'
    verbose_name = "Chat Engine"

    def ready(self):
        pass
