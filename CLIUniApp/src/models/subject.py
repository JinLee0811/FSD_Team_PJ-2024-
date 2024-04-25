class Subject:
    def __init__(self, id, name, student_id):
        self.id = id
        self.name = name
        self.mark = None  # 성적
        self.grade = None  # 등급
        self.student_id = student_id

    def assign_random_mark(self):
        """랜덤 성적을 생성하고 등급을 할당합니다."""
        from random import randint

        self.mark = randint(25, 100)
        self.grade = self.assign_grade(self.mark)

    def assign_grade(self, mark):
        """점수에 따라 등급을 할당합니다."""
        if mark < 50:
            return "F"  # Fail
        elif mark < 65:
            return "P"  # Pass
        elif mark < 75:
            return "CR"  # Credit
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
