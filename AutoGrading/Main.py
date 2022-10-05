from convertScore import percentConvert


while True:
    percentConvert()

    while True:
        stop = input("Would you like to continue? yes or no: ".lower())
        print("You inputted:", stop)
    
        if stop not in ["no", "yes"]:
            print("INVALID INPUT")

        else:
            print("Restarting program!")
            break
    
    if stop == "no":
        print("Closing program!")
        break


