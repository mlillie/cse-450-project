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

from analysis import Analysis
from gui import GUI
from algorithm import Algorithm
from data import Data
import datetime
from matplotlib import pyplot


if __name__ == '__main__':
    # store the different preference list files into an array
    file_array = []

    # will add an iterator which will pass all files in test_cases folder to Data in Analysis class
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

    # initial analysis
    # pass the files to the Analysis class and run algorithm
    analysis = Analysis()

    #show analysis of file array
    analysis.analyze_all(file_array)
    analysis.analyze_individual(file_array)

    # launch our GUI
    GUI().create_gui(file_100)


