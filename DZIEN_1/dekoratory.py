import time

#przykład 1
def pomiarczasu(funkcja):
    def wrapper():
        starttime = time.time()
        funkcja()
        endtime = time.time()
        wynik = endtime - starttime
        print(f"czas wykonania funkcji: {wynik} s")
    return wrapper

def usypiacz(funkcja):
    def wrapper():
        time.sleep(3)
        return funkcja()
    return wrapper


@pomiarczasu
@usypiacz
def big_lista():
    sum([i**5 for i in range(10_000_000)])

big_lista()
