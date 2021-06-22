class Student:

    def __init__(self, name, age, major, percentage, is_on_honor_roll):
        self.name = name
        self.age = age
        self.major = major
        self.percentage = percentage
        self.is_on_honor_roll = is_on_honor_roll

    # class functions
    def job_chances(self):
        if self.is_on_honor_roll:
            return "Very High."
        elif self.percentage >= 80 and not self.is_on_honor_roll:
            return "Average."
        else:
            return "Low."


"""
In the class Student, the parameters in the init function is to be user inputed, 
atleast in this case.
Inside the init function using the self.xyz key, we assign the user 
parameter to each attribute of the class.
Basically, {object}.name [the name attribute of the created object] = name 
[the inputed name parameter].
"""


class UInput:

    def __init__(self, prompt, p1, p2, p3):
        self.prompt = prompt
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
