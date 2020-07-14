##第八课
# 测试题 2，假设有 x = 1，y = 2，z = 3，请问如何快速将三个变量的值互相交换？
x = 1
y = 2
z = 3
x, y, z = z, y, x
print(x, y, z)
# 动动手 0，按照100分制，90分以上成绩为A，80到90为B，60到80为C，60以下为D，写一个程序，当用户输入分数，
# 自动转换为ABCD的形式打印。
num = int(input('请输入你的成绩：'))
if num > 90:
    print('A')
elif num > 80:
    print('B')
elif num > 60:
    print('C')
else:
    print('D')
# 1,请将以下代码修改为三元操作符实现：
# 1.	x, y, z = 6, 5, 4
# 2.	if x < y:
# 3.	    small = x
# 4.	    if z < small:
# 5.	        small = z
# 6.	elif y < z:
# 7.	    small = y
# 8.	else:
# 9.	    small = z
x, y, z = 6, 5, 4
small = (x if x < y else y)
small = (z if z < small else small)
print(small)
small = x if (x < y and a < z) else (y if y < z else z)
print(small)
