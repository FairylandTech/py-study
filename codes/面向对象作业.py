# coding=utf-8


class Star:

    def __init__(self, name, film):
        self.name = name
        self.film = film

    def playing(self):
        print(f"{self.name}出演了{self.film}, 非常好看")

    def __str__(self):
        return f"{self.name}是我的偶像, 我非常喜欢他的电影{self.film}"

    def __del__(self):
        print(f"我不喜欢{self.name}了")


if __name__ == "__main__":
    stats = {}
    for i in range(5):
        name = input("请输入明星名字: ")
        film = input("请输入明星电影: ")
        stats.update({name: film})

    for name, film in stats.items():
        star = Star(name, film)
        star.playing()
        print(star)
