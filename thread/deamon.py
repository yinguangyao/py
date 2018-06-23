from multiprocessing import Process
import time
import random
# 用deamon开启守护进程，守护进程内无法再开启子进程，否则会抛出异常
# 一定要在p.start前设置p为守护进程，这样可以禁止p创建子进程
class DiyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        print("this name is %s" % self.name)
if __name__ == "__main__":
    p = DiyProcess("test")
    p.deamon = True
    p.start()
    print("main process")