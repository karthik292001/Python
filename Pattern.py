n=5
for i in range(0,n+1):
    for j in range(0,n+1):
        if(i==0 or j==0 or j==5 or i==2):
            print("*",end='')
        else:
            print(" ",end='')
    print()