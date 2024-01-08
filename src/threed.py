import threading
import time


def calc_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def calc_factorial_without_threading(n):
    start_time = time.time()
    result = calc_factorial(n)
    end_tim = time.time()
    print(end_tim - start_time)
    return result


def calc_factorial_with_threading(n):
    start_time = time.time()

    thread = threading.Thread(target=calc_factorial, args=(n,))
    thread.start()
    thread.join()
    end_tim = time.time()
    print(end_tim - start_time)
    return

