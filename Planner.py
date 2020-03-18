from createTask import createTask


class Planner:
    def __init__(self):
        self.tasks = []

    def addTask(self, task):
        index = 0
        for i, t in enumerate(self.tasks):
            index = i
            if task < t:
                break
        else:
            self.tasks.append(task)
            return None

        self.tasks.insert(index, task)

    def getNextTasks(self, fromTime, deltaTime):
        return list(filter(lambda task: task.tegen >= fromTime and task.tegen < fromTime + deltaTime, self.tasks))

    def __str__(self):
        result = ""
        for task in self.tasks:
            result += str(task)
            result += "\n"

        return result

    @classmethod
    def fromJSON(cls, obj):
        planner = cls()
        for tsk in obj:
            planner.addTask(createTask(tsk))
        return planner
