a=int(input("Enter a number: "))
steps=0
while a > 0:
    if a % 2 == 0:
        a = a / 2
    else:
        a = a - 1
    steps += 1

print(steps)
        