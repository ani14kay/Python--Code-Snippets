# Incomplete

for _ in range(int(input())):
    n,q=map(int,input().split())
    ln=[]
    qn=[]
    for i in range(n):
        h,w=map(int,input().split())
        ln.append([h,w])
    for i in range(q):
        h1,w1,h2,w2=map(int,input().split())
        qn.append([h1,w1,h2,w2])
    print(ln)
    print(qn)
    area=0
    for i in range(q):
        h1,w1,h2,w2=q[i][0],q[i][1],q[i][2],q[i][3]
        