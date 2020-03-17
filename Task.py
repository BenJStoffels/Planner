class Task:
    def __init__(self, vak, titel, beschrijving, tegen, finished=False):
        self.vak = vak
        self.titel = titel
        self.beschrijving = beschrijving
        self.tegen = tegen
        self.finished = finished

    def finish(self):
        self.finished = True

    def __str__(self):
        if not self.finished:
            return f"{self.vak}: {self.titel},\n{self.beschrijving}\ntegen {self.tegen}"
        else:
            return "you're all good"

    def __gt__(self, other):
        if not isinstance(other, Task):
            raise TypeError("can't compare a task with something else")

        return self.tegen > other.tegen

    def __ge__(self, other):
        if not isinstance(other, Task):
            raise TypeError("can't compare a task with something else")

        return self.tegen >= other.tegen

    def __lt__(self, other):
        return not self >= other

    def __le__(self, other):
        return not self > other
