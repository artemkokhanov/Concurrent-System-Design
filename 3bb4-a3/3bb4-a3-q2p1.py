from threading import Thread, Semaphore
from time import sleep
from sys import stdout
from random import randint

N = 8

s = Semaphore(3)
TLines = ['A', 'B', 'C']

def request():
    s.acquire(); return TLines.pop()

def done(i):
    TLines.append(i); s.release()
    
class Communicating(Thread):
    def __init__(self, i):
        self.i = i; super().__init__()
    def run(self):
        while True:
            sleep(randint(0, 6))
            line = request();
            stdout.write(str(self.i) + ' communicating on ' + str(line) + '\n');
            sleep(randint(0, 3))
            stdout.write(str(self.i) + ' done\n');
            done(line)

for i in range(N): Communicating(i).start()
