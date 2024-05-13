import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


from colorama import Fore, init
from models.database import *
from models.subject import *

init(autoreset=True)
db = Database()


def clear_database(db):
    print(Fore.YELLOW + "Clearing Students Database.")
    confirmation = input(
        Fore.RED + "Are you sure you want to clear the database? (Y)ES or (N)O: "
    )
    if confirmation.lower() in ["yes", "y"]:
        db.clear_all()
        print(Fore.YELLOW + "Student Database cleared.")
    else:
        print("Database clear cancelled.")


def calculate_grade(average_mark):
    if average_mark >= 85:
        return "HD"
    elif average_mark >= 75:
        return "D"
    elif average_mark >= 65:
        return "C"
    elif average_mark >= 50:
        return "P"
    else:
        return "F"


def group_students(db):
    students = db.get_all_students()
    print(Fore.YELLOW + "Grade Grouping.")
    if not students:
        print("<nothing to display>")
        return

    grouped_students = {"HD": [], "D": [], "C": [], "P": [], "F": []}
    for student in students:
        average_mark = round(Subject.calculate_average_marks(student.subjects), 2)
        grade = calculate_grade(average_mark)
        student.average_mark = average_mark
        grouped_students[grade].append(student)

    # 모든 등급 그룹에 대해 결과 출력
    for grade, students in grouped_students.items():
        if students:  # 등급 그룹에 학생이 있는 경우에만 출력
            output = f"{grade} --> ["
            output += ", ".join(
                f"{student.name} :: {student.student_id} --> GRADE: {grade} - MARK: {student.average_mark}"
                for student in students
            )
            output += "]"
            print(output)


def partition_students(db):
    students = db.get_all_students()
    print(Fore.YELLOW + "PASS/FAIL Partition.")
    if not students:
        print("< Nothing to Display >")
        return

    pass_students = []
    fail_students = []
    for student in students:
        average_mark = Subject.calculate_average_marks(student.subjects)
        grade = calculate_grade(average_mark)
        student.average_mark = round(
            average_mark, 2
        )  # 평균 점수 소수점 둘째 자리까지 반올림
        student.grade = grade  # 학생 객체에 등급 추가

        if grade in ["HD", "D", "C", "P"]:
            pass_students.append(student)
        else:
            fail_students.append(student)

    # 출력 구문
    if pass_students:
        pass_output = "PASS --> ["
        pass_output += ", ".join(
            f"{student.name} :: {student.student_id} --> GRADE: {student.grade} - MARK: {student.average_mark}"
            for student in pass_students
        )
        pass_output += "]"
        print(pass_output)
    else:
        print("PASS --> []")

    if fail_students:
        fail_output = "FAIL --> ["
        fail_output += ", ".join(
            f"{student.name} :: {student.student_id} --> GRADE: {student.grade} - MARK: {student.average_mark}"
            for student in fail_students
        )
        fail_output += "]"
        print(fail_output)
    else:
        print("FAIL --> []")


def remove_student(db):
    # 입력 받은 학생 ID에서 공백을 제거
    student_id = input("Remove by Students ID: ").strip()
    removed = db.remove_student_by_id(student_id)
    if removed:
        print(Fore.YELLOW + f"Removing Student {student_id} Account.")
    else:
        print(Fore.RED + f"Student {student_id} does not exist.")


def show_students(db):
    students = db.get_all_students()
    print(Fore.YELLOW + "Student List")
    if not students:
        print("< Nothing to Display >")
        return

    for student in students:
        print(f"{student.name} :: {student.student_id} --> Email: {student.email}")
