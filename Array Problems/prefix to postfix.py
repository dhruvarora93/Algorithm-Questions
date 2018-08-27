def prefix_to_postfix(string):
    stack = []
    operators = ['+','-','/','*']

    for i in string[::-1]:
        if i not in operators:
            stack.append(i)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            temp = str(operand1) + str(operand2) + i
            stack.append(temp)

    return stack.pop()



print(prefix_to_postfix('*-A/BC-/AKL'))