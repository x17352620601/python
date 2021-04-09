#el.1TempConcvert.py
temp1 = eval(input("请输入摄氏温度:"))
f=temp1*1.8+32
print("转换后的温度为{}F".format(int(f)))
temp2 =eval(input("请输入华氏温度："))
c=(temp2-32)/1.8
print("转换后的温度为{}C".format(int(c)))

