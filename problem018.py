# -*- coding: utf-8 -*-
numbers = []
for i in range(15):
    numbers.append(list(map(int, input().split())))

for i in range(1, len(numbers)):
    for j in range(len(numbers[i])):
        l = 0
        r = 0
        if j != 0:
            l = numbers[i-1][j-1]
        if j != len(numbers[i]) - 1:
            r = numbers[i-1][j]

        numbers[i][j] += max(l, r)

print(max(numbers[-1]))