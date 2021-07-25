#!/usr/bin/env python3

MAX = 1000000

ans = 0
for i in range(MAX):
    s_decimal = str(i)
    if not s_decimal == s_decimal[::-1]:
        continue

    s_binary = '{:b}'.format(i)
    if not s_binary == s_binary[::-1]:
        continue

    ans += i

print(ans)
