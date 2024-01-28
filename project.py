#  1 دریافت چند جمله ای
#در ابتدا ما به عنوان ورودی تعداد توان رو از کاربر دریافت میکنیم
#و بعد با استفاده از حلقه ها تا زمانی که متعیر کمکی ما کوچکتر و مساوی تعداد توان هاست 
#ضریب هارو دریافت میکنیم و در مجموعه ضرایب ان را اضافه میکنیم
number_of_power = int(input("enter a number of power : "))
i = 0
coefficients = []
while i <= number_of_power :
    coefficient = int(input(f"enter coefficient of x^^{i} : "))
    coefficients.append(coefficient)
    i += 1
# 1 نمایش چند جمله ای
#یک استرینگ خالی بتعریف میکنیم 
# با استفاده از حلقه تا زمانی که متغیر کمکی ما از تعداد توان کوچکتر است 
# اگر درجه برابر متغیر کمکی نبود
#  با + جمع کنه و در همون استرینگ مقدار خالی رو بریزه  x^{i}  ام در i استرینگ خالی رو با ضریب 
#جمع کنه و در همون استرینگ مقدار رو بریزه x^{i}  ام در i در غیر اینصورت استرینگ خالی رو با ضریب ت 
#در اخر هم استرینگ تعریف شده رو چاپ میکینم 
equation_str = "" 
i = 0 
while i <= number_of_power :
    if i != number_of_power:
        equation_str += f"{coefficients[i]}x^{i} + "
    else :
        equation_str += f"{coefficients[i]}x^{i}"
    i += 1
print(equation_str)
#دریافت چند جمله ای 2
#در ابتدا ما به عنوان ورودی تعداد توان رو از کاربر دریافت میکنیم
#و بعد با استفاده از حلقه ها تا زمانی که متعیر کمکی ما کوچکتر و مساوی تعداد توان هاست 
#ضریب هارو دریافت میکنیم و در مجموعه ضرایب ان را اضافه میکنیم
number_of_power2 = int(input("enter a number of power : "))
i = 0
coefficients2 = []
while i <= number_of_power2 :
    coefficient2 = int(input(f"enter coefficient of x^^{i} : "))
    coefficients2.append(coefficient2)
    i += 1
# 2 نمایش چند جمله ای 
#یک استرینگ خالی بتعریف میکنیم 
# با استفاده از حلقه تا زمانی که متغیر کمکی ما از تعداد توان کوچکتر است 
# اگر درجه برابر متغیر کمکی نبود
#  با + جمع کنه و در همون استرینگ مقدار خالی رو بریزه  x^{i}  ام در i استرینگ خالی رو با ضریب 
#جمع کنه و در همون استرینگ مقدار رو بریزه x^{i}  ام در i در غیر اینصورت استرینگ خالی رو با ضریب ت 
#در اخر هم استرینگ تعریف شده رو چاپ میکینم 
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
#این تابع مقدار تابع را در یک نقطه دلخواه محاسبه میکند
#ابتدا تابع عدد که میخواهیم  مقدار ان را حساب کنیم میگیرد 
#answer = 0 قرار میدهیم 
# i= 0 میدهیم
#است  i<=number_of_power تا زمانی که  while با اسفاده از  
#میریزیم answer  میکنیم و در  coefficients[i]*(x**i)را به علاوه answer 
# یکی اضافه میکنیم  i به 
#در اخر هم مقدار تابع رو در اون نقطه چاپ میکند
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
    if i != len(sum_result):
         to_be_printed += f"{sum_result[i]}x{i} + "
    else :
        to_be_printed += f"{sum_result[i]}x{i}  "
    i += 1
print("the sum is :    ")
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

subtraction_result = subtraction(coefficients, coefficients2)
to_be_printed = ""
i = 0
while i < len(subtraction_result):
    if i != len(subtraction_result):
         to_be_printed += f"{subtraction_result[i]}x{i} + "
    else :
        to_be_printed += f"{subtraction_result[i]}x{i}  "
    i += 1
print("the subtraction is :    ")
print(to_be_printed)

#ضرب دو چند جمله ای
def Multiplication(coefficients,coefficients2 , number_of_power , number_of_power2):
    multiplication= []
    max_degree = number_of_power+number_of_power2 + 1
    i = 0
    while i <= max_degree :
        multiplication.append(0)
        i += 1
    for i in range(0,number_of_power+1) :
        for j in range(0,number_of_power2+1):
            multiplication[i+j] += coefficients[i]*coefficients2[j]
    return multiplication
multi_poly = Multiplication(coefficients,coefficients2 , number_of_power , number_of_power2)
to_be_printed = ""
i = 0
while i < len(multi_poly):
    if i != len(multi_poly):
         to_be_printed += f"{multi_poly[i]}x{i} + "
    else :
        to_be_printed += f"{multi_poly[i]}x{i}  "
    i += 1
print("the multiplication is :    ")
print(to_be_printed)   


































#numpyجمع با 
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
print("sum of the resulting polynomial with numpy")
print(eq)
#numpy تفریق با
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
print("subtraction of the resulting polynomial with numpy")
print(eq)

#numpy ضرب با  
import numpy as np
coefficients.reverse()
coefficients2.reverse()
Multiplication_coefficients = np.polymul(coefficients, coefficients2)
Multiplication_string = np.poly1d(Multiplication_coefficients)
print("Multiplication of the resulting polynomial with numpy")
print(Multiplication_string)
#numpy تقسیم با 

# numpyمشتق با  

import numpy as np
derivative_coefficients = np.polyder(coefficients)
derivative_string = np.poly1d(derivative_coefficients)
print("Derivative of the resulting polynomial with numpy:")
print(derivative_string)

#numpy انتگرال با 
import numpy as np
integral_coefficients = np.polyint(coefficients)
integral_string = np.poly1d(integral_coefficients)
print("integral of the resulting polynomial with numpy")
print(integral_string)
#numpy ریشه با 







#برازش منحنی 

import numpy as np
import matplotlib.pyplot as plt
number_of_power = int(input("Enter the number of power: "))
coefficients = []
for i in range(number_of_power + 1):
    coefficient = float(input(f"Enter coefficient of x^{number_of_power - i}: "))
    coefficients.append(coefficient)
x_data = np.linspace(-10, 10, 100)  
y_data = np.polyval(coefficients, x_data)  
plt.plot(x_data, y_data, label='Fitted Curve', color='green')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Curve Fitting')
plt.legend()
plt.grid(True)
plt.show()





