from datetime import date
from django.contrib import admin
from django.utils.html import format_html
from django.utils.timesince import timesince
from django_run_commands.models import Command

class CommandAdmin(admin.ModelAdmin):
    # fields = ('name',)
    fields = [
        'name',
        'args',
        'seconds',
        'order',
        'is_logged',
        'is_disabled',
    ]
    list_display = [
        'id',
        'name',
        'args',
        'seconds',
        'order',
        'is_logged',
        'is_disabled',
        'is_running',
        'started_at_str',
        'completed_at_str',
        'duration',
        'timesince'
    ]
    list_filter = ['name','seconds','is_disabled','is_running']
    readonly_fields = ['is_running','started_at','completed_at','duration','timesince']
    search_fields = ['name', ]

    def shell(self, command):
        return format_html('<code>python manage.py %s%s</code>' % (command.name,' %s' % command.args if command.args else ''))
    shell.short_description = 'shell'
    shell.allow_tags = True

    def started_at_str(self,command):
        if command.started_at:
            if command.started_at.date()==date.today():
                return command.started_at.strftime('%H:%M:%S')
            return command.started_at.strftime('%Y-%m-%d %H:%M:%S')
    started_at_str.short_description = 'started'

    def completed_at_str(self,command):
        if command.completed_at:
            if command.completed_at.date()==date.today():
                return command.completed_at.strftime('%H:%M:%S')
            return command.completed_at.strftime('%Y-%m-%d %H:%M:%S')
    completed_at_str.short_description = 'completed'

    def duration(self, command):
        if command.started_at and command.completed_at:
            s = str(command.completed_at - command.started_at)
            return s.split('.')[0] + '.' + s.split('.')[1][0:3] if '.' in s else s
    duration.short_description = 'duration'

    def timesince(self, command):
        if command.completed_at:
            return timesince(command.completed_at).split(',')[0]+' ago'
    timesince.short_description = 'timesince'

admin.site.register(Command, CommandAdmin)
