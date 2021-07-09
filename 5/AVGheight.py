student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
list_len = 0

for student in student_heights:
    total_height += student
    list_len += 1

avg = total_height / list_len

rounded = round(avg)

print(f"The average student height is {rounded}.")