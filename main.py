import datetime
import win10toast
from loadPlanner import loadPlanner


def main():
    planner = loadPlanner()
    nextTasks = planner.getNextTasks(
        datetime.datetime.now(), datetime.timedelta(hours=1.0))

    toaster = win10toast.ToastNotifier()

    for tsk in nextTasks:
        toaster.show_toast(f"{tsk.vak}: {tsk.titel}",
                           f"{tsk.beschrijving},\ntegen {tsk.tegen}", duration=5)


if __name__ == "__main__":
    main()
