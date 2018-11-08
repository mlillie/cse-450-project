# # Loop until every hospital has been matched
# while len(matching) != len(hospital_ids):
#     # Go through each hospital
#     for hospital in hospital_ids:
#         # Check to see if it has not matched
#         if hospitals_dict.get(hospital) is None:
#             # Go through the student prefs for this hospital
#             for student in hospital_prefs[hospital]:
#                 # Check to see if the student is not matched
#                 if students_dict.get(student) is None:
#                     hospitals_dict[hospital] = student
#                     students_dict[student] = hospital
#                     matching[hospital] = student
#                     proposals_count += 1
#                     break  # The hospital has matched so we can break
#                 else:
#                     # If it is, check the index of the student prefs to determine if we should
#                     # replace the current match
#                     hospital_matching = students_dict.get(student)
#                     # Check to see if the student prefers this hospital to it's current one
#                     if student_prefs[student].index(hospital) < student_prefs[student].index(hospital_matching):
#                         # if so, then switch them by deleting the current match from matching and swapping
#                         del matching[hospital_matching]
#                         hospitals_dict[hospital_matching] = None
#                         hospitals_dict[hospital] = student
#                         students_dict[student] = hospital
#                         matching[hospital] = student
#                         proposals_count += 1
#                         break  # The hospital has matched so we can break

# preferred patients
# age range of patient
# illness type
#
#
# preferred doc
# age range of doc
# gender of doc
from Data import Data

PATIENT_AGE_WEIGHT = 0.20
PATIENT_GENDER_WEIGHT = 0.20
PATIENT_PREFERRED_DOCTOR_WEIGHT = 0.60

DOCTOR_ILLNESS_WEIGHT = 0.60
DOCTOR_AGE_WEIGHT = 0.10
DOCTOR_PREFERRED_PATIENT_WEIGHT = 0.30


class Algorithm:

    def matching_algorithm(self, doctor_preference_list, patient_preference_list):
        pass

    def calculate_percentages(self):
        patient_values, patient_pref, doctor_values, doctor_pref = Data().read()
        doctor_pref_percentages = dict((key, []) for key in doctor_pref.keys())
        patient_pref_percentages = dict((key, []) for key in patient_pref.keys())

        for patient_id in patient_pref.keys():
            for doctor_id in doctor_pref.keys():
                doctor_pref_patient_ids = list(map(int, doctor_pref[doctor_id][0]))
                doctor_pref_patient_ids_length = len(doctor_pref_patient_ids)
                doctor_pref_patient_age = doctor_pref[doctor_id][1]
                doctor_pref_patient_age_length = len(doctor_pref_patient_age)
                doctor_pref_patient_illness = list(map(int, doctor_pref[doctor_id][2]))
                doctor_pref_patient_illness_length = len(doctor_pref_patient_illness)

                patient_age = patient_values[patient_id][1]
                patient_illness = patient_values[patient_id][2]

                patient_pref_index = doctor_pref_patient_ids.index(patient_id) + 1
                patient_pref_illness_index = doctor_pref_patient_illness.index(patient_illness) + 1
                patient_pref_age_index = -1

                for index, (lower, higher) in enumerate(doctor_pref_patient_age):
                    if int(lower) <= patient_age <= int(higher):
                        patient_pref_age_index = index + 1
                        break

                percentage = ((patient_pref_age_index / doctor_pref_patient_age_length) * DOCTOR_AGE_WEIGHT) + \
                             ((
                                          patient_pref_illness_index / doctor_pref_patient_illness_length) * DOCTOR_ILLNESS_WEIGHT) + \
                             ((patient_pref_index / doctor_pref_patient_ids_length) * DOCTOR_PREFERRED_PATIENT_WEIGHT)

                doctor_pref_percentages[doctor_id] = list(doctor_pref_percentages[doctor_id]) + [percentage]

        for doctor_id in doctor_pref.keys():
            for patient_id in patient_pref.keys():
                patient_pref_doc_ids = list(map(int, patient_pref[patient_id][0]))
                # TEMPORARY FIX
                patient_pref_doc_ids[:] = [x - 1 for x in patient_pref_doc_ids]
                patient_pref_doc_ids_length = len(patient_pref_doc_ids)
                patient_pref_gender = list(map(int, patient_pref[patient_id][1]))
                patient_pref_gender_length = len(patient_pref_gender)
                patient_pref_doctor_age = patient_pref[patient_id][2]
                patient_pref_doctor_age_length = len(patient_pref_doctor_age)

                doctor_age = doctor_values[doctor_id][1]
                doctor_gender = doctor_values[doctor_id][2]

                doctor_pref_index = patient_pref_doc_ids.index(doctor_id) + 1
                doctor_pref_gender_index = patient_pref_gender.index(doctor_gender) + 1
                doctor_pref_age_index = -1

                for index, (lower, higher) in enumerate(patient_pref_doctor_age):
                    if int(lower) <= doctor_age <= int(higher):
                        doctor_pref_age_index = index + 1
                        break

                percentage = ((doctor_pref_index / patient_pref_doc_ids_length) * PATIENT_PREFERRED_DOCTOR_WEIGHT) + \
                             ((doctor_pref_gender_index / patient_pref_gender_length) * PATIENT_GENDER_WEIGHT) + \
                             ((doctor_pref_age_index / patient_pref_doctor_age_length) * PATIENT_AGE_WEIGHT)

                patient_pref_percentages[patient_id] = patient_pref_percentages[patient_id] + [percentage]

        print(doctor_pref_percentages)
        print(patient_pref_percentages)
