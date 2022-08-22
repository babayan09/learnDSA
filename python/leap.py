y1= int(input("Enter First year to check   "))

if (y1%100!=0 and y1%4==0) or (y1%400==0):
    print("Entered year IS leap Year")
else:
    print("year is not leap year")
