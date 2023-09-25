#this code will help you len of every word present in a string in dictionary.

s="This is a sample string to demonstrate how to count word frequencies in a given string. The words in this string will be counted to show how often each word appears."
e=s.split(" ")
d={}
for i in e:
    if i[len(i)-1]==".":
        i=i[0:len(i)-1]
    d.setdefault(i,0)
    d[i]+=1
print(d)