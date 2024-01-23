li=[1,2,3,4]
grt=li[0]
smallest=li[0]
for i in range(len(li)):
    if(grt<li[i]):
        grt=li[i]
    if(smallest>li[i]):
        smallest=li[i]
print(grt)
print(smallest)

#  using sort
li=[1,2,3,4]
li.sort()
print(li[3])
print(li[0])
 
# min and max
li=[11,22,33,42]
print(min(li))
print(max(li))