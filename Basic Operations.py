from math import *
# importing external code to access functions


# use comments to either explain some advanced code or to check for errors and related by commenting out code
# use '#' to comment out a single code
''' 
use three quotes to comment out multiple blocks of code
'''


place_name = "New York"
year = 2013
wasGood = True
print("I went to " + place_name + '.')
print("It was the year", year)
# use ',' while adding integral values in print statements

# alternate process for integral print complications
print("It was the year " + str(year))
print(wasGood)
place_name = "Washington DC"
print("I went to " + place_name + '.')


print("Analysis\nof Earth")
print("Analysis \"of\" Earth")
phrase = "Rockwell Life Insurance"

# string common functions
print(phrase.lower())
print(phrase.isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("e"))
print(phrase.index("Life"))
# index gives location of first instance
print(phrase.replace("Life", "Home"))


print(33/(3*8.85))
print(10 % 3)
# '%' is the modulus function which returns the remainder after division
number = 5
print(str(number))
# changes the variable to string

number = -10
print(abs(number))
print(pow(3, 2))
print(pow(number, 3))
print(max(number, 4))
print(min(number, 4))
print(round(3.44))

# importing of external code or module done at start of file to access the next functions
print(floor(3.9))
print(ceil(3.1))
number = 16
print(sqrt(number))


name = input("Enter Your Name: ")
age = input("Enter Your Age: ")
print("Hello " + name + ". You are " + age + ".")


# basic calculator
num1 = input("Enter a Number: ")
num2 = input("Enter another Number: ")
# python by default takes input as string data type
result = int(num1) + int(num2)
print(result)

# we use float function for decimal values
num1 = input("Enter a Number: ")
num2 = input("Enter another Number: ")
result = float(num1) + float(num2)
print(result)
