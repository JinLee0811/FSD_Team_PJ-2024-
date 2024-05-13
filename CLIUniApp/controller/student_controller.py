import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import random

from colorama import *
from models.database import *
from models.student import *
from utils.validator import *

init(autoreset=True)

db = Database()


def login_student(db):
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    student = db.get_student_by_email(email)
    if student and student.password == password:
        print(Fore.YELLOW + "Login successful!")
        return student
    elif student is None:
        print(Fore.RED + "Student does not exist.")
        return None
    else:
        print(Fore.RED + "Incorrect email or password.")
        return None


def register_student(db):
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    email_valid = validate_email(email)
    password_valid = validate_password(password)
    if not (email_valid and password_valid):
        print(Fore.RED + "Incorrect email or password format.")
        return None
    if db.get_student_by_email(email):
        print(Fore.BLUE + f"Student {email} already exists")
        return None
    print(Fore.YELLOW + "Email and password formats acceptable")
    name = input("Enter your name: ")
    student_id = random.randint(100000, 999999)
    new_student = Student(name, email, password, str(student_id))
    db.add_student(new_student)
    db.update_student(new_student)
    print(Fore.YELLOW + f"Enrolling Student {new_student.name}.")
    return new_student


def change_password(student, db):
    if student is None:
        print("No student is logged in.")
        return
    print(Fore.YELLOW + "Updating Password")
    new_password = input("New password: ")
    confirm_password = input("Confirm password: ")
    if new_password != confirm_password:
        print(Fore.RED + "Passwords do not match - try again")
        return
    if validate_password(new_password):
        student.password = new_password
        db.update_student(student)
        print(Fore.YELLOW + "Password updated successfully.")
    else:
        print(Fore.RED + "Invalid password format.")
