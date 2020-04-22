'''
6. Створіть масив А[1..8] за допомогою генератора випадкових чисел з
елементами від -10 до 10 і виведіть його на екран. Підрахуйте кількість від’ємних елементів масиву.
'''

import numpy as np #библиотека для использования функции случайных чисел

A = np.random.randint(-10, 11, size = 8) #создание массива из 8 случайных чисел в диапазоне [-10; 10]

print('A:', A)

neg_count = 0 #инициализация переменной с количеством отрицательных элементов

for i in range(7): 
    if A[i] < 0: #если элмент меньше нуля - увеличиваем количество на 1
        neg_count += 1

print('\ncount of negative numbers :', neg_count)

