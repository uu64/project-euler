#!/usr/bin/env python

def fib(prev, now):
    return prev + now

p1 = 1
p2 = 1
count = 2
while True:
    tmp = fib(p1, p2)
    p1 = p2
    p2 = tmp
    count += 1
    if len(str(tmp)) == 1000:
        print(count)
        break
