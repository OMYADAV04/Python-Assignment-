def search_student_details():
    try:
        search_name = input("Enter student name to search: ")
        with open("students.txt", "r") as file:
            found = False
            for line in file:
                name, age = line.strip().split(',')
                if search_name.lower() == name.lower():
                    print(f"Name: {name}, Age: {age}")
                    found = True
                    break
            if not found:
                print(f"No student found with the name '{search_name}'.")
    except FileNotFoundError:
        print("No students found. Please add students first.")
    except Exception as e:
        print(f"An error occurred: {e}")
