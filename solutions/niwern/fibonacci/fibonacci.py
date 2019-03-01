import time


def fib(n):
    n_fib = 0
    n2_fib = 1
    if n == 0:
        return n_fib

    elif n == 1:
        return n2_fib

    for i in range(n - 1):
        t = n2_fib
        n2_fib = n_fib + n2_fib
        n_fib = t

    return n2_fib


def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


def fib3(n):
    fib_list = [0, 1]

    if n >= 1:
        for i in range(n - 1):
            fib_list.append(fib_list[-1] + fib_list[-2])

    return fib_list[n]


if __name__ == '__main__':
    count = 900
    repeat = 1000
    fib1_total = 0
    fib2_total = 0
    fib3_total = 0

    for i in range(repeat):
        start = time.time()
        fib(count)
        stop = time.time()

        fib1_total += stop - start

        start = time.time()
        fib2(count)
        stop = time.time()

        fib2_total += stop - start

        start = time.time()
        fib3(count)
        stop = time.time()

        fib3_total += stop - start

    print("######################")
    print("##  final solution  ##")
    print("######################\n")

    print('fib1 average: ', fib1_total/repeat)
    print('fib2 average: ', fib2_total/repeat)
    print('fib3 average: ', fib3_total/repeat)
