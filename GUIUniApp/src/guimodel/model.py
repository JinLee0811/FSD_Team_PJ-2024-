import os
import random
import sys

# rootDir 설정
currentPath = os.getcwd()
rootDir = currentPath.replace("GUIUniApp", "")
modelsPath = os.path.join(rootDir, "CLIUniApp/src/models/")
sys.path.append(modelsPath)

import database
import subject

db = database.Database()


class GUIUniAppModel:

    def __init__(self):
        self.logged_in_user = None
        self.database = db
        self.subject = subject.Subject

    # 로그인 인증
    def authenticate(self, email, password):
        student = self.database.get_student_by_email(email)
        if student and student.password == password:
            self.logged_in_user = student
            return True
        return False

    def enroll_subject(self, student):
        if len(student.subjects) >= 4:
            return False

        subject_ids = {s.id for s in student.subjects}
        new_id = random.choice(
            [
                str(i).zfill(3)
                for i in range(1, 1000)
                if str(i).zfill(3) not in subject_ids
            ]
        )

        new_subject = self.subject(new_id)
        new_subject.assign_random_mark()
        student.subjects.append(new_subject)
        self.database.update_student(self.logged_in_user)

        print(f"Enrolling in Subject - {new_id}")
        print(f"You are now enrolled in {len(student.subjects)} out of 4 subjects.")

        print(f"Showing {len(student.subjects)} subjects.")
        for subject in student.subjects:
            print(
                f"[ Subject::{subject.id} -- Mark = {subject.mark} -- Grade = {subject.grade} ]"
            )

        return True

    def add_subject(self, subject):
        if self.logged_in_user:
            if self.enroll_subject(self.logged_in_user):
                self.database.update_student(self.logged_in_user)
                return True
        return False

    def remove_subject(self, subject_id):
        if self.logged_in_user:
            subject_to_remove = next(
                (s for s in self.logged_in_user.subjects if s.id == subject_id), None
            )
            if subject_to_remove:
                self.logged_in_user.subjects.remove(subject_to_remove)
                self.database.update_student(self.logged_in_user)
                return True
        return False

    def logout(self):
        self.logged_in_user = None
