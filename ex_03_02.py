hours = input("Enter Hours:")
rph = input("Enter rate:")
try:
    h = float(hours)
    r = float(rph)
except:
    print("Error, please enter numeric input")
    quit()
print(h, r)
if h <=40:
    gross_pay = h * r
if h > 40:
    gross_pay = ((h-40) * r * 1.5) + 40 * r
print('pay:', gross_pay)