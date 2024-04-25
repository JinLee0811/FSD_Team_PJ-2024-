import random

from models.database import Database
from models.student import Student
from utils.validator import validate_email, validate_password

db = Database()


def login_student():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    student = db.get_student_by_email(email)
    if student and student.password == password:
        print("Login successful!")
        return student
    else:
        print("Invalid credentials.")
        return None


def register_student():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    if not validate_email(email):
        print("Invalid email format.")
        return None
    password = input("Enter your password: ")
    if not validate_password(password):
        print("Invalid password format.")
        return None
    if db.get_student_by_email(email):
        print("Email already registered.")
        return None

    # 랜덤 학생 ID 생성, 중복 방지 로직 포함
    while True:
        student_id = random.randint(1, 999999)
        student_id_formatted = str(student_id).zfill(6)  # 6자리 숫자로 포맷
        if not db.get_student_by_id(student_id_formatted):
            break  # 생성된 ID가 데이터베이스에 없으면 반복 중지

    student = Student(
        name=name, email=email, password=password, student_id=student_id_formatted
    )
    db.add_student(student)
    print(f"Registration successful. Your student ID is {student_id_formatted}.")
    return student


def change_password(student):
    if student is None:
        print("No student is logged in.")
        return
    new_password = input("Enter new password: ")
    if validate_password(new_password):
        student.password = new_password
        db.update_student(student)
        print("Password updated successfully.")
    else:
        print("Invalid password format.")
