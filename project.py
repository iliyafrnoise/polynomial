number_of_power = int(input("enter a number of power : "))
i = 0
coefficients = []
while i <= number_of_power :
    coefficient = int(input(f"enter coefficient of x^^{i} : "))
    coefficients.append(coefficient)
    i += 1
equation_str = "" 
i = 0 
while i <= number_of_power :
    if i != number_of_power:
        equation_str += f"{coefficients[i]}x^{i} + "
    else :
        equation_str += f"{coefficients[i]}x^{i}"
    i += 1
print(equation_str)
number_of_power2 = int(input("enter a number of power : "))
i = 0
coefficients2 = []
while i <= number_of_power2 :
    coefficient2 = int(input(f"enter coefficient of x^^{i} : "))
    coefficients2.append(coefficient2)
    i += 1
equation_str2 = ""
i = 0 
while i <= number_of_power2 :
    if i != number_of_power2:
        equation_str2 += f"{coefficients2[i]}x^{i} + "
    else :
        equation_str2 += f"{coefficients2[i]}x^{i}"
    i += 1
print(equation_str2)
# x{0}محاسبه مقدار تابع در 
def calculate(coefficients , number_of_power ):
    x = int(input("enter x : "))
    answer = 0 
    i = 0 
    while i <= number_of_power :
        answer += coefficients[i]*(x**i)
        i += 1
    return(answer)
print(calculate(coefficients,number_of_power))

#تابع جمع دو  چند جمله ای
def sum(coefficients, coefficients2):
    minimum = min(len(coefficients), len(coefficients2))
    maximum = max(len(coefficients), len(coefficients2))
    result = []
    i = 0

    if minimum == len(coefficients):
        minimum_func = coefficients
        maximum_func = coefficients2
    else:
        minimum_func = coefficients2
        maximum_func = coefficients

    while len(minimum_func) < len(maximum_func):
        minimum_func.append(0)

    while i < len(minimum_func):
        result.append(maximum_func[i] + minimum_func[i])
        i += 1

    return result

sum_result = sum(coefficients, coefficients2)
to_be_printed = ""
i = 0
while i < len(sum_result):
    to_be_printed += f"{sum_result[i]}x{i} + "
    i += 1

to_be_printed += "0"

print(to_be_printed)

#محاسبه تفریق دو چند جمله ای
def subtraction(coefficients, coefficients2):
    maximum_func = []
    minimum_func = []
    result = []
    i = 0

    minimum = min(len(coefficients), len(coefficients2))
    maximum = max(len(coefficients), len(coefficients2))

    if maximum == len(coefficients):
        maximum_func = coefficients
        minimum_func = coefficients2
    else:
        maximum_func = coefficients2
        minimum_func = coefficients

    while len(minimum_func) < len(maximum_func):
        minimum_func.append(0)

    while i < minimum:
        result.append(maximum_func[i] - minimum_func[i])
        i += 1

    return result

sum_result = subtraction(coefficients, coefficients2)
to_be_printed = ""
i = 0
while i < len(sum_result):
    to_be_printed += f"{sum_result[i]}x{i} + "
    i += 1

to_be_printed += "0"

print(to_be_printed)


import numpy as np

MatrixCoef1 = np.array(coefficients)
MatrixCoef2 = np.array(coefficients2)

MatrixCoefResult = MatrixCoef2 + MatrixCoef1
eq = ""
i = 0
while i <= max(number_of_power , number_of_power2) :
    if i != max(number_of_power2 , number_of_power):
        eq += f"{MatrixCoefResult[i]}x^{i} + "
    else :
        eq += f"{MatrixCoefResult[i]}x^{i}"
    i += 1
print(eq)

import numpy as np

MatrixCoef1 = np.array(coefficients)
MatrixCoef2 = np.array(coefficients2)

MatrixCoefResult = MatrixCoef1 - MatrixCoef2
eq = ""
i = 0
while i <= max(number_of_power , number_of_power2) :
    if i != max(number_of_power2 , number_of_power):
        eq += f"{MatrixCoefResult[i]}x^{i} + "
    else :
        eq += f"{MatrixCoefResult[i]}x^{i}"
    i += 1
print(eq)







