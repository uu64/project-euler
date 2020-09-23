# -*- coding: utf-8 -*-

num_en = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'forty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety',
    '100': 'hundred',
}

def print_num_en(num):
    i_str = str(num)

    if len(i_str) == 1:
        s = num_en[i_str]

    if len(i_str) == 2:
        if num % 10 == 0 or num < 20:
            s = num_en[i_str]
        else:
            s = num_en[i_str[0]+'0'] + '-' + num_en[i_str[1]]

    if len(i_str) == 3:
        s = num_en[i_str[0]] + ' ' + num_en['100']
        if num % 100 != 0:
            s += ' and ' + print_num_en(int(i_str[1:]))

    if len(i_str) == 4:
        s = 'one thousand'

    return s

def main():
    sum = 0
    for i in range(1, 1001):
        s = print_num_en(i).replace('-', '').replace(' ', '')
        sum += len(s)
    print(sum)

if __name__ == '__main__':
    main()
