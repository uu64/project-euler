#!/usr/bin/env python3

import math

# NOTE: 9! * 8 = 2903040 < 10000000
MAX = math.factorial(9) * 7

for i in range(3, MAX + 1):
    fac_sum = 0
    for c in str(i):
        fac_sum += math.factorial(int(c))
    if fac_sum == i:
        print(i)

