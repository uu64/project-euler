#!/usr/bin/env python
import eulerlib

def is_prime(n):
  if n < 2:
    # 2未満は素数でない
    return False
  if n == 2:
    # 2は素数
    return True
  for p in range(2, n):
      if n % p == 0:
        # nまでの数で割り切れたら素数ではない
        return False
  # nまでの数で割り切れなかったら素数
  return True

max = 0
for i in range(-1000, 1001):
    print(i)
    for j in range(-1000, 1001):
        n = 0
        while True:
            ans = n*n + i*n + j
            if ans <= 1 and not is_prime(ans):
                if max < n:
                    max = n
                break
            print(ans)
            n += 1

print(max)