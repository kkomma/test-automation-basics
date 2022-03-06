accountBalance = 10500
while(True):
    b = 0
    a = int(input("enter (1) for deposit, (2) withdraw, (3) balance enquiry = "))
    if a not in [1,2,3]:
        print("Please enter the valid option")
        while a not in [1,2,3]:
            a = int(input("enter (1) for deposit, (2) withdraw, (3) balance enquiry = "))
    if a in [1,2]:
        b = int(input("enter amount = "))
    if a == 2:
        if accountBalance <= 0:
            print("Your dont have any balance in the bank, exiting the bank")
            exit(0)
        while b <= 0 or b > accountBalance:
            b = int(input("Please enter the amount less than or equal to your account balance {} ".format(accountBalance)))
            if b <= accountBalance and b > 0:
                break
        accountBalance = accountBalance - b
        print("Your new balance after withdrawing {} is {}".format(b, accountBalance))
    elif a == 1:
        accountBalance = accountBalance + b
        print("Your new balance after depositing {} is {}".format(b, accountBalance))
    elif a == 3:
        print("Your balance is {}".format(accountBalance))
    exitFlag = int(input("Enter (1) to exit and any other number to continue "))
    if exitFlag == 1:
        print("Exiting the test bank")
        break