#1. Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за
# погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько 
# дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов 
# Цельсия. Напишите программу, помогающую синоптикам в работе.

#Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.

#Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50

import random
count_day = int(input('сколько дней: '))
temp = 0
count = 0
count_max = 0

for i in range(count_day):
    temp += random.randint(-2, 2)
    if temp > 0:
        count += 1
    else:
        count = 0
    print(temp)
    if count > count_max:
        count_max = count
    print(count_max)