#!/usr/bin/env python
import eulerlib

cache = {}

def is_prime(n):
    if n in cache:
        return cache[n]
    if n < 2:
        cache[n] = False
        return False
    if n == 2:
        cache[n] = True
        return True
    for p in range(3, n, 2):
        if n % p == 0:
            cache[n] = False
            return False
    cache[n] = True
    return True

ans = 0
max = 0
for i in range(-1000, 1001):
    for j in range(3, 1001):
        n = 0
        while True:
            tmp = n*n + i*n + j
            if not is_prime(tmp):
                if max < n:
                    max = n
                    ans = i * j
                break
            n += 1

print(ans)