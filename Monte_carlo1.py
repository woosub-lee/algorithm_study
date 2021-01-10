import random
import multiprocessing


def monte_carlo(count):
    monte = 0
    for j in range(count):
        ok = 0
        for i in range(1000000):
            x = random.random()*2
            y = random.random()*2
            if (x-1) * (x-1) + (y-1) * (y-1) <= 1:
                ok += 1
        monte += 4 * (ok/1000000)
    print(monte / count)


num_list = [1000, 1000, 1000, 1000]
if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)
    pool.map(monte_carlo, num_list)
    pool.close()
    pool.join()
