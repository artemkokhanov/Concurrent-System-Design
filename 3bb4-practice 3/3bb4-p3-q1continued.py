from threading import Thread, Semaphore
from time import sleep
from sys import stdout

barrier1 = Semaphore(0)
barrier2 = Semaphore(0)
barrier3 = Semaphore(0)

class Ping(Thread):
    def run(self):
        while True:
            stdout.write('ping\n'); sleep(2)    # task
            barrier1.release()                  # signal
            barrier3.release()                  # signal
            barrier2.acquire()                  # wait
            barrier2.acquire()                  # wait

class Pong(Thread):
    def run(self):
        while True:
            stdout.write('pong\n'); sleep(2)    # task
            barrier2.release()                  # signal
            barrier3.release()                  # signal
            barrier1.acquire()                  # wait
            barrier1.acquire()                  # wait

class Kapow(Thread):
    def run(self):
        while True:
            stdout.write('kapow\n'); sleep(2)   # task
            barrier1.release()                  # singal
            barrier2.release()                  # signal
            barrier3.acquire()                  # wait
            barrier3.acquire()                  # wait

Ping().start(); Pong().start(); Kapow().start() # create and run threads