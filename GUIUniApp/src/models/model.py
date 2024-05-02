import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from models.database import Database, Student

class GUIUniAppModel:
    def __init__(self):
        self.database = Database()
        self.logged_in_user = None

    def authenticate(self, email, password):
        student = self.database.get_student_by_email(email)
        if student and student.password == password:
            self.logged_in_user = student
            return True
        return False

    def register_student(self, email, password, name, student_id):
        if not self.database.get_student_by_email(email) and not self.database.get_student_by_id(student_id):
            new_student = Student(email, password, name, student_id)
            self.database.add_student(new_student)
            return True, "Registration successful."
        return False, "Email or student ID already registered."

    def get_subjects(self):
        if self.logged_in_user:
            return self.logged_in_user.subjects
        return []

    def add_subject(self, subject):
        if self.logged_in_user:
            self.logged_in_user.subjects.append(subject)
            self.database.update_student(self.logged_in_user)
            return True
        return False

    def remove_subject(self, subject):
        if self.logged_in_user:
            self.logged_in_user.subjects.remove(subject)
            self.database.update_student(self.logged_in_user)
            return True
        return False