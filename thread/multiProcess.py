from multiprocessing import Process
import os
def run_proc(name):
    print("%s is running(%s)" % (name, os.getpid()))
if __name__ == "__main__":
    print("Parent process %s" % os.getpid())
    p = Process(target=run_proc, args=("test",))
    print("Child process will start")
    p.start()
    print("child process end")
    # join可以登当前子进程结束后继续往下进行，类似同步
    p.join()