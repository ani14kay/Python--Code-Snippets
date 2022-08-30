t="Timur"
lt = [t[i] for i in range(len(t))]
lt.sort()
tt=''
for i in lt:
    tt+=i
for _ in range(int(input())):
    n=int(input())
    x=input()
    lx = [x[i] for i in range(len(x))]
    lx.sort()
    xx=''
    for i in lx:
        xx+=i
    if xx==tt:
        print("YES")
    else:
        print("NO")