# Take input for P & T & R
P = int(input('Enter Principal Amount:-'))
T = int(input('Enter Rate of Interest:-'))
R = int(input('Enter Time of Year:-'))


# Calculate amount
Total = P * (1 + R/100) ** T

# Calculate Compound interest
compound_interest = Total - P

# Display result 
print('Compound Interest is:-',compound_interest)