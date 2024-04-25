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
from models.database import Database  # Database 클래스를 가져오는 부분 추가

db = Database()  # Database 인스턴스를 생성


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
            current_student = login_student()
        elif choice == "r" and current_student is None:
            register_student()
        elif choice == "c" and current_student is not None:
            change_password(current_student)
        elif choice == "e" and current_student is not None:
            if len(current_student.subjects) < 4:
                enroll_subject(
                    current_student, db
                )  # db 인스턴스를 enroll_subject 함수에 전달
            else:
                print("You are already enrolled in the maximum number of 4 subjects.")
        elif choice == "r" and current_student is not None:
            remove_subject(
                current_student, db
            )  # db 인스턴스를 remove_subject 함수에 전달
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
