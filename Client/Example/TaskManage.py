import Tasks.Task
import User
import GlobleData
import threading
import queue
import time

class TaskManage:
    def __init__(self):
         self.taskLock = threading.Lock()
         self.task = queue.Queue();

    def PutTask(self, task):
        with self.taskLock:
            self.task.put(task)
    def GetTask(self):
        with self.taskLock:
            return self.task.get()
    def PrintTaskQueue(self):
        for i in range(len(self.task)):
            print(self.task[i].GetInfo());

    def Run(self):
        while True:
            curTask = self.GetTask();
            print(curTask.GetInfo());
            curTask.Run();
            time.sleep(1)


