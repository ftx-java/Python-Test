##第六课
# 测试题 4 请用最快速度说出答案：not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9
# “短路逻辑” 3 and 4 == 4，而 3 or 4 == 3。
print(not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9)
#动动手 0. 请写一个程序打印出 0~100 所有的奇数。
for i in range(101):
    if i % 2 != 0:
        print(i)
# 2. 爱因斯坦曾出过这样一道有趣的数学题：有一个长阶梯，若每步上2阶，最后剩1阶；若每步上3阶，最后剩2阶；若每步上5阶，
# 最后剩4阶；若每步上6阶，最后剩5阶；只有每步上7阶，最后刚好一阶也不剩。请编程求解该阶梯至少有多少阶？
i = 0
while 1:
    if ((i % 2 == 1) and (i % 3 == 2) and (i % 5 == 4) and (i % 6 == 5) and (i % 7 == 0)):
        print(i)
        break
    else:
        i += 1

x = 7
i = 1
flag = 0
while i <= 100:
    if (x % 2 == 1) and (x % 3 == 2) and (x % 5 == 4) and (x % 6 == 5):
        flag = 1
    else:
        x = 7 * (i + 1)  # 根据题意，x一定是7的整数倍，所以每次乘以7
    i += 1

if flag == 1:
    print('阶梯数是：', x)
else:
    print('在程序限定的范围内找不到答案！')
