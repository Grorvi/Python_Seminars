#Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.( 3 методами)

string = """Слово слово буква буква цифра"""
list = string.lower().split()
print(string)
print(list)
catalog = {}
for world in list:
    catalog[world] = catalog.get(world, 0) + 1
count = 0
for _ in catalog:
    count +=1
print(count)
key = catalog.keys()
print(len(key))
print(len(set(list)))