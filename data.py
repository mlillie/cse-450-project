# data.py
# -----------------------------------------------------------------------------------------------
# This class file will be used to process the excel files that are built outside of this program.
# These excel files will be used to create the preference lists.
# The program should be able to handle any number of preference lists,
# this assumes that the preference lists are correct in that they have the same
# number of doctors as patients and the values are valid for the algorithm.

# Created By: Jacky Fonseca
# Last Edit: 11/21/2018

# TODO: Need to edit the read function to take any arbitrary excel file with any number of preferences.
import operator

import xlrd
import os

PATIENT_AGE_WEIGHT = 0.20
PATIENT_GENDER_WEIGHT = 0.20
PATIENT_PREFERRED_DOCTOR_WEIGHT = 0.60

DOCTOR_ILLNESS_WEIGHT = 0.60
DOCTOR_AGE_WEIGHT = 0.10
DOCTOR_PREFERRED_PATIENT_WEIGHT = 0.30

class Data:

    def read(self, file):
        # path = os.getcwd() + "\\test_cases\Sample2.xlsx"
        path = os.getcwd() + file

        wb = xlrd.open_workbook(path)
        sheet = wb.sheet_by_index(0)

        # dictionaries for starting values and preference lists
        patient_values = {}
        patient_pref = {}
        doctor_values = {}
        doctor_pref = {}

        # retrieves data from xlsx sheet
        for j in range(sheet.nrows):
            if j > 0:

                # Patient's assigned values
                patient_values[j-1] = sheet.row_values(j, 0, 2)

                # Patient's preference lists
                """
                pt1 = Preferred doctor list
                pt2 = Preferred gender list
                pt3 = Preferred age range list (in tuples)
                """
                pt1 = str((sheet.row_values(j, 2, 4))[0]).split(",")
                pt2 = str((sheet.row_values(j, 3, 4))[0]).split(",")
                pt3 = (str((sheet.row_values(j, 4, 5))[0]).replace("(", ""))

                # creates age ranges and adds them as tuples to a list
                age_range = []
                while pt3.find(")") != -1:
                    pair = tuple((pt3[:pt3.find(")")]).split(","))
                    age_range.append(pair)
                    pt3 = (pt3.replace(",".join(pair) + ")", ""))[1:]

                # adds preferences to dictionary
                patient_pref[j-1] = (pt1, pt2, age_range)

                # Doctor's assigned values
                doctor_values[j-1] = sheet.row_values(j, 5, 7)

                # Doctor's preference
                """
                    pt1 = Preferred patient list
                    pt2 = Preferred age range list (in tuples)
                    pt3 = Preferred illness type list 
                """
                dt1 = str((sheet.row_values(j, 7, 8))[0]).split(",")

                # creates age ranges and adds them as tuples to a list
                age_range = []
                dt2 = str((sheet.row_values(j, 8, 9))[0]).replace("(", "")
                while dt2.find(")") != -1:
                    pair = tuple((dt2[:dt2.find(")")]).split(","))
                    age_range.append(pair)
                    dt2 = (dt2.replace(",".join(pair) + ")", ""))[1:]

                dt3 = str((sheet.row_values(j, 9, 10))[0]).split(",")

                # adds preferences to dictionary
                doctor_pref[j - 1] = (dt1, age_range, dt3)

        # print(patient_values)
        # print(doctor_values)
        # print(patient_pref)
        # print(doctor_pref)

        return patient_values, patient_pref, doctor_values, doctor_pref

    def calc_percentages(self, data, weights=(PATIENT_AGE_WEIGHT, PATIENT_GENDER_WEIGHT,
                                              PATIENT_PREFERRED_DOCTOR_WEIGHT, DOCTOR_ILLNESS_WEIGHT, DOCTOR_AGE_WEIGHT,
                                              DOCTOR_PREFERRED_PATIENT_WEIGHT)):

        patient_values, patient_pref, doctor_values, doctor_pref = data
        doctor_ids = doctor_pref.keys()
        patient_ids = patient_pref.keys()
        patient_percentages = {p: dict.fromkeys(doctor_ids, 0.0) for p in patient_ids}

        doctor_percentages = {d: dict.fromkeys(patient_ids, 0.0) for d in doctor_ids}

        for p_id in patient_ids:
            for d_id in doctor_ids:
                # First calculation of  patient percentage to doctor
                patient_pref_doc_ids = list(map(int, patient_pref[p_id][0]))
                patient_pref_doc_ids_length = len(patient_pref_doc_ids)
                patient_pref_gender = list(map(int, patient_pref[p_id][1]))
                patient_pref_gender_length = len(patient_pref_gender)
                patient_pref_doctor_age = patient_pref[p_id][2]
                patient_pref_doctor_age_length = len(patient_pref_doctor_age)

                doctor_age = doctor_values[d_id][0]
                doctor_gender = doctor_values[d_id][1]

                doctor_pref_index = patient_pref_doc_ids.index(d_id)
                doctor_pref_gender_index = patient_pref_gender.index(doctor_gender)
                doctor_pref_age_index = -1

                for index, (lower, higher) in enumerate(patient_pref_doctor_age):
                    if int(lower) <= doctor_age <= int(higher):
                        doctor_pref_age_index = index
                        break

                patient_percentages[p_id][d_id] = (((patient_pref_doc_ids_length - doctor_pref_index) /
                                                    patient_pref_doc_ids_length) * weights[2]) + \
                                                  (((patient_pref_gender_length - doctor_pref_gender_index) /
                                                    patient_pref_gender_length) * weights[1]) + \
                                                  (((patient_pref_doctor_age_length - doctor_pref_age_index) /
                                                    patient_pref_doctor_age_length) * weights[0])

                # Second calculation of doctor percentage to patient
                doctor_pref_patient_ids = list(map(int, doctor_pref[d_id][0]))
                doctor_pref_patient_ids_length = len(doctor_pref_patient_ids)
                doctor_pref_patient_age = doctor_pref[d_id][1]
                doctor_pref_patient_age_length = len(doctor_pref_patient_age)
                doctor_pref_patient_illness = list(map(int, doctor_pref[d_id][2]))
                doctor_pref_patient_illness_length = len(doctor_pref_patient_illness)

                patient_age = patient_values[p_id][0]
                patient_illness = patient_values[p_id][1]

                patient_pref_index = doctor_pref_patient_ids.index(p_id)
                patient_pref_illness_index = doctor_pref_patient_illness.index(patient_illness)
                patient_pref_age_index = -1

                for index, (lower, higher) in enumerate(doctor_pref_patient_age):
                    if int(lower) <= patient_age <= int(higher):
                        patient_pref_age_index = index
                        break

                doctor_percentages[d_id][p_id] = (((doctor_pref_patient_age_length - patient_pref_age_index) /
                                                   doctor_pref_patient_age_length) * weights[4]) + \
                                                 (((doctor_pref_patient_illness_length - patient_pref_illness_index) /
                                                   doctor_pref_patient_illness_length) * weights[3]) + \
                                                 (((doctor_pref_patient_ids_length - patient_pref_index) /
                                                   doctor_pref_patient_ids_length) * weights[5])

        # print(patient_percentages)
        print(doctor_percentages)

        # Sort the nested dictionary by the value (percentage)
        patient_percentages = {key: dict(sorted(values.items(), key=operator.itemgetter(1), reverse=True)) for
                               key, values in
                               patient_percentages.items()}
        doctor_percentages = {key: dict(sorted(values.items(), key=operator.itemgetter(1), reverse=True)) for
                              key, values in
                              doctor_percentages.items()}
        return patient_percentages, doctor_percentages
