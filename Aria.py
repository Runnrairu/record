def search(S):
    max_score = 0
    Aria_now = None
    S_long = len(S)
    for i in range(K):
        j = -1
        if prime[S_long-A[i][2]]+A[i][1]<= max_score:
            continue
        while(True):
            j = S.find(A[i][0],j+1)
            if j==-1:
                break
            S_copy2 = S[0:j] + S[j+A[i][2]:]
            score = search_memo(S_copy2)+A[i][1]
            if max_score < score:
                max_score = score
                Aria_now = (j,A[i][0])                
    return (max_score,Aria_now)
 
 
 
def search_memo(S):
    global already_sum
    if S not in already_sum:
        already_sum[S] = search(S)
    return already_sum[S][0]
 
 
N,K = [int(i) for i in raw_input().split()]
S = raw_input()
S_copy = S
A = []
len_i = []
for i in range(K):
	Copy = []
	Copy = raw_input().split()
	Copy[1]=int(Copy[1])
	A.append(Copy)
	A[i].append(len(A[i][0]))
prime =[0]*(N+1)
sorted(A, key=lambda x: -x[1]) 
for i in range(1,N+1):
    for k in range(K):
        if A[k][2] <= i:
            if prime[i-A[k][2]] + A[k][1] > prime[i]:
                prime[i]= prime[i-A[k][2]] + A[k][1]
already_sum ={}
maxlu = search_memo(S)
while(already_sum[S][1] != None):
    a,b=already_sum[S][1]
    print(str(a)+" "+b)
    S = S[0:a] + S[a+len(b):]
print(maxlu)
