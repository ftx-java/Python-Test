##第九课
# 测试题 5. 目测以下程序会打印什么？
while True:
    while True:
        break
        print(1)
    print(2)
    break
print(3)
# 动动手 0. 设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容中包含"*"则不计算在内。
mykey = input("请输入密码:")
realkey = '666qwer'
i = 3
while i:
    if mykey == realkey:
        print("密码正确")
        break
    elif mykey.find('*') != -1:
        mykey = input("请重新输入密码:")
    else:
        i -= 1
        if i == 0:
            print('解锁次数已用完')
            break
        print('密码错误，还有', i, '次机会')
        mykey = input("请重新输入密码:")
# 动动手 1. 编写一个程序，求 100~999 之间的所有水仙花数。
# 如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数。
n = 153
while n < 1000:
    temp = n
    index = 0
    x = temp % 10
    temp = (temp - x) / 10
    y = temp % 10
    temp = (temp - y) / 10
    z = temp % 10
    index = x ** 3 + y ** 3 + z ** 3
    if index == n:
        print(index)
    n += 1
# 解法二
for i in range(100, 1000):
    index = i
    sum = 0
    while index:
        sum += (index % 10) ** 3
        index //= 10
    if sum == i:
        print(i)
# 动动手 2.有红、黄、蓝三种颜色的球，其中红球 3 个，黄球 3 个，绿球 6 个。先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配。
for i in range(0, 4):
    for j in range(0, 4):
        for k in range(2, 7):
            if i + j + k == 8:
                print("红球：", i, "黄球", j, "绿球", k)
