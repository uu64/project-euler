# -*- coding: utf-8 -*-

product = 1

for i in range(2, 100):
    product = product * i

s = str(product)
array = list(map(int, s))

print(sum(array))