input_lines = input()
c=0
s=[input() for i in range(input_lines)]
d=input_lines
j=0
while j<d-2:
    k=j+1
    while k<d-1:
        l=k+1
        while l<d:
            f=s[j]+s[k]+s[l]
            if f % 7 ==0:
                c+=1
            l+=1
        k+=1
    j+=1
print c
