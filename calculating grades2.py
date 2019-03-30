MAX = 5
total = 0.0
for counter in range(MAX):
    score1= float(input('Enter your first score in range 1-100: '))
    total = score1 + total
    if 1> score1 > 100:
       score1 = float(input('Error: Enter your first score in range 1-100: ')) 
    else:
       score2= float(input('Enter your second score in range 1-100: '))
       total = score2 + total
    if 1> score2 > 100:
       score2 = float(input('Error: Enter your second score in range 1-100: ')) 
    else:
       score3= float(input('Enter your third score in range 1-100: '))
       total = score3 + total
    if 1> score3 > 100:
       score3 = float(input('Error: Enter your third score in range 1-100: ')) 
    else:
       score4= float(input('Enter your fourth score in range 1-100: '))
       total = score4 + total
    if 1> score4 > 100:
       score4 = float(input('Error: Enter your fourth score in range 1-100: ')) 
    else:
       score5= float(input('Enter your last score in range 1-100: '))
    if 1> score5 > 100:
       score5 = float(input('Error: Enter your fifth score in range 1-100: ')) 
    else:
       total = score5 + total 
       average = total/5
       print('Your average is', average)
