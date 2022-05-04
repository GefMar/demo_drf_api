from django.db import models

__all__ = ("OperationSystemChoice",)


class OperationSystemChoice(models.TextChoices):
    ANY = "ANY", "Any os"
    MACOS = "MACOS", "Apple MacOS"
    LINUX = (
        "LINUX",
        "Linux",
    )
    WINDOWS = "WINDOWS1", "Microsoft Windows"
