# number of occurence of element
li=[1,2,2,3,45,5]
num=2
count=0
for i in range(len(li)):
    if(li[i]==num):
        count+=1
if(count==0):
    print('element not found')
else:
    print('{0} occured {1} times'.format(num,count))
    
# using count method
li=[1,2,3,4]
num=0
print('{0} occured {1} times'.format(num,li.count(num)))