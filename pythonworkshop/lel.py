def outer_function():
    a=20
    def inner_function():
        a=30
        print("inner:",a)
    inner_function()
    print('a:',a)
a=10
outer_function()
print('a:',a)A