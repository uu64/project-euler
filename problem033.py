#!/usr/bin/env python

# x / y
# x = a*10 + b
# y = c*10 + d

def is_digit_cancelling_fractions(x, y):
    a = int(x / 10)
    b = int(x % 10)
    c = int(y / 10)
    d = int(y % 10)
    if b == c and a != d and a*j == d*i:
        return True, (a, d)
    if a == d and b != c and b*j == c*i:
        return True, (b, c)
    return False, None

bunshi = 1
bunbo = 1
for i in range(10, 100):
    for j in range(i, 100):
        is_dcf, nums = is_digit_cancelling_fractions(i, j)
        if is_dcf:
            bunshi *= nums[0]
            bunbo *= nums[1]

while True:
    if bunbo % bunshi != 0 or bunshi == 1:
        break
    bunbo /= bunshi
    bunshi /= bunshi

print(bunbo)
