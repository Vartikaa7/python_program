def palindrom(s):
    n=len(s)
    for i in range(n//2):
        if s[i]!=s[n-i-1]:
            return False
    return True
s=input()
c=palindrom(s)
print(c)