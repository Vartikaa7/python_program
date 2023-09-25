def rev(s):
    b=""
    for i in s:
        b=i+b
    return b
s=input()
c=rev(s)
if s==c:
    print("yes")
else:
    print("no")