#If name less than 3 characters lnog = name must be at least 3 characters otherwise if it's more than 50 characters name must be maximum of 50 characters
#otherwise - name looks good!
a=str(input("enter your name"))
if len(a)<3:
    print("the name must be atleast 3 characters ")
elif len(a)>50:
    print("names that are bigger than your mom doesnt work")
else:
        print("the name is correct")