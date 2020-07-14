##第33课
# 测试 1
try:
    for i in range(3):
        for j in range(3):
            if i == 2:
                raise KeyboardInterrupt
            print(i, j)
except KeyboardInterrupt:
    print('退出啦')


# 动动手 2
def int_input(temp=''):
    while True:
        try:
            int(input(temp))
            break
        except ValueError:
            print('清输入整数')


int_input('请输入一个整数：')
int(input('请输入'))