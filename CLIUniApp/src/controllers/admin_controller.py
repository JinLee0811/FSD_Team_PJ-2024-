# src/controllers/admin_controller.py
from models.database import Database

db = Database()


def clear_database():
    db.clear_all()
    print("Database cleared.")


def group_students():
    students = db.get_all_students()
    grouped_students = {}  # Logic to group students by grade
    print(grouped_students)


def partition_students():
    students = db.get_all_students()
    pass_fail = {}  # Logic to partition students by pass/fail
    print(pass_fail)


def remove_student():
    student_id = input("Enter student ID to remove: ")
    if db.remove_student_by_id(student_id):
        print("Student removed.")
    else:
        print("Student not found.")


def show_students():
    students = db.get_all_students()
    for student in students:
        print(student)
