# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file


import urllib.request
import re
from bs4 import BeautifulSoup

my_html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1951764.html').read()
my_soup = BeautifulSoup(my_html, "html.parser")

s=0
# Retrieve all of the anchor tags
all_tags = my_soup('span')
for my_tag in all_tags:
    # Look at the parts of a tag
    y=str(my_tag)
    x= re.findall("[0-9]+",y)
    for i in x:
        i=int(i)
        s=s + i
print(s)