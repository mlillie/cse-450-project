from tkinter import *
from tkinter.ttk import *

p_ages_ordered = []
d_ages_ordered = []
d_genders_ordered = []
p_types_ordered = []
p_ages = [(101, 110), (91, 100), (81, 90), (71, 80), (61, 70), (51, 60), (41, 50), (31, 40), (21, 30), (11, 20),
          (0, 10)]
d_ages = [(81, 90), (71, 80), (61, 70), (51, 60), (41, 50), (31, 40), (21, 30)]
d_genders = [3, 2, 1, 0]
p_types = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


class GUI:

    def delete_p_age(self, l):
        global p_ages
        global p_ages_ordered
        # Delete from Listbox
        selection = l.curselection()
        if selection:
            value = l.get(selection[0])
            l.delete(selection[0])
            # Delete from list that provided it
            ind = int(p_ages.index(value))
            del (p_ages[ind])
            p_ages_ordered.append(value)

    def delete_p_illness(self, l):
        global p_types
        global p_types_ordered
        # Delete from Listbox
        selection = l.curselection()
        if selection:
            value = l.get(selection[0])
            l.delete(selection[0])
            # Delete from list that provided it
            ind = int(p_types.index(value))
            del (p_types[ind])
            p_types_ordered.append(value)

    def delete_d_age(self, l):
        global d_ages
        global d_ages_ordered
        # Delete from Listbox
        selection = l.curselection()
        if selection:
            value = l.get(selection[0])
            l.delete(selection[0])
            # Delete from list that provided it
            ind = int(d_ages.index(value))
            del (d_ages[ind])
            d_ages_ordered.append(value)

    def delete_d_gender(self, l):
        global d_genders
        global d_genders_ordered
        # Delete from Listbox
        selection = l.curselection()
        if selection:
            value = l.get(selection[0])
            l.delete(selection[0])
            # Delete from list that provided it
            ind = int(d_genders.index(value))
            del (d_genders[ind])
            d_genders_ordered.append(value)

    def application(self):
        global p_ages
        global p_ages_ordered
        global p_types
        global p_types_ordered
        global d_genders
        global d_genders_ordered
        global d_ages
        global d_ages_ordered

        window = Tk()
        window.title("Advanced Stable Matching GUI")
        window.geometry('1000x800')

        scroll = Scrollbar(window, orient='vertical')
        scroll.grid(column=10, rowspan=50, sticky=N + S)

        prompt = Label(window, text="Add another doctor and patient.", font='Helvetica 12 bold')
        prompt.grid(column=0, row=0, columnspan=1, sticky=W)

        """Doctor values"""
        d_prompt = Label(window, text="Add values to each doctor.", font='Helvetica 10 italic')
        d_gender_lbl = Label(window, text="Gender of the doctor.")
        gender_values = Label(window, text="0=male, 1=female, 2=other, and 3=neither.")
        d_gender_combo = Combobox(window, width=5)
        d_gender_combo['values'] = (0, 1, 2, 3)
        d_age_lbl = Label(window, text="Age range of the doctor.")
        d_age_combo = Combobox(window, width=5)
        d_age_combo['values'] = ("30-40", "41-50", "51-60", "61-70", "71-80")

        d_prompt.grid(column=0, row=3, columnspan=1, rowspan=3, pady=15, sticky=W)
        d_gender_lbl.grid(column=0, row=7, columnspan=1, sticky=W)
        gender_values.grid(column=0, row=8, columnspan=1, sticky=W)
        d_gender_combo.grid(column=1, row=7, columnspan=1, sticky=W)
        d_age_lbl.grid(column=0, row=9, columnspan=1, sticky=W)
        d_age_combo.grid(column=1, row=9, columnspan=1, sticky=W)

        """Doctor preferences"""
        d_p_prompt = Label(window, text="Configure the doctor's preferences.", font='Helvetica 10 italic')
        d_age_p_lbl = Label(window, text="Age of patients.")
        d_age_b_lbl = Label(window, text="Click the 'Add' button.")

        # Age preferences
        p_age_list = Listbox(window)
        for e in p_ages:
            p_age_list.insert(0, e)

        p_ages_button = Button(window, text="Add age", command=lambda: self.delete_p_age(p_age_list))

        # Illness preferences
        p_illness_list = Listbox(window)
        for e in p_types:
            p_illness_list.insert(0, e)

        d_type_p_lbl = Label(window, text="Type of illness.")
        d_type_b_lbl = Label(window, text="Click the 'Add' button.")

        p_illness_button = Button(window, text="Add illness", command=lambda: self.delete_p_illness(p_illness_list))

        d_p_prompt.grid(column=0, row=10, columnspan=1, rowspan=1, pady=15, sticky=W)
        d_age_p_lbl.grid(column=0, row=11, columnspan=1, sticky=W)
        d_age_b_lbl.grid(column=0, row=12, columnspan=1, sticky=W)
        p_age_list.grid(column=0, row=13, sticky=W)
        p_ages_button.grid(column=0, row=17, sticky=W)
        d_type_p_lbl.grid(column=1, row=11, columnspan=1, sticky=W)
        d_type_b_lbl.grid(column=1, row=12, columnspan=1, sticky=W)
        p_illness_list.grid(column=1, row=13, sticky=W)
        p_illness_button.grid(column=1, row=17, sticky=W)

        # Separator for doctors/patients
        Separator(window, orient=HORIZONTAL).grid(column=0, row=19, columnspan=3, sticky='ew')

        """Patient values """
        p_prompt = Label(window, text="Add values to each patient.", font='Helvetica 10 italic')
        p_illness_lbl = Label(window, text="Illness type the patients has.")
        p_illness_combo = Combobox(window, width=5)
        p_illness_combo['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        p_illness_help_lbl = Label(window, text="0-9 indicates sickness type.")
        p_age_lbl = Label(window, text="Age range of the patient.")
        p_age_combo = Combobox(window, width=5)
        p_age_combo["values"] = ("0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70", "71-80", "81-90",
                                 "91-100", "100-110")

        p_prompt.grid(column=0, row=19, columnspan=1, rowspan=3, pady=15, sticky=W)
        p_illness_lbl.grid(column=0, row=24, columnspan=1, sticky=W)
        p_illness_help_lbl.grid(column=0, row=25, columnspan=1, sticky=W)
        p_illness_combo.grid(column=1, row=24, columnspan=1, sticky=W)
        p_age_lbl.grid(column=0, row=26, columnspan=1, sticky=W)
        p_age_combo.grid(column=1, row=26, columnspan=1, sticky=W)

        """Patient values """
        p_d_prompt = Label(window, text="Configure the patients's preferences.", font='Helvetica 10 italic')

        # Configure patient's preference for the age of doctors.
        d_age_list = Listbox(window)
        for e in d_ages:
            d_age_list.insert(0, e)

        p_age_d_lbl = Label(window, text="Age of doctors.")
        p_age_b_lbl = Label(window, text="Click the 'Add' button.")
        d_age_button = Button(window, text="Add age", command=lambda: self.delete_d_age(d_age_list))

        # Configure patient's preference for the gender of doctors.
        d_gender_list = Listbox(window)
        for e in d_genders:
            d_gender_list.insert(0, e)

        p_gender_d_lbl = Label(window, text="Gender of doctors.")
        p_gender_b_lbl = Label(window, text="Click the 'Add' button.")
        d_gender_button = Button(window, text="Add gender", command=lambda: self.delete_d_gender(d_gender_list))

        p_d_prompt.grid(column=0, row=27, columnspan=1, rowspan=1, pady=15, sticky=W)

        # Patient pref for age grids
        p_age_d_lbl.grid(column=0, row=28, sticky=W)
        d_age_list.grid(column=0, row=30, sticky=W)
        p_age_b_lbl.grid(column=0, row=29, sticky=W)
        d_age_button.grid(column=0, row=31, sticky=W)

        # Patient pref for gender grids
        p_gender_d_lbl.grid(column=1, row=28, sticky=W)
        d_gender_list.grid(column=1, row=30, sticky=W)
        p_gender_b_lbl.grid(column=1, row=29, sticky=W)
        d_gender_button.grid(column=1, row=31, sticky=W)

        window.mainloop()


if __name__ == '__main__':
    GUI().application()