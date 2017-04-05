num_students = int(input())
roster = []

while num_students > 0:
    name = input()
    grade = float(input())
    roster.append([name, grade])
    num_students -= 1

print(sorted(roster))
print(sorted(roster, key=lambda name: name[1]))


# name_grade.append(['Adam', 87])
# name_grade.append(['Betty', 90])
# name_grade.append(['Frank', 85])

# print(sorted(name_grade))
# name_grade = (sorted(name_grade, key=lambda name: name[1]))


# for i in name_grade:
#     print(name_grade[i][1])