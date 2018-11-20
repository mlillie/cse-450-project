from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from data import Data
from algorithm import Algorithm


def test():
    root = Tk()
    root.resizable(False, False)
    root.title("Advanced Stable Matching")

    canvas = Canvas(root, width=1225, height=525)
    canvas.pack(side=LEFT)
    frame = Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor='nw')

    data = Data()

    patient_values, patient_pref, doctor_values, doctor_pref = data.read("\\test_cases\Sample2.xlsx")

    # Tree view for patient's values and preferences
    Label(frame, text="Patients' Values and Preferences:", font='Helvetica 18 bold').grid(column=0, row=0, sticky=W)
    patient_tree = Treeview(frame, columns=('Age', 'Illness Type', 'Preferred Doctor', 'Preferred Gender',
                                            'Preferred Age Range'), height=4)
    patient_tree.heading('Age', text='Age')
    patient_tree.heading('Illness Type', text='Illness Type')
    patient_tree.heading('Preferred Doctor', text='Preferred Doctor')
    patient_tree.heading('Preferred Gender', text='Preferred Gender')
    patient_tree.heading('Preferred Age Range', text='Preferred Age Range')
    patient_tree.column('Age', minwidth=300, stretch=0, anchor=CENTER)
    patient_tree.column('Illness Type', minwidth=300, stretch=0, anchor=CENTER)
    patient_tree.column('Preferred Doctor', minwidth=300, stretch=0, anchor=CENTER)
    patient_tree.column('Preferred Gender', minwidth=300, stretch=0, anchor=CENTER)
    patient_tree.column('Preferred Age Range', minwidth=300, stretch=YES, anchor=CENTER)

    for key, values in patient_values.items():
        patient_tree.insert('', 'end', text="Patient_" + str(key), values=(values[0], values[1], patient_pref[key][0],
                                                                           patient_pref[key][1],
                                                                           patient_pref[key][2]))

    # Scrollbar for the tree view
    patient_vsb = Scrollbar(frame, orient="vertical", command=patient_tree.yview)
    patient_vsb.grid(column=30, row=1, sticky='ns')

    patient_tree.configure(yscrollcommand=patient_vsb.set)

    patient_tree.grid(column=0, row=1, columnspan=30, sticky='nsew')

    def weights_check(dv):
        try:
            if dv.get() > 100:
                dv.set(100)
            elif dv.get() < 0:
                dv.set(0)
        except (TclError, ValueError):
            pass

    # Patient's Preferences
    patient_age_weight_dv = DoubleVar()
    patient_gender_weight_dv = DoubleVar()
    patient_pref_weight_dv = DoubleVar()

    patient_age_weight_dv.trace('w', lambda name, index, mode: weights_check(patient_age_weight_dv))

    patient_gender_weight_dv.trace('w', lambda name, index, mode: weights_check(patient_gender_weight_dv))

    patient_pref_weight_dv.trace('w', lambda name, index, mode: weights_check(patient_pref_weight_dv))

    patient_age_weight_label = Label(frame, text="Enter Patient's Age Weight (0-100)%: ")
    patient_age_weight_label.grid(column=0, row=6, sticky=W)
    patient_age_weight_entry = Entry(frame, width=4, textvariable=patient_age_weight_dv)
    patient_age_weight_entry.grid(column=1, row=6, sticky=W)

    patient_gender_weight_label = Label(frame, text="Enter Patient's Gender Weight (0-100)%: ")
    patient_gender_weight_label.grid(column=0, row=7, sticky=W)
    patient_gender_weight_entry = Entry(frame, width=4, textvariable=patient_gender_weight_dv)
    patient_gender_weight_entry.grid(column=1, row=7, sticky=W)

    patient_pref_weight_label = Label(frame, text="Enter Patient's Pref Weight (0-100)%: ")
    patient_pref_weight_label.grid(column=0, row=8, sticky=W)
    patient_pref_weight_entry = Entry(frame, width=4, textvariable=patient_pref_weight_dv)
    patient_pref_weight_entry.grid(column=1, row=8, sticky=W)

    # Tree view for doctors's values and preferences
    Label(frame, text="Doctors' Values and Preferences:", font='Helvetica 18 bold').grid(column=0, row=9, sticky=W)
    doctor_tree = Treeview(frame, columns=('Age', 'Gender', 'Preferred Patient', 'Preferred Age Range',
                                           'Preferred Illness'), height=4)
    doctor_tree.heading('Age', text='Age')
    doctor_tree.heading('Gender', text='Gender')
    doctor_tree.heading('Preferred Patient', text='Preferred Patient')
    doctor_tree.heading('Preferred Age Range', text='Preferred Age Range')
    doctor_tree.heading('Preferred Illness', text='Preferred Illness')
    doctor_tree.column('Age', minwidth=300, stretch=0, anchor=CENTER)
    doctor_tree.column('Gender', minwidth=300, stretch=0, anchor=CENTER)
    doctor_tree.column('Preferred Patient', minwidth=300, stretch=0, anchor=CENTER)
    doctor_tree.column('Preferred Age Range', minwidth=300, stretch=YES, anchor=CENTER)
    doctor_tree.column('Preferred Illness', minwidth=300, stretch=0, anchor=CENTER)

    for key, values in doctor_values.items():
        doctor_tree.insert('', 'end', text="Doctor_" + str(key), values=(values[0], values[1], doctor_pref[key][0],
                                                                         doctor_pref[key][1],
                                                                         doctor_pref[key][2]))

    # Scrollbar for the tree view
    doctor_vsb = Scrollbar(frame, orient="vertical", command=doctor_tree.yview)
    doctor_vsb.grid(column=30, row=10, sticky='ns')

    doctor_tree.configure(yscrollcommand=doctor_vsb.set)

    doctor_tree.grid(column=0, row=10, columnspan=30, sticky='nsew')

    # Doctors' preferences
    doctor_age_weight_dv = DoubleVar()
    doctor_illness_weight_dv = DoubleVar()
    doctor_pref_weight_dv = DoubleVar()

    doctor_age_weight_dv.trace('w', lambda name, index, mode: weights_check(doctor_age_weight_dv))

    doctor_illness_weight_dv.trace('w', lambda name, index, mode: weights_check(doctor_illness_weight_dv))

    doctor_pref_weight_dv.trace('w', lambda name, index, mode: weights_check(doctor_pref_weight_dv))

    doctor_age_weight_label = Label(frame, text="Enter Doctor's Age Weight (0-100)%: ")
    doctor_age_weight_label.grid(column=28, row=6, sticky=E)
    doctor_age_weight_entry = Entry(frame, width=4, textvariable=doctor_age_weight_dv)
    doctor_age_weight_entry.grid(column=29, row=6, sticky=E)

    doctor_gender_weight_label = Label(frame, text="Enter Doctor's Illness Weight (0-100)%: ")
    doctor_gender_weight_label.grid(column=28, row=7, sticky=E)
    doctor_gender_weight_entry = Entry(frame, width=4, textvariable=doctor_illness_weight_dv)
    doctor_gender_weight_entry.grid(column=29, row=7, sticky=E)

    doctor_pref_weight_label = Label(frame, text="Enter Doctor's Pref Weight (0-100)%: ")
    doctor_pref_weight_label.grid(column=28, row=8, sticky=E)
    doctor_pref_weight_entry = Entry(frame, width=4, textvariable=doctor_pref_weight_dv)
    doctor_pref_weight_entry.grid(column=29, row=8, sticky=E)

    # Results page
    Label(frame, text="Matching Results:", font='Helvetica 18 bold').grid(column=0, row=12, sticky=W)
    results_tree = Treeview(frame, columns=2, height=4)

    results_tree.heading('#0', text='Doctor/Patient')
    results_tree.heading('#1', text='Opposition Match')
    results_tree.column('#1', minwidth=300, stretch=YES, anchor=CENTER)
    results_tree.column('#0', minwidth=300, stretch=YES, anchor=CENTER)

    # Scrollbar for the tree view
    results_vsb = Scrollbar(frame, orient="vertical", command=results_tree.yview)
    results_vsb.grid(column=30, row=13, sticky='ns')

    results_tree.configure(yscrollcommand=results_vsb.set)

    results_tree.grid(column=0, row=13, columnspan=30, sticky='nsew')

    # Handling the matching buttons
    def match_doctor_button():
        d_age_weight = doctor_age_weight_dv.get() / 100.0
        d_illness_weight = doctor_illness_weight_dv.get() / 100.0
        d_pref_weight = doctor_pref_weight_dv.get() / 100.0

        p_age_weight = patient_age_weight_dv.get() / 100.0
        p_gender_weight = patient_gender_weight_dv.get() / 100.0
        p_pref_weight = patient_pref_weight_dv.get() / 100.0

        if d_age_weight + d_illness_weight + d_pref_weight != 1 or p_age_weight + p_gender_weight + p_pref_weight != 1:
            messagebox.showerror("Error", "Invalid Preference Weights")
        else:
            results_tree.delete(*results_tree.get_children())
            algorithm = Algorithm()
            percentages = Data().calc_percentages((patient_values, patient_pref, doctor_values, doctor_pref), (
                p_age_weight, p_gender_weight, p_pref_weight, d_illness_weight, d_age_weight, d_pref_weight))
            results = algorithm.doctor_matching_algorithm((patient_values, patient_pref, doctor_values, doctor_pref),
                                                          percentages)

            del percentages

            for key, value in results.items():
                results_tree.insert('', 'end', text="Doctor_" + str(key), values=("Patient_" + str(value)))

            del results

    def match_patient_button():
        d_age_weight = doctor_age_weight_dv.get() / 100.0
        d_illness_weight = doctor_illness_weight_dv.get() / 100.0
        d_pref_weight = doctor_pref_weight_dv.get() / 100.0

        p_age_weight = patient_age_weight_dv.get() / 100.0
        p_gender_weight = patient_gender_weight_dv.get() / 100.0
        p_pref_weight = patient_pref_weight_dv.get() / 100.0

        if d_age_weight + d_illness_weight + d_pref_weight != 1 or p_age_weight + p_gender_weight + p_pref_weight != 1:
            messagebox.showerror("Error", "Invalid Preference Weights")
        else:
            results_tree.delete(*results_tree.get_children())
            algorithm = Algorithm()
            percentages = Data().calc_percentages((patient_values, patient_pref, doctor_values, doctor_pref), (
                p_age_weight, p_gender_weight, p_pref_weight, d_illness_weight, d_age_weight, d_pref_weight))
            results = algorithm.patient_matching_algorithm((patient_values, patient_pref, doctor_values, doctor_pref),
                                                           percentages)
            del percentages

            for key, value in results.items():
                results_tree.insert('', 'end', text="Patient_" + str(key), values=("Doctor_" + str(value)))

            del results

    Button(frame, text="Match Doctor -> Patient", command=match_doctor_button).grid(column=0, row=14, sticky=W)
    Button(frame, text="Match Patient -> Doctor", command=match_patient_button).grid(column=29, row=14, sticky=E)

    root.mainloop()


if __name__ == '__main__':
    test()
