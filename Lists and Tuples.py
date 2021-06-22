subjects = ['Economics', 'Accountancy', 'English', 'Chemistry']
print(subjects[0])
print(subjects[-1])
print(subjects[0:2])

subjects[1] = 'Physics'
grades = [34, 55, 91, 31]

# using list functions
subjects.extend(grades)
subjects.append('Biology')
subjects.insert(2, 'Bengali')
grades.remove(91)
grades.clear()
print(subjects.pop())
print(subjects.index('English'))
print(subjects.count('Economics'))

friends = ['Karen', 'Jacob', 'John']
friends.sort()
print(friends)
friends2 = friends.copy()
print(friends2)


coordinates = (0, 2)
# tuples are immutable, cannot be modified
coordinates_list = [(4, 2), (2, 1), (0, 7)]
print(coordinates_list)
