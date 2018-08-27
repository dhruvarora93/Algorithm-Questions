def multiply(num1,num2):
    str_to_int = {}
    for i in range(10):
        str_to_int[str(i)] = i

    number1 = 0

    for i,j in enumerate(num1[::-1]):
        number1 += (pow(10,i) * str_to_int[j])

    number2 = 0

    for i, j in enumerate(num2[::-1]):
        number2 += (pow(10, i) * str_to_int[j])

    return str(number1 * number2)

print(multiply("123","456"))
