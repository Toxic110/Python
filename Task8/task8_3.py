m = int(input('m = '))
n = int(input('n = '))
a = []
b = []
for i in range(n):
    a.append(int(input('mass = ')))

for x in range(len(a)):
    if a[x] + min(a) <= m:
        b += [[a[x], min(a)]]
        a[x] += m
        a[a.index(min(a))] += m
    else:
        if a[x] > m:
            continue
        else:
            b += [[a[x]]]
print('boats needed', len(b))
