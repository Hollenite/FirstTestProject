student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
highest_score = 0
for each_score in student_scores:
    if each_score > highest_score:
        highest_score = each_score


print(highest_score)