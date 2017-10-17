import math
W,H,M,N=[int(i) for i in raw_input().split()]
c=[]
for i in range(M):
    c.append(map(int, raw_input().split()))
b=[]
for i in range(N):
    b.append(map(int, raw_input().split()))
pi=3.14159265358
for i in range(N): #美術品ごとに判定していく
    t=0
    for j in range(M): #カメラごとの判定
       d=(c[j][0]-b[i][0])**2+(c[j][1]-b[i][1])**2
       d=d**(1/2.0)
       if d<c[j][4]: #必要条件である距離の判定
            rad1=2*pi*(c[j][2]-(c[j][3]/2))/360
            rad2=2*pi*(c[j][2]+(c[j][3]/2))/360
            if b[i][0]-c[j][0]!=0:
               k=math.atan2((b[i][1]-c[j][1])/(b[i][0]-c[j][0]))
            elif b[i][1]<c[j][1]:
               k=-pi/2
            else:
                k=pi/2

            if k>rad1 and k<rad2:
               t=1
               print 'yes'
               break
    if t==0:
        print 'no'
