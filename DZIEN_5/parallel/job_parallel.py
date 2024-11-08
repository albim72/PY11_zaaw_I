import math
import sys

sys.set_int_max_str_digits(1000000)

from joblib import Parallel, delayed

def compute_factorial(n):
    print(f"obliczanie silnii {n}")
    return math.factorial(n)

numbers = [5,7,19,112,180,260,400,10000]

results = Parallel(n_jobs=4)(delayed(compute_factorial)(n) for n in numbers)

print(f'wyniki silnia: {results}')
