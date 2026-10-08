num_students = int(input("Enter the number of students in the class: "))
total_class_score = 0

for i in range(num_students):
    print(f"\nEnter scores for student {i + 1}:")

total_score = 0 

for j in range(5):
    score = float(input(f"Enter score for test {j + 1}: "))
    total_score += score

average_score = total_score / 5
print(f"Average score for student {i + 1}: {average_score:.2f}")

total_class_score = total_score+total_class_score
print(total_class_score)

overall_class_average = total_class_score / (num_students * 5)
print(f"\nOverall average score for the class: {overall_class_average:.2f}")