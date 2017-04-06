num_students = int(input("How many students in this class? "))
roster = []
grades = []
names = []
second_low = 0

while num_students > 0:
    name = input("What is the first name? ")
    grade = float(input("What is their grade? "))
    roster.append([name, grade])
    num_students -= 1

for name, grade in roster:
    grades.append(grade)
    grades = sorted(list(set(grades)))

second_low = grades[1]

for name, grade in roster:
    if grade == second_low:
        names.append(name)

names.sort()
print('\n'.join(names))
