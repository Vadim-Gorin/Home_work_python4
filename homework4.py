# 1. Вычислить число c заданной точностью d
# Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""
import random
import os 

def digit_P(number_digit):
    size = 500000 # число прогонов, чем больше тем выше точность
    i = 0
    count = 0     # количество точек в круге
    result = 0

    while (i < size):
        # получаем случайные координаты Х и У на плоскости
        x = random.random()
        y = random.random()

        # уравнение окружности (x^2 + y^2) = r^2
        # при r=1 если (x^2 + y^2) <1 то точка внутри круга, иначе вне круга
        if (pow(x, 2) + pow(y, 2)) < 1:
            count = count + 1
        i = i + 1

    # Значение Пи = (площадь круга / площадь квадрата) * 4
    result = round (((count / size) * 4), number_digit)  
    return result

size_of_PI = int(input("Введите точность числа: ")) 
pi = digit_P(size_of_PI)
os.system('CLS') 
print ("Значение числа Пи =", pi)
"""

"""
# 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import os

N = int(input("Введите число N: "))
original_number = N
result_list = list()

# наименьшее простое число=2, перебираем от 2 до N 
i = 2 
while i <= N:
    if N % i == 0:
        result_list.append(i)
        N = N / i
        i = 2
    else:
        i = i + 1
os.system('CLS') 
print(f"Простые множители числа {original_number} приведены в списке: {result_list}")
"""

"""
# 2. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import os

# задаем элементы руками
def handle_Newlist (size):
   my_list = list()
   print ()
   for i in range (size):
      print("Введите элемент №", i+1,":  ", end='')
      num = int(input())
      my_list.insert(i, num)
   print ()
   print ("Исходный список:")
   print (my_list)
   return my_list

# получаем исх список 
os.system('CLS') 
digit = int(input("Введите количество элементов исходной последовательности: "))
new_list = handle_Newlist(digit)

# получаем результ список
Result_list = list()
for i in new_list:
    if i not in Result_list:
        Result_list.append(i)

print ()
print("Список из неповторяющихся элементов исходной последовательности:")
print (Result_list)
"""


"""
# 3. Задана натуральная степень k. 
#    Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена, 
#    записать в файл многочлен степени k.
#    Пример:- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import os

# генерируем случайным образом список коэффициентов многочлена
import random
def random_Newlist (size):
   my_list = list()
   for i in range (size):
      num = random.randint(1,101)
      my_list.insert(i, num)
   return my_list

# получаем текстовку с уравнением
def create_equation(coeff):
    my_list= coeff[::-1]
    result = ''    
    # нет коэффициентов - уравнение "нулевое" (х=0)
    if len(my_list) < 1:
        result = 'x = 0'
    else:
        for i in range(len(my_list)):
            if i != len(my_list) - 1 and my_list[i] != 0 and i != len(my_list) - 2:
                result = result + f'{my_list[i]}x^{len(my_list)-i-1}'
                if my_list[i+1] != 0:
                    result = result + ' + '
            elif i == len(my_list) - 2 and my_list[i] != 0:
                result = result + f'{my_list[i]}x'
                if my_list[i+1] != 0:
                    result = result + ' + '
            elif i == len(my_list) - 1 and my_list[i] != 0:
                result = result + f'{my_list[i]} = 0'
            elif i == len(my_list) - 1 and my_list[i] == 0:
                result = result + ' = 0'
    return result


# запись в файл
def inFile(text_message):
    f = open('file_task4.txt', 'w')
    f.write(text_message)
    f.close()

os.system('CLS') 
k = int(input("Введите степень многочлена k: "))
coeff_list = random_Newlist(k)
buffer = create_equation(coeff_list)
inFile(buffer)
"""
