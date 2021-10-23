from multiprocessing import Process, Lock


def f(lim, i):
    lim.acquire()
    try:
        print('hello world', i)
    finally:
        lim.release()


if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()
