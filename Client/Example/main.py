
import win32com.client
import GlobleData
from TaskManage import TaskManage
from CommonFunction import Print 
from Tasks.TuijingyanTask import TuijingyanTask

dm = win32com.client.Dispatch('dm.dmsoft')  

if __name__ == "__main__":
    Print.info('错误码,1代表成功，其他代表失败：' + str(dm.Reg(GlobleData.dmreg, '')))
    Print.info('版本号' + str(dm.ver()))
    Print.info(dm.ver());


    task = TuijingyanTask();
    taskman = TaskManage();
    taskman.PutTask(task);
    taskman.Run();