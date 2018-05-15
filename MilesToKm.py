def milestokm():
    choice = input("""
                  _______________________________________________________
                  | •WELCOME TO THE Miles To Km / Km to Miles calculator.|
                  | • type                                               |
                  | • "MilesToKm"                                        |
                  | • or                                                 |
                  | • "KmToMiles"                                        |
                  | • and hit 'ENTER' or if you want                     |
                  | • to Quit type                                       |
                  | • "Quit"                                             |
                  |______________________________________________________|
                   """)

    if choice == "MilesToKm" or choice == "M":
        number = float(input("type in the number that you want to calculate"))
        print(number * 1.6)
        print("do you want to calculate again?")
        more = input("type YES or NO and hit 'ENTER'")
        if more == "YES" or more == "Y":
            milestokm()
        elif more == "NO" or more == "N":
            print("thanks for using this program!")
        else:
            print("you did not type YES or NO try again")


    elif choice == "KmToMiles" or choice == "K":
        number = float(input("type in the number that you want to calculate"))
        print(number / 1.6)
        print("do you want to calculate again?")
        more = input("type YES or NO and hit 'ENTER'")
        if more == "YES" or more == "Y":
            milestokm()
        elif more == "NO" or more == "N":
            print("thanks for using this program!")
    elif choice == "Quit" or choice == "Q":
        print("thanks for using this program!")
    else:
        print("you did not pick MilesToKM or KMToMiles")
        milestokm()

milestokm()



