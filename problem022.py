path = "./names.txt"

def delte_double_quote(s):
    return s.strip('"')

f = open(path, "r")
data = f.read().split(",")
f.close()

data = map(delte_double_quote, data)

print(data)