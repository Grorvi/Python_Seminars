#Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве),
# которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива.
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива


import random
length_mass_1 = int(input("Введите длину 1 списка: "))
random_mass_1 = [random.randint(1,30) for _ in range(length_mass_1)]
length_mass_2 = int(input("Введите длину 2 списка: "))
random_mass_2 = [random.randint(1,30) for _ in range(length_mass_2)]
temp_list = []
print(random_mass_1)
print(random_mass_2)
for i in random_mass_1:
    if i not in random_mass_2:
        temp_list.append(i)
print(temp_list)

