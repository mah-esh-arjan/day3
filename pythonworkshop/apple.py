#N students take K apples and distribute them among each other evenly .the remaning (the undivisual) part reamains in the basket.
#how many apple will remain in the basket. the program read number N and K .it should print the two answer for the above question
stu=int(input("enter the number of student in class:"))
app=int(input("enter the number of apple:"))
div=(app/stu)
remain=(app%stu)
print("each student get:",div)
print("the remaning apple",remain)