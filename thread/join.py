from multiprocessing import Process
import time
import random
def piao(name):
    print('%s is piaoing' %name)
    time.sleep(random.randint(1,3))
    print('%s is piao end' %name)
if __name__ == "__main__":
    p1=Process(target=piao,args=('1',))
    p2=Process(target=piao,args=('2',))
    p3=Process(target=piao,args=('3',))
    p4=Process(target=piao,args=('4',))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    #有的同学会有疑问:既然join是等待进程结束,那么我像下面这样写,进程不就又变成串行的了吗?
    #当然不是了,必须明确：p.join()是让谁等？
    #很明显p.join()是让主线程等待p的结束，卡住的是主线程而绝非进程p，

    #详细解析如下：
    #进程只要start就会在开始运行了,所以p1-p4.start()时,系统中已经有四个并发的进程了
    #而我们p1.join()是在等p1结束,没错p1只要不结束主线程就会一直卡在原地,这也是问题的关键
    #join是让主线程等,而p1-p4仍然是并发执行的,p1.join的时候,其余p2,p3,p4仍然在运行,等#p1.join结束,可能p2,p3,p4早已经结束了,这样p2.join,p3.join.p4.join直接通过检测，无需等待
    # 所以4个join花费的总时间仍然是耗费时间最长的那个进程运行的时间
    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print('主线程')


    #上述启动进程与join进程可以简写为
    # p_l=[p1,p2,p3,p4]
    # 
    # for p in p_l:
    #     p.start()
    # 
    # for p in p_l:
    #     p.join()