day_conversions = {
    "sun": "Sunday",
    "mon": "Monday",
    "tue": "Tuesday",
    "wed": "Wednesday",
    "thur": "Thursday",
    "fri": "Friday",
    "sat": "Saturday"
}
# you can also use integral value for keys

print(day_conversions["thur"])
a = input("Enter the Key: ")
print(day_conversions.get(a.lower(), "Key is Invalid."))


# 2D lists and 3D lists

num_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

num_grid_1 = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
]

print(num_grid[1][2])
print(num_grid_1[1][0][2])


# nested for loops

for row in num_grid:
    for col in row:
        print(col)

for row in num_grid_1:
    for col in row:
        for item in col:
            print(item)
