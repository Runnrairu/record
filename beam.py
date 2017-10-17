import sys
H,W=[int(i) for i in raw_input().split()]
s=[]
s=sys.stdin.readlines()
j=0 #縦
k=0 #横
c=1 #通過数
vector='r'
while True:
    if s[j][k]=='_':
        if vector =='r':
            k=k+1
        elif vector=='l':
            k=k-1
        elif vector=='u':
            j=j-1
        else:
            j=j+1
    elif s[j][k]=='/':      
        if vector =='r':
            vector='u'
            j=j-1
        elif vector=='l':
            vector='d'
            j=j+1
        elif vector=='u':
            vector='r'
            k=k+1
        else:
            vector='l'
            k=k-1
    else:
        if vector =='r':
            vector='d'
            j=j+1
        elif vector=='d':
            vector='r'
            k=k+1
        elif vector=='l':
            vector='u'
            j=j-1
        else:
            vector='l'
            k=k-1
    if j==-1 or j==H or k==-1 or k==W:
        break
    else:
        c=c+1
print c
