from time import sleep
from threading import *
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hii(Thread):
    def run(self):
        for i in range(5):
            print("Hii")
            sleep(1)
            
t1=Hello()
t2=Hii()
#simultaneous execution of hello and hii on different core Here we have used 
# start insetad of run because by default Thread package has run class if we have some other method name it won't execute
t1.start()
sleep(0.2) # to avoid collision like HiiHello
t2.start()

t1.join()
t2.join()

print("bye")
    
            