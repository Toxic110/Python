a = int(input())
b = int(input())
arr = []

for i in range(a, b + 1):
    if (i % 2 == 0):
        print(i)
        arr.append(i)

print(' '.join(str(x) for x in arr))
