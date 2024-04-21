# src/models/subject.py
class Subject:
    def __init__(self, name):
        self.name = name
        self.id = self.generate_subject_id()
        self.mark = None
        self.grade = None

    def generate_subject_id(self):
        # ID 생성 로직 (가정)
        from random import randint

        return f"{randint(100, 999):03}"
