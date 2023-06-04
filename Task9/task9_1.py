n = int(input('n = '))
uniq = set()
numbers = input()
arr = numbers.split()

for idx, i in enumerate(arr):
    if (idx + 1 <= n):
        uniq.add(i)
print(len(uniq))
