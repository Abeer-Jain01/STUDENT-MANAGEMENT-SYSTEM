from datetime import datetime

from config import TOTAL_FEES, DATE_FORMAT
from database import load_database, save_database
from utils import generate_roll_number, read_non_empty
import fee_manager


# ============================================================
# ADD STUDENT
# ============================================================

def add_student():

    database = load_database()

    print("\n")
    print("=" * 65)
    print("                    ADD NEW STUDENT")
    print("=" * 65)

    name = read_non_empty("ENTER STUDENT NAME: ")
    dob = read_non_empty("ENTER DATE OF BIRTH (DD/MM/YYYY): ")
    gender = read_non_empty("ENTER GENDER: ")
    course = read_non_empty("ENTER COURSE: ")
    semester = read_non_empty("ENTER SEMESTER NUMBER: ")
    address = read_non_empty("ENTER ADDRESS: ")
    phone = read_non_empty("ENTER PHONE NUMBER: ")
    email = read_non_empty("ENTER EMAIL: ")
    parent_name = read_non_empty("ENTER PARENT/GUARDIAN NAME: ")
    parent_phone = read_non_empty("ENTER PARENT/GUARDIAN PHONE: ")
    blood_group = read_non_empty("ENTER BLOOD GROUP: ")
    admission_year = read_non_empty("ENTER ADMISSION YEAR: ")
    attendance = read_non_empty("ENTER ATTENDANCE (%): ")

    roll_number = generate_roll_number(database)

    new_student = {
        "name": name,
        "dob": dob,
        "gender": gender,
        "course": course,
        "semester": semester,
        "address": address,
        "phone": phone,
        "email": email,
        "parent_name": parent_name,
        "parent_phone": parent_phone,
        "blood_group": blood_group,
        "admission_year": admission_year,
        "attendance": attendance,
        "fees": {
            "total": TOTAL_FEES,
            "paid": 0,
            "remaining": TOTAL_FEES,
        },
        "payment_history": [],
        "status": "Active",
        "created_at": datetime.now().strftime(DATE_FORMAT),
    }

    database[roll_number] = new_student

    save_database(database)

    print("\n")
    print("=" * 65)
    print("             STUDENT ADDED SUCCESSFULLY!")
    print("=" * 65)
    print("STUDENT NAME  :", name)
    print("ROLL NUMBER   :", roll_number)
    print("COURSE        :", course)
    print("SEMESTER      :", semester)
    print("TOTAL FEES    : Rs.", TOTAL_FEES)
    print("FEES PAID     : Rs.0")
    print("FEES REMAINING: Rs.", TOTAL_FEES)
    print("=" * 65)

    input("\nPRESS ENTER TO CONTINUE...")


# ============================================================
# VIEW STUDENT
# ============================================================

def get_student():

    database = load_database()

    print("\n")
    print("=" * 65)
    print("                   GET STUDENT INFORMATION")
    print("=" * 65)

    roll_number = input("ENTER 5 DIGIT ROLL NUMBER: ")
    roll_number = roll_number.strip()

    if roll_number not in database:
        print("\nSTUDENT NOT FOUND!")
        input("\nPRESS ENTER TO CONTINUE...")
        return

    student = database[roll_number]

    while True:

        print("\n")
        print("=" * 65)
        print("                   STUDENT INFORMATION")
        print("=" * 65)
        print("ROLL NUMBER       :", roll_number)
        print("NAME              :", student["name"])
        print("DATE OF BIRTH     :", student["dob"])
        print("GENDER            :", student["gender"])
        print("-----------------------------------------------")
        print("COURSE            :", student["course"])
        print("SEMESTER          :", student["semester"])
        print("ADMISSION YEAR    :", student["admission_year"])
        print("-----------------------------------------------")
        print("ADDRESS           :", student["address"])
        print("PHONE             :", student["phone"])
        print("EMAIL             :", student["email"])
        print("-----------------------------------------------")
        print("PARENT/GUARDIAN   :", student["parent_name"])
        print("PARENT PHONE      :", student["parent_phone"])
        print("-----------------------------------------------")
        print("BLOOD GROUP       :", student["blood_group"])
        print("ATTENDANCE        :", student["attendance"], "%")
        print("-----------------------------------------------")
        print("TOTAL FEES        : Rs.", student["fees"]["total"])
        print("FEES PAID         : Rs.", student["fees"]["paid"])
        print("FEES REMAINING    : Rs.", student["fees"]["remaining"])
        print("-----------------------------------------------")
        print("STATUS            :", student["status"])
        print("ADDED ON          :", student["created_at"])
        print("=" * 65)

        print("\n1. UPDATE STUDENT INFORMATION")
        print("2. PAY FEES")
        print("3. VIEW PAYMENT HISTORY")
        print("4. BACK")

        choice = input("\nENTER YOUR CHOICE: ")
        choice = choice.strip()

        if choice == "1":
            update_student(roll_number)
            database = load_database()
            student = database[roll_number]

        elif choice == "2":
            fee_manager.pay_fees(roll_number)
            database = load_database()
            student = database[roll_number]

        elif choice == "3":
            fee_manager.payment_history(roll_number)

        elif choice == "4":
            break

        else:
            print("\nINVALID CHOICE!")


# ============================================================
# UPDATE STUDENT
# ============================================================

