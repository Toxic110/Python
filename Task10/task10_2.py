arr = list(range(10, -6, -1))
tmp = dict()

for i in arr:
    tmp[i] = i**i

print(tmp)
