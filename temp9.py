#Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический)
#на K элементов вправо, K – положительное число.

N = int(input("Введите N "))
K = int(input("Введите K "))
my_list = [ i for i in range(N)]
print(my_list)
my_list_end = my_list[K:] + my_list[:K]
print(my_list_end)


