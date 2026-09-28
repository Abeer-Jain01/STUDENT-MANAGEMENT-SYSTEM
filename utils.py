import random

from config import ROLL_NUMBER_MIN, ROLL_NUMBER_MAX


def generate_roll_number(database):
    # keep picking a random number until we find a unique one
    while True:
        roll_number = str(random.randint(ROLL_NUMBER_MIN, ROLL_NUMBER_MAX))

        if roll_number not in database:
            return roll_number


def read_non_empty(prompt):
    # keep asking until the user types something
    while True:
        value = input(prompt)
        value = value.strip()

        if value != "":
            return value

        print("THIS FIELD CANNOT BE BLANK.")
