# Decorator to add a report header
def report_header(func):
    def wrapper(*args, **kwargs):
        # *args and **kwargs allow any number of positional
        # and keyword arguments.
        print("=" * 40)
        print("        STUDENT REPORT")
        print("=" * 40)

        func(*args, **kwargs)

        print("=" * 40)

    return wrapper


class Report:
    college = "ABC Engineering College"

    # Constructor (Magic Method)
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    # Class Method
    @classmethod
    def change_college(cls, new_name):
        cls.college = new_name

    # Magic Method
    def __str__(self):
        return f"Name : {self.name}\nRoll No : {self.roll}\nMarks : {self.marks}"

    # Decorator applied to display report
    @report_header
    def display_report(self):
        print(f"College : {Report.college}")
        print(self)

        if self.marks >= 40:
            print("Result : PASS")
        else:
            print("Result : FAIL")


# Main Program
student1 = Report("Deep", 101, 85)
student1.display_report()

print()

# Change college name
Report.change_college("MIT ADT UNIVERSITY")

student2 = Report("Atharva", 102, 90)
student2.display_report()



"""
========================================
        STUDENT REPORT
========================================
College : ABC Engineering College
Name : Deep
Roll No : 101
Marks : 85
Result : PASS
========================================

========================================
        STUDENT REPORT
========================================
College : MIT ADT UNIVERSITY
Name : Atharva
Roll No : 102
Marks : 90
Result : PASS
========================================
"""