#  1 دریافت چند جمله ای
#در شروع ابتدا درجه اخرین جمله دریافت میشه 
#با استفاده از حلقه هر مرحله تا زمانی که حلقه برقراره :
#ضریب دریافت میشه 
# و در لیست اضافه میشه 
number_of_power = int(input("enter a number of power : "))
i = 0
text = "enter a coffiecient  x^"
coefficients = []
while i <= number_of_power :
    coefficient = int(input("enter x^{i}"))
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
 
while 0 <= number_of_power  :
    if 0 != number_of_power :
        equation_str += f"{coefficients[number_of_power]}x^{number_of_power} +  " 
    else :
        equation_str += f"{coefficients[number_of_power]}x^{number_of_power}    "
    number_of_power -= 1
print(equation_str)
#دریافت چند جمله ای 2
#در شروع ابتدا درجه اخرین جمله دریافت میشه 
#با استفاده از حلقه هر مرحله تا زمانی که حلقه برقراره :
#ضریب دریافت میشه 
# و در لیست اضافه میشه 
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
#این تابع در ابتدا دو لیست ضرایب رو هم اندازه میکنه
#بعد عناصر موجود در این دو لیست رو باهم جمع میکنه 
#و در یک لیست جدا میریزه 
#مربوط به خودش در یک استرینگ خالی که تعریف شده میریزه#ه  x{i}سپس این ضرایب رو در کنار 
#در اخر اون استرینگ رو چاپ میکنیم که همون حاصل جمع دو چندجمله ای هست     
def Sum(coefficients, coefficients2):
    minimum = min(len(coefficients), len(coefficients2))
    maximum = max(len(coefficients), len(coefficients2))
    sum_result = []
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
        sum_result.append(maximum_func[i] + minimum_func[i])
        i += 1
    return sum_result

sum_result = Sum(coefficients, coefficients2)
to_be_printed = ""
i = 0
while i < len(sum_result):
    if i != len(sum_result):
         to_be_printed += f"{sum_result[i]}x^^{i} + "
    else :
        to_be_printed += f"{sum_result[i]}x^^{i}  "
    i += 1
print("the sum is :    ")
print(to_be_printed)

#محاسبه تفریق دو چند جمله ای
#این تابع در ابتدا دو لیست ضرایب رو هم اندازه میکنه
#بعد عناصر موجود در این دو لیست رو باهم تفریق میکنه 
#و در یک لیست جدا میریزه 
#مربوط به خودش در یک استرینگ خالی که تعریف شده میریزه  x{i}سپس این ضرایب رو در کنار 
# در اخر اون استرینگ رو چاپ میکنیم که همون حاصل تفریق دو چندجمله ای هست     
def Subtraction(coefficients, coefficients2):
    subtraction_result = []
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

    while i < len(minimum_func):
        subtraction_result.append(maximum_func[i] - minimum_func[i])
        i += 1

    return subtraction_result

subtraction_result = Subtraction(coefficients, coefficients2)
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
#این تابع ضرب دو چند جمله ای رو حساب میکنه 
#ابتدا به اندازه جمع درجات مجموعه اولی و مجموعه دومی به علاوه یک در مجموعه ضرایب ضرب 0 اضافه می کنیم
#  بعد با استفاده از وایل تو در تو عنصر ضرب مجموعه ضرایب اولی رو در  عنصر ضرایب دومی در عنصر مجموعه ضرایب میریزیم
# تابع رو فرا میخونیم که ضرب دو مجموعه رو حساب کنه 
#   و  x^^{i}+ یک استرینگ خالی تعریف میکنیم کهضرایب رو درکنار
#چاپ میکنه 
def Multiplication(coefficients,coefficients2 , number_of_power , number_of_power2):
    multiplication= []
    max_degree = number_of_power + number_of_power2 + 1
    i = 0
    while i <= max_degree :
        multiplication.append(0)
        i += 1
    i = 0
    while i <= number_of_power :
        j = 0
        while j <= number_of_power2 :
              multiplication[i+j]  +=  coefficients[i] * coefficients2[j]
              j += 1
        i += 1

    return multiplication
multi_poly = Multiplication(coefficients,coefficients2 , number_of_power , number_of_power2)
to_be_printed = ""
i = 0
while i < len(multi_poly) :
    if i != len(multi_poly):
         to_be_printed += f"{multi_poly[i]}x^{i} + "
    else :
        to_be_printed += f"{multi_poly[i]}x^{i}    "
    i += 1
print("the multiplication is :  ")
print(to_be_printed)   

