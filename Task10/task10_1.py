pets = dict()

name = input('Введите кличку питомца ')
kind = input('Введите вид питомца ')
age = int(input('Введите возраст питомца '))
owner = input('Введите имя владельца ')
pets[name] = dict()
pets[name]['Вид питомца'] = kind
pets[name]['Возраст питомца'] = age
pets[name]['Имя владельца'] = owner

ageSuffix = ("год" if 11 <= age <= 19 or age % 10 == 1 else
             "года" if 2 <= age % 10 <= 4 else
             "лет")

print(next(iter(pets)))

print('Это', pets[name]['Вид питомца'], 'по кличке', '"' +
      next(iter(pets)) + '".', 'Возраст: ', pets[name]['Возраст питомца'], ageSuffix)
