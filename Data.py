import xlrd
import os

# CREATED BY: JACKY FONSECA
# LAST MODIFICATION: 11/07/2018


class Data:
    def read(self):
        path = os.getcwd() + "\\test_cases\examplesample.xlsx"

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
                patient_values[j-1] = sheet.row_values(j, 0, 3)

                # Patient's preference lists
                """
                pt1 = Preferred doctor list
                pt2 = Preferred gender list
                pt3 = Preferred age range list (in tuples)
                """
                pt1 = str((sheet.row_values(j, 3, 4))[0]).split(",")
                pt2 = str((sheet.row_values(j, 4, 5))[0]).split(",")
                pt3 = (str((sheet.row_values(j, 5, 6))[0]).replace("(", ""))

                # creates age ranges and adds them as tuples to a list
                age_range = []
                while pt3.find(")") != -1:
                    pair = tuple((pt3[:pt3.find(")")]).split(","))
                    age_range.append(pair)
                    pt3 = (pt3.replace(",".join(pair) + ")", ""))[1:]

                # adds preferences to dictionary
                patient_pref[j-1] = (pt1, pt2, age_range)

                # Doctor's assigned values
                doctor_values[j-1] = sheet.row_values(j, 7, 10)

                # Doctor's preference
                """
                    pt1 = Preferred patient list
                    pt2 = Preferred age range list (in tuples)
                    pt3 = Preferred illness type list 
                """
                dt1 = str((sheet.row_values(j, 9, 10))[0]).split(",")

                # creates age ranges and adds them as tuples to a list
                age_range = []
                dt2 = str((sheet.row_values(j, 10, 11))[0]).replace("(", "")
                while dt2.find(")") != -1:
                    pair = tuple((dt2[:dt2.find(")")]).split(","))
                    age_range.append(pair)
                    dt2 = (dt2.replace(",".join(pair) + ")", ""))[1:]

                dt3 = str((sheet.row_values(j, 11, 12))[0]).split(",")

                # adds preferences to dictionary
                doctor_pref[j - 1] = (dt1, age_range, dt3)

        return patient_values, patient_pref, doctor_values, doctor_pref

