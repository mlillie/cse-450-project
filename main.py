# main.py
# -----------------------------------------------------------------------------------------------
# This is the entry point for the program.
# It will set up the classes and run the algorithm.
# Top-Level View:
#   1. Read the data from the excel files and build the lists (Data class)
#   2. Use the data and feed it into the algorithm class (Algorithm class)
#   3. Perform the analysis of the algorithm, account for efficiency, time, space (Analysis class)

# Team Members: Matthew Lillie, Jacky Fonseca, Paul Witulski
# Last edit: 11/25/18

from algorithm import Algorithm
from data import Data
from analysis import Analysis
from matplotlib import pyplot
import datetime
from matplotlib.dates import date2num

if __name__ == '__main__':

    file_array = []
    # will add an iterator which will pass all files in test_cases folder to Data
    file_3 = "\\test_cases\\3_pref_lists.xlsx"
    file_5 = "\\test_cases\\5_pref_lists.xlsx"
    file_10 = "\\test_cases\\10_pref_lists.xlsx"
    file_50 = "\\test_cases\\50_pref_lists.xlsx"
    file_100 = "\\test_cases\\100_pref_lists.xlsx"

    file_array.append(file_3)
    file_array.append(file_5)
    file_array.append(file_10)
    file_array.append(file_50)
    file_array.append(file_100)

    # save the preference list read from the excel file
    y_points = []
    time_points = []

    for file in file_array:
        data = Data().read(file)
        start_time = datetime.datetime.now() # get the start time
        algorithm = Algorithm()
        algorithm.doctor_matching_algorithm(data, Data().calc_percentages(data))
        end_time = datetime.datetime.now() # get the end time
        total_time = end_time - start_time
        time_points.append(total_time.microseconds)
        y_points.append(algorithm.get_swap_count())

        pyplot.plot(total_time.microseconds, algorithm.get_swap_count(), 'o', label = file)
        pyplot.legend(loc='upper left')

        print("Total time: " + str(total_time) + '\n')
        print("Total swap count: " + str(algorithm.get_swap_count()) + '\n')

    # Algorithm().patient_matching_algorithm(data, Data().calc_percentages(data))
    # then the returned preference lists from Data will be given to Algorithms
    # Analysis will need to monitor the algorithm
    # TODO: The Analysis class will be used to log the results from Algorithm
    analysis = Analysis()

    print('Analyzing Algorithms...')

    #print("Total swap count: " + str(algorithm.get_swap_count()) + '\n')

    #analysis.plotTC(analysis.fconst, 10, 1000, 10, 10)
    #analysis.plotTC(analysis.flinear, 10, 1000, 10, 10)
    #analysis.plotTC(analysis.fsquare, 10, 1000, 10, 10)
    #analysis.plotTC(analysis.fshuffle, 10, 1000, 1000, 10)
    #analysis.plotTC(analysis.fsort, 10, 1000, 10, 10)

    # show plot
    pyplot.title('Time Complexity Analysis')
    pyplot.xlabel('Time to execute (microseconds)')
    pyplot.ylabel('# of swaps')
    #dates = date2num(time_points)
    pyplot.plot(time_points, y_points, 'k', alpha=0.2)
    #pyplot.gcf().autofmt_xdate()
    pyplot.show()
