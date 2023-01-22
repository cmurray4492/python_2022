"""Factorial Function From Deitel Book"""
import time

start_time = time.time()


def factorial(number):
    """Return a factorial number"""
    if number <= 1:
        return 1
    return number * factorial(number - 1)  # recursive call


# If range is much larger there is a recursion error
for i in range(50):
    print(f'{i}! = {factorial(i)}')

end_time = time.time()

total_time = end_time - start_time
print(total_time)
