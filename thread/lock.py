# 举个例子，如果有多个进程一起在终端打印，那么就会导致打印混乱，这个时候可以加上进程锁
# 从打印的结果来看，进程锁不会保证执行顺序，但是会保证running和done一起执行，也就是会保证acquire和release中间的代码完整运行
from multiprocessing import Process,Lock
import os,time
def work(lock, i):
    # lock.acquire()
    print('%s is running' % i)
    time.sleep(2)
    print('%s is done' % i)
    # lock.release()
if __name__ == '__main__':
    lock=Lock()
    for i in range(3):
        p=Process(target=work,args=(lock,i))
        p.start()