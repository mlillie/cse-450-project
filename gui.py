from tkinter import *
from tkinter.ttk import *

p_ages_ordered = ""
d_ages_ordered = ""
d_genders_ordered = ""
p_types_ordered = ""
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
            l.delete(selection[0])
            # Delete from list that provided it
            value = eval(l.get(selection[0]))
            ind = p_ages.index(value)
            del (p_ages[ind])
            p_ages_ordered += ind.ToString()


    def application(self):
        global p_ages
        global p_ages_ordered
        window = Tk()

        window.geometry('700x600')
        scroll = Scrollbar(window, orient='vertical')
        scroll.grid(column=10, rowspan=30, sticky=N + S)

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

        p_age_list = Listbox(window)
        for e in p_ages:
            p_age_list.insert(0, e)

        d_type_p_lbl = Label(window, text="Type of illness.")
        d_type_b_lbl = Label(window, text="Click the 'Add' button.")

        p_age_list = Listbox(window)
        for e in p_ages:
            p_age_list.insert(0, e)

        p_ages_button = Button(window, text="Add age", command=self.delete_p_age(p_age_list))

        d_p_prompt.grid(column=0, row=10, columnspan=1, rowspan=1, pady=15, sticky=W)
        d_age_p_lbl.grid(column=0, row=11, columnspan=1, sticky=W)
        d_age_b_lbl.grid(column=0, row=12, columnspan=1, sticky=W)
        p_age_list.grid(column=0, row=13, sticky=W)
        p_ages_button.grid(column=0, row=17, sticky=W)
        d_type_p_lbl.grid(column=0, row=18, columnspan=1, sticky=W)
        d_type_b_lbl.grid(column=0, row=19, columnspan=1, sticky=W)

        """Patient values""
        p_prompt = Label(window, text="Add values to each patient.", font='Helvetica 10 italic')
        p_gender_lbl = Label(window, text="Illness type the patients has.")
        p_gender_combo = Combobox(window, width=5)
        p_gender_combo['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        p_age_lbl = Label(window, text="Age range of the patient.")
        p_age_combo = Combobox(window, width=5)
        p_age_combo["values"] = ("0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70", "71-80", "81-90",
                                 "91-100", "100-110")

        p_prompt.grid(column=0, row=11, sticky=W, pady=15)
        p_gender_lbl.grid(column=0, row=13, sticky=W)
        p_gender_combo.grid(column=1, row=13, sticky=W)
        p_age_lbl.grid(column=0, row=15, sticky=W)
        p_age_combo.grid(column=1, row=15, columnspan=2, sticky=E)"""

        window.mainloop()


if __name__ == '__main__':
    GUI().application()
