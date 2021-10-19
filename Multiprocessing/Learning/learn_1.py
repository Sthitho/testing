from time import sleep
from multiprocessing import Pool


def f(x):
    sleep(2)
    return x


if __name__ == '__main__':
    pool = Pool(processes=3)
    input_values = [x for x in range(5)]
    # results = [print(f(x)) for x in input_values] # non-threaded
    results = pool.map(f, input_values)
    print(results)


