# -*- coding=utf-8 -*-
from random import random
from time import time


class ReservoidSampling():
    """对应于reservoidSampling.py，此处蓄水池算法直接给定大小和物品数目"""

    def reservoidSampling(self, size, totalNum):
        size = min(size, totalNum)
        if size < 1:
            return None
        pool = []
        for i in range(size):
            pool.append(i)

        for i in range(size, totalNum):
            if self.rand(i+1) < size:
                pool[self.rand(size)] = i

        return pool

    def rand(self, i):
        return int(random()*i)


def main():
    size, totalNum, repeatTimes = 10, 20, 5000000
    counter = [0 for i in range(totalNum)]
    start = time()
    ex = ReservoidSampling()
    for i in range(repeatTimes):
        pool = ex.reservoidSampling(size, totalNum)
        for item in pool:
            counter[item] += 1
    print('time used: ', time()-start)
    print(min(counter), max(counter))
    for item in counter:
        print(item, end=' ')


if __name__ == "__main__":
    main()
