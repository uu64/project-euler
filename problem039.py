#!/usr/bin/env python3

c_max = 0
ans = 0
for p in range(4, 1001):
    count = 0
    # k < i + j
    for k in range(1, int(p/2)):
        for i in range(1, int(p/2)):
            j = p - (i + k)
            if k*k == i*i + j*j:
                # print(f"{i}, {j}, {k}")
                count += 1
    if ans < count:
        ans = p

print(ans)
