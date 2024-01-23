#prime number
num=13
n=num//2
for i in range(2,n+1):
    if(num%i==0):
        print('Not prime')
        break
    else:
        print('prime number')
        break