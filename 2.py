side1 = int(input("Length Of Side 1 \n"))
side2 = int(input("Length Of Side 2 \n"))
side3 = int(input("Length Of Side 3 \n"))

if (side1 == side2) and (side3 == side1):
    print("Equilateral")

elif (side1 == side2) or (side2 == side3) or (side3 == side1):
    print("Isosceles")

else:
    print("Scalene")    