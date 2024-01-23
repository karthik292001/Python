# using slicing
li=[1,2,3,4]
new_li=li[0:4]
print(new_li)

# using extend method
li=[1,2,3,4]
new_li=[]
new_li.extend(li)
print(new_li)

# using list method
li=[1,2,3,4]
new_li=list(li)
print(new_li)

# using copy method
li=[1,2,3,4]
new_li=li.copy()
print(new_li)

# using list comprehension
li=[1,2,3,4]
new_li=[i for i in li]
print(new_li)