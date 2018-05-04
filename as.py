import sys



numb = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9",
    "zero":"0"
}




s= input()
i=0
p = []

while(i<len(s)):#最後まで読み込んだら終わり

    n = []
    flg=True
    while(flg):
        
        if i == len(s) or s[i]==";":
            flg = False
            i+=1
            break
        if s[i] != ";":
            n.append(s[i])
        i +=1
    p.append(numb["".join(n)])
    
print("".join(p))
