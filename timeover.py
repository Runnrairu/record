#キューを導入してやり直したい
import numpy as np
import math
N,M=[int(i) for i in raw_input().split()]
a=[]
c=0
while True:
    n=raw_input()
    c=c+1
    if c==M:
        break
    a.append(n)
for i in range(N):
    for j in range(M):
        if a[i][j]=='s':
            s1=i
            s2=j
            break


b=[1,-1]
start1=s1
start2=s2b=[1,-1]
start1=s1
start2=s2
r1=np.random.choice(b,2000000)
r2=np.random.choice(b,2000000)
d=100000000000000000

for i in range(1999999):
    if s1+r1[i]>=0 and s1+r1[i]<=M-1 and s2+r2[i]>=0 and s2+r2[i]<=N-1:
        if a[s1+r1[i]-1][s2+r2[i]-1]==1:
           s1=start1
           s2=start2
           C=0 
        elif r1[i]!=r1[i-1] or r2[i]!=r2[i-1] :
            s1=s1+r1[i]
            s2=s2+r2[i]
            c=c+1
            if a[s1-1][s2-1]=='g' and d>c:
                d=c
                s1=start1
                s2=start2
                c=0
    else:
        s1=start1
        s2=start2
        C=0
    
print d
