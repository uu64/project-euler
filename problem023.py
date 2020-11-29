#!/usr/bin/env python

import math

MAX = 28123
abundants = []

def is_abundant(number):
    divisors = {1}
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            divisors.add(i)
            divisors.add(int(number / i))
    return sum(divisors) > number


def is_abundant_sum(number):
    for i in abundants:
        if (number - i) in abundants:
            return True
    return False


for i in range (2, MAX + 1):
    if is_abundant(i):
        abundants.append(i)

ans = 0
for i in range(24, MAX + 1):
    print(i)
    if not is_abundant_sum(i):
        ans += i

print(ans)
