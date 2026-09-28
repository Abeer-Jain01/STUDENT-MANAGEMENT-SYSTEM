import os

# folder where this file (config.py) is saved
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# folder and file where we keep the student data
DATA_DIR = os.path.join(BASE_DIR, "data")
DATABASE_FILE = os.path.join(DATA_DIR, "students_database.json")

# every new student gets this much total fees
TOTAL_FEES = 200000

# roll numbers will be random numbers between these two
ROLL_NUMBER_MIN = 10000
ROLL_NUMBER_MAX = 99999

DATE_FORMAT = "%d/%m/%Y %H:%M:%S"
