# Ildiko Fallahpour
# Complete

# The software package is $99.
# The discount is:
# If 10 or more but less than 20 packages are purchased the discount is 10%.
# If 20 or more but less than 50 packages are purchased the discount is 20%. 
# If 50 or more but less than 100 packages are purchased the discount is 30%.
# If 100 or more packages are purcased the discount is 40%.

# Assign the package price to a named constant. 
 
SOFTWARE_PRICE = 99

# Get the number of the purchased softwares from the user
# while assigning the value to software_purchased variable.

SOFTWARE_PURCHASED = int(input('How many software packages did you purchase? '))

# Assign discounts.

DISCOUNT_40 = SOFTWARE_PURCHASED * SOFTWARE_PRICE * 0.4
DISCOUNT_30 = SOFTWARE_PURCHASED * SOFTWARE_PRICE * 0.3
DISCOUNT_20 = SOFTWARE_PURCHASED * SOFTWARE_PRICE * 0.2
DISCOUNT_10 = SOFTWARE_PURCHASED * SOFTWARE_PRICE * 0.1
FULL_PRICE = SOFTWARE_PURCHASED * SOFTWARE_PRICE

# Determine the amount of discount and display it with the total cost.

if   SOFTWARE_PURCHASED >= 100 :
     print('Discount amount: $', DISCOUNT_40,) 
     print('Total amount: $', FULL_PRICE - DISCOUNT_40,) 
elif 50 <= SOFTWARE_PURCHASED <= 99 :
     print('Discount amount: $', DISCOUNT_30,) 
     print('Total amount: $', FULL_PRICE - DISCOUNT_30,) 
elif 20 <= SOFTWARE_PURCHASED <= 49 :
     print('Discount amount: $', DISCOUNT_20,) 
     print('Total amount: $', FULL_PRICE - DISCOUNT_20,)
elif 10 <= SOFTWARE_PURCHASED <= 19 :
     print('Discount amount: $', DISCOUNT_10,)
     print('Total amount: $', FULL_PRICE - DISCOUNT_10,) 
else:        
     print('Discount amount: $ 0')
     print('Total amount: $', FULL_PRICE,)     


     


