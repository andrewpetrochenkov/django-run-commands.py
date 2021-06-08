from django.contrib import admin
from django.utils.html import format_html
from django.utils.timesince import timesince
from django_run_commands.models import Log

class LogAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'args',
        'shell',
        'out',
        'started_at',
        'completed_at',
        'duration',
        'timesince'
    ]
    list_filter = ['name',]
    search_fields = ['name', ]

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def shell(self, log):
        return format_html('<code>python manage.py %s%s</code>' % (log.name,' %s' % log.args if log.args else ''))
    shell.short_description = 'shell'
    shell.allow_tags = True

    def duration(self, log):
        if log.started_at and log.completed_at:
            s = str(log.completed_at - log.started_at)
            return s.split('.')[0] + '.' + s.split('.')[1][0:6] if '.' in s else s
    duration.short_description = 'duration'

    def timesince(self, log):
        if log.completed_at:
            return timesince(log.completed_at).split(',')[0]+' ago'
    timesince.short_description = ''

admin.site.register(Log, LogAdmin)

