def view_all_students():
    try:
        with open("students.txt", "r") as file:
            print("List of Students:")
            for line in file:
                name, age = line.strip().split(',')
                print(f"Name: {name}, Age: {age}")
    except FileNotFoundError:
        print("No students found. Please add students first.")
    except Exception as e:
        print(f"An error occurred: {e}")
