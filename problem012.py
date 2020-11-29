# -*- coding: utf-8 -*-
import eulerlib


def tri_number_generator():
    idx = 1
    tri_number = 0
    while True:
        tri_number += idx
        idx += 1
        yield tri_number


def main():
    # TODO: 素数の数をどう決めるか
    primes = eulerlib.get_primes(100000)

    for number in tri_number_generator():
        i = number
        exp_count = 0
        divisor_count = 1
        idx = 0
        prime = primes[idx]
        while True:
            if i % prime == 0:
                i /= prime
                exp_count += 1
            else:
                divisor_count *= (exp_count + 1)
                exp_count = 0
                idx += 1
                prime = primes[idx]
            if i == 1:
                divisor_count *= (exp_count + 1)
                break
        if divisor_count > 500:
            break

    print(number)


if __name__ == "__main__":
    main()