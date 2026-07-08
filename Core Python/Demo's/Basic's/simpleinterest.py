# # Take input for P & T & R
# P = int(input('Enter Principal Amount:-'))
# T = int(input('Enter Rate of Interest:-'))
# R = int(input('Enter Time of Year:-'))

# # Perform 
# Total = (P * T * R) / 100

# # Display result

# print(f'Calculate simple interest {P} & {T} & {R} is {Total}...')

Dividend = int(input('Enter Dividend:-'))
Divisor = int(input('Enter Divisor:-'))

Q = Dividend // Divisor
R = Dividend % Divisor

print('Quotient is:-',Q)
print('Reminder is:-',R)