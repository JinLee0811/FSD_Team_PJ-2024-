import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


from colorama import *
from controller.student_controller import *
from controller.subject_controller import *
from models.database import *

init(autoreset=True)

db = Database()


def student_menu():
    current_student = None
    while True:
        print(Fore.BLUE + "\nStudent Menu:")
        if current_student is None:
            print(Fore.BLUE + "(l) Login")
            print(Fore.BLUE + "(r) Register")
            print(Fore.BLUE + "(x) Exit to Main Menu")
        else:
            print(Fore.BLUE + "\nStudent Course Menu")
            print(Fore.BLUE + "(c) Change Password")
            print(Fore.BLUE + "(e) Enrol in Subject")
            print(Fore.BLUE + "(r) Remove Enrolled Subject")
            print(Fore.BLUE + "(s) Show Enrolled Subjects")
            print(Fore.BLUE + "(x) Exit to Main Menu")

        choice = input("Enter your choice: ").lower()

        if choice == "l" and current_student is None:
            print(Fore.GREEN + "\nStudent Sign In")
            current_student = login_student(db)
        elif choice == "r" and current_student is None:
            print(Fore.GREEN + "\nStudent Sign Up")
            register_student(db)
        elif choice == "c" and current_student is not None:
            change_password(current_student, db)
        elif choice == "e" and current_student is not None:
            enroll_subject(current_student, db)
        elif choice == "r" and current_student is not None:
            remove_subject(current_student, db)
        elif choice == "s" and current_student is not None:
            show_enrolled_subjects(current_student)
        elif choice == "x":
            if current_student is not None:
                current_student = None
                print("Logged out successfully.")
            else:
                break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")
