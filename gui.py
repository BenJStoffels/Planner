from loadPlanner import loadPlanner

from tkinter import Tk, Label, Frame, Entry, StringVar, OptionMenu, Button
from tkinter import TOP, X, LEFT, BOTTOM, END


class TaskGui:
    def __init__(self, planner, geometry="400x630+1072+51"):
        self.root = Tk()
        self.root.geometry(geometry)
        self.root.title("Schooltaken")
        self.root.config(bg="white")

        self.title = Label(self.root, text="Taken",
                           bg="black", fg="white")
        self.title.pack(side=TOP, fill=X)

        self.taskFrame = Frame(self.root, bg="white")

        self.taskLabels = []
        for task in planner:
            taskLabel = Label(self.taskFrame, text=str(task),
                              bg="white", fg="black")
            taskLabel.pack(side=TOP, fill=X, pady=10)
            self.taskLabels.append(taskLabel)

        self.taskFrame.pack(side=TOP, fill=X, pady=50, padx=20)

        self.addTaskButton = Button(
            self.root, text="Maak nieuwe taak", command=self.addTask)
        self.addTaskButton.pack(side=TOP)

    def addTask(self):
        print("adding task")

    def main(self):
        self.root.mainloop()


if __name__ == "__main__":
    planner = loadPlanner()
    gui = TaskGui(planner)

    gui.main()
