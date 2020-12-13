#!/usr/bin/env python

nums = set()

count = 1
while 17*count < 1000:
    tmp = 17*count
    s = str(tmp).zfill(3)
    if len(set(s)) == 3:
        nums.add(s)
    count += 1

for i in (13, 11, 7, 5, 3, 2):
    tmp = nums.copy()
    nums = set()
    for s in tmp:
        for j in range(10):
            c = str(j)
            if not c in s and int(c + s[:2]) % i == 0:
                nums.add(c + s)

ans = 0
for s in nums:
    for i in range(10):
        c = str(i)
        if not c in s:
            ans += int(c + s)

print(ans)
