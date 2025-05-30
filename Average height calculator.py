student_heights = input("Enter your heights in centimete\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
avg_height = 0
total_height = 0
for each_height in student_heights:
    height = each_height
    height1 = (each_height / (n+1))
    avg_height += height1
    total_height = total_height + height
print(f"your total height is {total_height}cms")
print(f"Total number of people is {n+1}")
print(f"your avg height is {round(avg_height, 2)}cms")
# print(n)
# n replaces being 0 , 1 ,2 and so on till x-1 places where x
# is the number of items in the list


# list = ["a", "b", "c"]
# print(len(list))
# gives 3