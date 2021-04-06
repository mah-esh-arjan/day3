a=input("enter your name :")
b=len(a)
if b<3:
    print("name must be atleast 3 characters")
elif b>50:
    print("name must be maximum of 50 characters")
else:
    print("name looks good ")