temp = int(input("What Is The Temperature?\n"))

if temp<0:
    print("Freezing Weather")
elif temp>0 and temp<=10:
    print("Very Cold Weather")
elif temp>10 and temp<=20:
    print("Cold Weather")
elif temp>20 and temp<=30:
    print("Normal Weather")
elif temp>30 and temp<40:
    print("Its Hot")          
elif temp>=40:
    print("Its Very Hot")