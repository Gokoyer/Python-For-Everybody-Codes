""" 
9.4 Write a program to read through the mbox-short.txt and figure out who has 
sent the greatest number of mail messages. The program looks for 'From ' lines 
and takes the second word of those lines as the person who sent the mail. The 
program creates a Python dictionary that maps the sender's mail address to a 
count of the number of times they appear in the file. After the dictionary is 
produced, the program reads through the dictionary using a maximum loop to find 
the most prolific committer. 
"""
data_file = input('Enter the file name: ')
try:
    open_file = open(data_file)
except:
    print('File cannot be opened:', data_file)
    exit()

counts = dict()

for line in open_file:
    if line.startswith('From '):
        words = line.split()
        #print (words)
        counts[words[1]] = counts.get(words[1], 0) + 1
            
#print (counts)

maximum = 0

for email in counts:
    if counts[email] > maximum :
        maximum = counts[email]
        best_email = email
        
print (best_email, maximum)