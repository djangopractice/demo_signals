from django.apps import AppConfig


class PollsConfig(AppConfig):
    name = 'polls'
    verbose_name = 'Polls Application'

    def ready(self):
        import polls.signals
