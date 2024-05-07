import admin_system
import student_system
from colorama import Fore, init

init(autoreset=True)


def main_menu():
    while True:
        print(Fore.BLUE + "\nUniversity System:")
        choice = input(Fore.BLUE + "\n(A)dmin\n(S)tudent\n(X)Exit\n> ").upper()

        if choice == "A":
            admin_system.admin_menu()  # admin_system 모듈에서 admin_menu 함수 호출
        elif choice == "S":
            student_system.student_menu()  # student_system 모듈에서 student_menu 함수 호출
        elif choice == "X":
            print(Fore.YELLOW + "Thank you for using CLIUniApp.")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
