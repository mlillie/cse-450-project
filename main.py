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

if __name__ == '__main__':

    # will add an iterator which will pass all files in test_cases folder to Data
    # file = "3_pref_lists"
    # file = "5_pref_lists"
    # file = "10_pref_lists"
    file = "\\test_cases\Sample2.xlsx"
    # save the preference list read from the excel file
    data = Data().read(file)

    algorithm = Algorithm()
    algorithm.doctor_matching_algorithm(data, Data().calc_percentages(data))
    # Algorithm().patient_matching_algorithm(data, Data().calc_percentages(data))
    # then the returned preference lists from Data will be given to Algorithms
    # Analysis will need to monitor the algorithm
    # TODO: The Analysis class will be used to log the results from Algorithm
    analysis = Analysis()

    print('Analyzing Algorithms...')

    print("Total swap count: " + str(algorithm.get_swap_count()) + '\n')

    #analysis.plotTC(analysis.fconst, 10, 1000, 10, 10)
    #analysis.plotTC(analysis.flinear, 10, 1000, 10, 10)
    #analysis.plotTC(analysis.fsquare, 10, 1000, 10, 10)
    #analysis.plotTC(analysis.fshuffle, 10, 1000, 1000, 10)
    #analysis.plotTC(analysis.fsort, 10, 1000, 10, 10)

    # show plot
    pyplot.show()
