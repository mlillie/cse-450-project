# analysis.py
# -----------------------------------------------------------------------------------------------
# This class file will be used to analysis the algorithm that we have implemented for
# the advanced stable matching. It will have some of the following attributes:
#
#   1. Plot the time complexity of the algorithm given a certain number of preferences.
#   2. Plot the space allocated of the algorithm given a certain number of preferences.
#   3. Derive the overall efficiency of the algorithm from the data generated.

# Created By: Paul Witulski
# Last Edit: 11/08/2018

# TODO: Until we get enough data collected to plot and analysis the results of the algorithm.
# TODO: Will try to get the functionality ready using sample data and update as progess happens.

from matplotlib import pyplot
import numpy as np
import timeit
from functools import partial
import random


class Analysis:
    # def __init__(self):
        # print('Analyzing Algorithms...')

        # self.plotTC(fconst, 10, 1000, 10, 10)
        # self.plotTC(flinear, 10, 1000, 10, 10)
        # self.plotTC(fsquare, 10, 1000, 10, 10)
        # plotTC(fshuffle, 10, 1000, 1000, 10)
        # self.plotTC(fsort, 10, 1000, 10, 10)

        # enable this in case you want to set y axis limits
        # pyplot.ylim((-0.1, 0.5))

        # show plot
        # pyplot.show()

    def fconst(N):
        # O(1) function
        x = 1

    def flinear(N):
        # O(n) function
        x = [i for i in range(N)]

    def fsquare(N):
        # O(n^2) function
        for i in range(N):
            for j in range(N):
                x = i*j

    def fshuffle(N):
        # O(N)
        random.shuffle(list(range(N)))

    def fsort(N):
        x = list(range(N))
        random.shuffle(x)
        x.sort()

    def plotTC(fn, nMin, nMax, nInc, nTests):
        # Run timer and plot time complexity
        x = []
        y = []
        for i in range(nMin, nMax, nInc):
            N = i
            testNTimer = timeit.Timer(partial(fn, N))
            t = testNTimer.timeit(number=nTests)
            x.append(i)
            y.append(t)
        p1 = pyplot.plot(x, y, 'o')
        # pyplot.legend([p1,], [fn.__name__, ])
