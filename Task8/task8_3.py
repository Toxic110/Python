m = int(input('m = '))
n = int(input('n = '))
boats = 0

t = sorted([int(input('mass = ')) for _ in range(n)], reverse=True)
while len(t):
    boats += 1
    k = m - t.pop(0)
    for i in range(len(t)):
        if t[i] <= k:
            t.pop(i)
            break

print('boats needed', boats)
