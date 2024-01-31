"""
Write a program that prompts for a file name, then opens that file and reads through the file,
 and print the contents of the file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt
"""

file_name = input("Enter file name: ")
open_name = open(file_name, "r")
read_name = open_name.read()
rstrip_name = read_name.rstrip()
print(rstrip_name.upper()) 
