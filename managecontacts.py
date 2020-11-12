from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

class ManageContactsFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.style = Style()

        self.style.configure('TFrame', background = 'white')

        self.pack(fill = BOTH, expand = TRUE)

        self.create_view_all_contacts_frame()

    def create_view_all_contacts_frame(self):
        self.view_all_contacts_frame = Frame(self)
        self.view_all_contacts_frame.place(relx=.5, rely=.5, anchor=CENTER)

        self.style.configure('TButton', font=(NONE, 15), width=20)

        self.add_new_contact_button = Button(self.view_all_contacts_frame, text="Add New Contact",
        command = self.create_add_new_contact_frame )
        self.add_new_contact_button.grid(row=0, column=1, sticky=E, pady=10)

        self.style.configure('TLabel', background='white', font=(NONE, 15))

        self.name_label = Label(self.view_all_contacts_frame, text="Name: ")
        self.name_label.grid(row=1, column=0, pady=10, sticky=W)

        self.name_entry = Entry(self.view_all_contacts_frame, font=(NONE, 15), width=62)
        self.name_entry.grid(row=1, column=1, sticky=W)

        self.style.configure('Treeview.Heading', font=(NONE, 15))
        self.style.configure('Treeview', font=(NONE, 14), rowheight=25)

        self.contacts_treeview = Treeview(self.view_all_contacts_frame,
        columns=('name', 'phone_no', 'email_id', 'city'), show='headings')
        self.contacts_treeview.heading('name', text="Name", anchor=W)
        self.contacts_treeview.heading('phone_no', text="Phone No", anchor=W)
        self.contacts_treeview.heading('email_id', text="Email Id", anchor=W)
        self.contacts_treeview.heading('city', text="City", anchor=W)
        self.contacts_treeview.column('name', width=250)
        self.contacts_treeview.column('phone_no', width=150)
        self.contacts_treeview.column('email_id', width=200)
        self.contacts_treeview.column('city', width=150)
        self.contacts_treeview.grid(row=2, column=0, columnspan=2, pady=10)

    def create_add_new_contact_frame(self):
        self.view_all_contacts_frame.destroy()

        self.add_new_contact_frame = Frame(self)
        self.add_new_contact_frame.place(relx=.5, rely=.5, anchor=CENTER)

        self.style.configure('TLabel', background='white', font=(NONE, 15))

        self.name_label = Label(self.add_new_contact_frame, text="Name: ")
        self.name_label.grid(row=0, column=0, sticky=W)

        self.name_entry = Entry(self.add_new_contact_frame, font=(NONE, 15), width=20)
        self.name_entry.grid(row=0, column=1, pady=10)

        self.phone_no_label = Label(self.add_new_contact_frame, text="Phone No: ")
        self.phone_no_label.grid(row=1, column=0, sticky=W)

        self.phone_no_entry = Entry(self.add_new_contact_frame, font=(NONE, 15), width=20)
        self.phone_no_entry.grid(row=1, column=1, pady=10)

        self.email_id_label = Label(self.add_new_contact_frame, text="Email Id: ")
        self.email_id_label.grid(row=2, column=0, sticky=W)

        self.email_id_entry = Entry(self.add_new_contact_frame, font=(NONE, 15), width=20)
        self.email_id_entry.grid(row=2, column=1, pady=10)

        self.city_label = Label(self.add_new_contact_frame, text="City: ")
        self.city_label.grid(row=3, column=0, sticky=W)

        self.city_combobox = Combobox(self.add_new_contact_frame, font=(NONE, 15), width=20,
        values=('Greater Noida', 'Noida', 'Delhi', 'Gurgaon', 'Mumbai'))
        self.city_combobox.grid(row=3, column=1, pady=10)
        self.city_combobox.current(0)

        self.profile_pic_label = Label(self.add_new_contact_frame, text="Profile Pic: ")
        self.profile_pic_label.grid(row=4, column=0)

        self.style.configure('TButton', font=(NONE, 15), width=20)

        self.profile_pic_button = Button(self.add_new_contact_frame, text="Choose your profile pic",
        command = self.profile_pic_button_click)
        self.profile_pic_button.grid(row=4, column=1)

        self.add_button = Button(self.add_new_contact_frame, text="Add")
        self.add_button.grid(row=5, column=1, pady=10)

    def profile_pic_button_click(self):
        print(filedialog.askopenfilename())