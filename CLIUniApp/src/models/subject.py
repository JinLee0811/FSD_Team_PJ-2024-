# src/models/subject.py
class Subject:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.mark = None  # 성적
        self.grade = None  # 등급

    def assign_random_mark(self):
        """랜덤 성적을 생성하고 등급을 할당합니다."""
        from random import randint

        self.mark = randint(25, 100)
        self.grade = "Pass" if self.mark >= 50 else "Fail"
