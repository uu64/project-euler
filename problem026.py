# -*- coding: utf-8 -*-
# 参考: http://kj02db.kanazawa-gu.ac.jp/fujimoto/tips/divdec.html

MAX = 1000

def is_finite(number):
    while True:
        if number % 2 == 0:
            number /= 2
        else:
            break
    while True:
        if number % 5 == 0:
            number /= 5
        else:
            break
    return number == 1


def get_recurring_section(number):
    result = ""
    remainder = []
    dividend = 10
    while True:
        q, r = divmod(dividend, number)
        if r in remainder:
            index = result.find(str(q))
            return result[index:]
        else:
            result += str(q)
            dividend = r*10
            remainder.append(r)


def main():
    result = {}
    for i in range(1, MAX+1, 2):
        if is_finite(i):
            continue
        else:
            result[i] = get_recurring_section(i)

    sorted_result = sorted(result.items(), key=lambda x:len(x[1]))
    print(sorted_result[-1])
    print(len(sorted_result[-1][1]))

if __name__ == '__main__':
    main()