# src/models/database.py
import pickle


class Database:
    def __init__(self):
        self.filename = "data/students.data"
        self.students = self.load_students()

    def load_students(self):
        try:
            with open(self.filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return []

    def save_students(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self.students, f)

    def get_student_by_email(self, email):
        return next(
            (student for student in self.students if student.email == email), None
        )

    def add_student(self, student):
        if not self.get_student_by_email(student.email):
            self.students.append(student)
            self.save_students()

    def update_student(self, student):
        for idx, s in enumerate(self.students):
            if s.email == student.email:
                self.students[idx] = student
                self.save_students()
                break

    def remove_student_by_id(self, student_id):
        original_len = len(self.students)
        self.students = [s for s in self.students if s.id != student_id]
        if len(self.students) < original_len:
            self.save_students()

    def get_all_students(self):
        return self.students

    def clear_all(self):
        self.students = []
        self.save_students()
