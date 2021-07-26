#!/usr/bin/env python3

def is_prime(number):
    i = 2
    while i*i <= number:
        if number % i == 0:
            return False
        i += 1
    return number != 1

def is_truncatable_prime(number):
    if not is_prime(number):
        return False

    s = str(number)
    truncated = set()
    for i in range(1, len(s)):
        truncated.add(int(s[i:]))
        truncated.add(int(s[:-i]))

    for i in truncated:
        if not is_prime(i):
            return False

    return True

count = 0
ans = 0
num = 11
while count < 11:
    if is_truncatable_prime(num):
        print(num)
        ans += num
        count += 1
    num += 2

print(ans)

