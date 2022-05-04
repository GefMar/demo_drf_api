import random

from celery import chord
from django.db.models.signals import post_save
from django.dispatch import receiver

from .celery import finally_task, sum_task
from .models import Post


@receiver(post_save, sender=Post)
def notifications_send_celery(sender, instance, created, *args, **kwargs):
    tasks = [sum_task.s(*range(random.randint(10, 30), random.randint(35, 100))) for _ in range(random.randint(3, 10))]
    chord(tasks)(finally_task.s())
    print("notifications_send_celery")
