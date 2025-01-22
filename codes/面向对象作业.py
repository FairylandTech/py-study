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
        print(f"我不喜欢{self.film}了")




if __name__ == '__main__':
    zhou_xing_chi = Star("周星驰", "功夫")
    zhou_xing_chi.playing()
