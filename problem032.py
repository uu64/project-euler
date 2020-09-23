# -*- coding: utf-8 -*-

# m桁*n桁の積は(m+n)桁、または(m+n-1)桁
# 上記より、本問題では4桁の整数についてのみ、パンデジタル積かどうかを判定すれば良い

def get_pandigital_numbers():
    pandigital_numbers = [[i for i in range (1, 10)]]

    for i in range(1, 4):
        pandigital_numbers.append([])
        for j in pandigital_numbers[i-1]:
            for k in range(1, 10):
                if str(k) in str(j):
                    pass
                else:
                    pandigital_numbers[i].append(int(str(j)+str(k)))

    return pandigital_numbers


def check(multiplicand, multiplier, product):
    if len(set(str(multiplicand) + str(multiplier) + str(product))) == 9:
        return True
    else:
        False


def main():
    pandigital_numbers = get_pandigital_numbers()
    pandigital_products = []
    for i in pandigital_numbers[3]:

        # m=1, n=4の場合
        for j in pandigital_numbers[0]:
            if i % j == 0 and int(i/j) in pandigital_numbers[3]:
                if check(j, int(i/j), i) and i not in pandigital_products:
                    pandigital_products.append(i)
                    print("{}*{}={}".format(j, int(i/j), i))

        # m=2, n=3の場合
        for j in pandigital_numbers[1]:
            if i % j == 0 and int(i/j) in pandigital_numbers[2]:
                if check(j, int(i/j), i) and i not in pandigital_products:
                    pandigital_products.append(i)
                    print("{}*{}={}".format(j, int(i/j), i))

        # 積は一度だけ数え上げればよいので(m, n) = (3, 2)と(m, n) = (4, 1)はスキップ

    result = 0
    for i in pandigital_products:
        result += i
    print(result)


if __name__ == "__main__":
    main()