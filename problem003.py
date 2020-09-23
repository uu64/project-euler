# -*- coding: utf-8 -*-

prime_list = []

def get_next_prime(current):
    next = current + 1
    while True:
        for prime in prime_list:
            if next % prime == 0:
                break
            else:
                prime_list.append(next)
                return next
        next += 1


def trial_division(number):
    result = []
    if number < 2:
        return 1
    prime = 2
    prime_list.append(prime)
    while number != 1:
        if number % prime == 0:
            number /= prime
            result.append(prime)
        else:
            prime = get_next_prime(prime)
    return result

print(trial_division(600851475143))

