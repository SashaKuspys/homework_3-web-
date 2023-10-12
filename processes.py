import time
import multiprocessing


def factorize(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors


def factorize_sync(*numbers):
    results = []
    for num in numbers:
        factors = factorize(num)
        results.append(factors)
    return results


def factorize_parallel(*numbers):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(factorize, numbers)
    return results


# Перевірка часу виконання функції factorize
start_time_factorize = time.time()
a, b, c, d = factorize_sync(128, 255, 99999, 10651060)
end_time_factorize = time.time()
print("Час виконання функції factorize: {:.4f} секунд".format(end_time_factorize - start_time_factorize))

# Перевірка часу виконання синхронної версії
start_time = time.time()
a, b, c, d = factorize_sync(128, 255, 99999, 10651060)
end_time = time.time()
print("Час виконання синхронної версії: {:.4f} секунд".format(end_time - start_time))

# Перевірка часу виконання покращеної версії (паралельні обчислення)
start_time_parallel = time.time()
a, b, c, d = factorize_parallel(128, 255, 99999, 10651060)
end_time_parallel = time.time()
print("Час виконання покращеної версії (паралельні обчислення): {:.4f} секунд".format(
    end_time_parallel - start_time_parallel))

# Перевірка результатів
assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
             1521580, 2130212, 2662765, 5325530, 10651060]
