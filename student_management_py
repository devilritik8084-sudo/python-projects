def add_student():
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    file = open("students.txt", "a")
    file.write(name + "," + age + "," + course + "\n")
    file.close()

    print("\n✅ Student Added Successfully!")


def view_students():
    try:
        file = open("students.txt", "r")
        print("\n===== STUDENT LIST =====")
        data = file.read()

        if data == "":
            print("No students available.")
        else:
            print(data)

        file.close()

    except FileNotFoundError:
        print("No students found.")


def search_student():
    search = input("Enter Student Name: ")

    try:
        file = open("students.txt", "r")

        found = False

        for line in file:
            if search.lower() in line.lower():
                print("\n✅ Student Found")
                print(line)
                found = True

        if not found:
            print("❌ Student Not Found")

        file.close()

    except FileNotFoundError:
        print("No students found.")


def update_student():

    search = input("Enter Student Name to Update: ")

    try:
        file = open("students.txt", "r")
        students = file.readlines()
        file.close()

        file = open("students.txt", "w")

        found = False

        for student in students:

            data = student.strip().split(",")

            if data[0].lower() == search.lower():

                print("\nStudent Found")

                new_age = input("Enter New Age: ")
                new_course = input("Enter New Course: ")

                file.write(data[0] + "," + new_age + "," + new_course + "\n")

                found = True

            else:
                file.write(student)

        file.close()

        if found:
            print("✅ Student Updated Successfully!")

        else:
            print("❌ Student Not Found")

    except FileNotFoundError:
        print("No students found.")


def delete_student():

    search = input("Enter Student Name to Delete: ")

    try:
        file = open("students.txt", "r")
        students = file.readlines()
        file.close()

        file = open("students.txt", "w")

        found = False

        for student in students:

            data = student.strip().split(",")

            if data[0].lower() == search.lower():
                found = True
                continue

            file.write(student)

        file.close()

        if found:
            print("✅ Student Deleted Successfully!")

        else:
            print("❌ Student Not Found")

    except FileNotFoundError:
        print("No students found.")


while True:

    print("\n===================================")
    print("   STUDENT MANAGEMENT SYSTEM")
    print("===================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("\nThank You for using Student Management System.")
        break

    else:
        print("Invalid Choice. Please try again.")