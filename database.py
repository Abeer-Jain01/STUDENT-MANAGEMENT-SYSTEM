import json
import os

from config import DATABASE_FILE, DATA_DIR


def load_database(db_file=DATABASE_FILE):
# make sure the data folder exists first
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

# if the database file does not exist, make an empty one
    if not os.path.exists(db_file):
        file = open(db_file, "w")
        json.dump({}, file, indent=4)
        file.close()

# now read the file and return the data
    file = open(db_file, "r")
    data = json.load(file)
    file.close()

    return data


def save_database(database, db_file=DATABASE_FILE):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    file = open(db_file, "w")
    json.dump(database, file, indent=4)
    file.close()
