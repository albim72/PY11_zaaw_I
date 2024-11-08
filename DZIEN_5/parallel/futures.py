import concurrent.futures
import time

def task(n):
    print(f"start zadania {n}")
    time.sleep(2)
    print(f"koniec zdarzenia {n}")
    return n*2

with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
    futures = [executor.submit(task,i) for i in range(5)]
    results = [future.result() for future in concurrent.futures.as_completed(futures)]

print(f"Wyniki: {results}")
