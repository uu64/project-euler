#!/usr/bin/env python3

target = (1, 10, 100, 1000, 10000, 100000, 1000000)

d = 1
while 9*d*10**(d-1) < target[-1]:
    d += 1

s = ''.join([str(i) for i in range(1, 10**d)])

ans = 1
for i in target:
    ans *= int(s[i - 1])
print(ans)

