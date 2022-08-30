# Time Limit Exceeded

for _ in range(int(input())):
    n=int(input())
    l1=input().split()
    l2=input().split()
    l3=input().split()
    p1,p2,p3=0,0,0

    for i in range(n):
        x1=l1[i]
        if x1 in l2 and x1 in l3:
            p1+=0
            l2.remove(x1)
            l3.remove(x1)
        elif x1 in l2:
            p1+=1
            p2+=1
            l2.remove(x1)
        elif x1 in l3:
            p1+=1
            p3+=1
            l3.remove(x1)
        else:
            p1+=3
            
    for i in range(len(l2)):
        x2=l2[i]

        if x2 in l3:
            p2+=1
            p3+=1
            l3.remove(x2)
        else:
            p2+=3
            
    p3+= 3*len(l3)
    
    print(p1,p2,p3)
