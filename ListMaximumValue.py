#max num in array
a=[2,90,4,5]
great=a[0]
for i in range(len(a)):
    if(a[i]>great):
        great=a[i]
print('Maximum',great)
#min num in array
a=[2,90,4,5]
great=a[0]
for i in range(len(a)):
    if(a[i]<great):
        great=a[i]
print('Minimum',great)