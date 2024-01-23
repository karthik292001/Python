num=int(input())
m=num//2
flag=0
for i in range(1,m):
    if(i*i==num):
        flag=1
        break
if(flag==1):
    print("spy number")
else:
     print("not spy number")

