#!/usr/bin/env python3

# NOTE: 9! * 8 = 2903040 < 10000000
MAX = 362880 * 7
factorials = {
    '0': 1,
    '1': 1,
    '2': 2,
    '3': 6,
    '4': 24,
    '5': 120,
    '6': 720,
    '7': 5040,
    '8': 40320,
    '9': 362880
}
ans = 0

for i in range(10, MAX + 1):
    s = str(i)
    fac_sum = 0
    for c in s:
        fac_sum += factorials[c]

    if fac_sum == i:
        ans += fac_sum
        print(i)

print(ans)

