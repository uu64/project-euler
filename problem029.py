#!/usr/bin/env python

A_MAX = 100
B_MAX = 100
ans = set()

for a in range(2, A_MAX + 1):
    n = a
    for b in range(2, B_MAX + 1):
        n *= a
        ans.add(n)

print(len(ans))

