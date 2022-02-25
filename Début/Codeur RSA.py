import random

np = []
for n in range(2, 10000000):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        np.append(n)
        print(n/1000000)
print(np)
