import time

from django.conf import settings
from django.core.management.base import BaseCommand

from django_run_commands.models import Command, Log
from django_run_commands.utils import run_commands

SLEEP = float(getattr(settings,'RUN_COMMANDS_SLEEP',0.1))


class Command(BaseCommand):

    def handle(self, *args, **options):
        while True:
            run_commands()
            time.sleep(SLEEP)

