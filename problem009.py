# -*- coding: utf-8 -*-

# a**2 + b**2 = c**2
# a = m**2 - n**2
# b = 2mn
# c = m**2 + n**2
# m + n = 500/m (m > n)

def main():
    # m > n > 0
    m = 2
    n = 1
    while True:
        if 500 % m == 0:
            n = int(500/m - m)
            if m > n:
                break
        m += 1
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    print("m:{}, n:{}".format(m, n))
    print("a(b):{}, b(a):{}, c:{}".format(a, b, c))
    print(a*b*c)





if __name__ == '__main__':
    main()