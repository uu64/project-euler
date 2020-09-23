# -*- coding: utf-8 -*-

terms = [1]
for i in range(2, 21):
    for number in terms:
        if number == 1:
            continue
        else:
            if i % number == 0:
                i /= number
    if i != 1:
        terms.append(int(i))

result = 1
for i in terms:
    result *= i

print(result)