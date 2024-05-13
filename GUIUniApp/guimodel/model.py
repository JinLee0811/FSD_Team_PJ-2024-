import os
import random
import sys

# Set the root directory
currentPath = os.getcwd()
rootDir = currentPath.replace("GUIUniApp", "")
modelsPath = os.path.join(rootDir, "CLIUniApp/")
sys.path.append(modelsPath)
print("Check root directory")
print(modelsPath)


# Import classes from CLIUniApp (models.database, models.student, and models.subject)
from models.database import *
from models.student import *
from models.subject import *

db = Database()


class GUIUniAppModel:

    def __init__(self):
        self.logged_in_user = None
        self.database = db
        self.subject = Subject

    def authenticate(self, email, password):
        # Get the student with the provided email from the database
        student = self.database.get_student_by_email(email)
        # Check if the student exists and the password is correct
        if student and student.password == password:
            self.logged_in_user = student
            return True
        return False

    def enroll_subject(self, student):
        # Check if the student exists and the password is correct
        if len(student.subjects) >= 4:
            return False
        
        # Generate a unique subject ID
        subject_ids = {s.id for s in student.subjects}
        new_id = random.choice(
            [
                str(i).zfill(3)
                for i in range(1, 1000)
                if str(i).zfill(3) not in subject_ids
            ]
        )

        # Create a new subject instance with the generated ID
        new_subject = self.subject(new_id)
        new_subject.assign_random_mark()
        student.subjects.append(new_subject)
        
        # Print for debugging
        print(f"new subject{new_subject}")
        print(f"Enrolling in Subject - {new_id}")
        print(f"You are now enrolled in {len(student.subjects)} out of 4 subjects.")
        return True

    def add_subject(self):
        if self.logged_in_user:
            if self.enroll_subject(self.logged_in_user):
                self.database.update_student(self.logged_in_user)
                return True
        return False

    def remove_subject(self, subject_id):
        # Check if a user is logged in
        if self.logged_in_user:
            # Find the subject to remove from the student's list of subjects
            subject_to_remove = next((s for s in self.logged_in_user.subjects if s.id == subject_id), None)
            if subject_to_remove:
                self.logged_in_user.subjects.remove(subject_to_remove)
                self.database.update_student(self.logged_in_user)
                return True
        return False

    def logout(self):
        # Set the logged-in user to None
        self.logged_in_user = None
