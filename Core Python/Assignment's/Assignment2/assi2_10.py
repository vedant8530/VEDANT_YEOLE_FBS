# Write a program to reverse three-digit number.
n = int(input("Entet thr third-digit number:"))

x = n // 100
y = (n // 10) % 10
z = n % 10

reverce = (z * 100) + (y * 10) + x

print("Reverce number =", reverce)