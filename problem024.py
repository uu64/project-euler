#!/usr/bin/env python

DIGITS = 10
INDEX = 1000000

counter = 0
def f(s, num_set):
    global counter
    if len(num_set) == 0:
        counter += 1
        if counter == INDEX:
            print(s)

    for i in num_set:
        c = str(i)
        tmp = num_set[:]
        tmp.remove(c)
        f(s+c, tmp)
        if counter == INDEX:
            return

f('', [ str(i) for i in range(DIGITS) ])
