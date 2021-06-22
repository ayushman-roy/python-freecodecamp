majors = open("Student Majors.txt", "r")

'''
File Mode Types -
"r" = read
"w" = write
"a" = append 
"r+" = read and write
'''

if majors.readable():
    print(majors.readline())
    print(majors.readline(5))

print(majors.readlines()[2])

for major in majors.readlines():
    print(major)

print(majors.read())

majors.close()


a_majors = open("Student Majors.txt", "a")

print("Be Careful as your following entries will affect external files.")
user_input1 = input("Enter Your Name : ")
user_input2 = input("Enter Your Major : ")
if a_majors.writable():
    a_majors.write("\n" + user_input1 + " - " + user_input2)
else:
    print("File is not writeable.")

a_majors.close()


'''
w_majors = open("Student Majors.txt", "w")
'''

'''
z_majors = open("Student Majors.html", "w")
'''

'''
when in writing mode, it will overwrite the entire file

if w_majors.writable():
    w_majors.write("USER INPUT.")
'''

'''
if z_majors.writable():
    z_majors.write("<p>USER INPUT.<p/>")
'''

'''
w_majors.close()
'''
