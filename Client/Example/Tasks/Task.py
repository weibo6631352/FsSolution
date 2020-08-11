from User import User
from CommonFunction import Print 
class Task:
    def __init__(self):
        self.name = 'none';
        self.count = 1;
        self.user = User();
    def GetInfo(self):
        return ('任务' + ':' + self.name + ',' + str(self.count) + '次, 用户' ) + self.user.user +  ', 角色' + self.user.juese +  ', ' + str(self.user.area) + '区';

    def Run(self):
        Print.info('任务' + GetInfo());



