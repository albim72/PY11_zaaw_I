import threading

def worker(num,shared_variable):
    shared_variable.append(num)
    print(f'Wątek {threading.current_thread()} dodał {num} do zmiennej współdzielonej')

shared_vaiable = []
threads= []

for i in range(5):
    t = threading.Thread(target=worker,args=(i,shared_vaiable))
    threads.append(t)
    t.start()

for t  in threads:
    t.join()

print(f'zmienna współdzielona po zakończeniu pracy wątków: {shared_vaiable}')
