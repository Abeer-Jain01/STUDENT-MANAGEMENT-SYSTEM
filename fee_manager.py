from datetime import datetime

from config import DATE_FORMAT
from database import load_database, save_database


# ============================================================
# PAY FEES
# ============================================================

def pay_fees(roll_number):

    database = load_database()

    if roll_number not in database:
        print("\nSTUDENT NOT FOUND!")
        return

    student = database[roll_number]
    remaining = student["fees"]["remaining"]

    print("\n")
    print("=" * 65)
    print("                       PAY FEES")
    print("=" * 65)
    print("TOTAL FEES     : Rs.", student["fees"]["total"])
    print("FEES PAID      : Rs.", student["fees"]["paid"])
    print("FEES REMAINING : Rs.", remaining)
    print("=" * 65)

    try:
        amount = float(input("ENTER AMOUNT TO PAY: Rs."))
    except ValueError:
        print("\nPLEASE ENTER A VALID NUMBER.")
        return

    if amount <= 0:
        print("\nAMOUNT MUST BE GREATER THAN ZERO.")
        return

    if amount > remaining:
        print("\nYOU CANNOT PAY MORE THAN THE REMAINING FEES.")
        print("REMAINING FEES: Rs.", remaining)
        return

    # update the student's fee info
    student["fees"]["paid"] = student["fees"]["paid"] + amount
    student["fees"]["remaining"] = student["fees"]["remaining"] - amount

    # add this payment to the history list
    payment = {
        "amount": amount,
        "date": datetime.now().strftime(DATE_FORMAT),
        "remaining_after_payment": student["fees"]["remaining"],
    }
    student["payment_history"].append(payment)

    save_database(database)

    print("\n")
    print("=" * 65)
    print("                  PAYMENT SUCCESSFUL!")
    print("=" * 65)
    print("AMOUNT PAID      : Rs.", amount)
    print("TOTAL PAID       : Rs.", student["fees"]["paid"])
    print("FEES REMAINING   : Rs.", student["fees"]["remaining"])

    if student["fees"]["remaining"] == 0:
        print("\n*** ALL FEES PAID ***")

    print("=" * 65)
    input("\nPRESS ENTER TO CONTINUE...")


# ============================================================
# PAYMENT HISTORY
# ============================================================

def payment_history(roll_number):

    database = load_database()

    if roll_number not in database:
        print("\nSTUDENT NOT FOUND!")
        return

    student = database[roll_number]

    print("\n")
    print("=" * 65)
    print("                    PAYMENT HISTORY")
    print("=" * 65)

    if len(student["payment_history"]) == 0:
        print("\nNO PAYMENTS HAVE BEEN MADE YET.")
    else:
        count = 1
        for payment in student["payment_history"]:
            print("\nPayment", count)
            print("Amount      : Rs.", payment["amount"])
            print("Date        :", payment["date"])
            print("Remaining   : Rs.", payment["remaining_after_payment"])
            print("-" * 50)
            count = count + 1

    print("\nTOTAL PAID     : Rs.", student["fees"]["paid"])
    print("TOTAL REMAINING: Rs.", student["fees"]["remaining"])
    print("=" * 65)

    input("\nPRESS ENTER TO CONTINUE...")
