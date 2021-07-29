#!/usr/bin/env python3

# REF: https://hiragn.hatenablog.com/entry/2020/10/06/190907
# 問題文に記載の 918,273,645 より大きなパンデジタル数が存在するか調べる。
# 
# 整数を x , 整数の桁数を a , 掛け合わせるベクトルを (1, 2, ..., n) (1 > n) とするとき、
# 積を連結することで得られるパンデジタル数の上位桁は x と一致する。
# したがって x の最上位の桁は 9 であり、x と 整数 n の積の桁数は
# n = 1 のとき a , n > 2 の時 a + 1 である。
# 
# したがって方程式 a + (a + 1)(n - 1) = 9 が成り立ち、
# その解は (a, n) = (4, 2), (1, 5) である。
# 
# 以上より x = 9 と (1, 2, 3, 4, 5), 
# 9000 <= x <= 9999 と (1, 2) の範囲を調べればよい。

def get_concatenated_product(x, n):
    tmp = []
    for j in range(1, n + 1):
        tmp.append(str(x * j))

    return int(''.join(tmp))

def is_pandigital_num(num):
    return set(str(num)) == {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

ans = 0

num = get_concatenated_product(9, 5)
if is_pandigital_num(num) and ans < num:
    ans = num

for i in range(9000, 10000):
    num = get_concatenated_product(i, 2)
    if is_pandigital_num(num) and ans < num:
        print(f"{i}, {num}")
        ans = num

print(ans)

