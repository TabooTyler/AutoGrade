def percentConvert():
    totalQuestions = int(input("Enter the amount of questions: "))
    amountCorrect = int(input("Enter the amount answered correctly: "))

    percentage = (amountCorrect / totalQuestions) * 100

    if percentage == 100:
        print("Congratulations! 100%")
        
    elif percentage >= 99:
        print("A+")
        
    elif percentage >= 94:
        print("A")

    elif percentage >= 90:
        print("A-")
        
    elif percentage >= 89:
        print("B+")
        
    elif percentage >= 84:
        print("B")
        
    elif percentage >= 80:
        print("B-")
        
    elif percentage >= 79:
        print("C+")
        
    elif percentage >= 74:
        print("C")
        
    elif percentage >= 70:
        print("C-")
        
    elif percentage >= 69:
        print("D+")
        
    elif percentage >= 64:
        print("D")
        
    elif percentage >= 60:
        print("D-")
        
    else:
        print("F")