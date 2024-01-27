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
import matplotlib.pyplot as plt

# ورودی‌ها
x = np.arange(number_of_power + 1)  # 0 تا number_of_power
y = np.array(coefficients)

# برازش یک چندجمله‌ای
degree = number_of_power
coefficients = np.polyfit(x, y, degree)

# ساختن یک تابع چندجمله‌ای با استفاده از ضرایب برازش شده
poly_function = np.poly1d(coefficients)

# تولید نقاط برای رسم خط برازش
x_fit = np.linspace(0, number_of_power, 100)
y_fit = poly_function(x_fit)

# نمایش داده‌ها و خط برازش شده
plt.plot(x_fit, y_fit, color='red', label='خط برازش شده')
plt.scatter(x, y, label='نقاط داده‌ها')
plt.xlabel('متغیر مستقل')
plt.ylabel('متغیر وابسته')
plt.title('برازش چندجمله‌ای به داده‌ها')
plt.legend()
plt.grid(True)
plt.show()










