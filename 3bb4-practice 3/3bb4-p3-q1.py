from threading import Thread, Semaphore
from time import sleep
from sys import stdout

barrier1, barrier2 = Semaphore(0), Semaphore(0) # create semaphores

class Ping(Thread):
    def run(self):
        while True:
            stdout.write('ping\n'); sleep(2)    # task
            barrier1.release()                  # signal
            barrier2.acquire()                  # wait

class Pong(Thread):
    def run(self):
        while True:
            stdout.write('pong\n'); sleep(2)    # task
            barrier2.release()                  # signal
            barrier1.acquire()                  # wait

Ping().start(); Pong().start()                  # create and run threads