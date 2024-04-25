import pickle


class Database:
    def __init__(self):
        self.filename = "data/students.data"
        self.students = self.load_students()

    def load_students(self):
        try:
            with open(self.filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError):
            return []

    def save_students(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self.students, f)

    def get_student_by_email(self, email):
        return next(
            (student for student in self.students if student.email == email), None
        )

    def get_student_by_id(self, student_id):
        return next(
            (student for student in self.students if student.student_id == student_id),
            None,
        )

    def add_student(self, student):
        if not self.get_student_by_email(student.email) and not self.get_student_by_id(
            student.student_id
        ):
            self.students.append(student)
            self.save_students()
        else:
            print("Student with this email or ID already exists.")

    def update_student(self, student):
        found = False
        for idx, s in enumerate(self.students):
            if s.student_id == student.student_id:  # 학생 ID로 업데이트
                self.students[idx] = student
                found = True
                break
        if found:
            self.save_students()
        else:
            print("Student not found.")

    def remove_student_by_id(self, student_id):
        original_len = len(self.students)
        self.students = [s for s in self.students if s.student_id != student_id]
        if len(self.students) < original_len:
            self.save_students()

    def get_all_students(self):
        return self.students

    def clear_all(self):
        self.students = []
        self.save_students()

    def remove_student_by_email(self, email):
        original_len = len(self.students)
        self.students = [s for s in self.students if s.email != email]
        if len(self.students) < original_len:
            self.save_students()
