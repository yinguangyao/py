from multiprocessing import Process
import os
def run_proc(name):
    print("%s is running(%s)" % (name, os.getpid()))
# 自己实现Process的时候必须实现run方法，因为start的时候调用的run，在run里面调用targat
class DiyProcess(Process):
    def __init__(self, target, args):
        super().__init__()
        self.target = target
        self.args = args
    def run(self):
        print("it's diy process")
        self.target(self.args)
if __name__ == "__main__":
    print("Parent process %s" % os.getpid())
    p = DiyProcess(target=run_proc, args=("test",))
    print("Child process will start")
    p.start()
    # join可以登当前子进程结束后继续往下进行，类似同步
    p.join()
    print("child process end")
n=100 #在windows系统中应该把全局变量定义在if __name__ == '__main__'之上就可以了
def work():
    global n
    n=0
    print('子进程内: ',n)


if __name__ == '__main__':
    p=Process(target=work)
    p.start()
    print('主进程内: ',n)