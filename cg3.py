def main():
    total = 0.0
    for score in range(5):
        score1= float(input('Enter your first score in range 1-100: '))
        total = score1 + total
        if 1> score1 > 100:
           score1 = float(input('Error: Enter your first score in range 1-100: ')) 
        else:
            score2= float(input('Enter your second score in range 1-100: '))
            total = score2 + total
            if 1> score2 > 100:
                score2 = float(input('Error: Enter your second score in range 1-100: '))
                total = score2 + total
            else:
                score3= float(input('Enter your third score in range 1-100: '))
                total = score3 + total
                if 1> score3 > 100:
                   score3 = float(input('Error: Enter your third score in range 1-100: '))
                   total = score3 + total 
                else:
                    score4= float(input('Enter your fourth score in range 1-100: '))
                    total = score4 + total
                    if 1> score4 > 100:
                       score4 = float(input('Error: Enter your fourth score in range 1-100: '))
                       total = score4 + total
                    else:
                       score5= float(input('Enter your last score in range 1-100: '))
                       total = score5 + total
                       if 1> score5 > 100:
                          score5 = float(input('Error: Enter your fifth score in range 1-100: ')) 
                       else:
                           total = score5 + total 
                           average = total/5
                           print('Your average is', average)

                           determine_grade()

def determine_grade():
    average = total / 5
    if average >= 90:
        print('Your average is:' ,average, 'which is an A')
    elif 80 <= average < 90:
        print('Your average is:' ,average, 'which is a B')
    elif 70 <= average < 80:
        print('Your average is:' ,average, 'which is a C')
    elif 60 <= average < 70:
        print('Your average is:' ,average, 'which is a D')
    else:
        print('Your average is:' ,average, 'which is an F')
main()
       
