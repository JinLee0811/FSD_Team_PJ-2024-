# src/student_system.py
from controllers.student_controller import (
    change_password,
    enroll_subject,
    login_student,
    register_student,
    remove_subject,
    show_enrolled_subjects,
)


def student_menu():
    current_student = None
    while True:
        print("\nStudent Menu:")
        print("1. Login")
        print("2. Register")
        print("3. Change Password")
        print("4. Enroll in Subject")
        print("5. Remove Enrolled Subject")
        print("6. Show Enrolled Subjects")
        print("X. Exit to Main Menu")
        choice = input("Enter your choice: ").upper()

        if choice == "1":
            current_student = login_student()
        elif choice == "2":
            register_student()
        elif choice == "3":
            if current_student:
                change_password(current_student)
            else:
                print("Please log in first.")
        elif choice == "4":
            if current_student:
                enroll_subject(current_student)
            else:
                print("Please log in first.")
        elif choice == "5":
            if current_student:
                remove_subject(current_student)
            else:
                print("Please log in first.")
        elif choice == "6":
            if current_student:
                show_enrolled_subjects(current_student)
            else:
                print("Please log in first.")
        elif choice == "X":
            break
        else:
            print("Invalid choice. Please try again.")
