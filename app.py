from student import Student

def main():
    students = []

    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            roll = input("Enter roll no: ")
            marks = input("Enter marks: ")

            student = Student(name, roll, marks)
            students.append(student)
            print("✅ Student added successfully")

        elif choice == "2":
            print("\n--- Student List ---")
            for s in students:
                print(s.display())

        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()

