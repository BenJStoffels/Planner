from Task import Task
from datetime import datetime


def createTask(obj):
    year = obj["tegen"]["year"]
    month = obj["tegen"]["month"]
    day = obj["tegen"]["day"]
    hour = obj["tegen"]["hour"]
    minute = obj["tegen"]["minute"]
    tegen = datetime(year, month, day, hour, minute)

    finished = obj.get("finished", False)

    return Task(obj["vak"], obj["titel"], obj["beschrijving"], tegen, finished=finished)
