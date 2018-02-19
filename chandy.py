def sitazan(n,A):
    zan =0 
    for j in range(N-n):
         zan += A[1][j+n]
    return zan

N=input()
A=[]
for i in range(2):
    A.append(map(int, raw_input().split()))
points = []
uepoint = 0
for i in range(N):
    uepoint += A[0][i]
    points.append(uepoint + sitazan(i,A))
print max(points)
