#!/usr/bin/env python3

def rec(s, coins):
    if s == 200:
        return 1

    if s < 200:
        count = 0
        for i, v in enumerate(coins):
            count += rec(s + v, coins[i:])
        return count

    return 0

print(rec(0, [1, 2, 5, 10, 20, 50, 100, 200]))

