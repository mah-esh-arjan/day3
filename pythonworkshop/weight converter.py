a = int(input("enter the weight of the person: "))

unit = input("(L)bs or (K)g: ")

if  unit.upper() == "L":
    converted_lbs=a * 0.45
    print(f"the person weighht if {converted_lbs} kilos")
elif unit.upper() ==