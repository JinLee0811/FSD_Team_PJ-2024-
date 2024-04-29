import random

from colorama import Back, Fore, Style, init

init(autoreset=True)


class Subject:
    def __init__(self, id):
        self.id = id
        self.mark = None  # 성적
        self.grade = None  # 등급

    def assign_random_mark(self):
        """랜덤 성적을 생성하고 등급을 할당합니다."""
        self.mark = random.randint(25, 100)
        self.grade = self.assign_grade(self.mark)

    @staticmethod
    def assign_grade(mark):
        """점수에 따라 등급을 할당합니다."""
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


def enroll_subject(student, db):
    if len(student.subjects) >= 4:
        print(Fore.RED + "Students are allowed to enrol in 4 subjects only")
        return

    while True:
        # 랜덤 과목 ID 생성 (1 ~ 999 사이의 숫자를 문자열로 변환)
        subject_id = str(random.randint(1, 999)).zfill(3)  # 항상 3자리를 유지

        # 이미 등록된 과목 ID와 중복되는지 확인
        if not any(s.id == subject_id for s in student.subjects):
            break  # 중복되지 않는 ID 발견 시 while 루프 탈출

    # 과목 객체 생성 및 랜덤 성적 할당
    new_subject = Subject(subject_id)
    new_subject.assign_random_mark()

    # 학생의 과목 목록에 과목 객체 추가
    student.subjects.append(new_subject)

    # 데이터베이스에 학생 정보 업데이트
    db.update_student(student)
    print(Fore.YELLOW + f"Enrolling in Subject - {subject_id}")
    print(
        Fore.YELLOW
        + f"You are now enrolled in {len(student.subjects)} out of 4 subjects."
    )


def remove_subject(student, db):
    if student is None:
        print("No student is logged in.")
        return
    subject_id = input("Remove subject by ID:")
    original_length = len(student.subjects)
    student.subjects = [
        subject for subject in student.subjects if subject.id != subject_id
    ]
    if len(student.subjects) < original_length:
        db.update_student(student)  # 데이터베이스 업데이트
        print(Fore.YELLOW + f"Droping Subject - {subject_id}")
        print(
            Fore.YELLOW
            + f"You are now enrolled in {len(student.subjects)} out of 4 subjects."
        )
    else:
        print("Subject not found in your enrolled list.")


def show_enrolled_subjects(student):
    if student is None:
        print("No student is logged in.")
        return
    if not student.subjects:
        print(Fore.YELLOW + f"Showing 0 subjects")
        return

    print(Fore.YELLOW + f"Showing {len(student.subjects)} subjects.")
    for subject in student.subjects:
        print(
            f"[ Subject::{subject.id} -- Mark = {subject.mark} -- grade = {subject.grade} ]"
        )
