# algorithm.py
# -----------------------------------------------------------------------------------------------
# This class file will implement the actual algorithm from the project proposal document.
# As such, this is an advanced stable matching algorithm which uses doctor and patient
# preference lists but instead of just having the preferred doctor/patient, the list
# will contain other attributes that weigh the matching stable pairs to be found.


# Created by Matthew Lillie
# Last edit: 11/09/18

from data import Data

PATIENT_AGE_WEIGHT = 0.20
PATIENT_GENDER_WEIGHT = 0.20
PATIENT_PREFERRED_DOCTOR_WEIGHT = 0.60

DOCTOR_ILLNESS_WEIGHT = 0.60
DOCTOR_AGE_WEIGHT = 0.10
DOCTOR_PREFERRED_PATIENT_WEIGHT = 0.30


class Algorithm:

    def doctor_matching_algorithm(self):
        return self.doctor_matching_algorithm(Data().read("\\test_cases\Sample2.xlsx"))

    def doctor_matching_algorithm(self, pref_lists):
        patient_values, patient_pref, doctor_values, doctor_pref = pref_lists
        doctor_ids = doctor_pref.keys()
        patient_ids = patient_pref.keys()
        matching = dict()
        doctors_dict = dict.fromkeys(doctor_ids)
        patients_dict = dict.fromkeys(patient_ids)
        # Loop until every doctor has been matched
        while len(matching) != len(doctor_ids):
            # Go through each doctor
            for doctor in doctor_ids:
                # Check to see if it has not matched
                if doctors_dict.get(doctor) is None:
                    # Go through the patient prefs for this doctor
                    doctor_pref_patient_ids = list(map(int, doctor_pref[doctor][0]))
                    for patient in doctor_pref_patient_ids:
                        # Check to see if the patient is not matched
                        if patients_dict.get(patient) is None:
                            doctors_dict[doctor] = patient
                            patients_dict[patient] = doctor
                            matching[doctor] = patient
                            break  # The doctor has matched so we can break
                        else:
                            # If it is, check the percentage calculation of the patient prefs to determine if we should
                            # replace the current match
                            doctor_matching = patients_dict.get(patient)

                            percentage_to_current = self.calculate_percentages_patient(patient_pref,
                                                                                       doctor_values, doctor,
                                                                                       doctor_matching)
                            percentage_to_possible = self.calculate_percentages_patient(patient_pref,
                                                                                        doctor_values, doctor, patient)
                            # Check to see if the patient prefers this doctor to it's current one
                            if percentage_to_current < percentage_to_possible:
                                # if so, then switch them by deleting the current match from matching and swapping
                                del matching[doctor_matching]
                                doctors_dict[doctor_matching] = None
                                doctors_dict[doctor] = patient
                                patients_dict[patient] = doctor
                                matching[doctor] = patient
                                break  # The doctor has matched so we can break
        print("Doctor matches: ", matching)

    def patient_matching_algorithm(self):
        return self.patient_matching_algorithm(Data().read("\\test_cases\Sample2.xlsx"))

    def patient_matching_algorithm(self, pref_lists):
        patient_values, patient_pref, doctor_values, doctor_pref = pref_lists
        doctor_ids = doctor_pref.keys()
        patient_ids = patient_pref.keys()
        matching = dict()
        doctors_dict = dict.fromkeys(doctor_ids)
        patients_dict = dict.fromkeys(patient_ids)
        # Loop until every patient has been matched
        while len(matching) != len(patient_ids):
            # Go through each patient
            for patient in patient_ids:
                # Check to see if it has not matched
                if patients_dict.get(patient) is None:
                    # Go through the doctor prefs for this patient
                    patient_pref_doctor_ids = list(map(int, patient_pref[patient][0]))
                    for doctor in patient_pref_doctor_ids:
                        # Check to see if the doctor is not matched
                        if doctors_dict.get(doctor) is None:
                            doctors_dict[doctor] = patient
                            patients_dict[patient] = doctor
                            matching[patient] = doctor
                            break  # The doctor has matched so we can break
                        else:
                            # If it is, check the percentage calculation of the doctor prefs to determine if we should
                            # replace the current match
                            patient_matching = doctors_dict.get(doctor)

                            percentage_to_current = self.calculate_percentages_doctor(patient_values, doctor_pref,
                                                                                      patient_matching,
                                                                                      patient)
                            percentage_to_possible = self.calculate_percentages_doctor(patient_values, doctor_pref,
                                                                                       doctor, patient)
                            # Check to see if the doctor prefers this patient to it's current one
                            if percentage_to_current < percentage_to_possible:
                                # if so, then switch them by deleting the current match from matching and swapping
                                del matching[patient_matching]
                                patients_dict[patient_matching] = None
                                patients_dict[patient] = patient
                                doctors_dict[doctor] = patient
                                matching[patient] = doctor
                                break  # The doctor has matched so we can break
        print("Patient matches: ", matching)

    def calculate_percentages_patient(self, patient_pref, doctor_values, doctor_id, patient_id):
        patient_pref_doc_ids = list(map(int, patient_pref[patient_id][0]))
        patient_pref_doc_ids_length = len(patient_pref_doc_ids)
        patient_pref_gender = list(map(int, patient_pref[patient_id][1]))
        patient_pref_gender_length = len(patient_pref_gender)
        patient_pref_doctor_age = patient_pref[patient_id][2]
        patient_pref_doctor_age_length = len(patient_pref_doctor_age)

        doctor_age = doctor_values[doctor_id][0]
        doctor_gender = doctor_values[doctor_id][1]

        doctor_pref_index = patient_pref_doc_ids.index(doctor_id)
        doctor_pref_gender_index = patient_pref_gender.index(doctor_gender)
        doctor_pref_age_index = -1

        for index, (lower, higher) in enumerate(patient_pref_doctor_age):
            if int(lower) <= doctor_age <= int(higher):
                doctor_pref_age_index = index
                break

        # print("patient_pref: ", doctor_pref_index,
        #       ((patient_pref_doc_ids_length - doctor_pref_index) / patient_pref_doc_ids_length) *
        #       PATIENT_PREFERRED_DOCTOR_WEIGHT)
        # print("patient_pref_gender: ", doctor_pref_gender_index,
        #       ((patient_pref_gender_length - doctor_pref_gender_index) / patient_pref_gender_length) *
        #       PATIENT_GENDER_WEIGHT)
        # print("patient_pref_age: ", doctor_pref_age_index,
        #       ((patient_pref_doctor_age_length - doctor_pref_age_index) / patient_pref_doctor_age_length) *
        #       PATIENT_AGE_WEIGHT)

        patient_to_doctor_percentage = (((patient_pref_doc_ids_length - doctor_pref_index) /
                                         patient_pref_doc_ids_length) * PATIENT_PREFERRED_DOCTOR_WEIGHT) + \
                                       (((patient_pref_gender_length - doctor_pref_gender_index) /
                                         patient_pref_gender_length) * PATIENT_GENDER_WEIGHT) + \
                                       (((patient_pref_doctor_age_length - doctor_pref_age_index) /
                                         patient_pref_doctor_age_length) * PATIENT_AGE_WEIGHT)

        return patient_to_doctor_percentage

    def calculate_percentages_doctor(self, patient_values, doctor_pref, doctor_id, patient_id):
        doctor_pref_patient_ids = list(map(int, doctor_pref[doctor_id][0]))
        doctor_pref_patient_ids_length = len(doctor_pref_patient_ids)
        doctor_pref_patient_age = doctor_pref[doctor_id][1]
        doctor_pref_patient_age_length = len(doctor_pref_patient_age)
        doctor_pref_patient_illness = list(map(int, doctor_pref[doctor_id][2]))
        doctor_pref_patient_illness_length = len(doctor_pref_patient_illness)

        patient_age = patient_values[patient_id][0]
        patient_illness = patient_values[patient_id][1]

        patient_pref_index = doctor_pref_patient_ids.index(patient_id)
        patient_pref_illness_index = doctor_pref_patient_illness.index(patient_illness)
        patient_pref_age_index = -1

        for index, (lower, higher) in enumerate(doctor_pref_patient_age):
            if int(lower) <= patient_age <= int(higher):
                patient_pref_age_index = index
                break

        doctor_to_patient_percentage = (((doctor_pref_patient_age_length - patient_pref_age_index) /
                                         doctor_pref_patient_age_length) * DOCTOR_AGE_WEIGHT) + \
                                       (((doctor_pref_patient_illness_length - patient_pref_illness_index) /
                                         doctor_pref_patient_illness_length) * DOCTOR_ILLNESS_WEIGHT) + \
                                       (((doctor_pref_patient_ids_length - patient_pref_index) /
                                         doctor_pref_patient_ids_length) * DOCTOR_PREFERRED_PATIENT_WEIGHT)

        return doctor_to_patient_percentage
