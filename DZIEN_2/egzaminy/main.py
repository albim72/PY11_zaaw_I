from homework import Homework
from exam import Exam

print("____________ Homework ___________")
g = Homework()
g.grade = 93
assert g.grade >= 90
print(f'ocena za projekt: {g.grade}')

print("____________ Exam ___________")
ex = Exam()
ex.part_a_grade = 88
ex.part_b_grade = 67

assert ex.part_a_grade >= 80
assert ex.part_b_grade >= 55

print(f'ocena całościowa: A -> {ex.part_a_grade}, B -> {ex.part_b_grade}')
