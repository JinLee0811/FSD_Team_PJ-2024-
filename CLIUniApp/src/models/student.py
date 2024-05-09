from models.subject import Subject


class Student:
    def __init__(self, name, email, password, student_id, grade=None, mark=None):
        self.name = name
        self.email = email
        self.password = password
        self.student_id = student_id
        self.grade = grade
        self.mark = mark
        self.subjects = []
        self.average_mark = None
