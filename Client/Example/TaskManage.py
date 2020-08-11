import Task
import User
import GlobleData

class TaskManage:
    def __init__():
         self.taskLock = threading.Lock()
         self.task = Queue();

    def PutTask(task):
        with taskLock:
            self.task.put(task)
    def GetTask():
        with taskLock:
            return self.task.get()
    def PrintTaskQueue():
        for i in range(len(task)):
            print(task[i].GetInfo());

    def Run():
        for i in range(len(task)):
            curTask = GetTask();
            print(curTask.GetInfo());


