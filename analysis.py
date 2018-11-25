# analysis.py
# -----------------------------------------------------------------------------------------------
# This class file will be used to analysis the algorithm that we have implemented for
# the advanced stable matching. It will have some of the following attributes:
#
#   1. Plot the time complexity of the algorithm given a certain number of preferences.
#   2. Plot the space allocated of the algorithm given a certain number of preferences.
#   3. Derive the overall efficiency of the algorithm from the data generated.

# Created By: Paul Witulski
# Last Edit: 11/25/2018

# TODO: Until we get enough data collected to plot and analysis the results of the algorithm.
# TODO: Will try to get the functionality ready using sample data and update as progress happens.

from matplotlib import pyplot
import numpy as np
import timeit
from functools import partial
import random


class Analysis:

    def plot_efficiency(self):
        # used to plot the number of swaps
        return

    def plot_time_complexity(self):
        # used to plot the time it takes to complete the algorithm
        return

    def plot_space_complexity(self):
        # used to plot amount of memory used to complete the algorithm
        return

    # def __init__(self):
        # print('Analyzing Algorithms...')

        # self.plotTC(fconst, 10, 1000, 10, 10)
        # self.plotTC(flinear, 10, 1000, 10, 10)
        # self.plotTC(fsquare, 10, 1000, 10, 10)
        # plotTC(fshuffle, 10, 1000, 1000, 10)
        # self.plotTC(fsort, 10, 1000, 10, 10)

        # show plot
        # pyplot.show()

    def fconst(self, N):
        # O(1) function
        x = 1

    def flinear(self, N):
        # O(n) function
        x = [i for i in range(N)]

    def fsquare(self, N):
        # O(n^2) function
        for i in range(N):
            for j in range(N):
                x = i*j

    def fshuffle(self, N):
        # O(N)
        random.shuffle(list(range(N)))

    def fsort(self, N):
        x = list(range(N))
        random.shuffle(x)
        x.sort()

    def plotTC(self, fn, nMin, nMax, nInc, nTests):
        # Run timer and plot time complexity
        x = []
        y = []
        for i in range(nMin, nMax, nInc):
            N = i
            testNTimer = timeit.Timer(partial(fn, N))
            t = testNTimer.timeit(number=nTests)
            x.append(i)
            y.append(t)
        p1 = pyplot.plot(x, y, 'o', label = fn.__name__)
        pyplot.legend(loc = 'upper left')
        #pyplot.legend([p1,], [fn.__name__, ])

