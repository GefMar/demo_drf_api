from celery import chain
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .celery import example_one_task, example_two_task
from .models import Notification


@receiver(post_save, sender=Notification)
def notifications_send_celery(sender, instance, created, *args, **kwargs):
    result = chain(example_one_task.s(2), example_two_task.s())()
    print(result.get())
