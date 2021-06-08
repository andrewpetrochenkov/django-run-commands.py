from setuptools import setup

setup(
    name='django-run-commands',
    version='2021.6.8',
    packages=[
        'django_run_commands',
        'django_run_commands.admin',
        'django_run_commands.management',
        'django_run_commands.management.commands',
        'django_run_commands.migrations',
        'django_run_commands.models'
    ]
)
