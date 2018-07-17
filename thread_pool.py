from threading import Thread
import time, Queue

class ThreadPool():
    def __init__(self, max_thread = 10):
        self.q = Queue.Queue(max_thread)

        for i in range(max_thread):
            self.q.put(Thread)

    def add_thread(self):
        return self.q.put(Thread)

    def get_thread(self):
        return self.q.get()


if __name__ == "__main__":

    pool = ThreadPool()

    def haveasleep(num, pool):
        print "I'm %d" % num
        time.sleep(2)
        pool.add_thread()
        
    for i in range(20):
        thread  = pool.get_thread()
        thd = thread(target=haveasleep, args=(i, pool))
        thd.start()

    


