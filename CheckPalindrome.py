#palindrome
num=int(input('Enter the value='))
temp=num
n=0
while(num>0):
    rem=num%10
    n=n*10+rem
    num=num//10
if(n==temp):
    print("Palindrome")
else:
    print("Not palindrome")