##第10课
# 动动手 0. 自己动手试试看，并分析在这种情况下，向列表添加数据应当采用哪种方法比较好？
# 假设给定以下列表：
# member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
# 要求将列表修改为：
# member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
# 方法一：使用 insert() 和 append() 方法修改列表。
# 方法二：重新创建一个同名字的列表覆盖。
number = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
number.insert(1, 88)
number.insert(3, 90)
number.insert(5, 85)
number.insert(7, 90)
number.insert(9, 88)
print(number)
# 方法二
number = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
print(number)
# 动动手1. 利用 for 循环打印上边 member 列表中的每个内容，如图：
for m in number:
    print(m)
for m in range(len(number)):
    if m % 2 == 0:
        print(number[m], number[m + 1])
old = [1, 2, 2, 2, 3, 5]
new = old
old = [6]
print(new)

##第12课
# 1. 请问如何将下边这个列表的'小甲鱼'修改为'小鱿鱼'？1.	list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]
list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]
list1[1][2][0] = '小鱿鱼'
print(list1)
# 5.列表推导式或列表解析
list2 = [i * i for i in range(10)]
print(list2)

##第13课
# 5. x, y, z = 1, 2, 3 请问x, y, z是元组吗？
x, y, z = 1, 2, 3
t = x, y, z
print(type(x), type(t))
# 7. 上节课我们通过课后作业的形式学习到了“列表推导式”，那请问如果我把中括号改为小括号，会不会得到“元组推导式”呢？
tuple1 = (x ** 2 for x in range(10))
print(tuple1, type(tuple1))

##第15课
# 测试题 0. 还记得如何定义一个跨越多行的字符串吗
str1 = '''
chuimiexiaoshanhe
吹灭小山河
'''
print(str1)
# 2. file1 = open('C:\windows\temp\readme.txt', 'r')
# 表示以只读方式打开“C:\windows\temp\readme.txt”这个文本文件，但事实上这个语句会报错，知道为什么吗？你会如何修改？
str2 = 'C:\windows\temp\readme.txt'
str3 = r'C:\windows\temp\readme.txt'
print(str2, str3)
# 3. 有字符串：str1 = '<a href="http://www.fishc.com/dvd" target="_blank">鱼C资源打包</a>'，请问如何提取出子字符串：'www.fishc.com'
str4 = '<a href="http://www.fishc.com/dvd" target="_blank">鱼C资源打包</a>'
str4 = str4[16:29]
print(str4)
print(str4[20:-36])
print(str4)
# 6. 据说只有智商高于150的鱼油才能解开这个字符串（还原为有意义的字符串）：
# str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
str5 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99'
print(str5[::3])
# 动动手 0. 请写一个密码安全性检查的脚本代码：check.py
# 低级
skey = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
num = '0123456789'
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = input('请输入你的密码：')
lenkey = len(key)
flag = 0
for i in key:
    if i in skey:
        flag += 1
        break
for i in key:
    if i in num:
        flag += 1
        break
for i in key:
    if i in chars:
        flag += 1
        break
if lenkey <= 8 and flag == 1:
    print("低级密码")
elif lenkey > 8 and flag == 2:
    print("中极密码")
elif lenkey >= 16 and flag == 3 and key[0] in chars:
    print("高级密码")
else:
    print("密码等级不够或不符合规范，请重新设置密码密码：")

##第16课
# 测试 4. 如果想要显示Pi = 3.14，format前边的字符串应该怎么填写呢？  1.	''.format('Pi = ', 3.1415)
str6 = '{0} {1:.2f}'
print(str6.format('Pi= ', 3.1415))
print("{{1}}".format("不打印", "打印"))
# 测试 3 你认为调用 max('I love FishC.com') 会返回什么值？为什么？
print(max('I love FishC.com'))
# 动动手 0. 猜想一下 min() 这个BIF的实现过程
list3 = [10, 2, 2, 4, 5, 6, 4, 15, 8, 5]
small = list3[0]
for i in list3:
    if i < small:
        small = i
print(small)
# 1. 视频中我们说 sum() 这个BIF有个缺陷，就是如果参数里有字符串类型的话就会报错，请写出一个新的实现过程，自动“无视”参数里的字符串并返回正确的计算结果
list4 = [1, 2, 'sfd', 7, 'rasf', 4, 3, 2]
sum = 0
for i in list4:
    if isinstance(i, str):
        continue
    else:
        sum += i
print(sum)
