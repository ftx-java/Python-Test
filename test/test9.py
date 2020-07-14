##第21课
# 动动手 0，将使用lambda表达式将函数转化为匿名函数
a = lambda x, y=3: x * y
print(a(5))
# 1 ,将lambda表示是转化为函数
b = lambda x: x if x % 2 else None


def lam(x):
    if x % 2 == 1:
        return x
    else:
        return None


print(b(3), lam(3))
# 3 求出100以内3的倍数
print(list(filter(lambda x: not x % 3, range(100))))
print(list(x for x in range(100) if not (x % 3)))
# 4 使用zip将两个元祖绑定在一起
tuple1 = 1, 3, 5, 7, 9
tuple2 = 2, 4, 6, 8, 10
print(list(zip(tuple1, tuple2)))
# 5,将4 的结果每对元组换成列表
print(list(map(lambda x, y: [x, y], tuple1, tuple2)))


# 6查看打印结果
def fun(n):
    return lambda s: s * n


x = fun(3)
print(x(2))
print(x('lala'))


##第22课
# 动动手 0,使用递归实现pow
def power(x, y):
    if y == 1:
        return x
    y -= 1
    x *= power(x, y)
    return x


print(power(2, 4))
