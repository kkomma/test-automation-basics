a='4.5.6.1a'
print(a.isalnum())

for aa in a:
    if aa.isalpha():
        print('isalpha',aa)
    if aa.isdigit():
        print('isdigit', aa)
    if not aa.isalnum():
        print('alnum', aa)
    