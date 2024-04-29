import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from colorama import Back, Fore, Style, init
from models.database import Database
from models.subject import Subject  # Make sure to import the Subject class

init(autoreset=True)
db = Database()


def clear_database(db):
    print(Fore.YELLOW + "Clearing Students Database.")
    confirmation = input(
        Fore.RED + "Are you sure you want to clear the database? (Y)ES or (N)O: "
    )
    if confirmation.lower() == "yes":
        db.clear_all()
        print(Fore.YELLOW + "Student Database cleared.")
    else:
        print("Database clear cancelled.")


def group_students(db):
    students = db.get_all_students()
    print(Fore.YELLOW + "Grade Grouping.")
    if not students:
        print("<nothing to display>")
        return

    # 평균 점수에 따라 학생들을 그룹화
    grouped_students = {"HD": [], "D": [], "C": [], "P": [], "F": []}
    for student in students:
        average_mark = Subject.calculate_average_marks(student.subjects)
        if average_mark >= 85:
            grade = "HD"
        elif average_mark >= 75:
            grade = "D"
        elif average_mark >= 65:
            grade = "C"
        elif average_mark >= 50:
            grade = "P"
        else:
            grade = "F"

        # 각 학생 객체에 평균 점수 저장
        student.average_mark = average_mark

        # 해당 학점 그룹에 학생 추가
        grouped_students[grade].append(student)

    # 그룹화된 학생들을 그룹 별로 한 번에 출력
    for grade, students in grouped_students.items():
        if students:  # 학생이 있는 그룹만 출력
            print(f"Group {grade}:")
            for student in students:
                print(f"- {student.name}, Average Mark: {student.average_mark}")


def partition_students(db):
    students = db.get_all_students()
    print(Fore.YELLOW + "PASS/FAIL Partition.")
    if not students:
        print("< Nothing to Display >")
        return

    # Pass/Fail로 구분
    pass_students = [
        student
        for student in students
        if Subject.calculate_average_marks(student.subjects) >= 50
    ]
    fail_students = [
        student
        for student in students
        if Subject.calculate_average_marks(student.subjects) < 50
    ]

    # Pass/Fail로 출력
    if pass_students:
        print("PASS Students:")
        for student in pass_students:
            average_mark = Subject.calculate_average_marks(student.subjects)
            print(f"- {student.name}, Average Mark: {average_mark}")
    else:
        print("No pass students.")

    if fail_students:
        print("FAIL Students:")
        for student in fail_students:
            average_mark = Subject.calculate_average_marks(student.subjects)
            print(f"- {student.name}, Average Mark: {average_mark}")
    else:
        print("No fail students.")


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
