# src/models/student.py
class Student:
    def __init__(self, name, email, password, student_id):
        self.name = name
        self.email = email
        self.password = password
        self.student_id = student_id
        self.subjects = []

    def enroll_subject(self, subject):
        if len(self.subjects) < 4:
            self.subjects.append(subject)
            return True
        return False

    def drop_subject(self, subject_id):
        for subject in self.subjects:
            if subject.id == subject_id:
                self.subjects.remove(subject)
                return True
        return False
