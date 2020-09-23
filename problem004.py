# -*- coding: utf-8 -*-

def is_kaibun(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False

palindromic_number= []

for i in range(999, 100, -1):
    flag = False
    for j in range(999, 100, -1):
        number = i*j
        if is_kaibun(number):
            palindromic_number.append(number)

print(max(palindromic_number))