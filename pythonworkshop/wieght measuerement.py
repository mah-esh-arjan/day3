#input the weight of a person in either kg or lbs. If the person provides his/her weight in kg then covert it into lbs else convert it to kg.
weight=int(input("enter your wieght in either lbs or kg"))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    converted_lbs = weight * 0.45
    print(f"the person weight is {converted_lbs} kilos")
elif unit.upper() == "K":
    converted_kg = weight / 0.45
    print(f"the person weight is {converted_kg}")
else:
    print(f"enter the character you stupid person")



