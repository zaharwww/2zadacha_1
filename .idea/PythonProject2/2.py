import time

def log(mes, log_file):
    current_time = round(time.time() - START_TIME, 5)
    log_file.write(f"[{current_time}s] {mes}\n")

def binary_r(func, interval, epsilon, log_file):
    a, b = interval
    fa, fb = func(a), func(b)

    log(f"Проверка: f({a})={fa}, f({b})={fb}", log_file)

    if fa * fb > 0:
        log("Нет корней", log_file)
        return None

    def search(a, b):
        mid = (a + b) / 2
        fmid = func(mid)

        log(f"Середина: x={mid}, f(x)={fmid}", log_file)

        if abs(fmid) < epsilon:
            log("Сходимость", log_file)
            return mid

        if func(a) * fmid < 0:
            return search(a, mid)
        else:
            return search(mid, b)

    return search(a, b)

def binary_i(func, interval, epsilon, log_file):
    a, b = interval
    fa, fb = func(a), func(b)

    log(f"Проверка: f({a})={fa}, f({b})={fb}", log_file)

    if fa * fb > 0:
        log("Нет корней", log_file)
        return None

    while True:
        mid = (a + b) / 2
        fmid = func(mid)

        log(f"Середина: x={mid}, f(x)={fmid}", log_file)

        if abs(fmid) < epsilon:
            log("Сходимость", log_file)
            return mid

        if func(a) * fmid < 0:
            b = mid
        else:
            a = mid

def test_function(x):
    return x ** 3 - x - 2 - x ** 4 + x ** 5

if __name__ == "__main__":
    epsilon = 1e-5
    interval = [-1000, 1000]
    START_TIME = time.time()

    with open("recursive_log.txt", "w") as log_file:
        START_TIME = time.time()
        log("Начало", log_file)
        root_recursive = binary_r(test_function, interval, epsilon, log_file)
        log(f"Найденный корень: x={root_recursive}", log_file)

    with open("iterative_log.txt", "w") as log_file:
        START_TIME = time.time()
        log("Начало", log_file)
        root_iterative = binary_i(test_function, interval, epsilon, log_file)
        log(f"Найденный корень: x={root_iterative}", log_file)

    print(f"Рекурсивный метод нашёл корень: x = {root_recursive}")
    print(f"Итеративный метод нашёл корень: x = {root_iterative}")

    with open("recursive_log.txt", "r") as log_file:
        content = log_file.read()
        print(content)
    with open("iterative_log.txt", "r") as log_file:
        content_1 = log_file.read()
        print(content_1)
