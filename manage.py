#!/usr/bin/env python
import os
import sys

PROJECT_NAME = '{{project_name}}'
os.environ.setdefault('DJANGO_ENV', 'dev')
DJANGO_ENV = os.environ.get('DJANGO_ENV')

settings_module = '%s.conf.%s_settings' % (PROJECT_NAME, DJANGO_ENV)

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
