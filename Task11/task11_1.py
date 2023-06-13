num = int(input())


def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)


list = []

for i in range(factorial(num), 0, -1):
    list.append(factorial(i))

print(list)
