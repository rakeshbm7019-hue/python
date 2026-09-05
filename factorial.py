def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial (recursive):", factorial(5))

import math
print("Factorial (math):", math.factorial(5))
