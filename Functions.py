def sayHi(name, age):
    print('Hello ' + str(name) + ', you are ' + str(age))


a = input("Type your name : ")
b = input("Type your age : ")
sayHi(a, b)


def cube(num):
    answer = num*num*num
    return answer


a = float(input("The Number whose cube is required : "))
print(cube(a))


# using functions and if statements and try//except error catching
def max_num(num1, num2, num3):
    try:
        num1 = float(num1)
        num2 = float(num2)
        num3 = float(num3)
        if num1 >= num2 and num1 >= num3:
            print(num1, "is the Maximum Value.")
        elif num2 >= num1 and num2 >= num3:
            print(num2, "is the Maximum Value.")
        else:
            print(num3, "is the Maximum Value.")
    except ValueError as err:
        print(err)
    ''' Alternate Except -
    except ValueError:
        print('Invalid Input.')'''


print("Type 3 numbers and the program will return the maximum value: ")
[x, y, z] = [input(), input(), input()]
max_num(x, y, z)
