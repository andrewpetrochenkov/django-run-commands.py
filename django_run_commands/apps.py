from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError

class Config(AppConfig):
    name = 'django_run_commands'
    verbose_name = 'run-commands'

    def ready(self):
        from .models import Command, Log

        try:
            Command._meta.verbose_name_plural = 'Commands (%s)' % Command.objects.all().count()
            Log._meta.verbose_name_plural = 'Logs (%s)' % Log.objects.all().count()
        except (OperationalError, ProgrammingError):
            pass
