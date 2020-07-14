##第25课
# 测试 1，将数据创建成字典
dict1 = {'F': 70, 'C': 67, 'h': 104, 'i': 105, 's': 115}
dict2 = dict(F=70, C=67, h=104, i=105, s=115)
print(dict1, dict2)


# 动动手 0写一个通讯录小程序
def tongXun():
    print('欢迎进入通讯录小程序')
    dict3 = {}
    while 1:
        n = int(input('请输入指令：'))
        if n == 1:
            name = input('请输入联系人姓名：')
            if dict3.get(name) == None:
                print('暂无该联系人')
            else:
                print(name + ':' + dict3.get(name))
        elif n == 2:
            name = input('请输入联系人姓名：')
            if dict3.get(name) == None:
                num = input('请输入联系人电话：')
                dict3.setdefault(name, num)
            else:
                print('您输入的姓名在通讯录中已存在：' + name + ':' + dict3.get(name))
                flag = input('是否修改用户资料(yes/no)：')
                if flag == 'yes':
                    num = input('请输入联系人电话：')
                    dict3[name] = num
        elif n == 3:
            name = input('请输入联系人姓名：')
            if dict3.get(name) == None:
                print('暂无该联系人')
            else:
                dict3.pop(name)
                print('已删除该联系人')
        elif n == 4:
            print('感谢使用本通讯录')
            break
        else:
            print('输入指令错误，请重新输入')


tongXun()

##第27课
set1 = {1, 3, 5, 6, 3, 2}
print(set1)
set1 = {1, 1.0}
print(set1)
