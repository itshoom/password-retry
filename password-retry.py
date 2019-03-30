password = '123456'
x = 3
while x > 0:
    pwd = input('请输入密码: ')
    if pwd == password:
        print('登陆成功!')
        break
    else:
        x -= 1
        if x >= 1:
            print('密码错误,还剩', x, '次机会')
        if x == 0:
            print('请重置密码')