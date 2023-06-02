x = int(input())
ctx = 0
i = 1
while i * i < x:
    if x % i == 0:
        ctx += 2
    i += 1
if i * i == x:
    ctx += 1
print(ctx)
