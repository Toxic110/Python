# count_moves(x2, y2) - возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции

class Turtle(object):
    x = 0
    y = 0
    s = 1

    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s <= 0:
            print('S не может быть 0 или меньше')
        else:
            self.s -= 1

    def count_moves(self, x2, y2):
        print(abs(x2-self.x)//self.s + abs(y2-self.y)//self.s)


tuple = Turtle(4, 4, 1)

tuple.count_moves(2, 2)
