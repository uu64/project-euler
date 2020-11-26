#!/usr/bin/env python

youbi = {
    0: "mon",
    1: "tue",
    2: "wed",
    3: "thu",
    4: "fri",
    5: "sat",
    6: "sun",
}

def is_leap(year):
    return year%4 == 0 and (year%400 == 0 or year%100 != 0)


def get_days(month, is_leap):
    if month == 9 or month == 4 or month == 6 or month == 11:
        return 30
    elif month == 2:
        return 29 if is_leap == True else 28
    else:
        return 31

sum_days = 0
ans = 0
for y in range(1900, 2001):
    for m in range(1, 13):
        sum_days += get_days(m, is_leap(y))%7
        mod = sum_days%7
        if y!= 1900 and mod == 6:
            ans += 1

print(ans)