from threading import Thread, Semaphore
from sys import stdout
from random import sample

s1 = Semaphore(0)
s2 = Semaphore(0)
s3 = Semaphore(0)

def doing(s):
    global tr; e.acquire(); tr = tr + s; e.release()

class P1(Thread):
    def run(self):
        doing('P1')
        s1.release()
        s1.release()

class P2(Thread):
    def run(self):
        s1.acquire()
        doing('P2')
        s2.release()

class P3(Thread):
    def run(self):
        s1.acquire()
        doing('P3')
        s3.release()

class P4(Thread):
    def run(self):
        s2.acquire()
        doing('P4')
        s3.release()

class P5(Thread):
    def run(self):
        s3.acquire()
        s3.acquire()
        doing('P5')

for _ in range(20):
    tr, e = '', Semaphore(1) # trace and lock for trace
    PS = [P1(), P2(), P3(), P4(), P5()]
    for p in sample(PS, k=5): p.start()
    for p in PS: p.join()
    assert tr in ('P1P2P3P4P5', 'P1P2P4P3P5', 'P1P3P2P4P5')
