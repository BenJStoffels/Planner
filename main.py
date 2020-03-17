import json
import datetime
import win10toast
from Planner import Planner

with open("tasks.json", "r") as jsonFile:
    tasks = json.load(jsonFile)

planner = Planner.fromJSON(tasks)

nextTasks = planner.getNextTasks(
    datetime.datetime.now(), datetime.timedelta(hours=1.0))

toaster = win10toast.ToastNotifier()

for tsk in nextTasks:
    toaster.show_toast(f"{tsk.vak}: {tsk.titel}",
                       f"{tsk.beschrijving},\ntegen {tsk.tegen}", duration=5)
