from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(500):
            print("hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(500):
            print("hi")
            sleep(1)

f1=Hello()
f2=Hi()
f1.start()
#print("bye")
sleep(.2)
f2.start()
#print("bye2")
f1.join()
f2.join()
print(Bye)

