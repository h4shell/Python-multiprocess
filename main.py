import multiprocessing
from time import sleep


def fun1(y, i):
    sleep(100)

    while i <= 3:
        print(i)
        y[i] = {'Type': 'fx', 'ID': 2}
        i = i + 1


def fun2(x, i):
    print(x)
    while i <= 10:
        print(i)
        x[i] = {'Type': 'fx', 'ID': 1}
        i = i + 1


if __name__ == '__main__':
    with multiprocessing.Manager() as manager:

        # Inizializzo le variabili come multiprocessing.Manager()
        x = manager.dict()
        y = manager.dict()

        # dichiaro variabili di istanza
        i = 0

        # configuro i processi
        f1 = multiprocessing.Process(target=fun1, args=(y, i,))
        f2 = multiprocessing.Process(target=fun2, args=(x, i,))

        # avvio i processi
        f1.start()
        f2.start()

        # aspetto che i processi terminino
        f1.join()
        f2.join()

        # Done
        print(x)
        print("\n\n\n\n")
        print(y)
