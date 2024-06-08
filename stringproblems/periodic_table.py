import periodictable
# Function to get information about an element
def get_element_info(symbol):
    # Check if the symbol is valid
    if not periodictable.elements.symbol(symbol):
        print("Invalid element symbol.")
        return    
    # Access information about the specified element
    element = periodictable.elements.symbol(symbol)    
    # Print information about the element
    print(f"Element: {element.name}")
    print(f"Symbol: {element.symbol}")
    print(f"Atomic Number: {element.number}")
    print(f"Atomic Weight: {element.mass}")
    print(f"Density: {element.density}")
nameMap = []
for elm in periodictable.elements:
    nameMap.append((elm.symbol,elm.name,elm.number,elm.mass,elm.density))
nameMap.sort(key=lambda x: x[1])
print(nameMap)        
print('referece: https://ptable.com/?lang=en#Properties')
print('reference: https://en.wikipedia.org/wiki/List_of_chemical_elements')
print('Enter one of the above symbols to get information about the element eg Na for sodium(case senstive)')
# Prompt the user to input an element symbol
element_symbol = input("Enter the symbol of the element: ")
# Call the function to get information about the specified element
get_element_info(element_symbol)