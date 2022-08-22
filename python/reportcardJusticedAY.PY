


print("ENTER MARKS OUT OF 100 ------------------\n")
m1= float(input("Enter  MARKS of English   "))
m2= float(input("Enter  Marks to History   "))
m3=float( input("Enter  Marks to Maths  "))
m4= float(input("Enter  Marks to Science  "))
totalm=(m1+m2+m3+m4)*100/400
if totalm>=75:
    print("Distinction")
elif totalm<=75 and totalm>=60:
    print("I Division")
elif totalm<=50 and totalm>=59.9:
    print(" II Division")
elif totalm<=40 and totalm>=49.9:
    print("III Division")
else:
    print("You Failed")

