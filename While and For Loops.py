num = float(input("Enter the Number whose Booster Array is required: "))
# booster array is just a hypothetical function
while num > 1:
    a = num - 1
    print(num * a)
    num -= 1
print(1.0)


food = ["Noodles",  "Chicken Wings", "Ice Cream"]
for i in range(len(food)):
    print(food[i])


def self_exponential(x):
    if x >= 0:
        result = 1
        for n in range(x):
            result = result*x
        return result
    elif x < 0:
        return "Negative Value is out of scope."


exp_num = int(input("Enter the Number to be Self Raised: "))
print(self_exponential(exp_num))
