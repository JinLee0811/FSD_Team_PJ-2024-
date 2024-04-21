import admin_system
import student_system


# src/main.py
def main_menu():
    while True:
        print("\nWelcome to CLIUniApp")
        choice = input(
            "Choose an option:\n(A) Admin\n(S) Student\n(X) Exit\n> "
        ).upper()

        if choice == "A":
            admin_system.admin_menu()  # admin_system 모듈에서 admin_menu 함수 호출
        elif choice == "S":
            student_system.student_menu()  # student_system 모듈에서 student_menu 함수 호출
        elif choice == "X":
            print("Thank you for using CLIUniApp.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