def update_student(roll_number):

    database = load_database()

    if roll_number not in database:
        print("\nSTUDENT NOT FOUND!")
        return

    student = database[roll_number]

    while True:

        print("\n")
        print("=" * 65)
        print("                  UPDATE STUDENT INFORMATION")
        print("=" * 65)

        print("1. Name")
        print("2. Date of Birth")
        print("3. Gender")
        print("4. Course")
        print("5. Semester")
        print("6. Address")
        print("7. Phone")
        print("8. Email")
        print("9. Parent/Guardian Name")
        print("10. Parent/Guardian Phone")
        print("11. Blood Group")
        print("12. Admission Year")
        print("13. Attendance")
        print("14. Student Status")
        print("15. Update All Information")
        print("16. Back")

        choice = input("\nENTER YOUR CHOICE: ")
        choice = choice.strip()

        if choice == "1":
            student["name"] = input("ENTER NEW NAME: ")

        elif choice == "2":
            student["dob"] = input("ENTER NEW DATE OF BIRTH: ")

        elif choice == "3":
            student["gender"] = input("ENTER NEW GENDER: ")

        elif choice == "4":
            student["course"] = input("ENTER NEW COURSE: ")

        elif choice == "5":
            student["semester"] = input("ENTER NEW SEMESTER: ")

        elif choice == "6":
            student["address"] = input("ENTER NEW ADDRESS: ")

        elif choice == "7":
            student["phone"] = input("ENTER NEW PHONE: ")

        elif choice == "8":
            student["email"] = input("ENTER NEW EMAIL: ")

        elif choice == "9":
            student["parent_name"] = input("ENTER NEW PARENT/GUARDIAN NAME: ")

        elif choice == "10":
            student["parent_phone"] = input("ENTER NEW PARENT/GUARDIAN PHONE: ")

        elif choice == "11":
            student["blood_group"] = input("ENTER NEW BLOOD GROUP: ")

        elif choice == "12":
            student["admission_year"] = input("ENTER NEW ADMISSION YEAR: ")

        elif choice == "13":
            student["attendance"] = input("ENTER NEW ATTENDANCE: ")

        elif choice == "14":
            new_status = input("ENTER NEW STATUS (Active/Inactive/Graduated): ")
            new_status = new_status.strip()
            if new_status != "":
                student["status"] = new_status

        elif choice == "15":
            student["name"] = input("NAME: ")
            student["dob"] = input("DATE OF BIRTH: ")
            student["gender"] = input("GENDER: ")
            student["course"] = input("COURSE: ")
            student["semester"] = input("SEMESTER: ")
            student["address"] = input("ADDRESS: ")
            student["phone"] = input("PHONE: ")
            student["email"] = input("EMAIL: ")
            student["parent_name"] = input("PARENT/GUARDIAN NAME: ")
            student["parent_phone"] = input("PARENT/GUARDIAN PHONE: ")
            student["blood_group"] = input("BLOOD GROUP: ")
            student["admission_year"] = input("ADMISSION YEAR: ")
            student["attendance"] = input("ATTENDANCE: ")
            print("\nALL INFORMATION UPDATED!")

        elif choice == "16":
            break

        else:
            print("\nINVALID CHOICE!")
            continue

        save_database(database)
        print("\nINFORMATION UPDATED SUCCESSFULLY!")


# ============================================================
# REMOVE STUDENT
# ============================================================

def remove_student():

    database = load_database()

    print("\n")
    print("=" * 65)
    print("                     REMOVE STUDENT")
    print("=" * 65)

    roll_number = input("ENTER ROLL NUMBER: ")
    roll_number = roll_number.strip()

    if roll_number not in database:
        print("\nSTUDENT NOT FOUND!")
        input("\nPRESS ENTER TO CONTINUE...")
        return

    student = database[roll_number]

    print("\nSTUDENT FOUND")
    print("------------------------------")
    print("NAME  :", student["name"])
    print("ROLL  :", roll_number)
    print("COURSE:", student["course"])
    print("------------------------------")

    confirm = input("\nARE YOU SURE YOU WANT TO REMOVE THIS STUDENT? (Y/N): ")

    if confirm.lower() == "y":
        del database[roll_number]
        save_database(database)
        print("\nSTUDENT REMOVED SUCCESSFULLY!")
    else:
        print("\nOPERATION CANCELLED.")

    input("\nPRESS ENTER TO CONTINUE...")


# ============================================================
# LIST ALL STUDENTS
# ============================================================

def list_students():

    database = load_database()

    print("\n")
    print("=" * 80)
    print("                         ALL STUDENTS")
    print("=" * 80)

    if len(database) == 0:
        print("\nNO STUDENTS FOUND.")
        input("\nPRESS ENTER TO CONTINUE...")
        return

    print(
        f"{'ROLL NO.':<12}"
        f"{'NAME':<25}"
        f"{'COURSE':<20}"
        f"{'SEM':<8}"
        f"{'STATUS':<15}"
    )
    print("-" * 80)

    for roll_number in database:
        student = database[roll_number]
        print(
            f"{roll_number:<12}"
            f"{student['name'][:23]:<25}"
            f"{student['course'][:18]:<20}"
            f"{student['semester']:<8}"
            f"{student['status']:<15}"
        )

    print("=" * 80)
    input("\nPRESS ENTER TO CONTINUE...")
