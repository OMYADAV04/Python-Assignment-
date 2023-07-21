def add_student_details():
    try:
        with open("students.txt", "a") as file:
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            file.write(f"{name},{age}\n")
            print("Student details added successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid age.")
    except Exception as e:
        print(f"An error occurred: {e}")
