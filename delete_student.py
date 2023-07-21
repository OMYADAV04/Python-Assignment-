def delete_student_details():
    try:
        delete_name = input("Enter student name to delete: ")
        with open("students.txt", "r") as file:
            lines = file.readlines()
        with open("students.txt", "w") as file:
            deleted = False
            for line in lines:
                name, age = line.strip().split(',')
                if delete_name.lower() != name.lower():
                    file.write(line)
                else:
                    deleted = True
            if deleted:
                print(f"Student '{delete_name}' deleted successfully.")
            else:
                print(f"No student found with the name '{delete_name}'.")
    except FileNotFoundError:
        print("No students found. Please add students first.")
    except Exception as e:
        print(f"An error occurred: {e}")
