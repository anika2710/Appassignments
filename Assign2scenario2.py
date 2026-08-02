# Decorator
def hospital_header(func):
    def wrapper(*args, **kwargs):
        print("=" * 35)
        print("     HOSPITAL RECORD")
        print("=" * 35)
        func(*args, **kwargs)
        print("=" * 35)
    return wrapper


# Patient Class
class Patient:
    def __init__(self, pid, name, cost):
        self.pid = pid
        self.name = name
        self.cost = cost

    @hospital_header
    def display(self):
        print("Patient ID :", self.pid)
        print("Name :", self.name)
        print("Treatment Cost :", self.cost)

        if self.cost >= 50000:
            print("Category : Special")
        else:
            print("Category : General")


# Hospital Class
class Hospital:
    def add_patient(self, patient):
        print("Patient Added Successfully!\n")

    def display_patient(self, patient):
        patient.display()


# Main Program
p1 = Patient(101, "Yashraj", 60000)

hospital = Hospital()
hospital.add_patient(p1)
hospital.display_patient(p1)

"""
===================================
     HOSPITAL RECORD
===================================
Patient ID : 101
Name : Yashraj
Treatment Cost : 60000
Category : Special
===================================
"""