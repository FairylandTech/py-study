class Dog():

    def eat(self):
        print("吃饭")

    def drink(self):
        print("喝水")

    def watch_home(self):
        print("看家")

class Husky(Dog):

    def eat(self):
        print("吃狗粮")

    def dismantle_home(self):
        print("拆家")

class HappyDog(Dog):

    def eat(self):
        print("吃狗粮，吃骨头")

class ChineseDog(Dog):

    def eat(self):
        print("吃剩饭")

if __name__ == '__main__':
    h = Husky()
    h.eat()
    h.dismantle_home()
    h.drink()
    h.watch_home()

    s = HappyDog()
    s.eat()
    s.drink()
    s.watch_home()

    c = ChineseDog()
    c.eat()
    c.drink()
    c.watch_home()
