# src/student_system.py
from controllers.student_controller import login_student, register_student, change_password, enroll_subject, remove_subject, show_enrolled_subjects

def student_menu():
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

        if choice == '1':
            login_student()
        elif choice == '2':
            register_student()
        elif choice == '3':
            change_password()
        elif choice == '4':
            enroll_subject()
        elif choice == '5':
            remove_subject()
        elif choice == '6':
            show_enrolled_subjects()
        elif choice == 'X':
            break
        else:
            print("Invalid choice. Please try again.")
