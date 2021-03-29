import time
import logging
import random

from django.utils import timezone

from logs.models import Log

logger = logging.getLogger('my_logs')


def write_log(method: str, ms: int):
    date_now = timezone.now()
    date_timestamp = int(
        time.mktime(
            date_now.timetuple(),
        )
    )
    logger.info(f'{method},{ms},{date_timestamp}')
    print("SELAMMM")
    Log.objects.create(
        method=method,
        ms=ms,
        timestamp=date_timestamp,
    )


def generate_random() -> int:
    return random.randint(0, 3)


def wait_random() -> int:
    generated_random = generate_random()
    time.sleep(generated_random)
    return generated_random * 1000
