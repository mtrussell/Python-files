def main():
    grades = 0
    i = 0

    while i < 5:
        grades = grades + float(input("Enter a Grade"))
        i += 1


    average = grades / 5
    print(average)
    return average





def determine_grade():
    grade = main()

    if 90 <= grade <= 100:
        print("You got an A")
    elif 80 <= grade < 90:
        print ("You got a B")
    elif 70 <= grade < 80:
        print ("You got a C")
    elif 60 <= grade < 70:
        print ("You got a D")
    elif grade < 60:
        print ("You got an F")
    else:
        print ("Your grades did not average between 0 and 100. Please try again.")





determine_grade()
