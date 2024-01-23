s='i am https://www.youtube.com/'
s=s.split()
for i in s:
    if i.startswith('http://') or i.startswith('https://'):
        print('yes')
        
s='i am https://www.youtube.com/'
import re
url=re.findall('http[s]://',s)
print(url)