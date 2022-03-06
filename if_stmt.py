while(True):

    a = int(input("enter a value: "))
    b = int(input("enter b value: "))

    if a + b == 15:
        print(f'{a} + {b} = {a+b}')
    elif a - b == 4:
        print(f'{a} - {b} = {a-b}')
    elif a * b == 36:
        print(f'{a} * {b} = {a*b}')
    else:
        print("none of the above conditions are true")

    exitFlag = int(input("Enter (1) to exit and any other number to continue "))
    if exitFlag == 1:
        print("Exiting the program")
        break