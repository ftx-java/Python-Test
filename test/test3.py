##第五课
# 测试题 3. 我们人类思维是习惯于“四舍五入”法，你有什么办法使得 int() 按照“四舍五入”的方式取整吗？
print(int(6.4 + 0.5))
print(int(6.6 + 0.5))
# 动动手 0. 针对视频中小甲鱼提到的小漏洞，再次改进我们的小游戏：当用户输入错误类型的时候，及时提醒用户重新输入，防止程序崩溃。
temp = input('请输入数字：')
while not temp.isdigit():
    print('输入不合理，请重新输入：')
    temp = input('请输入数字：')
print(temp)
print(type('a'), type(str))
# 1. 写一个程序，判断给定年份是否为闰年。（注意：请使用已学过的 BIF 进行灵活运用）
year = int(input('请输入年份：'))
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print('输入的是闰年')
else:
    print('输入的不是闰年')
