'''
42. Підрахувати кількість елементів одновимірного масиву, для яких
виконується нері вність i*i < a[i] < i!
'''

import math as m #библиотека для использования факториала

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count = 0 #количество элементов

for i in range(len(arr)): #для всех элементов
    if i**2 < arr[i] and arr[i] < m.factorial(i): #если условие для элемента выполняется
        count += 1 #увеличиваем количество на 1

print('count =', count)
