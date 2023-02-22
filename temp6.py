#Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи
# оно является, то есть выведите такое число n, что φ(n)=A. Если А не является
# числом Фибоначчи, выведите число -1.

number = int(input('Введите число'))
fibonaci_1 = 1
fibonaci = 2
count = 4

while fibonaci < number:
    temp = fibonaci
    fibonaci = fibonaci + fibonaci_1
    fibonaci_1 = temp
    count += 1

if number == fibonaci:
    print(f'Число {number} равно числу Фибоначи с номером {count}')

else:
    print('Такого числа Фтбоначи нет')

