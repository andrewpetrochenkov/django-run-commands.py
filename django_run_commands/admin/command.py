from django.contrib import admin
from django.utils.html import format_html
from django.utils.timesince import timesince
from django_run_commands.models import Command

class CommandAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'args',
        'separator',
        'shell',
        'seconds',
        'order',
        'is_logged',
        'is_disabled',
        'is_running',
        'started_at',
        'completed_at',
        'duration',
        'timesince'
    ]
    list_filter = ['seconds','is_disabled','is_running']
    readonly_fields = ['is_running','started_at','completed_at','duration','timesince']
    search_fields = ['name', ]

    def shell(self, command):
        return format_html('<code>python manage.py %s%s</code>' % (command.name,' %s' % command.args if command.args else ''))
    shell.short_description = 'shell'
    shell.allow_tags = True

    def duration(self, command):
        if command.started_at and command.completed_at:
            s = str(command.completed_at - command.started_at)
            return s.split('.')[0] + '.' + s.split('.')[1][0:6] if '.' in s else s
    duration.short_description = 'duration'

    def timesince(self, command):
        if command.completed_at:
            return timesince(command.completed_at).split(',')[0]+' ago'
    timesince.short_description = ''

admin.site.register(Command, CommandAdmin)
