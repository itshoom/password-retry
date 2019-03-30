password = '123456'
x = 3
while x > 0:
    x -= 1
    pwd = input('请输入密码: ')
    if pwd == password:
        print('登陆成功!')
        break
    else:
        print('密码错误,')
        if x > 0:
            print('还剩', x, '次机会')
        else:
            print('请重置密码')