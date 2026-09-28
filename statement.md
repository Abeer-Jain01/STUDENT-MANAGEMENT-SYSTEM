# Problem Statement

## Problem Statement

Most small educational institutes and coaching centres still manage student records using paper registers or random excel sheets, this makes it slow and error prone to look up a student's details or check remaining fee. What's needed is a simple tool with no external dependency that one admin can run on their computer to keep the student/fee data organized.

## Scope of the Project

This project is a command line Student Management System which can do:

- Store student data (personal, academic, fee info) persistently in a JSON file
- Menu based add/view/update/remove/list operations for students
- Track fee payments for each student along with full history and balance
- Basic input validation - no blank fields, payment amount has to be positive, cant pay more than whats remaining

Out of scope for now: multi user access, GUI/web version, integration with any accounting software. Mentioned as future scope in the project report.

## Target Users

- Admin staff of small colleges/schools/coaching centres who handle student records and fee collection
- Single user on a single machine, not meant for multiple people using it at once

## High Level Features

1. Student Record Management - add/view/update/remove student records (name, DOB, gender, course, semester, contact info, guardian details, blood group, admission year, attendance, status)
2. Fee Management - update fees paid vs remaining balance, view full payment history with dates
3. Reporting - table listing all students (roll no, name, course, semester, status)
4. Data Persistence - all data saved to the JSON file after every operation
