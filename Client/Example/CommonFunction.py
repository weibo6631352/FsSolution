
import os
import time
import threading
import sys

class Print(object):
    logLock = threading.Lock()
    logPath = ''
    @staticmethod
    def info(message):
        out_message =  Print.timeStamp() + '  ' + 'INFO: ' +str(message)
        Print.write(out_message)
        print(out_message)

    @staticmethod
    def GetLogPath():
        if Print.logPath is None or Print.logPath == '':
            logDir = os.path.split(os.path.abspath(sys.argv[0]))[0]
            Print.logPath = os.path.join(logDir,'log.txt')
            print('日志存放位置：' + Print.logPath)
        return Print.logPath

    @staticmethod
    def write(message):
        logPath = Print.GetLogPath()
        with Print.logLock:
            with open(logPath,'a+') as f:
                f.write(message)
                f.write('\n')

    @staticmethod
    def timeStamp():
        local_time = time.localtime(time.time())
        return time.strftime("%Y_%m_%d-%H_%M_%S", local_time)