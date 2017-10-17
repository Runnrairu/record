x,y=[int(i) for i in raw_input().split()]
k=input()
N=input()
a=[]
for i in range(N):
    a.append(map(int, raw_input().split()))
a.sort(key=lambda a:(((a[0]-x)**2+(a[1]-y)**2))**0.5)
b=0
for j in range(k):
    b=b+a[j][2]
c=float(b)/k
d=int(c)
if c-d>=0.5:
    c=c+1

print int(c)
