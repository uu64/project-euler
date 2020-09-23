# -*- coding: utf-8 -*-

def next_fibo(prev, current, i, sum):
    if current % 2 == 0:
        sum += current
    if current <= 4000000:
        next_fibo(current, prev + current, i + 1, sum)
    else:
        print(sum)

# 第一項目
next_fibo(0, 1, 1, 0)
