#!/usr/bin/env python

exp = 5
# 9**5 * 7 = 413343 < 1000000
MAX = 9**exp * 6 # 354294

# exp = 4
# # 9**4 * 6 = 39366 < 100000
# MAX = 9**exp * 5 # 32805

ans = 0
for i in range(2, MAX + 1):
    s = str(i)
    l = len(s)

    tmp = 0
    for j in range(l):
        tmp += int(s[-(j+1)]) ** exp
    if tmp == i:
        print(i)
        ans += i


print(ans)
