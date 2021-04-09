day,dayup=1,0.01
for i in range(365):
    if i%10 in [0,1,2,3,]:
        day=day
    else:
        day=day*(1+dayup)
print("练习学习365天的能力值为：{:.2f}".format(day))
