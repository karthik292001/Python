#swapping two elements in list
a=[1,2,3,4]
a[1]=a[1]+a[2]
a[2]=a[1]-a[2]
a[1]=a[1]-a[2]
print(a)
#other method
a = [6,54,4,3,6]
a[2],a[3]=a[3],a[2]
print(a)