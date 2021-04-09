dayup,dayb=1.0,0.01
for i in range(365):
    if i%7 in range(1,6):
        dayup = dayup * ( 1 + dayb)
    else:
        dayup = dayup * (1-dayb)
print("{:.2f}".format(dayup))
