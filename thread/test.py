# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
# 仅为测试这句话是否正确
# 从打印结果可以看出来，全局变量count在每个进程中都是互不影响的
# from multiprocessing import Process
# count = 10;
# def init(index):
#     global count
#     count -= index
#     print("index is %d" % index)
#     print("count is %d" % count)
# if __name__ == "__main__":
#     for i in range(10):
#         p = Process(target=init, args=(i,))
#         p.start()
import threading
count = 10;
lock = threading.Lock()
def init(index):
    global count
    lock.acquire()
    count -= index
    print("index is %d" % index)
    print("count is %d" % count)
    lock.release()
if __name__ == "__main__":
    for i in range(10):
        p = threading.Thread(target=init, args=(i,))
        p.start()