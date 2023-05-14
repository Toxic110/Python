a = 46275
b = [int(i) for i in str(a)][3] ** [int(i) for i in str(a)][4]
c = b * [int(i) for i in str(a)][2]
d = c / ([int(i) for i in str(a)][0] - [int(i) for i in str(a)][1])

print(d)
