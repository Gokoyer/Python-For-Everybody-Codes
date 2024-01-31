"""
Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL,
read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers 
in the file and enter the sum below: We provide two files for this assignment. One is a sample file where we give you the sum for your testing
and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1951767.json (Sum ends with 66)
"""

import urllib.request, json

my_location = input('Enter location: ')
print('Retrieving', my_location)
with urllib.request.urlopen(my_location) as url:
    my_Load = json.loads(url.read().decode())

print('Retrieved', len(str(my_Load)), 'characters')
get_load = my_Load.get("comments")
#print(data)
s = total = 0
for i in range(len(getLoad)):
    count_load = get_load[i]
    get_count= count_load.get("count")
    s = s + 1
    total = total + int(get_count)
print("Count:",s)
print("Sum:",total)