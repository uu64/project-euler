#!/usr/bin/env python3

def sieve(limit):
    is_prime = [True for _ in range(limit)]
    # primes = []

    is_prime[0] = is_prime[1] = False
    for i in range(2, len(is_prime)):
        if is_prime[i]:
            # primes.append(i)
            for j in range(i*2, len(is_prime), i):
                is_prime[j] = False

    # remove not circular primes
    circular_primes = set()
    for i in range(2, len(is_prime)):
        if is_prime[i]:
            s_prime = str(i)
            for j in range(1, len(s_prime)):
                tmp = int(f"{s_prime[j:]}{s_prime[:j]}")
                if not is_prime[tmp]:
                    is_prime[i] = False
                    break

        if is_prime[i]:
            circular_primes.add(i)

    return circular_primes


ans = sieve(1000000)
# ans = sieve(100)
print(ans)
print(len(ans))

