from datetime import datetime, timedelta

from django.core.management import call_command

from .models import Command


def run_commands():
    qs = Command.objects.all()
    if qs.filter(is_running=True).count():
        qs.filter(is_running=True).update(is_running=False)
    for c in filter(lambda c:not c.is_disabled,qs.order_by('order')):
        if not c.completed_at or c.completed_at<datetime.now()-timedelta(seconds=c.seconds):
            c.call_command()
