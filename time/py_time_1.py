"""A simple program todemonstrate how to measure Python execution time"""
import time

start_time = time.time()

total = 0
for i in range(1, 5000):
    for j in range(1, 5000):
        total += i
        total += j

end_time = time.time()

total_time = end_time - start_time
print(total_time)
