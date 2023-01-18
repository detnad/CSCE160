# This program determines whether a bank customer
# qualifies for a loan.

MIN_SALARY = 30000.0
MIN_YEARS = 2

salary = float(input('Enter your annual salary: '))
years_on_job = int(input('Enter the number of years employed: '))

# Determine whether the customer qualifies for the loan
if salary < MIN_SALARY:
    print('You must earn at least $', format(MIN_SALARY, ',.2f'), 'per year to qualify.')
else:
    if years_on_job >= MIN_YEARS:
        print('You qualify for the loan.')
    else:
        print('You must have been employed', 'for at least', MIN_YEARS, 'years to qualify.')
