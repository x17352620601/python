money = input("请输入带符号的金钱额度：")
if money[-1] in ['$']:
    RMB= eval(money[0:-1])  / 6
    print("转换后的金额为{:.2f}￥".format(RMB))
if money[-1] in ['￥']:
    dolls =eval( money[0:-1])*6
    print("转换后的金额为{:.2f}$".format(dolls))
else:
    print("输入错误")
