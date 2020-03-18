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

    def __iter__(self):
        self._counter = 0
        return self

    def __next__(self):
        try:
            current_task = self.tasks[self._counter]
            self._counter += 1
            if current_task.finished:
                return next(self)

            return current_task
        except IndexError:
            raise StopIteration

    def __str__(self):
        result = ""
        for task in self:
            result += str(task)
            result += "\n"

        return result

    @classmethod
    def fromJSON(cls, obj):
        planner = cls()
        for tsk in obj:
            planner.addTask(createTask(tsk))
        return planner
