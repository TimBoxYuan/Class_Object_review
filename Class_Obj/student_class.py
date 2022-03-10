# Class is a Blue Print of a house. It contains details about of the house.
# Based on details and descriptions, we can build a house == Object (name, grade...)

# Attributes: variables

# Methods: functions
# student1.function1()

# While you can mannually assign attributes to object: student1.grade = 40
# Use init method to do the same thing
# init method is a special one, bc it is called everytime objects are created
# student1 = Student('Tim', '95') 
# init method is called such that 'Tim' is assigned to name, 95 is assigned to grade


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def check_pass_fail(self):
        if self.grade >60:
            return True
        else:
            return False




# Create 2 objects from the class
student1 = Student('Tim', 70)
student2 = Student('Emily', 50)

print(student1.check_pass_fail())
print(student2.check_pass_fail())



class Complex:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def add(self, number):
        real = self.real + number.real
        image = self.image + number.image
        result = Complex(real, image)
        return result



n1 = Complex(5, 6)
n2 = Complex(3,1)

result = n1.add(n2)

print(result.real)
print(result.image)