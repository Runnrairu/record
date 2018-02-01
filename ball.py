# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

import math

def o_mod(x,y):
    if math.fmod(x,y) <0:
        return math.fmod(x,y)+y
    else:
        return math.fmod(x,y)

a,b,x,y,r,theta,L=[int(i) for i in raw_input().split()]
theta = theta/360.0*2*math.pi
X = L*math.cos(theta)+x-r 
Y = L*math.sin(theta)+y-r
a_num = int(math.floor(X/(a-2*r)))
b_num = int(math.floor(Y/(b-2*r)))
if a_num % 2 == 0:
    x_out = o_mod(X,a-2*r)+r
else:
    x_out = a-(o_mod(X,a-2*r)+r)
if b_num % 2 == 0:
    y_out = o_mod(Y,b-2*r)+r
else:
    y_out = b-(o_mod(Y,b-2*r)+r)

print str(x_out)+" "+str(y_out)
