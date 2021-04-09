N=input("请输入一个5位数字：")
for i in range(5):
    if N[i]!=N[4-i]:
        m=1
        break
    else:
        m=0
if m in [1]:
    print("不是回文数")
else:
    print('是回文数')
