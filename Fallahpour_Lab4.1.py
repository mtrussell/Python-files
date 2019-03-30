# Ildiko Fallahpour
# Complete

# This program calculates and displays the user's budgeting.
print('This program sums up your monthly spending,')
print('and displays how successful your budgeting was.')
print()
# Get the planned budget amount.

BUDGET = float(input('Enter the amount you budgeted this month: '))

# Initialize an accumulator variable.
total = 0

# Get the amount what the user spent.
spent = float(input('Enter the amount you spent (0 to quit): '))
total = (total + spent)
while spent != 0:
    spent = float(input('Enter the amount you spent (0 to quit): '))
    total = (total + spent)
    
if total < BUDGET:
   # Calculate the total spending and display the planned budget amount.
   print('You spent: $',format(total, '.2f'))      
   print('You budgeted: $',format(BUDGET, '.2f'))

   # Calculate how much is the saving, praise the user.
   print('You are $',BUDGET-total, 'under budget.')
   print('Good job!')

# Calculate the total spending and display the planned budget amount.
else:
     print('You spent: $',format(total, '.2f'))      
     print('You budgeted: $',format(BUDGET, '.2f'))

     # Calculate how much is the over spending, warn the user.
     print('You are $',total-BUDGET, 'over budget.')
     print('PLAN BETTER NEXT TIME!')            


