# src/admin_system.py
from controllers.admin_controller import clear_database, group_students, partition_students, remove_student, show_students

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Clear Database File")
        print("2. Group Students by Grade")
        print("3. Partition Students by Pass/Fail")
        print("4. Remove a Student")
        print("5. Show All Students")
        print("X. Exit to Main Menu")
        choice = input("Enter your choice: ").upper()

        if choice == '1':
            clear_database()
        elif choice == '2':
            group_students()
        elif choice == '3':
            partition_students()
        elif choice == '4':
            remove_student()
        elif choice == '5':
            show_students()
        elif choice == 'X':
            break
        else:
            print("Invalid choice. Please try again.")
