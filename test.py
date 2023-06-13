def godlet(god):
    return {
        god < 0: 'ошибка',
        god % 10 == 0: 'лет',
        god % 10 == 1: 'год',
        god % 10 > 1 and god % 10 < 5: 'года',
        god % 10 > 4: 'лет',
        god % 100 > 10 and god % 100 < 20: 'лет'
    }[True]


print(godlet(1))
