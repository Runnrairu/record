c=0
n,m=[int(i) for i in raw_input().split()]
a=[]
for i in range(m):
    a.append(raw_input().split())
b= [['0' for i in range(m)] for j in range(3)]#証言
for i in range(m):#情報の整理 b[i][0]：発言者　b[i][1]：発言対象者 b[i][2]：発言対象の言われ方
    b[i][0]=int(a[i][0])
    b[i][1]=int(a[i][2])
    if a[i][4]=='an':
        b[i][2]=1
    else:
        b[i][2]=-1
ran=[-1,1]
list=[1 for i in range(n)]#村人が嘘つきか正直者か

for l in range(n):
    for k in range(l):
        for j in range(2):
            
            t=0
            for i in range (m):#発言をひとつずつ処理
                if list[b[i][1]-1]!=list[b[i][0]-1]*b[i][2]:#発言対象者が正直か＝発言者が正直かどうか×発言
                    break
                elif t==m-1:
                    c=c+1
                t=t+1
            if j==0:
                list[k]=-list[k]

if c==0:
    print -1
else:
    an=1
    while c!=0 and c!=1:
        if c/2.0==c/2:
            an=an+1
            c=c/2
        else:
            an=an+1
            c=(c-1)/2
    print an
