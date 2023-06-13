import collections

pets = dict()

last = 0


def create():
    global last
    # last = collections.deque(pets, maxlen=1)[0] <-- Эта конструкция выдает ошибку, я не гуру python и не смог разобраться что за ошибка
    name = input('Введите кличку питомца ')
    kind = input('Введите вид питомца ')
    age = int(input('Введите возраст питомца '))
    owner = input('Введите имя владельца ')
    pets[last + 1] = dict()
    pets[last + 1][name] = dict()
    pets[last + 1][name]['Вид питомца'] = kind
    pets[last + 1][name]['Возраст питомца'] = age
    pets[last + 1][name]['Имя владельца'] = owner
    last += 1
    return True


def read(id):
    pet = get_pet(id)

    if pet:
        return print(f'Это {pet[next(iter(pet))]["Вид питомца"]} по кличке "{next(iter(pet))}". Возраст: {pet[next(iter(pet))]["Возраст питомца"]} {get_suffix(pet[next(iter(pet))]["Возраст питомца"])}. Имя владельца: {pet[next(iter(pet))]["Имя владельца"]}')
    else:
        return False


def update(id):
    pet = get_pet(id)
    if pet:
        name = input('Введите кличку питомца ')
        kind = input('Введите вид питомца ')
        age = int(input('Введите возраст питомца '))
        owner = input('Введите имя владельца ')
        newInfoPet = {
            id: {
                name: {
                    'Вид питомца': kind,
                    'Возраст питомца': age,
                    'Имя владельца': owner
                }
            }
        }
        pets.update(newInfoPet)
    else:
        return False


def delete(id):
    pet = get_pet(id)
    if pet:
        del pets[id]
    else:
        return False


def get_pet(id):
    return pets[id] if id in pets.keys() else print('Питомец не найден')


def get_suffix(age):
    return {
        age < 0: 'ошибка',
        age % 10 == 0: 'лет',
        age % 10 == 1: 'год',
        age % 10 > 1 and age % 10 < 5: 'года',
        age % 10 > 4: 'лет',
        age % 100 > 10 and age % 100 < 20: 'лет'
    }[True]


def pets_list():
    for pet in pets.items():
        print(pet)


command = input('Введите команду ')

while command != 'stop':
    if command == 'create':
        create()
        command = input('Введите команду ')
    if command == 'read':
        id = int(input('Введите индентефикатор питомца '))
        read(id)
        command = input('Введите команду ')
    if command == 'update':
        id = int(input('Введите индентефикатор питомца '))
        update(id)
        command = input('Введите команду ')
    if command == 'delete':
        id = int(input('Введите индентефикатор питомца '))
        delete(id)
        command = input('Введите команду ')
    if command != 'create' and command != 'read' and command != 'update' and command != 'delete' and command != 'stop':
        print('Такой команды не существует')
        command = input('Введите команду ')

print(pets_list())
