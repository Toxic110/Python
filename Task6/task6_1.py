n = int(input())
ctx = 0

while n > 0:
    num = int(input())
    if (num == 0):
        ctx += 1
    n -= 1
print("Нулей было", ctx)
