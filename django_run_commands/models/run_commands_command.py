__all__ = ['Command']

from datetime import datetime
from io import StringIO
import logging

from django.db import models
from django.core.management import call_command

from .run_commands_log import  Log

class Command(models.Model):
    name = models.CharField(max_length=255)
    args = models.CharField(max_length=255,null=True,blank=True)
    separator= models.TextField(default=' ')
    seconds = models.IntegerField()
    order = models.IntegerField(default=0)

    is_disabled = models.BooleanField(null=True,verbose_name='disabled')
    is_logged = models.BooleanField(null=True,verbose_name='logged')

    is_running = models.BooleanField(default=False,verbose_name='running')
    started_at = models.DateTimeField(null=True)
    completed_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'run_commands_command'
        indexes = [
           models.Index(fields=['name',]),
           models.Index(fields=['is_disabled',]),
           models.Index(fields=['is_running',]),
        ]
        ordering = ('name','args',)


    def call_command(self):
        kwargs = {'is_running':False}
        type(self).objects.filter(pk=self.pk).update(is_running=True)
        try:
            argv = self.args.split(self.separator or ' ') if self.args else []
            f = StringIO()
            started_at=datetime.now()
            call_command(self.name,*argv, stdout=f)
            completed_at=datetime.now()
            out = f.getvalue()
            if self.is_logged:
                Log(name=self.name,argv = self.args,started_at=started_at,completed_at=completed_at,out=out).save()
            kwargs.update(started_at=started_at,completed_at=completed_at)
        except Exception as e:
            logging.error(e, exc_info=True)
            raise e
        type(self).objects.filter(pk=self.pk).update(**kwargs)


    def __str__(self):
        return ' '.join(filter(None,[self.name,self.args]))
