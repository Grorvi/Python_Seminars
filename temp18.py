#Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива.
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива

import random
length_mass_1 = int(input("Введите длину 1 списка: "))
random_mass_1 = [random.randint(1,30) for _ in range(length_mass_1)]
count = 0
temp_list = []
for i in range(-1, length_mass_1-1):
    if random_mass_1[i-1] < random_mass_1[i] and random_mass_1[i+1] < random_mass_1[i]:
        count += 1
print(random_mass_1)
print(count)