import string

path = "./names.txt"

alphabets = string.ascii_lowercase
score_dict = {}
for i in range(len(alphabets)):
    score_dict[alphabets[i]] = i + 1

def delte_double_quote(s):
    return s.strip('"')

f = open(path, "r")
data = f.read().split(",")
f.close()

data = map(delte_double_quote, data)
data.sort()

ans = 0
for i in range(len(data)):
    score = 0
    s = data[i].lower()
    for c in s:
        score = score + score_dict[c]
    score = score * (i + 1)

    ans = ans + score
print(ans)