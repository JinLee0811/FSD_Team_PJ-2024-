import random


class Subject:
    def __init__(self, id):
        self.id = id
        self.mark = None  # 성적
        self.grade = None  # 등급

    def assign_random_mark(self):
        self.mark = random.randint(25, 100)
        self.grade = self.assign_grade(self.mark)

    @staticmethod
    def assign_grade(mark):
        if mark < 50:
            return "F"  # Fail
        elif mark < 65:
            return "P"  # Pass
        elif mark < 75:
            return "C"  # Credit
        elif mark < 85:
            return "D"  # Distinction
        else:
            return "HD"  # High Distinction

    def calculate_average_marks(subjects):
        # 주어진 과목들의 평균 점수를 계산합니다.
        if not subjects:
            return 0
        total_marks = sum(subject.mark for subject in subjects)
        return total_marks / len(subjects)
