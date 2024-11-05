from homework import Homework
from exam import Exam
from grade import ExamG
from weakgrade import ExamH

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

print("____________ ExamG ___________")
first = ExamG()
first.math_grade = 34
first.alg_grade = 13
first.prog_grade = 55

print(f"egzamin - I termin: matematyka -> {first.math_grade}, algorytmika -> {first.alg_grade}, "
      f"programowania -> {first.prog_grade}")


sec = ExamG()
sec.math_grade = 54
sec.alg_grade = 73
sec.prog_grade = 89

print(f"egzamin - II termin: matematyka -> {sec.math_grade}, algorytmika -> {sec.alg_grade}, "
      f"programowania -> {sec.prog_grade}")

print(f'podajmy wyniki I egzaminu z archiwum:\n')

print(f"egzamin archiwum - I termin: matematyka -> {first.math_grade}, algorytmika -> {first.alg_grade}, "
      f"programowania -> {first.prog_grade}")

print("____________ ExamH ___________")
first = ExamH()
first.math_grade = 23
first.alg_grade = 11
first.prog_grade = 45

print(f"egzamin H - I termin: matematyka -> {first.math_grade}, algorytmika -> {first.alg_grade}, "
      f"programowania -> {first.prog_grade}")


sec = ExamH()
sec.math_grade = 54
sec.alg_grade = 73
sec.prog_grade = 89

print(f"egzamin H - II termin: matematyka -> {sec.math_grade}, algorytmika -> {sec.alg_grade}, "
      f"programowania -> {sec.prog_grade}")

print(f'podajmy wyniki I egzaminu z archiwum:\n')

print(f"egzamin H archiwum - I termin: matematyka -> {first.math_grade}, algorytmika -> {first.alg_grade}, "
      f"programowania -> {first.prog_grade}")

pop = ExamH()
pop.math_grade = 88
pop.alg_grade = 95
pop.prog_grade = 94

print(f"egzamin H poprawka: matematyka -> {pop.math_grade}, algorytmika -> {pop.alg_grade}, "
      f"programowania -> {pop.prog_grade}")

print("HISTORIA:\n")
print(f"egzamin H - II termin: matematyka -> {sec.math_grade}, algorytmika -> {sec.alg_grade}, "
      f"programowania -> {sec.prog_grade}")
print(f"egzamin H - I termin: matematyka -> {first.math_grade}, algorytmika -> {first.alg_grade}, "
      f"programowania -> {first.prog_grade}")
