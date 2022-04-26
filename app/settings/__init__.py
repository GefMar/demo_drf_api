from .base import *
from .celery import *
from .database import *
from .drf import *
from .lang import *

DEBUG = bool(int(os.getenv("DEBUG", 0)))

if DEBUG:
    from .dev import *
else:
    from .prod import *
