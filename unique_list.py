def unique(a):
    b=[0]*(max(a)+1)
    for i in a:
        b[i]+=1
    for i in range(max(a)+1):
        if b[i]>=1:
            print(i,end=" ")
a=[1,2,3,3,3,4]
c=unique(a)