def rotation(vector):#鬼の回転
    if vector == "N":
        vector = "E"
    elif vector == "E":
        vector = "S"
    elif vector == "S":
        vector = "W"
    elif vector =="W":
        vector = "N"
    return vector  





def move(oni):
    while(True):#現在の方向に進めるか否かを判定し、進めたら進ませる
        if oni[3] == "N":
            if oni[1] != 0 and data1[oni[1]-1][oni[2]] == "0":
                oni[1] = oni[1]-1
                break
            else:
                oni[3] = rotation(oni[3])
        if oni[3] == "E":
            if oni[2] != n-1 and data1[oni[1]][oni[2]+1] == "0":
                oni[2] = oni[2]+1
                break
            else:
                oni[3] = rotation(oni[3])
        if oni[3] == "S":
            if oni[1] != m-1 and data1[oni[1]+1][oni[2]] == "0":
                oni[1] = oni[1]+1
                break
            else:
                oni[3] = rotation(oni[3])
        if oni[3] == "W":
            if oni[2] != 0 and data1[oni[1]][oni[2]-1] == "0":
                oni[2] = oni[2]-1
                break
            else:
                oni[3] = rotation(oni[3])
    oni[0] += 1
    
    
    
def main(argv):
    global data1,m,n
    f = open(argv[0])
    data1 = f.read()  # ファイル終端まで全て読んだデータを返す
    f.close()
    data1 = data1.rstrip("\n\r")
    data1=[list(x) for x in data1.split()]
    oni = [0,-1,-1,"N"] #時刻に対する鬼の座標
    hunter = [-1,-1] #ハンターの初期位置
    m = len(data1)
    n = len(data1[0])
    
    flg = 0 #ハンター発見フラグ
    for i in range(m):#タテ
        for j in range(n):#ヨコ
            if data1[i][j] == "A":
                hunter[0]=i
                hunter[1]=j
                flg += 1
            if data1[i][j] == "B":#鬼
                oni[1] = i
                oni[2] = j
                flg += 1
            if flg == 2:
                break
        if flg == 2:
                break
    
    
    data1[hunter[0]][hunter[1]] = data1[oni[1]][oni[2]] = "0"
    data2 = [[None for j in range(n)]for i in range(m)]
    data2[hunter[0]][hunter[1]] = 0
    oldlist = [[hunter[0],hunter[1]]]
    turn = 0
    while len(oldlist) > 0:
        newlist = []
        turn += 1
        for (y,x) in oldlist:
            for (y2,x2) in [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]:
                if 0 <= y2 < m and 0 <= x2 < n and data2[y2][x2]==None and data1[y2][x2]=="0":
                    data2[y2][x2] = turn
                    newlist.append((y2,x2))
        oldlist = newlist
    
    turn = 1
    while(True):#n秒目の鬼の位置にハンターは到達可能か判定する
        move(oni)
        if data2[oni[1]][oni[2]] <= turn:
            break
        turn += 1
    print turn
