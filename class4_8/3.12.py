N =eval(input("请输入水平真加N的值："))
tmp =1
for i in range(365):
    if i%7 in range(1,5):
        tmp=tmp *(1+N)
print("年终值为：{:.4f}".format(tmp))
