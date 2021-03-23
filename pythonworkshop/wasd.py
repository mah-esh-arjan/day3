#function with no parameters and with no-return type
def sub():
    a=int(input("enter the number:"))
    b=int(input("Enter the number:"))
    c=a-b
    print(c)
sub()
##function with parameters and with no-return type
def add(a,b):
    c=a+b
    print(c)
a=int(input("enter the number:"))
b=int(input("Enter the number:"))
add(a,b)
#function with no parameter and with return type
def sum():
    a=int(input("enter the number:"))
    b=int(input("Enter the number:"))
    c=a+b
    return c
print(sum())
#function with  parameter and with return type
def sum(a,b):
    c=a+b
    return c
a=int(input("enter the number:"))
b=int(input("Enter the number:"))
print(sum(a,b))
