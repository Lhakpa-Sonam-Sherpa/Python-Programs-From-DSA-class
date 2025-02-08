number = ""
operator = ""
operator_array = []
operand_array = []
expression = input("Enter the math expression:\n\t")
# expression = "123+12"
for character in expression:
    print(f"{character}")
    if character.isdigit():
        number = number + character
    elif not character.isdigit():
        operand_array.append(number)
        operator_array.append(character)
        number = ""
    
operand_array.append(number)

print(f"operand: {operand_array}\noperator: {operator_array}")
