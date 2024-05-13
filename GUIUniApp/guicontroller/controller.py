import os
import sys
import tkinter as tk
from tkinter import messagebox

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Import classes from guiframe.view and guimodel.model modules
from guiframe.view import EnrolmentFrame, LoginFrame
from guimodel.model import GUIUniAppModel


class GUIUniAppController:
    def __init__(self, master):
        self.master = master
        self.model = GUIUniAppModel() # Create an instance of GUIUniAppModel
        self.current_frame = None
        self.show_login_frame() # Show the login frame initially

    def show_login_frame(self):
        self.switch_frame(LoginFrame)  # Switch to the login frame

    def show_enrolment_frame(self):
        self.switch_frame(EnrolmentFrame)  # Switch to the enrolment frame

    def switch_frame(self, frame_class):
        # Destroy the current frame if it exists
        if self.current_frame is not None:
            self.current_frame.destroy()
            
        # Create a new instance of the frame and display it    
        self.current_frame = frame_class(self.master, self)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        self.current_frame.bind("<Button-1>", lambda event: self.current_frame.focus_set())
        self.current_frame.focus_set()

    def authenticate(self, email, password):
        # Attempt authentication with the given email and password
        if self.model.authenticate(email, password):
            messagebox.showinfo("Login Successful", "You have successfully logged in!")
            self.logged_in_user = self.model.logged_in_user
            return True
        else:
            messagebox.showerror("Login Failed", "Incorrect Login credentials")
            return False

    def add_subject(self):
        return self.model.add_subject() # Call the add_subject method in the model

    def remove_subject(self, subject_id):
        return self.model.remove_subject(subject_id)  # Call the remove_subject method in the model

    def logout(self):
        self.model.logout()  # Call the logout method in the model
        self.show_login_frame() # Switch to the login frame after logout
