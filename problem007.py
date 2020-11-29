# -*- coding: utf-8 -*-

prime_list = [2]
number = 3
while True:
    for i in range(len(prime_list)):
        if number % prime_list[i] == 0:
            break
        else:
            if i == len(prime_list)-1:
                prime_list.append(number)

    if len(prime_list) == 10001:
        break
    number += 2
print(number)
