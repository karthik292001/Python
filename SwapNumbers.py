#swapping two numbers
num1=int(input('Enter first number: '))
num2=int(input('Enter second number: '))
print('Before swapping num1 is {0} and num2 is {1}'.format(num1,num2))
num1=num1+num2
num2=num1-num2
num1=num1-num2
print('After swapping num1 is {0} and num2 is {1}'.format(num1,num2))   