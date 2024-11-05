from homework import Homework

print("____________ Homework ___________")
g = Homework()
g.grade = 93
assert g.grade >= 90
print(f'ocena za projekt: {g.grade}')
