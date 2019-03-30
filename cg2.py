def main():
    
    total = 0
    x = 0
    while x <= 5:
    
        score_x = float(input('Enter score#1 in range 1-100: '))
        score_x = float(input('Enter score#2 in range 1-100: '))
        score_x = float(input('Enter score#3 in range 1-100: '))
        score_x = float(input('Enter score#4 in range 1-100: '))
        score_x = float(input('Enter score#5 in range 1-100: '))
        total = score_x + total
        AVERAGE = total / 5
        if 1 > score_x > 100:
            print('Error: enter a number in range 1-100')

        determine_grade()

def determine_grade():
    AVERAGE = total / 5
    if AVERAGE >= 90:
        print('Your average is:' ,AVERAGE, 'which is an A')
    elif 80 <= AVERAGE < 90:
        print('Your average is:' ,AVERAGE, 'which is a B')
    elif 70 <= AVERAGE < 80:
        print('Your average is:' ,AVERAGE, 'which is a C')
    elif 60 <= AVERAGE < 70:
        print('Your average is:' ,AVERAGE, 'which is a D')
    else:
        print('Your average is:' ,AVERAGE, 'which is an F')
main()
       

