import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

current_dir = os.path.dirname(os.path.abspath(__file__))
black_logo_path = os.path.join(current_dir, "uts_b_logo.jpeg")
white_logo_path = os.path.join(current_dir, "uts_w_logo.png")

class LoadingScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="black")
        self.master = master
        self.create_widgets()

    def create_widgets(self):

        logo_path = black_logo_path
        logo_image = Image.open(logo_path)
        logo_image = logo_image.resize((180, 180), Image.Resampling.LANCZOS)
        logo_img = ImageTk.PhotoImage(logo_image)
        self.logo_label = tk.Label(self, image=logo_img, bg="black", anchor="center")
        self.logo_label.image = logo_img
        self.logo_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label = tk.Label(
            self,
            text="Welcome to GUIUniApp",
            fg="#ffffff",
            font="Arial 26 bold",
            bg="black",
        )
        label.place(relx=0.5, rely=0.3, anchor="n")


class LoginFrame(tk.Frame):

    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        self.pack(expand=True)

    def create_widgets(self):
       
        # Logo image
        logo_path = white_logo_path
        logo_image = Image.open(logo_path)
        logo_image = logo_image.resize((50, 50), Image.Resampling.LANCZOS)  
        logo_img = ImageTk.PhotoImage(logo_image)

        # Create main frame
        main_frame = tk.Frame(self, bg="white")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Label_Login page
        self.logo_label = tk.Label(
            main_frame,
            text="Student Portal",
            image=logo_img,
            compound=tk.LEFT,
            padx=10,
            fg="#000000",
            font="Arial 26 bold",
            bg="white",
        )
        self.logo_label.image = logo_img
        self.logo_label.pack(pady=(80, 20))

        # Login_fraime box
        login_box = tk.Frame(main_frame, bg="white", padx=20, pady=20)
        login_box.place(relx=0.5, rely=0.3, anchor=tk.N)

        # Label_email,password
        self.email_label = tk.Label(
            login_box,
            text="Email:",
            justify="left",
            fg="#000000",
            font="Arial 14 bold",
            bg="white",
        )
        self.password_label = tk.Label(
            login_box,
            text="Password:",
            justify="left",
            fg="#000000",
            font="Arial 14 bold",
            bg="white",
        )
        self.email_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
        self.password_label.grid(row=2, column=0, sticky=tk.W, pady=(20, 10))

        # entry_email,password
        emailText = tk.StringVar()
        self.email_entry = tk.Entry(
            login_box,
            width=30,
            textvariable=emailText,
            font="Arial 14 bold",
            relief=tk.GROOVE,
            highlightthickness=2,
            highlightbackground="gray",
        )
        passwordTxt = tk.StringVar()
        self.password_entry = tk.Entry(
            login_box,
            width=30,
            textvariable=passwordTxt,
            font="Arial 14 bold",
            show="*",
            relief=tk.GROOVE,
            highlightthickness=2,
            highlightbackground="gray",
        )
        self.email_entry.grid(row=1, column=0, padx=5, pady=(0, 5))
        self.email_entry.focus()
        self.password_entry.grid(row=3, column=0, padx=5, pady=(0, 30))
        self.password_entry.focus()

        # button_login
        self.lg_button = tk.Button(main_frame, 
                              text="Login", 
                              font="Arial 14 bold", 
                              width=15, 
                              height=2, 
                              relief=tk.GROOVE, 
                              borderwidth=5,
                              highlightbackground='#ffffff',
                              bg="#000000", 
                              fg="#FF0080",
                              command=self.login)
        self.lg_button.place(x=110, y=380)

    # Login method
    def login(self):
        print("Login method entered")

        email = self.email_entry.get()
        password = self.password_entry.get()

        print(email)
        print(password)

        if self.controller.authenticate(email, password) == True:
            print("Authentication successful")
            self.controller.show_enrolment_frame()
        else:
            print("Authentication failed - showing message")
            self.email_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)

        print("Login method exited")


