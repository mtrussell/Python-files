# Ildiko Fallahpour
# Complete

# This program calculates and displays the amount of ingredients needed
# for a desired amount of cookies
# using the original recipe for 48 cookies.
# The original recipe is as follows:
# 1.5  cups of sugar
# 1    cup  of butter
# 2.75 cups of flour.

# Assign the ingredients by creating four variables: orig_cookies, orig_sugar,
# orig_butter, orig_flour.

ORIG_COOKIES = 48
ORIG_SUGAR = 1.5
ORIG_BUTTER = 1
ORIG_FLOUR = 2.75

# Get the number of the desired amount of cookies from the user
# while assigning the value to desired_cookies variable.

desired_cookies = int(input('How many cookies would you like to make? '))

# Calculate the necesary amount of ingredients needed for desired_cookies
# by using formula:
# (original amount of ingredient * desired amount of cookies)
# /original amount of cookies
# while assigning the results to three variables as follows:
# new_sugar, new_butter and new_flour.

new_sugar =(ORIG_SUGAR*desired_cookies)/ORIG_COOKIES
new_butter =(ORIG_BUTTER*desired_cookies)/ORIG_COOKIES
new_flour=(ORIG_FLOUR*desired_cookies)/ORIG_COOKIES

# Display the necessary amount of ingredients needed
# to make the desired amount of cookies.


                       
print("To make ", desired_cookies, ' cookies, you will need:\n', \
format(new_sugar, '.2f'), ' cups of sugar\n', \
format(new_butter, '.2f'), ' cups of butter\n', \
format(new_flour, '.2f'), ' cups of flour')