# ام یک چند جمله ای  n  مشتق 
# این تابع مشتق چندجمله ای رو حساب میکنه 
#با استفاده از حلقه ها تا زمانی که حلقه برقرار است 
# در لیست مشتق  , صفر رو اضافه میکنیم 
# و  لیست مشتق را برابر لیست ضرایب  ضرب در توان میکنیم
#در ادامه لیست  مشتق   رو باز میگردونیم
#بعد در ادامه یک ورودی برای تعداد دفعات مشتق گرفتن دریافت میکنیم 
#تا وقتی که حلقه برقرار است  while  دوباره با استفاده از حلقه 
#تابع رو فرا میخونیم که مشتق رو حساب کنه 
##   و  x^^{i}+ یک استرینگ خالی تعریف میکنیم کهضرایب رو درکنار
#چاپ میکنه 

def Derivative( coefficients , number_of_power ):
    derivative = []
    i = 1
    while i <= number_of_power :
        derivative.append(0)
        derivative[i-1] = coefficients[i]*i
        i += 1
    return derivative
number_of_derivative = int(input("enter a number of derivative :   "))
derivative_result = coefficients
i = 0
while  i < number_of_derivative :    
    derivative_result = Derivative(derivative_result , len(derivative_result)-1)
    i += 1
to_be_printed = ""
i = 0
while i < len(derivative_result):
    if i != len(derivative_result):
         to_be_printed += f"{derivative_result[i]}x{i} + "
    else :
        to_be_printed += f"{derivative_result[i]}x{i}  "
    i += 1
print("the derivative result is :    ")
print(to_be_printed)   

#ام چند جمله ای  n انتگرال 
# این تابع انتگرال چندجمله ای رو حساب میکنه 
#با استفاده از حلقه ها تا زمانی که حلقه برقرار است 
# در لیست انتگرال  , صفر رو اضافه میکنیم 
# و  لیست انتگرال را برابر لیست ضرایب تقسیم بر توان به علاوه یک  میکنیم
#در ادامه لیست  انتگرال   رو باز میگردونیم
#بعد در ادامه یک ورودی برای تعداد دفعات انتگرال گرفتن دریافت میکنیم 
#تا وقتی که حلقه برقرار است  while  دوباره با استفاده از حلقه 
#تابع رو فرا میخونیم که انتگرال رو حساب کنه 
##   و  x^^{i}+ یک استرینگ خالی تعریف میکنیم کهضرایب رو درکنار
#چاپ میکنه 
def Integral( coefficients , number_of_power ) :
    integral=[]
    i = 0
    while i <= number_of_power :
        integral[i+1].append(coefficients[i]/(i+1))
        i += 1
    return integral
number_of_integral = int(input("enter a number of integral :   "))
integral_result = coefficients
i = 0
while i < number_of_integral:
    integral_result = Integral(integral_result, len(integral_result))
    i += 1
to_be_printed = ""
i = 0
while i < len(integral_result):
    if i != len(integral_result):
         to_be_printed += f"{integral_result[i]}x{i} + "
    else :
        to_be_printed += f"{integral_result[i]}x{i}  "
    i += 1
print("the integral result is :    ")
print(to_be_printed)   


#numpyجمع با 
# با استفاده از کتابخانه نامپای دو لیست به دو ارایه تبدیل میشن که جمع دو ارایه , ارایه مجموع ضرایب رو تشکیل میده
#که یک کلاس از کتابخانه نامپای است   استفاده میکنیم  np.poly1d برای نوشتن به فرم چند جمله ای از 
# در اخر حاصل را چاپ می کنیم
import numpy as np 
coefficients.reverse()
coefficients2.reverse()
sum_Coef1 = np.array(coefficients)
sum_Coef2 = np.array(coefficients2)
sum_MatrixCoefResult =sum_Coef1  + sum_Coef2
sum_matrix_result=np.poly1d(sum_MatrixCoefResult)
print("sum of the resulting polynomial with numpy")
print(sum_matrix_result)
#numpy تفریق با
# با استفاده از کتابخانه نامپای دو لیست به دو ارایه تبدیل میشن که تفریق دو ارایه, تفریق ارایه  ضرایب رو تشکیل میده
#که یک کلاس از کتابخانه نامپای است   استفاده میکنیم  np.poly1d برای نوشتن به فرم چند جمله ای از 
# در اخر حاصل را چاپ می کنیم
import numpy as np
subtraction_Coef1 = np.array(coefficients)
subtraction_Coef2 = np.array(coefficients2)
subtraction_MatrixCoefResult = subtraction_Coef1 - subtraction_Coef2
subtraction_matrix_result=np.poly1d(subtraction_MatrixCoefResult)
print("subtraction of the resulting polynomial with numpy")
print(subtraction_matrix_result)

