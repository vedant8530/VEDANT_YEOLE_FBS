# Convert the time entered in hh,min and sec into seconds.
hours = int(input('Enter hours:- '))
minutes = int(input('Enter minutes:- '))
second = int(input('Enter seconds:- '))

total_second = (hours * 3600) + (minutes * 60) + second

print('Total second :- ', total_second)