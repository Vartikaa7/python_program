def perf(n):
    sum=1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            sum+=(i+n//i)
    if sum==n:
        return True
    else:
        return False
n=int(input())
c=perf(n)
print(c)