# main.py
# -----------------------------------------------------------------------------------------------
# This is where the main program will be executed.
#
# Team 5
# Members: Matthew Lillie, Jacqueline Fonseca, Paul Witulski
# Last edit: 11/08/18

# TODO: Need to refactor to pass all files in test_cases folder to Data class
# TODO: Then the result from the Data class will be returned and given to the Algorithm class


from data import Data
from algorithm import Algorithm
from analysis import Analysis

if __name__ == '__main__':
    # will add an iterator which will pass all files in test_cases folder to Data
    # file = "3_pref_lists"
    # file = "5_pref_lists"
    # file = "10_pref_lists"
    file = "\\test_cases\Sample2.xlsx"

    # save the preference list read from the excel file
    pref_lists = Data().read(file)

    # then the returned preference lists from Data will be given to Algorithms
    Algorithm().matching_algorithm(pref_lists)

    # Analysis will need to monitor the algorithm
    # TODO: The Analysis class will be used to log the results from Algorithm
    Analysis()
