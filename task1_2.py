# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# n=int(input())
# r1=list(map(int,input().split(' ')))
# r2=list(map(int,input().split(' ')))
 
# a1=[]
# a2=[]
 
# for i in range(1,n+1):
#     if (i in r1) & (i in r2):
#         a1+=[i]
#     if (not (i in r1)) & (not (i in r2)):
#         a2+=[i]
        
# for i in a1:
#     print(i,end=' ')
# print()
# for i in a2:
#     print(i,end=' ')

# Просто про фермерсое хозяйство Карелии и соседние кусты! Условия жесть!!!

count_bushes  = int(input('Введите кол-во кустов: '))
list_bushes = [int(input('Введите кол-во ягод на кусте: ')) for _ in range(count_bushes)]
max_sum = 0
for i in list_bushes:
    sum = list_bushes[i % count_bushes] + list_bushes[(i + 1) % count_bushes] + list_bushes[(i + 2) % count_bushes]
    if sum >= max_sum:
        max_sum = sum
print(max_sum)