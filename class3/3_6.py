'''import time
scale = 50
print("Starting".center(scale,'-'))
t = time.clock()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    t -= time.clock()
    print("{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,-t))
    time.sleep(0.05)
print("\n"+"ending".center(scale,'-'))'''
import  time
scale = 50
for i in range(scale + 1):
    a = "Staring"
    b = '..'*i
    c = "Done"
    time.sleep(0.05)
    print("\r{}{}".format(a,b),end='')
print("\r{}{}{}".format(a,b,c),end='')