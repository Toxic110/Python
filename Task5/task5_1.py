a = int(input())

if (a > 0) and (a % 2 == 0):
    print('Положительное четное число')
elif (a < 0) and (a % 2 == 0):
    print('Отрицательное четное число')
elif a == 0:
    print('Нуливое число')
else:
    print('Число не является четным')