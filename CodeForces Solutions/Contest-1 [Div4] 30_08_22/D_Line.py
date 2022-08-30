# Incomplete

for _ in range(int(input())):
    n=int(input())
    x=input()
    sum1=0
    for i in range(n):
        if x[i]=='L':
            sum1+=i
        else:
            sum1+=n-i-1
    print(sum1)
    mid=n//2
    x1=x[:mid]
    x2=x[mid:]
    cl=x1.count('L')
    c2=x2.count('R')
    
    for k in range(1,n+1):
        sum2=sum1
        if c1-k>0:
            x1.index('L')
        for i in range(k):
            if i<=mid and x[i]=='L':
                sum2+=(n-i-1)-i
            elif i>mid and x[i]=='R':
                sum2+=i-(n-i-1)
        