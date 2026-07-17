# Write a program to swap two numbers using third variable.
x = 10
y = 20
print(f"Before swapping x={x} y={y}..")

x = x + y
y = x - y
x = x - y
print(f"After swapping x={x} y={y}..")