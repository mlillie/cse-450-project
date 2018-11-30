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

from data import Data
from algorithm import Algorithm
import timeit
from functools import partial
import random
import datetime
from matplotlib import pyplot


class Analysis:
    # run count
    run_count = 0

    # build graph
    x_points1 = []
    y_points1 = []
    x_points2 = []
    y_points2 = []

    # constructor
    def __init__(self):
        print('Analyzing Algorithm..')

    # used to analyze the algorithm given the initial test case files as a whole
    def analyze_all(self, file_array):
        # save the preference list read from the excel file
        y_points = []
        time_points = []

        # iterate over all the files
        for file in file_array:
            data = Data().read(file)
            start_time = datetime.datetime.now()  # get the start time
            algorithm = Algorithm()
            algorithm.doctor_matching_algorithm(data, Data().calc_percentages(data))
            end_time = datetime.datetime.now()  # get the end time
            total_time = end_time - start_time
            time_points.append(total_time.microseconds)
            y_points.append(algorithm.get_swap_count())

            pyplot.plot(total_time.microseconds, algorithm.get_swap_count(), 'o', label=file)
            pyplot.legend(loc='upper left')

            print("Total time: " + str(total_time) + '\n')
            print("Total swap count: " + str(algorithm.get_swap_count()) + '\n')

            # Algorithm().patient_matching_algorithm(data, Data().calc_percentages(data))
            # then the returned preference lists from Data will be given to Algorithms

            # debugging
            # print("Total swap count: " + str(algorithm.get_swap_count()) + '\n')

        # show plot
        pyplot.title('Time Complexity Analysis')
        pyplot.xlabel('Time to execute (microseconds)')
        pyplot.ylabel('# of swaps')
        pyplot.plot(time_points, y_points, 'k', alpha=0.2)
        pyplot.show()

    # used to analyze the algorithm given the initial test case files as a whole
    def analyze_individual(self, file_array):
        # save the preference list read from the excel file
        y_points = []
        time_points = []

        # iterate over all the files
        for file in file_array:
            data = Data().read(file)
            start_time = datetime.datetime.now()  # get the start time
            algorithm = Algorithm()
            algorithm.doctor_matching_algorithm(data, Data().calc_percentages(data))
            end_time = datetime.datetime.now()  # get the end time
            total_time = end_time - start_time
            time_points.append(total_time.microseconds)
            y_points.append(algorithm.get_swap_count())

            pyplot.plot(total_time.microseconds, algorithm.get_swap_count(), 'o', label=file)
            pyplot.legend(loc='upper left')

            print("Total time: " + str(total_time) + '\n')
            print("Total swap count: " + str(algorithm.get_swap_count()) + '\n')

            # show plot
            # pyplot.yticks(y_points)
            pyplot.title('Time Complexity Analysis')
            pyplot.xlabel('Time to execute (microseconds)')
            pyplot.ylabel('# of swaps')
            pyplot.plot(time_points, y_points, 'k', alpha=0.2)
            pyplot.show()

    # used to plot the number of swaps
    def plot_efficiency(self, __name__, algorithm, proposals):
        self.run_count += 1;
        print(str(self.run_count))

        pyplot.title('Performance Analysis')
        pyplot.xlabel('Instance Run Count')

        self.x_points1.append(self.run_count)
        self.y_points1.append(proposals)
        pyplot.plot(self.x_points1, self.y_points1, 'o', label='Proposals')

        self.x_points2.append(self.run_count)
        self.y_points2.append(algorithm.get_swap_count())
        pyplot.plot(self.x_points2, self.y_points2, 'o', label='Swaps')

        pyplot.legend(loc='upper left')
        pyplot.xticks(self.x_points1)
        pyplot.show()

        return

    def show_plot(self):
        self.performance_plot.show()

    # for reference
    def fconst(self, n):
        # O(1) function
        x = n

    # for reference
    def flinear(self, n):
        # O(n) function
        x = [i for i in range(n)]

    # for reference
    def fsquare(self, n):
        # O(n^2) function
        for i in range(n):
            for j in range(n):
                x = i*j

    # for reference
    def fshuffle(self, n):
        # O(N)
        random.shuffle(list(range(n)))

    # for reference
    def fsort(self, n):
        x = list(range(n))
        random.shuffle(x)
        x.sort()

    # for reference
    def plottest(self, fn, nMin, nMax, nInc, nTests):
        # Run timer and plot time complexity
        x = []
        y = []
        for i in range(nMin, nMax, nInc):
            N = i
            testNTimer = timeit.Timer(partial(fn, N))
            t = testNTimer.timeit(number=nTests)
            x.append(i)
            y.append(t)
        pyplot.legend(loc='upper left')
