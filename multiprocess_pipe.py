from multiprocessing import Process, Pipe

def send_msg(pipe):
    msg = {
        'name': 'biandour',
        'age': 12
    }
    pipe.send(msg)
    pipe.close()

if __name__ == "__main__":

    con1, con2 = Pipe()

    p1 = Process(target=send_msg, args=(con1,))
    p1.start()

    recved = con2.recv()
    print recved
    con2.close()
    p1.join()

