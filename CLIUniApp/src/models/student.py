# src/models/student.py
class Student:
    def __init__(self, name, email, password, student_id, grade=None, mark=None):
        self.name = name
        self.email = email
        self.password = password
        self.student_id = student_id
        self.grade = grade
        self.mark = mark
        self.subjects = []
        self.average_mark = None  # 평균 점수 추가

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
