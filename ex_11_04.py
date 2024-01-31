# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

    #importing the require modules
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
#accessing websites
my_link = "http://py4e-data.dr-chuck.net/known_by_Marykate.html"
open_link = urllib.request.urlopen(my_link).read()
my_soup = BeautifulSoup(open_link, 'html.parser')
all_num_list = list()
link_position = 18
Repeat_process = 7
#Retrieve all of the anchor tags
all_tags = my_soup('a')

while Repeat_process - 1  >= 0 :
    print("Process round", Repeat_process)
    target = all_tags[link_position - 1]
    print("target:", target)
    my_link = target.get('href', 2)
    print("Current url", my_link)
    open_link = urllib.request.urlopen(my_link).read()
    my_soup = BeautifulSoup(open_link, 'html.parser')
    all_tags = my_soup('a')
    Repeat_process = Repeat_process - 1