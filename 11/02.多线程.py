# 多任务可以由多进程完成，也可以由一个进程内的多线程完成。
# 我们前面提到了进程是由若干线程组成的，一个进程至少有一个线程。
# 由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，
# Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。

# Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。
# 绝大多数情况下，我们只需要使用threading这个高级模块。

# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
import time, threading

def loop():
    print('Thread %s is running..' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread(), n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

# 由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，Python的threading模块有个current_thread()函数，
# 它永远返回当前线程的实例。主线程实例的名字叫MainThread，子线程的名字在创建时指定，
# 我们用LoopThread命名子线程。名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……

#Lock
# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，
# 所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
# 来看看多个线程同时操作一个变量怎么把内容给改乱了：

import time, threading

#假定这是你的银行存款
balance = 0
def change_it(n):
    #先存后取，结果应该为0
    global balance
    balance = balance + n
    balance = balance - n

lock = threading.Lock()
def run_thread(n):
    for i in range(1000000):
        # 先要获取锁:
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

# 我们定义了一个共享变量balance，初始值为0，并且启动两个线程，先存后取，理论上结果应该为0，
# 但是，由于线程的调度是由操作系统决定的，当t1、t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了。
# 因是因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算：

# balance = balance + n
# 也分两步：
# 计算balance + n，存入临时变量中；
# 将临时变量的值赋给balance。
# 也就是可以看成：
# x = balance + n
# balance = x

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(6,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


#究其原因，是因为修改balance需要多条语句，而执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了。

# 如果我们要确保balance计算正确，就要给change_it()上一把锁，当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，
# 因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，
# 所以，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现：

#
# 当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。
#
# 获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保锁一定会被释放。
#
# 锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当然也很多，首先是阻止了多线程并发执行，
# 包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。其次，由于可以存在多个锁，不同的线程持有不同的锁，
# 并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。



# 多核CPU
# 如果你不幸拥有一个多核CPU，你肯定在想，多核应该可以同时执行多个线程。

# 我们可以监控到一个死循环线程会100%占用一个CPU。
#
# 如果有两个死循环线程，在多核CPU中，可以监控到会占用200%的CPU，也就是占用两个CPU核心。
#
# 要想把N核CPU的核心全部跑满，就必须启动N个死循环线程。
#
# 试试用Python写个死循环：

import threading, multiprocessing
print(multiprocessing.cpu_count())  # 4

def loop():
    x = 0
    while True:
        x = x * 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()



# 启动与CPU核心数量相同的N个线程，在4核CPU上可以监控到CPU占用率仅有102%，也就是仅使用了一核。
# 但是用C、C++或Java来改写相同的死循环，直接可以把全部核心跑满，4核就跑到400%，8核就跑到800%，为什么Python不行呢？
# 因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，
# 任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
# 这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。























