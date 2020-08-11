import User
from CommonFunction import Print 
from Tasks.Task import Task

class TuijingyanTask(Task):
    def __init__(self):
        Task.__init__(self)
        

    def Run(self):
        Print.info('退经验任务' + self.GetInfo());



