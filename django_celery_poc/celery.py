# django_celery/celery.py

import os
from celery import Celery

# Assure that Django project’s settings.py module is accessible through the "DJANGO_SETTINGS_MODULE" key.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_celery_poc.settings")

# Create celery app instance with main module "django_celery_poc" as the arg
# main module is the main django app that contains the "celery.py" file
app = Celery("django_celery_poc")

# Define django settings file as the config file celery
# Celery config variables will now be picked from django project's "settings.py" file
# Since we are using the namespace "CELERY", the celery config variables will have to be prepended with "CELERY_"
app.config_from_object("django.conf:settings", namespace="CELERY")

# Tell celery app to pick all the tasks from tasks.py file from each of the django apps
app.autodiscover_tasks()
