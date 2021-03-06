'''
17. Знайти суму елементів масиву дійсних чисел, що мають непарні номери.
Розмірність масиву 20. Заповнення масиву здійснити випадковими числами від 100
до 200.
'''

import numpy as np #библиотека для использования функции случайных чисел

arr = np.random.randint(100, 201, size = 20) #создание массива из 20 случайных чисел в диапазоне [100; 200]

print('arr:', arr)

odd_idx_summ = 0 #инициализация пемеренной для записи суммы

for i in range(20): #для всех элементов массива
    if i % 2 != 0: #если у элемента нечётный индекс
        odd_idx_summ += arr[i] #добавляем этот элемент

print('summ of odd-index elements = ', odd_idx_summ) #вывод суммы
