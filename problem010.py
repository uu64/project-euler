# -*- coding: utf-8 -*-

MAX = 2000000
MAX_ROOT = MAX**0.5
def main():
    # 2以外の偶数は素数じゃないので予め除く
    numbers = [i for i in range(3, MAX+1, 2)]
    idx = 0
    while True:
        n = numbers[idx]
        if n > MAX_ROOT:
            break
        numbers = list(filter(lambda x: x<=n or x%n!=0, numbers))
        idx += 1
    # 除いた2を足す
    print(2 + sum(numbers))

if __name__ == "__main__":
    main()