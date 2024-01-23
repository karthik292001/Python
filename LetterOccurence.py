s='manonj'
count=0
new=[]
s=list(s)

print(s)
for i in s:
    for j in s:
        if i==j:
            count+=1
    print(i,count)
    count=0