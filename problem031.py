#!/usr/bin/env python3

coins = [1, 2, 5, 10, 20, 50, 100, 200]
amount = 200
memo = {}

def rec(cur, coins):
    global memo
    if cur == amount:
        return 1

    if cur < amount:
        count = 0
        for i, v in enumerate(coins):
            new = cur + v
            if new > 200:
                continue
            if (v, new) not in memo:
                res = rec(new, coins[i:])
                memo[(v, new)] = res
            count += memo[(v, new)]
        return count

    return 0

print(rec(0, coins))

