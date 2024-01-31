""" 
Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything
other than a valid number catch it with a try/except and put out an appropriate message and ignore the
number. Enter 7, 2, bob, 10, and 4 and match the output below. 
 """

largest = None
smallest = None
while True:
    int_num = input('Enter a number: ')
    if int_num == 'done':
        break
    try:
        int_num = int(int_num)
    except:
        print('invalid input')
        continue
    if largest == None or int_num > largest:
        largest = int_num
    elif smallest == None or smallest > int_num:
        smallest = int_num

print('maximum is', largest)
print('minimum is', smallest)