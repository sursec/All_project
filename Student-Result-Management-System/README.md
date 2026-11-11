# Student Result Management System

A simple terminal-based Python project using OOP (Object-Oriented Programming).

## Features
- Add students with name, ID, and marks in five subjects
- Automatically calculate total, average, percentage, and grade
- Show Pass/Fail status
- Search students by ID
- Display all students
- Find the highest- and lowest-scoring students
- Show class performance summary
- Save and load student records using a CSV file

## Requirements
- Python 3 (no extra packages required)

## How to run
1. Extract the ZIP file.
2. Open the `student_result_management` folder in VS Code or a terminal.
3. Run:

   ```bash
   python main.py
   ```

4. Select an option from the menu.

The program automatically creates `students.csv` in the same folder after you add the first student. Do not delete this file if you want to keep your saved records.

## Rules used
- Each subject is marked out of 100.
- A student passes only if they get at least 33 in every subject.
- Grade is calculated from the average:
  - A+: 80 or above
  - A: 70–79.99
  - A-: 60–69.99
  - B: 50–59.99
  - C: 40–49.99
  - D: 33–39.99
  - F: below 33

## Project structure
```text
student_result_management/
├── main.py
└── README.md
```
