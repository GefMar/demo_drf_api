from app.celery import app


@app.task
def example_one_task(number):
    import time

    for _ in range(3):
        time.sleep(1)
    return number ** 2


@app.task
def example_two_task(number):
    import time

    for _ in range(3):
        time.sleep(1)
    return number ** 3
