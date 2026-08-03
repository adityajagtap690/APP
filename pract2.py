# Dynamic Report Generator
# Author: Mandar Joshi

# Decorator
def report_decorator(func):
    def wrapper(*args, **kwargs):
        print("=" * 50)
        print("      STUDENT REPORT GENERATOR")
        print("=" * 50)
        func(*args, **kwargs)
        print("=" * 50)
        print("        END OF REPORT")
        print("=" * 50)
    return wrapper


class Report:

    company = "MIT ADT University"

    # Constructor (Magic Method)
    def __init__(self, student_name, roll_no):
        self.student_name = student_name
        self.roll_no = roll_no
        self.subjects = {}

    # Add Subject Marks
    def add_marks(self, subject, marks):
        self.subjects[subject] = marks

    # Class Method
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    # Static Method
    @staticmethod
    def line():
        print("-" * 50)

    # Magic Method
    def __str__(self):
        return f"Student Name : {self.student_name}\nRoll No : {self.roll_no}"

    # Magic Method
    def __len__(self):
        return len(self.subjects)

    # Decorated Method
    @report_decorator
    def display_report(self):
        print("College :", Report.company)
        print(self)

        Report.line()

        total = 0
        print("Subject\t\tMarks")
        for subject, marks in self.subjects.items():
            print(f"{subject}\t\t{marks}")
            total += marks

        Report.line()
        print("Total Marks :", total)
        print("No. of Subjects :", len(self))


# Main Program
r1 = Report("Aditya Jagtap", 101)

r1.add_marks("Python", 90)
r1.add_marks("Java", 85)
r1.add_marks("DBMS", 88)
r1.add_marks("DSA", 91)

r1.display_report()

print("\nChanging College Name...\n")

Report.change_company("ABC Engineering College")

r2 = Report("Rahul Patil", 102)

r2.add_marks("Python", 80)
r2.add_marks("Java", 75)
r2.add_marks("DBMS", 82)

r2.display_report()