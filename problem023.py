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


for i in range (2, MAX + 1):
    if is_abundant(i):
        abundants.append(i)

is_abundant_sum = [ False for i in range(MAX+1) ]
for i in abundants:
    for j in abundants:
        if i+j <= MAX:
            is_abundant_sum[i+j] = True
        else:
            break

ans = 0
for i in range(1, MAX+1):
    if not is_abundant_sum[i]:
        ans += i

print(ans)