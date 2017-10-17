H,W,N=[int(i) for i in raw_input().split()]
a=[]
for i in range(H):
    a.append(map(int, raw_input().split()))
L=input()
b=[]
for j in range(L):
    b.append(map(int, raw_input().split()))
l=0
list=[0 for i in range(N)]
for k in range(L):
    if a[b[k][0]-1][b[k][1]-1]==a[b[k][2]-1][b[k][3]-1]:
        list[l]=list[l]+2
    elif l+1==N:
        l=0
    else:
        l=l+1
for m in range(N):
    print list[m]
