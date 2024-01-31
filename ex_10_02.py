""" 
10.2 Write a program to read through the mbox-short.txt and figure out the 
distribution by hour of the day for each of the messages. You can pull the hour out 
from the 'From ' line by finding the time and then splitting the string a second time 
using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted 
by hour as shown below. 
"""

d = dict()
lst = list()

file_name = input('enter the file name : ')
try:
    open_file = open(file_name,'r')
except:
    print('wrong file name !!!')

for line in open_file:
    
    st_line = line.strip()
    
    if st_line.startswith('From:'):
        continue
    elif st_line.startswith('From'):
        sp_line = st_line.split()
        
        time = sp_line[5]
        t_split = time.split(':')
        
        t1 = t_split[0].split()
        
        for t in t1:
            if t not in d:
                d[t] = 1
            else:
                d[t] = d[t] + 1

for k,v in d.items():
    lst.append((k,v))
lst = sorted(lst)

for k,v in lst:
    print(k,v)