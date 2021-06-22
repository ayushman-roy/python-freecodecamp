"""
Classes = Defines what a data-type is. It gives the framework for an object - a template.
Object = An actual piece of data, based on the framework provided in Class.
The attributes of a class is defined using the init (initialise) function.
Overview -
Modelling real world objects and creating custom data-types and then deifining specific cases.
"""

from Supplement import Student


studentA = Student("Jake", 18, "Biology", 89, False)
# created an object StudentA using framework provided in Student class.


print(studentA.is_on_honor_roll)
print(studentA.name)

studentB = Student("Matt", 16, "Economics", 96, True)
print(studentB.major)


print(studentA.name + " has a Job Chance of : " + studentA.job_chances())


"""
Class Functions = Functions inside of a class, which can also be applied to its objects.
Inheritance = Inherit class functions into a new class from an older class.
"""


# NewStudent Class inherits the functions of Student Class
class NewStudent(Student):

    # init function is redefined
    def __init__(self, name, age, major, percentage, is_on_honor_roll, nationality):
        # super() is basically calling out that all predefined parameters in sub-class will be the same here
        super().__init__(name, age, major, percentage, is_on_honor_roll)
        self.nationality = nationality

    # you can also override functions by rewriting and modifying them
    def is_exchange(self):
        if self.nationality.lower() == "united states" or self.nationality.lower == "us":
            return "Not an Exchange Student."
        else:
            return "Is an Exchange Student."


studentC = NewStudent("Roy", 17, "Accountancy", 99, True, "India")
print(studentC.is_exchange())
print(studentC.job_chances())


class NewStudent1(NewStudent):

    def section(self):
        if self.is_on_honor_roll or self.is_exchange():
            return "A"
        elif self.percentage >= 80:
            return "B"
        else:
            return "C"


studentD = NewStudent1("Elon", 21, "Physics", 94, True, "United States")
print(studentD.section())
print(studentD.job_chances())
