# Design Document — Student Management System

## 1. Problem Statement

See [`statement.md`](../statement.md) at the project root for the complete problem statement, scope, target users and main features of the project.

## 2. Objectives

The main objectives of this project are:

* To store and manage student records and fee information.
* To keep the program divided into different files so that it is easier to understand and manage.
* To avoid common mistakes such as empty inputs and invalid fee payments.
* To handle basic problems such as a missing database file without stopping the program.

## 3. Functional Requirements

The system has three main functional modules:

* **Student Records Management:** Add, view, update, remove and list students.
* **Fee Management:** Pay fees and view payment history.
* **Reporting / Listing:** Display all students in a simple table.

| No. | Requirement                                                  | Module               |
| --- | ------------------------------------------------------------ | -------------------- |
| 1   | Add a new student with a unique system-generated roll number | `student_manager.py` |
| 2   | View full details of a student using roll number             | `student_manager.py` |
| 3   | Update information of an existing student                    | `student_manager.py` |
| 4   | Remove a student record after confirmation                   | `student_manager.py` |
| 5   | List all students in a table                                 | `student_manager.py` |
| 6   | Record a fee payment for a student                           | `fee_manager.py`     |
| 7   | View the payment history of a student                        | `fee_manager.py`     |
| 8   | Save the data after every change                             | `database.py`        |

The three main modules are **Student Records Management, Fee Management and Reporting / Listing**. The program uses a menu-based system through which the administrator can perform these operations.

## 4. Non-Functional Requirements

| No. | Requirement     | How it is addressed                                                  |
| --- | --------------- | -------------------------------------------------------------------- |
| 1   | Performance     | Data is loaded and saved when required.                              |
| 2   | Reliability     | The database file is created if it is not available.                 |
| 3   | Usability       | Simple menus and clear messages are used.                            |
| 4   | Maintainability | The program is divided into different Python files.                  |
| 5   | Error Handling  | Invalid inputs and unavailable student records are handled properly. |

## 5. System Architecture Diagram

The system is divided into three layers:

1. **Presentation Layer:** `main.py` handles the main menu and user choices.
2. **Business Logic Layer:** `student_manager.py`, `fee_manager.py` and `utils.py` handle the main operations and rules of the system.
3. **Data Access Layer:** `database.py` reads and writes the JSON database file.

![System Architecture](diagrams/architecture.png)

## 6. Process Flow / Workflow Diagram

The process flow diagram shows how the administrator's menu choice moves through the different parts of the system and how the changes are finally saved.

![Process Flow](diagrams/process_flow.png)

## 7. Design Diagrams

### 7.1 Use Case Diagram

The Administrator is the only actor in the system. The diagram shows the main actions that can be performed, such as viewing student information, updating records, paying fees and viewing payment history.

![Use Case Diagram](diagrams/use_case.png)

### 7.2 Component Diagram

The project uses functions instead of classes. Therefore, this diagram shows the different Python modules and their main functions. It also shows how the student record is stored in the JSON file.

![Component Diagram](diagrams/class_diagram.png)

### 7.3 ER Diagram

The JSON database contains information about students, their fees and their payment history. The ER diagram shows the relationship between these parts of the stored data.

![ER Diagram](diagrams/er_diagram.png)

## 8. Database / Storage Design

The system uses one JSON file, `data/students_database.json`, to store all student records.

Each student is identified using a unique roll number. The record contains student details, fee information and payment history.

A student record contains information such as:

* Name
* Date of birth
* Gender
* Course
* Semester
* Address
* Phone number
* Email
* Parent name and phone number
* Blood group
* Admission year
* Attendance
* Total fees
* Fees paid
* Remaining fees
* Payment history
* Status
* Date of creation

The data is stored in JSON so that it can be saved and loaded easily without using an external database.