#numpy ضرب با  
# برعکس  میکنیم.inverse ابتدا داخل دو لیست را به کمک  
#حاصل ضرب دو لیست را حساب میکنیم و در لیست حاضل ضرب ضرایب میریزیم polymul به کمک تابع 
#که یک کلاس از کتابخانه نامپای است   استفاده میکنیم  np.poly1d برای نوشتن به فرم چند جمله ای از 
# در اخر حاصل را چاپ می کنیم
import numpy as np
Multiplication_coefficients = np.polymul(coefficients, coefficients2)
Multiplication_string = np.poly1d(Multiplication_coefficients)
print("Multiplication of the resulting polynomial with numpy")
print(Multiplication_string)
#numpy تقسیم با 
#ابتدا به کمک  کتابخانه نامپای دو لیست را به آرایه تبدیل میکنیم 
#میریزیم quotient, remainder حاصل تقسیم دو چند جمله ای را حساب میکنیم و در  polydiv با کمک تابع 
# که یک کلاس از کتابخانه نامپای است دو آرایه را فرم چندجمله ای  در میاوریمnp.poly1d به کمک
#را چاپ میکنیم  quotient, remainder در اخر 
import numpy as np
dividend = np.array(coefficients2)  
divisor = np.array(coefficients)  
quotient, remainder = np.polydiv(dividend, divisor)
quotient  = np.poly1d(quotient)
remainder = np.poly1d(remainder)
print("Quotient:" , quotient)
print("Remainder:", remainder)

# numpyمشتق با  
# تازمانی که متغیر کمکی از تعداد دفعات مشتق گرفتن کوجکتر استwhile با استفاده از حلقه 
# بار حساب میشه n مشتق لیست ضرایب  polyder ابتدا با استفاده از تابع 
## که یک کلاس از کتابخانه نامپای است دو آرایه را فرم چندجمله ای  در میاوریمnp.poly1d به کمک
#و در انتها مقدار مشتق رو جاپ میکنیم 
import numpy as np
derivativee_coefficients = coefficients
i = 0
while i < number_of_derivative :
    derivativee_coefficients = np.polyder(derivativee_coefficients)
    i += 1
derivative_string = np.poly1d(derivativee_coefficients)
print("Derivative of the resulting polynomial with numpy:")
print(derivative_string)

#numpy انتگرال با
#با استفاده از کتابخانه نامپای 
#به ارایه تبدیل میکنیم np.array لیست ضرایب رو با استفاده از 
#تا زمانی که حلقه برقرار است  while با استفاده از حلقه 
# انتگرال ضرایب گرفته میشه و در لیست انتگرال اضافه میشه np.polyint در لیستی که تعریف کردیم با استفاده از 
#تازمانی که حلقه برقرار است  while دوباره با استفاده از یک حلقه 
# مقدار  انتگرال چند چندجمله ای رو جاپ میکنیم  np.poly1d با استفاده از 
import numpy as np
coefficients_array = np.array(coefficients)
integrals = [coefficients_array]  
i = 0
while i < number_of_integral:
    integrals.append(np.polyint(integrals[-1]))
    i += 1
print("The integral results are:")
i = 0
while i < len(integrals):
    print(np.poly1d(integrals[i]))
    i += 1

#numpy ریشه با 
#این تابع ریشه چند جمله ای رو حساب میکنه
#  با استفاده از  کتابخانه نامپای
#حساب میکنیم np.roots ابتدا ریشه هارو به کمک تابع
#درانتها تابع رو فراخوانی میکنیم
#ریشه هارو در اخر چاپ میکنیم
import numpy as np
def finding_roots(coefficients):
    roots = np.roots(coefficients)    
    return roots
roots = finding_roots(coefficients)
print("Root(s) of the polynomial equation:", roots)

#برازش منحنی 
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def model_function(x, *coefficients):                                   
    powers_of_x = np.vstack([x**i for i in range(len(coefficients))]).T
    y = np.dot(powers_of_x, coefficients)
    return y
number_of_power = int(input("Enter the number of power: "))
coefficients = []
i = 0
while i <= number_of_power:
    coefficient = float(input(f"Enter the coefficient of x^{i}: "))
    coefficients.append(coefficient)
    i += 1
x_data = np.linspace(-10, 10, 100)
y_data = model_function(x_data, *coefficients) + np.random.normal(0, 5, len(x_data)) 
popt, pcov = curve_fit(model_function, x_data, y_data, p0=coefficients)
y_fit = model_function(x_data, *popt)
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, y_fit, color='green', label='Fitted curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Curve Fitting for the Polynomial')
plt.legend()
plt.grid(True)
plt.show()
