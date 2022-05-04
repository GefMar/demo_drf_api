import random

import factory
from factory import fuzzy

from .. import models


class NotificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Notification

    notification_text = fuzzy.FuzzyText(length=random.randint(100, 500))
    operation_system = fuzzy.FuzzyChoice(models.OperationSystemChoice.values)
