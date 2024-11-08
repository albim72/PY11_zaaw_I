import time
import concurrent.futures
from funkcja_prime import find_the_sum_prime_nums

numbers = [(1,10_000),(3,50_000),(5_000,100_000),(4,900),(8_000,15_000),(95_000,133_000),(200,67_340)]

def synchronicznie():
    starttime = time.time()
    for pair in numbers:
        st = time.time()
        prime_suma = find_the_sum_prime_nums(*pair)
        et = time.time()
        print(f'wynik = {prime_suma}, czas wykonania: {et-st} s')
    end_time = time.time()

    print(f'całkowity czas wykonania wszystkich sum (synchronicznie): {end_time - starttime} s')

def run_heavy_function(params):
    return find_the_sum_prime_nums(*params)

def asynchronicznie():
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        result = executor.map(run_heavy_function,numbers)
    end_time = time.time()
    print(list(result))
    print(f'całkowity czas wykonania wszystkich sum (asynchronicznie): {end_time - start_time} s')

def main():
    synchronicznie()
    asynchronicznie()

if __name__ == '__main__':
    main()
