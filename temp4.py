#Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

#*Примеры:*
#- 6,78 -> 7
#- 5 -> нет
#- 0,34 -> 3

a = float(input("Ведите числоa: "))
print(int(a*10)%10)