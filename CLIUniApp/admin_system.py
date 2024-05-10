import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


from controller.admin_controller import *
from models.database import *

db = Database()


def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("(c) Clear Database File")
        print("(g) Group Students by Grade")
        print("(p) Partition Students by Pass/Fail")
        print("(r) Remove a Student")
        print("(s) Show All Students")
        print("(x) Exit to Main Menu")
        choice = input("Enter your choice: ").lower()

        if choice == "c":
            clear_database(db)
        elif choice == "g":
            group_students(db)
        elif choice == "p":
            partition_students(db)
        elif choice == "r":
            remove_student(db)
        elif choice == "s":
            show_students(db)
        elif choice == "x":
            break
        else:
            print("Invalid choice. Please try again.")
