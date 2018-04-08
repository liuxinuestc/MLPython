__author__ = 'Xin'
import matplotlib.pyplot as plt

def f(a,b,N,a0,b0):
    if (a*a+b*b)>4:
        return 0
    if N>0:
        x = a*a-b*b+a0
        y = 2*a*b+b0
        return f(x,y,N-1,a0,b0)
    else: return 1
plt.figure(figsize=(20,20))
for a in [0.01*i for i in range(-200,200)]:
    for b in [0.01*j for j in range(-200,200)]:
        flag = f(0,0,20,a,b)
        if(flag==1):
            plt.plot(a,b,".k")
plt.show()

