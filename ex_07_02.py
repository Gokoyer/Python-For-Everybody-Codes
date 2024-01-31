""" 
Write a program that prompts for a file name, then opens that file and reads
through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and
compute the average of those values and produce an output as shown below. Do 
not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
when you are testing below enter mbox-short.txt as the file name. 
"""

file_name = input("Enter file name: ")
open_name = open(file_name)
s = 0.0
count = 0

for lx in open_name:
    if not lx.startswith("X-DSPAM-Confidence: "):
        continue
    else:
        s = s + float(lx[20:])
        count = count + 1
print("Average spam confidence:", s/count)


############# Altenatively ##########################
""" file_name = input("Enter file name: ")
open_name = open(file_name)
s = 0
count = 0

for lx in open_name:
    if not lx.startswith("X-DSPAM-Confidence: "):
        continue
    else:
        count = count + 1
        a = lx.find("0")
        x = lx[a:]
        s = s + float(x)
    avg = s/count
print("Average spam confidence:", avg) """