'''
8. Створіть цілочисельний масив А[1..15] за допомогою генератора
випадкових чисел з елементами від -15 до 30 і виведіть його на екран. Визначте найбільший елемент масиву і його індекс.
'''

import numpy as np #библиотека для использования функции случайных чисел

A = np.random.randint(-15, 31, size = 15) #создание массива из 15 случайных чисел в диапазоне [-15; 30]

print('A:', A)

print('\nmax element :', max(A), 'at', (np.where(A == max(A)))[0], 'position') #вывод максимального элемента и его индекса(или индексов, если такое значение не одно) в массиве
