for _ in range(int(input())):
    n=int(input())
    x1=input()
    x2=input()
    for i in range(len(x1)):
        if x1[i]=='B':
            x1=x1[:i]+'G'+x1[i+1:]
        if x2[i]=='B':
            x2=x2[:i]+'G'+x2[i+1:]
    if x1==x2:
        print("YES")
    else:
        print("NO")