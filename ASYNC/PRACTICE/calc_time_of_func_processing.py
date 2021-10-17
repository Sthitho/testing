def func1():
    for i in range(1, 9):
        print(i**2, i**3)

def main():
    import cProfile
    import pstats

    with cProfile.Profile() as pr:
        func1()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats() # prints stats
    stats.dump_stats(filename='STATS.prof') # dumps stats -> STATS.prof -> [terminal] snakeviz STATS.prof -> Vis.Rep

if __name__ == '__main__':
    main()