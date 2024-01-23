# to check sub string in string
string='i am am karthik am'
sub_str='am'
flag=0
li=string.split()
for i in li:
    if(i==sub_str):
        print('found')
        flag=1
        break
if(flag==0):
    print('not found')