import time
import functools
from concurrent.futures import ThreadPoolExecutor

# Decorator for caching results
def cache_results(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Cache hit for {args}")
            return cache[args]
        print(f"Computing result for {args}")
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@cache_results
def expensive_computation(x, y):
    time.sleep(2)  # simulate heavy work
    return x ** y

# Run computations concurrently
def run_tasks():
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(expensive_computation, i, 3) for i in range(1, 6)]
        for f in futures:
            print("Result:", f.result())

if __name__ == "__main__":
    run_tasks()
    # Second run will be faster due to caching
    run_tasks()
