import os

from celery import Celery

# Set default Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("shorter")

# Load settings from Django config
app.config_from_object("django.conf:settings", namespace="CELERY")

# Discover tasks in registered Django apps
app.autodiscover_tasks()
