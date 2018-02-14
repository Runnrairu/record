M,N=[int(i) for i in raw_input().split()]
meiro=[]
for i in range(N):
    meiro.append(raw_input().split())
flg = 0 #s,g発見フラグ
s=[-1,-1]
g=[-1,-1]
for i in range(N):
    for j in range(M):
        if meiro[i][j] =='s':
            s[0]=i
            s[1]=j
            flg +=1 
            
        if meiro[i][j]=='g':
            g[0]=i
            g[1]=j
            flg += 1
            meiro[i][j] = '0'
        if flg ==2:
            break
    if flg ==2:
        break
data_meiro = [[None for i in range(M)]for j in range(N)]
old_list=[[s[0],s[1]]]      #今の最先端を記録しておくリスト 
turn = 0    
data_meiro[s[0]][s[1]]=0
g_flg = 0 #ゴールフラグ
while(len(old_list)>0 and g_flg ==0):#次動けるところがなくなるとここが空白になりwhileが終わる
    new_list = [] #次動ける場所を記録しておくリスト
    turn += 1
    for (y,x) in old_list:
        for (y2,x2) in  [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]:
            if y2 ==g[0] and x2 ==g[1]:
                print turn
                g_flg = 1
                break
            elif 0 <= y2 < N and 0 <= x2 < M and data_meiro[y2][x2]==None and meiro[y2][x2]=='0':#まだいってなくて壁でもない
                data_meiro[y2][x2] = turn
                new_list.append((y2,x2))
        if g_flg == 1:
            break
    old_list = new_list #動けなかった場合、ここで空白になりwhileの条件を満たさなくなる

if g_flg ==0:
    print 'Fail'
