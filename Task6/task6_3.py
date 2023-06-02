a = int(input())
b = int(input())
arr = []

for i in range(a, b):
    if (i % 2 == 0):
        arr.append(i)

print(' '.join(str(x) for x in arr))
