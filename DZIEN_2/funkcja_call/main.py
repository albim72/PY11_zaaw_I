"""
Trzy przypadki użycia funckji __call__
1. licznik wywołań funckji
2. walidacja danych wejściowych
3. implementacja z pamięcią podręczną  (caching)
"""
from libcalls.counter import CallCounter

counter = CallCounter()
counter()
counter()
counter()
counter()
