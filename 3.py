name = input("What Is Your Name ?\n")
customerId = int(input("What Is Your Id ?\n"))
unit = float(input("Total Unit Consumed ?\n"))

if unit <= 199:
    bill = unit*1.2
    if bill <100:
        print("Total Charge = ",100)
    else:
        print("Total Charge = ",bill)    
elif unit<400:
    bill = unit*1.5
    if bill < 400:
        print("Total Chrage = ",bill)
    else:
        print("Total Charge = ",bill+200)    
elif unit < 600:
    bill = unit*1.8
    print("Total Charge = ",bill+200)
else:
    bill = unit*2  
    print("Total Charge = ",bill+200)      