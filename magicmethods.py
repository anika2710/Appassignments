class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Magic Method for displaying object
    def __str__(self):
        return f"Student Name: {self.name}, Marks: {self.marks}"

    # Magic Method for comparing marks
    def __gt__(self, other):
        return self.marks > other.marks


# Creating objects
s1 = Student("Atharva", 85)
s2 = Student("Rahul", 75)

# __str__() is called automatically
print(s1)
print(s2)

# __gt__() is called automatically
if s1 > s2:
    print(s1.name, "has higher marks.")
else:
    print(s2.name, "has higher marks.")

'''
Student Name: Atharva, Marks: 85
Student Name: Rahul, Marks: 75
Atharva has higher marks.
'''