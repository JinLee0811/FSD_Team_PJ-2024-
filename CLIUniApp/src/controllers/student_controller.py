import random

from models.database import Database
from models.student import Student
from utils.validator import validate_email, validate_password

db = Database()


def login_student(db):
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    student = db.get_student_by_email(email)
    if student and student.password == password:
        print("Login successful!")
        return student
    else:
        print("Invalid credentials.")
        return None


def register_student(db):
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    if not validate_email(email):
        print("Invalid email format.")
        return None
    password = input("Enter your password: ")
    if not validate_password(password):
        print("Invalid password format.")
        return None
    student_id = random.randint(100000, 999999)
    new_student = Student(name, email, password, str(student_id))
    db.add_student(new_student)
    print(f"Registration successful. Your student ID is {new_student.student_id}.")
    return new_student


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
