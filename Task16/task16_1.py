class Store(object):
    cash = 0

    def top_up(self, money):
        self.cash += money

    def count_1000(self):
        print(int(self.cash / 1000))

    def take_away(self, money):
        if (self.cash >= money):
            self.cash -= money
        else:
            print('в кассе не достаточно денег')


some_store = Store()

some_store.top_up(2000)
some_store.count_1000()
some_store.take_away(1000)
some_store.count_1000()
some_store.take_away(5000)
