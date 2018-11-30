# algorithm.py
# -----------------------------------------------------------------------------------------------
# This class file will implement the actual algorithm from the project proposal document.
# As such, this is an advanced stable matching algorithm which uses doctor and patient
# preference lists but instead of just having the preferred doctor/patient, the list
# will contain other attributes that weigh the matching stable pairs to be found.


# Created by Matthew Lillie
# Last edit: 11/26/18

# Minor updates by Paul Witulski
# Last edit: 11/25/18

class Algorithm:
    # private variable to keep track of number of swaps
    swap_count = 0

    def doctor_matching_algorithm(self, data, percentages):
        proposals = 0
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
            for d_id in doctor_ids:
                # Check to see if it has not matched
                if doctors_dict.get(d_id) is None:
                    # Go through the patient prefs for this doctor
                    doctor_pref_patient_ids = doctor_percentages[d_id].keys()
                    for p_id in doctor_pref_patient_ids:
                        # Check to see if the patient is not matched
                        if patients_dict.get(p_id) is None:
                            doctors_dict[d_id] = p_id
                            patients_dict[p_id] = d_id
                            matching[d_id] = p_id
                            proposals += 1
                            # print("Proposed: ", proposals)
                            break  # The doctor has matched so we can break
                        else:
                            # If it is, check the percentage calculation of the patient prefs to determine if we should
                            # replace the current match
                            doctor_matching = patients_dict.get(p_id)

                            percentage_to_current = patient_percentages[p_id][doctor_matching]
                            percentage_to_possible = patient_percentages[p_id][d_id]

                            # Check to see if the patient prefers this doctor to it's current one
                            if percentage_to_current < percentage_to_possible:
                                # if so, then switch them by deleting the current match from matching and swapping
                                del matching[doctor_matching]
                                doctors_dict[doctor_matching] = None
                                doctors_dict[d_id] = p_id
                                patients_dict[p_id] = d_id
                                matching[d_id] = p_id
                                proposals += 1
                                self.swap_count += 1
                                # print("Proposed: ", proposals)
                                break  # The doctor has matched so we can break
        print("Doctor matches: ", matching)
        if proposals <= len(doctors_dict.keys())**2:
            print("Algorithm is O(n^2). N = ", len(doctors_dict.keys()), ". Proposals = ", proposals)
        else:
            print("Algorithm is NOT O(n^2). N = ", len(doctors_dict.keys()), ". Proposals = ", proposals)
        return matching, proposals

    def patient_matching_algorithm(self, data, percentages):
        proposals = 0
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
            for p_id in patient_ids:
                # Check to see if it has not matched
                if patients_dict.get(p_id) is None:
                    # Go through the doctor prefs for this patient
                    patient_pref_doctor_ids = patient_percentages[p_id].keys()
                    for d_id in patient_pref_doctor_ids:
                        # Check to see if the doctor is not matched
                        if doctors_dict.get(d_id) is None:
                            doctors_dict[d_id] = p_id
                            patients_dict[p_id] = d_id
                            matching[p_id] = d_id
                            proposals += 1
                            break  # The doctor has matched so we can break
                        else:
                            # If it is, check the percentage calculation of the doctor prefs to determine if we should
                            # replace the current match
                            patient_matching = doctors_dict.get(d_id)

                            percentage_to_current = doctor_percentages[d_id][patient_matching]
                            percentage_to_possible = doctor_percentages[d_id][p_id]
                            # Check to see if the doctor prefers this patient to it's current one
                            if percentage_to_current < percentage_to_possible:
                                # if so, then switch them by deleting the current match from matching and swapping
                                del matching[patient_matching]
                                patients_dict[patient_matching] = None
                                patients_dict[p_id] = p_id
                                doctors_dict[d_id] = p_id
                                matching[p_id] = d_id
                                proposals += 1
                                # print("Proposed: ", proposals)
                                break  # The doctor has matched so we can break
        print("Patient matches: ", matching)
        if proposals <= len(doctors_dict.keys())**2:
            print("Algorithm is O(n^2). N = ", len(doctors_dict.keys()), ". Proposals = ", proposals)
        else:
            print("Algorithm is NOT O(n^2). N = ", len(doctors_dict.keys()), ". Proposals = ", proposals)
        return matching, proposals

    def get_swap_count(self):
        return self.swap_count
