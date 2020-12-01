#!/usr/bin/env python

import math

d = {}

def get_divisor_sum(number):
    divisors = {1}
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            divisors.add(i)
            divisors.add(int(number / i))
    return sum(divisors)


def is_amicable(a):
    if not a in d:
        b = get_divisor_sum(a)
        d[a] = b
    else:
        b = d[a]

    if not b in d:
        d[b] = get_divisor_sum(b)

    return d[b] == a and a != b

ans = 0
for i in range(1, 10001):
    if is_amicable(i):
        ans += i

print(ans)
