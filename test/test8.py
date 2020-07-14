##第17课
# 测试4. 请问这个函数有多少个参数？
list0 = [1, 2, 3, 4, 5]


def Myfuc(x):
    for i in x:
        print(i)


Myfuc(list0)


# 动动手 0. 编写一个函数power()模拟内建函数pow()，即power(x, y)为计算并返回x的y次幂的值。
def power(x, y):
    return x ** y


print(power(2, 4))


# 2. 编写一个将十进制转换为二进制的函数，要求采用“除2取余”（脑补链接）的方式，结果与调用bin()一样返回字符串形式。
def bin(x):
    y = str(x)
    if '.' in y:
        str1 = y[:y.index('.')]
        str2 = y[y.index('.'):]
        str2 = '0' + str2
    else:
        str1 = y[:]
        str2 = '0'
    a = int(str1)
    b = float(str2)
    print(a, b)

    list1 = []
    list2 = []
    while a:
        s1 = a % 2
        a //= 2
        list1.append(s1)
    index = 10
    while index:
        b = b * 2
        index -= 1
        if b > 1:
            list2.append(1)
            b -= 1
        elif b < 1:
            list2.append(0)
        elif b == 1:
            list2.append(1)
            break
    print(list1, list2)
    res1 = ''
    res2 = ''
    for i in list2:
        res2 += str(i)
    if len(list1) == 0:
        res1 = '0'
        res = '0.' + res2
    else:
        while list1:
            res1 += str(list1.pop())
        res = res1 + '.' + res2
    print(res)


bin(12.625)


##第18课
# 动动手 0
def fun1(*temp, base=3):
    sum = 0
    for i in temp:
        sum += i
    print(sum * base)


fun1(1, 2, 3, 4, 5, base=5)


# 2 统计子字符在字符串中出现的次数
def fun2(str1, str2):
    times = 0
    l = len(str1) - len(str2)
    for i in range(l + 1):
        if str2 == str1[i:i + len(str2)]:
            times += 1
    print('子字符串出现的次数为 ', times)


fun2('qwertyu iqwer', 'qwer')
print('qwer'[:3])

##第19课
# 测试 4
var = 'hi'


def fun3():
    global var
    var = 'baby'
    return fun4(var)


def fun4(var):
    var += 'i love you'
    fun5(var)
    return var


def fun5(var):
    var = 'lala'
    print(var)


print(fun3(), var)


# 动动手 0，回文
def Huiwen(str):
    l = len(str)
    if l % 2 == 0:
        if str[:len(str) // 2] == str[len(str) // 2:][::-1]:
            print('是回文')
        else:
            print('不是回文')
    else:
        if str[:len(str) // 2] == str[len(str) // 2 + 1:][::-1]:
            print('是回文')
        else:
            print('不是回文')


str1 = '上海自来水来自海上'
Huiwen(str1)


# 1统计各参数个数
def Times(*temp):
    index = 0
    for strtemp in temp:
        i = j = k = c = 0
        for x in strtemp:
            y = ord(x)
            if y >= 48 and y <= 57:
                i += 1
            elif y >= 65 and y <= 122:
                j += 1
            elif y == 32:
                k += 1
            else:
                c += 1
        index += 1
        print('第%d 个字符串共有： 英文字母%d 个，数字%d 个，空格%d 个，其他字符%d 个。' % (index, j, i, k, c))


Times('hello, 123 .com', '你好，23333 lalala.')


##第19课
# 测试 6，下面程序会打印的内容是什么
def funX():
    x = 5

    def funY():
        nonlocal x
        x += 1
        return x

    return funY


a = funX()
print(a())
print(a())
print(a())


def funX1():
    x = 5

    def funY1():
        nonlocal x
        x += 1
        return x

    return funY1()


a = funX1()
print(a)
print(a)
print(a)


# 动动手 0统计字符串中各个字符出现的次数
def numStr(str1):
    for i in str1:
        if i == '\n':
            print('\\n', str1.count(i))
        else:
            print(i, str1.count(i))


str1 = 'abbcddeeefggg'
numStr(str1)