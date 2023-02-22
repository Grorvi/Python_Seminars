#Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
#Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на
# новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и
# не превышают 30000.

import random
number_watermelon = int(input('Введите номер арбуза: '))
weight_1 = random.randint(1000, 3000)
print(f'Вес арбуза: {weight_1}')
max_weight = weight_1
min_weight = weight_1
for i in range(number_watermelon - 1):
    weight = random.randint(1000, 3000)
    print(f'Вес {i +2} арбуза: {weight}')
    if weight > max_weight:
        max_weight = weight
    elif weight < min_weight:
        min_weight = weight
print(f'Мин вес = {min_weight}, макс вес = {max_weight}')