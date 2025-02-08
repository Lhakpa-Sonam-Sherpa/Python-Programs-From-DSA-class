
#operator and operand seperator
def expression_separator(expression):
    number = ""
    operator = ""
    operator_array = []
    operand_array = []
    expression_arr = []
    for character in expression:
        print(f"{character}")
        if character.isdigit():
            number = number + character
        elif not character.isdigit():
            operand_array.append(number)
            operator_array.append(character)
            number = ""
        
    operand_array.append(number)
    expression_arr.append(operand_array)
    expression_arr.append(operator_array)
    return operand_array, operator_array



expr = input("Enter the math expression:\n\t")
# expr = "123+12"
ops = expression_separator(expr)
print(f"operand: {ops[0]}\noperator: {ops[1]}")
