import random
names = ["obi", "nduka", "ken","nnena"]
student_scores = {name : random.randint(1,100) for name in names}
passed_student = {student:score for (student , score) in student_scores.items() if score >= 60}
print(passed_student)

