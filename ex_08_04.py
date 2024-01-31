""" 
Open the file romeo.txt and read it line by line. For each line, split the line into 
a list of words using the split() method. The program should build a list of words.
For each word on each line check to see if the word is already in the list and if not 
append it to the list. When the program completes, sort and print the resulting 
words in python sort() order as shown in the desired output.
You can download the sample data at http://www.py4e.com/code3/romeo.txt 
"""
file_name = input("Enter the file: ")
open_name = open(file_name)
lst = list()
for line in open_name:
    for each in line:
        word = line.split()
        for wrd in word:
            if wrd not in lst:
               lst.append(wrd)
print(sorted(lst))
