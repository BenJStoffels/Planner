from Planner import Planner
import json


def loadPlanner():
    with open("tasks.json", "r") as jsonFile:
        tasks = json.load(jsonFile)

    return Planner.fromJSON(tasks)
