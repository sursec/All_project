import csv
import os

FILE_NAME = "students.csv"
SUBJECTS = ["Bangla", "English", "Math", "Science", "ICT"]


class Student:
    def __init__(self, name, student_id, marks):
        self.name = name
        self.student_id = student_id
        self.marks = marks

    def total_marks(self):
        return sum(self.marks)

    def average_marks(self):
        return self.total_marks() / len(self.marks)

    def percentage(self):
        return (self.total_marks() / (len(self.marks) * 100)) * 100

    def grade(self):
        average = self.average_marks()

        if average >= 80:
            return "A+"
        elif average >= 70:
            return "A"
        elif average >= 60:
            return "A-"
        elif average >= 50:
            return "B"
        elif average >= 40:
            return "C"
        elif average >= 33:
            return "D"
        else:
            return "F"

    def status(self):
       
        if all(mark >= 33 for mark in self.marks):
            return "Pass"
        return "Fail"


class ResultManager:
    def __init__(self):
        self.students = []
        self.load_from_csv()

    def add_student(self):
        print("\n--- Add New Student ---")
        name = input("Enter student name: ").strip()
        student_id = input("Enter student ID: ").strip()

        if not name or not student_id:
            print("Name and ID cannot be empty.")
            return

        if self.find_student(student_id):
            print("This student ID already exists.")
            return

        marks = []
        for subject in SUBJECTS:
            while True:
                try:
                    mark = float(input(f"Enter {subject} marks (0-100): "))
                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    print("Marks must be between 0 and 100.")
                except ValueError:
                    print("Please enter a valid number.")

        student = Student(name, student_id, marks)
        self.students.append(student)
        self.save_to_csv()
        print(f"Student {name} added successfully!")
        
        
    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def search_student(self):
        student_id = input("\nEnter student ID to search: ").strip()
        student = self.find_student(student_id)

        if student:
            self.show_student(student)
        else:
            print("Student not found.")

    def show_student(self, student):
        print("\n--- Student Result ---")
        print("Name:", student.name)
        print("ID:", student.student_id)

        for subject, mark in zip(SUBJECTS, student.marks):
            print(f"{subject}: {mark:g}")

        print("Total Marks:", f"{student.total_marks():g}", "/ 500")
        print("Average:", f"{student.average_marks():.2f}")
        print("Percentage:", f"{student.percentage():.2f}%")
        print("Grade:", student.grade())
        print("Status:", student.status())

    def show_all_students(self):
        if not self.students:
            print("\nNo student records found.")
            return

        print("\n--- All Students ---")
        for student in self.students:
            print(
                f"ID: {student.student_id} | Name: {student.name} | "
                f"Total: {student.total_marks():g}/500 | "
                f"Grade: {student.grade()} | Status: {student.status()}"
            )

    def show_top_and_lowest(self):
        if not self.students:
            print("\nNo student records found.")
            return

        highest = max(self.students, key=lambda s: s.total_marks())
        lowest = min(self.students, key=lambda s: s.total_marks())

        print("\n--- Highest Scoring Student ---")
        self.show_student(highest)

        print("\n--- Lowest Scoring Student ---")
        self.show_student(lowest)

    def class_summary(self):
        if not self.students:
            print("\nNo student records found.")
            return

        total_students = len(self.students)
        passed = sum(1 for s in self.students if s.status() == "Pass")
        failed = total_students - passed
        class_average = sum(s.average_marks() for s in self.students) / total_students

        print("\n--- Class Performance Summary ---")
        print("Total Students:", total_students)
        print("Passed:", passed)
        print("Failed:", failed)
        print(f"Class Average: {class_average:.2f}")
        print(f"Pass Rate: {(passed / total_students) * 100:.2f}%")

    def save_to_csv(self):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "ID"] + SUBJECTS)
            for student in self.students:
                writer.writerow([student.name, student.student_id] + student.marks)

    def load_from_csv(self):
        if not os.path.exists(FILE_NAME):
            return

        try:
            with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    marks = [float(row[subject]) for subject in SUBJECTS]
                    self.students.append(
                        Student(row["Name"], row["ID"], marks)
                    )
        except (KeyError, ValueError):
            print("Warning: students.csv could not be read. Please check the file.")


def main():
    manager = ResultManager()

    while True:
        print("\n==============================")
        print("   STUDENT RESULT MANAGER")
        print("==============================")
        print("1. Add Student")
        print("2. Search Student by ID")
        print("3. Show All Students")
        print("4. Show Highest and Lowest Scoring Students")
        print("5. Class Performance Summary")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.search_student()
        elif choice == "3":
            manager.show_all_students()
        elif choice == "4":
            manager.show_top_and_lowest()
        elif choice == "5":
            manager.class_summary()
        elif choice == "6":
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
