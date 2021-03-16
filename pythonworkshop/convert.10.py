#write a program to convert seconds to day, hour , minutes and seconds.
S=int(input("enter the number of seconds passed :"))
m=S/60
print(f"the minute is {m}")
h=m/60
print(f"the hour is {h}")
d=h/24
print(f"the day is {d}:")