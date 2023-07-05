import re

name = input('Name: ').strip()
matches = re.search(r'^(.+), ?(.+)$', name)#() denotes a group. 

if matches:#if matches is true and has a value
    name = matches.group(2)+" "+matches.group(1)#concantinate group 2, space and group 1
print(name)