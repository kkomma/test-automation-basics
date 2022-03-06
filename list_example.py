number_list = [1,2,3,4,5]
letter_list = ['a','b','c','d','e']

for i in range(len(number_list)):
    print('index',i)
    print('list value at index '+str(i)+' is::', number_list[i])


for i in range(3, len(letter_list)):
    print('index',i)
    print('list value at index '+str(i)+' is::', letter_list[i])

print(letter_list)
letter_list.remove('c')
print(letter_list)

print(number_list[-1])
number_list.append(6)
print(number_list)
print(number_list[2:])
print(number_list[:2])