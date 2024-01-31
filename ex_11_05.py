import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ID
total= 0

my_link = 'http://py4e-data.dr-chuck.net/comments_1951766.xml'
uh = urllib.request.urlopen(my_link)
my_read = uh.read()

my_ID = ID.fromstring(my_read)

lst = my_ID.findall('comments/comment/count')

counts = my_ID.findall('.//count')

total = 0

for count in counts:
    total += int(count.text)

print('total: ', total)