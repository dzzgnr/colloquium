'''
33. Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.
'''

A = [1, 2, 3, 0, 4, 5, 0, 6, 7, 0, 8, 0, 9, 6, 0, 6, 7, 0, 9, 2]

mult = 1 #переменная для произведения

for i in range(20): #для всех элементов
    if A[i] != 0: #если он не равен 0
        mult *= A[i] #умножаем на остальные

print('mult =', mult)
