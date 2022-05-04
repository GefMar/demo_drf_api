import datetime
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

app = Celery("example_project", broker=settings.CELERY_BROKER, backend=settings.CELERY_BACKEND)

app.conf.task_queue_max_priority = 4

app.conf.task_default_priority = 1
app.conf.worker_prefetch_multiplier = 1
app.conf.task_acks_late = 1
app.conf.result_expires = datetime.timedelta(hours=2)
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
