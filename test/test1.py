##第三课
# 0，编写程序：hello.py，要求用户输入姓名并打印“你好，姓名！”
name = input('请输入您的名字：')
print('你好，' + name + '！')
# 1. 编写程序：calc.py 要求用户输入1到100之间数字并判断，输入符合要求打印“你妹好漂亮”，不符合要求则打印“你大爷好丑”
n = int(input('请输入数字：'))
if n > 1 and n < 100:
    print('你妹好漂亮')
else:
    print('你大爷好丑')
# 5. 如果非要在原始字符串结尾输入反斜杠，可以如何灵活处理？
print('lalala\\')
str1 = r'lalala\\'
print(str1)
