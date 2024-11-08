class Grade:
    def __init__(self):
        self._value = 0
        
    def __get__(self, instance, owner):
        return self._value
    
    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("ocena musi byc wartością z przedziału 0-100!")
        self._value = value
        
        
class ExamG:
    math_grade = Grade()
    alg_grade = Grade()
    prog_grade = Grade()
