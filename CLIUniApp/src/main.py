import os
import sys

# 현재 스크립트의 디렉토리 경로를 얻습니다.
current_dir = os.path.dirname(os.path.abspath(__file__))
# 현재 스크립트의 부모 디렉토리(즉, src 디렉토리의 부모)의 경로를 얻습니다.
parent_dir = os.path.dirname(current_dir)
# 부모 디렉토리를 sys.path에 추가합니다.
sys.path.append(parent_dir)

import admin_system
import student_system
from colorama import Back, Fore, Style, init

init(autoreset=True)


# src/main.py
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
