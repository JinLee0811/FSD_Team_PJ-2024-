# src/controllers/student_controller.py
from models.student import Student
from models.database import Database
from utils.validator import validate_email, validate_password

db = Database()

def login_student():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    student = db.get_student_by_email(email)
    if student and student.password == password:
        print("Login successful!")
    else:
        print("Invalid credentials.")

def register_student():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    if not validate_email(email):
        print("Invalid email format.")
        return
    password = input("Enter your password: ")
    if not validate_password(password):
        print("Invalid password format.")
        return
    if db.get_student_by_email(email):
        print("Email already registered.")
        return
    student = Student(name=name, email=email, password=password)
    db.add_student(student)
    print("Registration successful.")

def change_password():
    email = input("Enter your email: ")
    student = db.get_student_by_email(email)
    if student:
        new_password = input("Enter new password: ")
        if validate_password(new_password):
            student.password = new_password
            db.update_student(student)
            print("Password updated successfully.")
        else:
            print("Invalid password format.")
    else:
        print("Student not found.")

def enroll_subject():
    # Implement subject enrollment logic
    pass

def remove_subject():
    # Implement subject removal logic
    pass

def show_enrolled_subjects():
    # Implement logic to display enrolled subjects
    pass
