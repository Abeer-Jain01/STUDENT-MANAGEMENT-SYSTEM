# Student Management System

Python console app to manage student records and fee stuff. Uses a JSON file as the "database" so there's no need to set up MySQL or anything like that.

## Overview

Most small colleges/coaching centres still keep student records in registers or random excel sheets, so finding a student's info or checking how much fee is left takes forever and mistakes happen a lot. This is a simple command line program where an admin can add/view/update/remove students and also handle their fee payments. Everything gets saved in data/students_database.json automatically, you don't have to do anything manually.

## Features

- Add Student - asks for all the details (name, DOB, gender, course, semester, address, phone, email, parent/guardian info, blood group, admission year, attendance) and gives a random 5 digit roll number to the student.
- Get Student Information - enter roll number and it shows the full profile + fee status.
- Update Student Information - can update one field at a time or update everything together.
- Pay Fees - takes a payment amount and reduces it from remaining fees (won't let you pay more than remaining, or pay 0/negative).
- View Payment History - shows all payments made so far with date and balance left after each one.
- Remove Student - deletes a record, asks for confirmation first.
- List All Students - table showing roll no, name, course, semester and status for everyone.

## Tech Used

Just Python 3, standard library only (json, os, random, datetime). No pip installs needed.

## Project Structure

```
StudentManagementSystem/
├── README.md
├── statement.md
├── src/
│   ├── main.py            -> menu loop, entry point
│   ├── config.py          -> constants/paths
│   ├── database.py        -> reads/writes the json file
│   ├── utils.py           -> roll number gen + input validation
│   ├── student_manager.py -> add/view/update/remove/list
│   └── fee_manager.py     -> pay fees, payment history
├── docs/
│   └── Project_Report.pdf
└── data/                  -> students_database.json (auto created)
```

## How to Run

1. python3 --version (make sure its 3.8+)
2. cd into the project folder
3. cd src
4. python3 main.py
5. use the menu, database file gets created on its own first time you run it

## Testing

Tested it manually - went through every menu option (add student, view info, update fields, pay fees including trying to overpay/underpay/zero amount, view history, remove a student, list all) a bunch of times to make sure nothing breaks.

## Screenshots / Diagrams

check the project report pdf, has all the screenshots + architecture/UML/ER diagrams in it.
