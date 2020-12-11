#!/usr/bin/env python

ans = 1
prev = 1
for i in range(2, 1001, 2):
    for j in range(4):
        ans += prev + i
        prev = prev + i

print(ans)