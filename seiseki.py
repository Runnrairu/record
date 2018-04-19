import csv

def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.
    
    #for i, v in enumerate(argv):
    #    print("argv[{0}]: {1}".format(i, v))
    data = []
    with open(argv[1]) as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:        
            data.append([int(x) for x in row[1:]])
        
    n = len(data)#生徒の人数        
    
    if argv[0]=="1":#項目１の場合
        Mean = [0]*6
        Median  = [0]*6 
        Variance = [0]*6
        print("Subject,Mean,Median,Variance")
        for i in range(6):
            datai=[]
            for j in range(n):
                datai.append(data[j][i])
                Mean[i] += datai[j]
            Mean[i] = float(Mean[i])/n
            for j in range(n):
                Variance[i] += (datai[j]-Mean[i])*(datai[j]-Mean[i]) 
            Variance[i] =float(Variance[i])/(n-1)#不偏分散！？
            m = len(datai)
            dataisort = sorted(datai)
            if m % 2 !=0:
                Median[i] = dataisort[(m+1)//2-1]#インデックスの関係上ひとつずらさないといけない
            else:
                Median[i] = float(dataisort[m//2-1]+dataisort[m//2])/2#同上
            Mean[i]=round(Mean[i],2)#四捨五入
            Variance[i]=round(Variance[i],2)#四捨五入
            
            print(",".join([header[i+1],"{0:.2f}".format(Mean[i]),"{0:.1f}".format(Median[i]),"{0:.2f}".format(Variance[i])]))
        
        
            
    else:
        print("Pair,Coefficient")
        Mean = [0]*6
        for i in range(6):
            for j in range(n):
                Mean[i] += data[j][i]
            Mean[i]= float(Mean[i])/n
        for x in range(6):
            for y in range(x):#これで総当りできる
                sumx = 0#分母の片方
                sumy = 0#分母の片方
                sum_u = 0 #分子
                
                for k in range(n):
                    sum_u += (data[k][x]-Mean[x])*(data[k][y]-Mean[y])
                    sumx +=  (data[k][x]-Mean[x])**2
                    sumy +=  (data[k][y]-Mean[y])**2
                r=sum_u/(sumx*sumy)**0.5
                r= round(r,3)
                if header[x+1]<header[y+1]:
                    print(header[x+1]+"-"+header[y+1]+","+"{0:.3f}".format(r))
                else:
                    print(header[y+1]+"-"+header[x+1]+","+"{0:.3f}".format(r))
    
    
    
