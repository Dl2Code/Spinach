from random import shuffle
import numpy as np

students = []
n = int(input("\nHow many students? "))
print("Please input the students name under here\n")
for _ in range(n):
    students.append(str(input("")))

students = list(filter(None, students))
print("\nThere are", len(students), "students & all of them will be shuffled in a group")
groups = int(input("How many groups do you want to create? "))

shuffle(students)
students_group = np.array_split(np.array(students), groups)
for i in range(groups):
    print("\n\n   __[Group " + str(i + 1) + "]__\n")
    count = 1
    for j in students_group[i]:
        print(str(count) + ". " + j)
        count += 1
