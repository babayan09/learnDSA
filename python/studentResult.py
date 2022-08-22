print(" Student Result\n")

print(" ENTER MARKS OUT OF 100")


n1=float(input(" Enter Marks Of 1st exmaination => "))
n2=float(input(" Enter Marks Of 2nd exmaination => "))

ex1_max=n1*50/100
ex2_max=n2*50/100



totalMarks=float((ex1_max+ex2_max)/2)

s1=float(input("Now Enter Sports marks => "))

sx1_max=s1*20/100



a1=float(input(" Enter Marks Of 1st Activity => "))
a2=float(input(" Enter Marks Of 2nd Activity => "))
a3=float(input(" Enter Marks Of 3rd Activity => "))



ax1_max=a1*30/100
ax2_max=a2*30/100
ax3_max=a3*30/100
activatyfull=float((ax1_max+ax2_max+ax3_max)/3)


print(" Total Marks Obtained Is examination => \n")
print(totalMarks)
print(" Total Marks Obtained In Sports  => \n")
print(sx1_max)
print(" Total Marks Obtained In Activity => \n")

print(activatyfull)

print("Total marks obtained After weightage")


print(float(totalMarks+activatyfull+sx1_max))
