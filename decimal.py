from decimal import Decimal

n = int(input())
total = 0
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

for i in student_marks[query_name]:
    total += i

avg = Decimal(total/3)
print(round(avg,2))