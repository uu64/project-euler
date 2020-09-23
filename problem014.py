# -*- coding: utf-8 -*-

MAX = 1000000
memo = {1: 1}


for i in range(2, MAX + 1):
    n = i
    history = []
    history.append(n)
    while True:
        if n % 2 == 0:
            next = n/2
        else:
            next = 3*n + 1

        if next in memo:
            while len(history) > 0:
                tmp = history.pop()
                memo[int(tmp)] = memo[next] + 1
                next = tmp
            break
        else:
            n = next
            history.append(n)

memo = sorted(memo.items(), key=lambda x:x[1])
# print(memo)
print(memo[-1])