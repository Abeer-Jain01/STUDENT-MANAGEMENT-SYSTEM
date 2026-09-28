# This is the starting point of the program.
# Run it with: python main.py

from student_manager import add_student, get_student, remove_student, list_students


def main():

    while True:

        print("\n")
        print("=" * 70)
        print("              STUDENT MANAGEMENT SYSTEM")
        print("=" * 70)
        print("1. ADD STUDENT")
        print("2. GET STUDENT INFORMATION")
        print("3. REMOVE STUDENT")
        print("4. LIST ALL STUDENTS")
        print("5. EXIT")
        print("=" * 70)

        choice = input("ENTER YOUR CHOICE: ")
        choice = choice.strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            get_student()

        elif choice == "3":
            remove_student()

        elif choice == "4":
            list_students()

        elif choice == "5":
            print("\nTHANK YOU FOR USING STUDENT MANAGEMENT SYSTEM.")
            break

        else:
            print("\nINVALID CHOICE!")


main()
