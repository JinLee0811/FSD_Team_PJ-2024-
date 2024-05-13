import random

class Subject:
    def __init__(self, id):
        self.id = id
        self.mark = None
        self.grade = None

    def assign_random_mark(self):
        self.mark = random.randint(25, 100)
        self.grade = self.assign_grade(self.mark)

    @staticmethod
    def assign_grade(mark):
        if mark < 50:
            return "F"
        elif mark < 65:
            return "P"
        elif mark < 75:
            return "C"
        elif mark < 85:
            return "D"
        else:
            return "HD"

    def calculate_average_marks(subjects):
        # 주어진 과목들의 평균 점수를 계산합니다.
        if not subjects:
            return 0
        total_marks = sum(subject.mark for subject in subjects)
        return total_marks / len(subjects)

    def __getstate__(self):
        state = self.__dict__.copy()
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
