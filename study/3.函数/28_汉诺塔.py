
# 将n-1层铁饼, 从A经过C移动到B.
# 然后将A铁饼移动到C
# 最后将铁饼, 从B经过A移动到C

def honio(n, a, b, c):
    if n > 0:
        honio(n-1, a, c, b)
        print(f"{a}移动到{c}")
        honio(n-1, b, a, c)


honio(3, "A", "B", "C")
