
print("C for Car\n")
print("B for Bus\n")
print("S for Scooter\n")
print("CC for Cycle\n")
print("M for MotorBike\n")

m= input("Enter  Car Type For parking  =>  ")

time=int(input("how many hours You need Space For => "))

n=m.lower()
if n=="c"  :
    print("Car Parking 10/- Per Hour Costing you => ")
    cost=10*time
    print(cost)
elif n=="b":
    print("Bus Parking 20/- Per Hour Costing you => ")
    cost=20*time
    print(cost)
elif n=="s":
    print("scooter Parking 5/- Per Hour Costing you => ")
    cost=5*time
    print(cost)
elif n=="cc":
    print("Cycle Parking 5/- Per Hour Costing you => ")
    cost=5*time
    print(cost)
elif n=="m":
    print("Motor Bike Parking 5/- Per Hour Costing you => ")
    cost=5*time
    print(cost)

else:
    print("INvalid Vechile")