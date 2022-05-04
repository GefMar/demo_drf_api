from app.celery import app


@app.task
def sum_task(*args):
    import time

    result = 0
    for itm in args:
        result += itm
        time.sleep(0.1)
    print("RESULT_TASK", result)
    return result


@app.task(ignore_result=True)
def finally_task(*args):
    print("RESULT TASK", args)
