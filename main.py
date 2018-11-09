from algorithm import Algorithm
from data import Data
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
    Algorithm().doctor_matching_algorithm(pref_lists)
    Algorithm().patient_matching_algorithm(pref_lists)
    # Analysis will need to monitor the algorithm
    # TODO: The Analysis class will be used to log the results from Algorithm
    Analysis()
