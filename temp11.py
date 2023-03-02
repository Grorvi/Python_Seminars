#Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется
# к символам с помощью постфикса формата _n.

#string = input("Enter a string: ")
#dictionary = {}

#for i in string:
   # dictionary[i] = dictionary.get(i, 0) + 1

    #if dictionary[i] == 1:
        #print(i, end = ", ")
    #else:
        #print(f'{i}_{dictionary[i] - 1}', end = ", ")

import random

my_list = [random.randint(1, 5) for _ in range(10)]
print(my_list)
my_dict = {}

for i in my_list:
    my_dict[i] = my_dict.get(i, 0) + 1
    print(i if my_dict.get(i) == 1 else f'{i}_{my_dict.get(i) - 1}', end=' ')
    print('\n' + f'{my_dict}')
