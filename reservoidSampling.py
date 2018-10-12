# -*- coding=utf-8 -*-
from random import random
from time import time


class ReservoidSmapling():
    """蓄水池算法：用于等概率的从一个集合中选取给定数目的个体。
    """

    def __init__(self, size):
        """
        Args:
            size (int): 蓄水池大小
            pool (list): 蓄水池
            curIndex(int): 当前进入元素编号
        """

        self._size = size
        self._pool = []
        self._curIndex = -1

    def reservoidSampling(self, item):
        """item为当前要加入的元素

        Args:
            item (int): 暂定为int，可以为任意类型
        """

        self._curIndex += 1
        if self._curIndex < self._size:
            self._pool.append(item)
        else:
            if self.rand(self._curIndex+1) < self._size:
                self._pool[self.rand(self._size)] = item

    def getPool(self):
        return self._pool

    def getTotalItems(self):
        return self._curIndex

    def rand(self, i):
        """等概率的选中i个位置中的一个
        """

        return int(random() * i)


def main():
    # 每一个item留下的概率p = size/totalNum, 出现的次数应为 p * repeatTimes
    size, totalNum, repeatTimes = 10, 20, 5000000
    counter = [0 for i in range(totalNum)]
    start = time()
    for j in range(repeatTimes):
        pool = ReservoidSmapling(size)
        for i in range(totalNum):
            pool.reservoidSampling(i)
        samplePool = pool.getPool()
        for item in samplePool:
            counter[item] += 1
    print('time used: ', time()-start)
    print(min(counter), max(counter))
    for item in counter:
        print(item, end=' ')


if __name__ == "__main__":
    main()
