import json
import getpass

students = [
    {"name": "Rahul", "age": "20", "grade": "A"},
    {"name": "Priya", "age": "21", "grade": "B"},
    {"name": "Arjun", "age": "19", "grade": "A"},
    {"name": "Sita", "age": "22", "grade": "C"}
]

username_db = "admin"
password_db = "Admin@123"

# Load students from file
def load_data():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except:
        pass

# Save students to file
def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file)

# Add student
def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")

    student = {
        "name": name,
        "age": age,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!")

# View students
def view_students():
    if len(students) == 0:
        print("No students found.")
        return

    print("\nID   Name        Age   Grade")
    print("-----------------------------")

    for i, s in enumerate(students):
        print(f"{i+1:<4} {s['name']:<10} {s['age']:<5} {s['grade']}")

# Search student
def search_student():
    name = input("Enter name to search: ")

    for s in students:
        if s["name"].lower() == name.lower():
            print("Student found:", s)
            return

    print("Student not found.")

# Delete student
def delete_student():
    name = input("Enter name to delete: ")

    for s in students:
        if s["name"].lower() == name.lower():
            students.remove(s)
            print("Student deleted.")
            return

    print("Student not found.")

# Update student
def update_student():
    name = input("Enter name to update: ")

    for s in students:
        if s["name"].lower() == name.lower():
            s["age"] = input("Enter new age: ")
            s["grade"] = input("Enter new grade: ")
            print("Student updated.")
            return

    print("Student not found.")

# Update login credentials 
def update_credentials():
    global username_db, password_db

    new_username = input("Enter new username: ")
    new_password = input("Enter new password: ")

    username_db = new_username
    password_db = new_password

    print("Username and password updated successfully!")

# fotgot password
def forgot_password():
    global password_db

    print("\n--- Reset Password ---")
    username = input("Enter your username: ")

    if username == username_db:
        new_password = input("Enter new password: ")
        password_db = new_password
        print("Password reset successful!")
    else:
        print("Username not found.")
    
#   Login Username and password  
def login():
    global username_db, password_db
    attempts = 3

    while attempts > 0:
        print("\n1. Login")
        print("2. Forgot Password")

        choice = input("Enter choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")

            if username == username_db and password == password_db:
                print("\nLogin successful!\n")
                return True
            else:
                print("Invalid username or password")
                attempts -= 1
                print("Attempts remaining:", attempts)

        elif choice == "2":
            forgot_password()

        else:
            print("Invalid choice")

    print("\nToo many failed attempts. Exiting program.")
    return False

# Main menu
def menu():
    load_data()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Update Credentials ")
        print("7. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            update_student()
        elif choice =="6":
            update_credentials()
        elif choice == "7":
            save_data()
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice")

if login():
    menu()