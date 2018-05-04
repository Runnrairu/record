import sys
n=int(input())
text=[]
for line in sys.stdin:
    text.append(line.strip("\n"))
m=len(text)
text=sorted(text, key=len)
count = 0
while(count < n):
    print(text[m-1-count])
    count +=1
