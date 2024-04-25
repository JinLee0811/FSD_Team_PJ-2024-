# src/controllers/admin_controller.py
from models.database import Database
from models.subject import Subject  # Make sure to import the Subject class

db = Database()


def clear_database():
    confirmation = input(
        "Are you sure you want to clear the database? This cannot be undone. Type 'yes' to confirm: "
    )
    if confirmation.lower() == "yes":
        db.clear_all()
        print("Database cleared.")
    else:
        print("Database clear cancelled.")


def group_students():
    students = db.get_all_students()
    if not students:
        print("<nothing to display>")
        return

    # 평균 점수에 따라 학생들을 그룹화
    grouped_students = {"A": [], "B": [], "C": [], "D": [], "F": []}
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

        # 그룹화된 학생들 출력
        print(f"Group {grade}:")
        print(f"- {student.name}, Average Mark: {average_mark}")


def partition_students():
    students = db.get_all_students()
    if not students:
        print("<nothing to display>")
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
        print("Pass Students:")
        for student in pass_students:
            average_mark = Subject.calculate_average_marks(student.subjects)
            print(f"- {student.name}, Average Mark: {average_mark}")
    else:
        print("No pass students.")

    if fail_students:
        print("Fail Students:")
        for student in fail_students:
            average_mark = Subject.calculate_average_marks(student.subjects)
            print(f"- {student.name}, Average Mark: {average_mark}")
    else:
        print("No fail students.")


def remove_student():
    student_id = input("Enter student ID to remove: ")
    removed = db.remove_student_by_id(student_id)
    if removed:
        print("Student removed.")
    else:
        print("Student not found.")


def show_students():
    students = db.get_all_students()
    if not students:
        print("<nothing to display>")
        return

    for student in students:
        # Assuming Student object has these attributes for simplicity
        print(f"Name: {student.name}, ID: {student.student_id}, Email: {student.email}")
