from functools import cache

@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def main():
    import cProfile
    import pstats

    with cProfile.Profile() as pr:
        for i in range(35):
            print(i, fib(i))
        print('done')

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

if __name__ == '__main__':
    main()