class EnrolmentFrame(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        self.pack(expand=True)
        
    def create_widgets(self):
        
         # Logo image
        logo_path = white_logo_path
        logo_image = Image.open(logo_path)
        logo_image = logo_image.resize((50, 50), Image.Resampling.LANCZOS)  
        logo_img = ImageTk.PhotoImage(logo_image)

        # Create main frame
        main_frame = tk.Frame(self, bg='white')
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Label_Enrolment page
        self.logo_label = tk.Label(main_frame, text="Enrolment Subject", image=logo_img, compound=tk.LEFT, padx=10, fg='#000000', font="Arial 26 bold", bg='white')
        self.logo_label.image = logo_img
        self.logo_label.pack(pady=(80, 50))
        
        # Student Info
        student = self.controller.model.logged_in_user
        student_info = f"Student: {student.name}_{student.student_id}"
        self.info_label = tk.Label(main_frame, text=student_info, bg='white', font="Arial 14 bold")
        self.info_label.pack(anchor=tk.W, padx=20)

        # Subjects Listbox
        self.subjects_listbox = tk.Listbox(main_frame, width=50, height=10)
        self.subjects_listbox.pack(padx=20, pady=20, ipadx=5)
        self.subjects_listbox.insert(tk.END, " No enrolled subjects")

        # button_enrol
        self.enrol_button = tk.Button(main_frame, 
                              text="Enrol Subject", 
                              font="Arial 12 bold", 
                              relief=tk.GROOVE, 
                              width=15, 
                              height=2, 
                              highlightbackground='#ffffff',
                              bg="#9eada2", 
                              fg="#000000",
                              command=self.enrol_subject)
        self.enrol_button.pack(side=tk.LEFT, padx=(20, 5), anchor=tk.NW)

        # button_delete
        self.delete_button = tk.Button(main_frame, 
                              text="Delete Subject", 
                              font="Arial 12 bold", 
                              relief=tk.GROOVE, 
                              width=15, 
                              height=2, 
                              highlightbackground='#ffffff',
                              bg="#9eada2", 
                              fg="#000000",
                              command=self.delete_subject)
        self.delete_button.pack(side=tk.RIGHT, padx=(5, 20), anchor=tk.NE)

        # button_logout
        self.logout_button = tk.Button(main_frame, 
                              text="Logout", 
                              font="Arial 12 bold", 
                              relief=tk.GROOVE, 
                              bg="#9eada2", 
                              fg="#FF0080",
                              highlightbackground='#ffffff',    
                              command=self.logout)
        self.logout_button.place(x=280, y=560)
        self.update_subjects_list()  

    # Enrol Subject method
    def enrol_subject(self):
        result = self.controller.add_subject()
        if result:
            self.update_subjects_list()
            messagebox.showinfo("Enrolment Success", "Subject enrolled successfully")
        else:
            messagebox.showinfo(
                "Enrolment Failed", "Only 4 subjects can be enrolled"
            )

    # Update Subject list method
    def update_subjects_list(self):
        self.subjects_listbox.delete(0, tk.END)
        student = self.controller.model.logged_in_user
        if student.subjects:  # 학생의 과목 리스트가 비어있지 않은 경우
            for subject in student.subjects:
                self.subjects_listbox.insert(
                    tk.END,
                    f" Subject::{subject.id} -- Mark = {subject.mark} -- Grade = {subject.grade}",
                )
        else:  # 학생의 과목 리스트가 비어있는 경우
            self.subjects_listbox.insert(tk.END, " No enrolled subjects")

    # Delete Subject method
    def delete_subject(self):
        if not self.subjects_listbox.curselection():
            return

        selected_index = self.subjects_listbox.curselection()[0]
        selected_subject = self.subjects_listbox.get(selected_index)
        subject_id = selected_subject.split(" -- ")[0].split("::")[1]

        confirm = messagebox.askyesno(
            "Confirmation", "Are you sure you want to delete this subject?"
        )
        if confirm:
            result = self.controller.remove_subject(subject_id)
            if result:
                self.subjects_listbox.delete(selected_index)
                self.update_subjects_list()
                messagebox.showinfo("Deletion", "Subject removed successfully")
            else:
                messagebox.showinfo("Deletion", "Failed to remove subject")

    # Logout method
    def logout(self):
        confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if confirm:
            self.controller.logout()
