# src/controllers/admin_controller.py
from models.database import Database
from models.subject import Subject  # Make sure to import the Subject class

db = Database()


def clear_database(db):
    confirmation = input(
        "Are you sure you want to clear the database? This cannot be undone. Type 'yes' to confirm: "
    )
    if confirmation.lower() == "yes":
        db.clear_all()
        print("Database cleared.")
    else:
        print("Database clear cancelled.")


def group_students(db):
    students = db.get_all_students()
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


def remove_student(db):
    # 입력 받은 학생 ID에서 공백을 제거
    student_id = input("Enter student ID to remove: ").strip()
    removed = db.remove_student_by_id(student_id)
    if removed:
        print("Student removed.")
    else:
        print("Student not found.")


def show_students(db):
    students = db.get_all_students()
    if not students:
        print("No students to display.")
        return

    print("List of All Students:")
    for student in students:
        print(f"Name: {student.name}, ID: {student.student_id}, Email: {student.email}")
