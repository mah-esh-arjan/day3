#write a program to find the sum of elements of list using while loop
lst=[10,31,37,30,56,63,70]
l=len(lst)
sum=0
for i in range(l):
    sum=sum+lst[i]
print("the sum is",sum)