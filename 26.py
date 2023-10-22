#Create a dictionary of student names and their scores, then find the average score
student_scores = {'Akash': 85,'Mahendra': 92,'Rohan': 78,'Atipra': 95,'Ram': 88}
average_score = sum(student_scores.values()) / len(student_scores)
print("Student Scores: ")
for name, score in student_scores.items():
    print(f"{name}: {score}")
print("\nAverage Score:", average_score)
