import re
open_file = open('regex_sum_1951762.txt')
my_no = 0
for my_line in open_file:
    my_line = my_line.rstrip()
    my_no = my_no + sum(map(lambda x: int(x), re.findall('([0-9]+)', my_line)))

print(my_no)