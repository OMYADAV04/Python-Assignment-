import add_student
import view_students
import search_student
import delete_student

def display_menu():
    print("Welcome to Student Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_student.add_student_details()
            elif choice == 2:
                view_students.view_all_students()
            elif choice == 3:
                search_student.search_student_details()
            elif choice == 4:
                delete_student.delete_student_details()
            elif choice == 5:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
