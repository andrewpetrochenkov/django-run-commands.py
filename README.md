[![](https://img.shields.io/pypi/v/django-run-commands.svg?maxAge=3600)](https://pypi.org/project/django-run-commands/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-run-commands.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-run-commands.py/actions)
### Installation
```bash
$ pip install django-run-commands
```

#### `settings.py`
```python
INSTALLED_APPS+=['django_run_commands']
```

#### `migrate`
```bash
$ python manage.py migrate
```

### Pros
+   sequential execution of commands without additional memory consumption and conflicts
+   easy admin panel/SQL management
+   logs

### How it works
1. add commands and set `seconds` interval
2. run `python -u manage.py run_commands`

### Examples
postgres INSERT
```sql
INSERT INTO run_commands_command(name,args,seconds)
VALUES
('command_name1','arg1 arg2',42),
('command_name2',NULL,42);
```

