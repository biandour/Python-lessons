from threading import Thread, Event
import time

class MyThread(Thread):
    def __init__(self, flag):
        Thread.__init__(self)
        self.flag = flag

    def run(self):
        print "I'm %s I'm going to sleep..." % self.name
        self.flag.wait()
        print "I'm %s I'm awake" % self.name


if __name__ == "__main__":

    flag = Event()

    for i in range(3):
        thd = MyThread(flag)
        thd.start()

    time.sleep(3)

    flag.set()
