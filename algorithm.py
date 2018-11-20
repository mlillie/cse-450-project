# algorithm.py
# -----------------------------------------------------------------------------------------------
# This class file will implement the actual algorithm from the project proposal document.
# As such, this is an advanced stable matching algorithm which uses doctor and patient
# preference lists but instead of just having the preferred doctor/patient, the list
# will contain other attributes that weigh the matching stable pairs to be found.


# Created by Matthew Lillie
# Last edit: 11/20/18

class Algorithm:

    def doctor_matching_algorithm(self, data, percentages):
        patient_values, patient_pref, doctor_values, doctor_pref = data
        patient_percentages, doctor_percentages = percentages
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
                    doctor_pref_patient_ids = doctor_percentages[doctor].keys()
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

                            percentage_to_current = patient_percentages[patient][doctor_matching]
                            percentage_to_possible = patient_percentages[patient][doctor]

                            # Check to see if the patient prefers this doctor to it's current one
                            if percentage_to_current < percentage_to_possible:
                                # if so, then switch them by deleting the current match from matching and swapping
                                del matching[doctor_matching]
                                doctors_dict[doctor_matching] = None
                                doctors_dict[doctor] = patient
                                patients_dict[patient] = doctor
                                matching[doctor] = patient
                                print("SWAP")
                                break  # The doctor has matched so we can break
        print("Doctor matches: ", matching)
        return matching

    def patient_matching_algorithm(self, data, percentages):
        patient_values, patient_pref, doctor_values, doctor_pref = data
        patient_percentages, doctor_percentages = percentages
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
                    patient_pref_doctor_ids = patient_percentages[patient].keys()
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

                            percentage_to_current = doctor_percentages[doctor][patient_matching]
                            percentage_to_possible = doctor_percentages[doctor][patient]
                            # Check to see if the doctor prefers this patient to it's current one
                            if percentage_to_current < percentage_to_possible:
                                # if so, then switch them by deleting the current match from matching and swapping
                                del matching[patient_matching]
                                patients_dict[patient_matching] = None
                                patients_dict[patient] = patient
                                doctors_dict[doctor] = patient
                                matching[patient] = doctor
                                print("SWAP")
                                break  # The doctor has matched so we can break
        print("Patient matches: ", matching)
        return matching
