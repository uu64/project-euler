# -*- coding: utf-8 -*-

def get_primes(limit):
    max = int(limit**0.5)
    # 2以外の偶数は素数じゃないので予め除く
    numbers = [i for i in range(3, limit+1, 2)]
    idx = 0
    while True:
        n = numbers[idx]
        if n > max:
            break
        numbers = list(filter(lambda x: x<=n or x%n!=0, numbers))
        idx += 1
    # 除いた2を足す
    numbers.insert(0, 2)
    return numbers