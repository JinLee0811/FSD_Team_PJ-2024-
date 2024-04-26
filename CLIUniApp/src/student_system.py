# src/student_system.py
from controllers.student_controller import (
    change_password,
    login_student,
    register_student,
)
from controllers.subject_controller import (
    enroll_subject,
    remove_subject,
    show_enrolled_subjects,
)
from models.database import Database

db = Database()


def student_menu():
    current_student = None
    while True:
        print("\nStudent Menu:")
        if current_student is None:
            print("(l) Login")
            print("(r) Register")
            print("(x) Exit to Main Menu")
        else:
            print("(c) Change Password")
            print("(e) Enrol in Subject")
            print("(r) Remove Enrolled Subject")
            print("(s) Show Enrolled Subjects")
            print("(x) Exit to Main Menu")

        choice = input("Enter your choice: ").lower()

        if choice == "l" and current_student is None:
            current_student = login_student(db)
        elif choice == "r" and current_student is None:
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
            print("Invalid choice. Please try again.")
