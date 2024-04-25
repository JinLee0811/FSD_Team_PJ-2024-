# src/admin_system.py
from controllers.admin_controller import (
    clear_database,
    group_students,
    partition_students,
    remove_student,
    show_students,
)


def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("(c) Clear Database File")
        print("(g) Group Students by Grade")
        print("(p) Partition Students by Pass/Fail")
        print("(r) Remove a Student")
        print("(s) Show All Students")
        print("(x) Exit to Main Menu")
        choice = input("Enter your choice: ").lower()  # Use lower() to match the case

        if choice == "c":
            clear_database()
        elif choice == "g":
            group_students()
        elif choice == "p":
            partition_students()
        elif choice == "r":
            remove_student()  # This function might need an ID input to function correctly
        elif choice == "s":
            show_students()
        elif choice == "x":
            break
        else:
            print("Invalid choice. Please try again.")
