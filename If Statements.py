student = input("Are you a Student? ")
social = input("Are you Social? ")


if student.lower() == "yes":
    is_student = True
elif student.lower() == "no":
    is_student = False
# do not use =0 or =1 while dealing with boolean values as =0 is 'false' and =1 is 'true'
else:
    is_student = 2

if social.lower() == "yes":
    is_social = True
elif social.lower() == "no":
    is_social = False
else:
    is_social = 2

if is_social == 2 and is_student == 2:
    print("Invalid Input.")
elif is_student and is_social:
    print("You are a Chad.")
elif is_student and not is_social:
    print("Its alright, You will be fine.")
elif not is_student and is_social:
    print("You have a higher chance to not be depressed.")
else:
    print("Buckle up mate, Its time to be Chad.")
