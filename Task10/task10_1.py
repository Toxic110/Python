pets = dict()

name = input('Введите кличку питомца ')
kind = input('Введите вид питомца ')
age = int(input('Введите возраст питомца '))
owner = input('Введите имя владельца ')
pets[name] = dict()
pets[name]['Вид питомца'] = kind
pets[name]['Возраст питомца'] = age
pets[name]['Имя владельца'] = owner


def ageSuffix(age):
    return {
        age < 0: 'ошибка',
        age % 10 == 0: 'лет',
        age % 10 == 1: 'год',
        age % 10 > 1 and age % 10 < 5: 'года',
        age % 10 > 4: 'лет',
        age % 100 > 10 and age % 100 < 20: 'лет'
    }[True]


print(next(iter(pets)))

print('Это', pets[name]['Вид питомца'], 'по кличке', '"' +
      next(iter(pets)) + '".', 'Возраст: ', pets[name]['Возраст питомца'], ageSuffix(age))
