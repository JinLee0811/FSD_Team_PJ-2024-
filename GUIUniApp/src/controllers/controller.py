import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import tkinter as tk
from tkinter import messagebox

from guimodel.model import GUIUniAppModel
from views.view import LoginFrame, EnrolmentFrame, RegistrationFrame

class GUIUniAppController:
    def __init__(self, master):
        self.master = master
        self.model = GUIUniAppModel()
        self.current_frame = None
        self.show_login_frame()

    def show_login_frame(self):
        self.switch_frame(LoginFrame)

    def show_enrolment_frame(self):
        self.switch_frame(EnrolmentFrame)

    # def show_registration_frame(self):
    #     self.switch_frame(RegistrationFrame)

    def switch_frame(self, frame_class):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self.master, self)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        self.current_frame.bind('<Button-1>', lambda event: self.current_frame.focus_set())
        self.current_frame.focus_set()
        
    def authenticate(self, email, password):
        if self.model.authenticate(email, password):
            messagebox.showinfo("Login Successful", "You have successfully logged in!")
            # logger.info("GUIUniAppController initialized")
            self.show_enrolment_frame()
        else:
            messagebox.showerror("Login Failed", "Incorrect credentials")

    # def register(self, email, password, name, student_id):
    #     success, message = self.model.register_student(email, password, name, student_id)
    #     if success:
    #         messagebox.showinfo("Registration Successful", message)
    #         self.show_login_frame()
    #     else:
    #         messagebox.showerror("Registration Failed", message)
    #     return success, message