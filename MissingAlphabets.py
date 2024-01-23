string='karthik'
l=[0]*26
for i in range(len(string)):
    m=string[i]
    n=ord(m)-97
    l[n]=1
for i in range(len(l)):
    if(l[i]==0):
        print(chr(i+97))