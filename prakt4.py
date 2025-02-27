import time

def timer_wrapper(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Час виконання функції {func.__name__}: {execution_time:.6f} секунд")
        return result

    return wrapper


def prime_generator():
    primes = []
    num = 2

    while True:
        is_prime = True

        for prime in primes:
            if prime * prime > num:
                break

            if num % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)
            yield num

        num += 1


def fibonacci_seq_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


@timer_wrapper
def prime_num_getter(n):
    gen = prime_generator()
    primes = [next(gen) for _ in range(n)]

    print(f"Перші {n} простих чисел: {primes}")
    return primes


@timer_wrapper
def fibonacci_num_getter(n):
    gen = fibonacci_seq_generator()
    fibonacci_numbers = [next(gen) for _ in range(n)]

    print(f"Перші {n} чисел Фібоначчі: {fibonacci_numbers}")
    return fibonacci_numbers


if __name__ == "__main__":
    print("Демонстрація роботи з простими числами:")
    prime_num_getter(10)

    print("\nДемонстрація роботи з числами Фібоначчі:")
    fibonacci_num_getter(10)