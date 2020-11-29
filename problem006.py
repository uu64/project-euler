# -*- coding: utf-8 -*-

total = 0
total_of_squares = 0
for i in range(1, 101):
    total += i
    total_of_squares += i*i

print(total_of_squares)
print(total*total - total_of_squares)