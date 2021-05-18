__all__ = ['Log']

from django.db import models

class Log(models.Model):
    name = models.CharField(max_length=255)
    args = models.CharField(max_length=255,null=True,blank=True)
    separator= models.TextField(null=True)

    out = models.TextField()
    started_at = models.DateTimeField()
    completed_at = models.DateTimeField()

    class Meta:
        db_table = 'run_commands_log'
        indexes = [
           models.Index(fields=['name',]),
           models.Index(fields=['-started_at',]),
           models.Index(fields=['-completed_at',]),
        ]
        ordering = ('-completed_at',)
