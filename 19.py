import numpy as np

arr = np.random.randint(200, 301, size = 20) #инициализация массива из 20 случайных чисел в диапазоне [200, 300] 

print('arr:', arr)

summ = 0 #переменная для суммы

for i in range(20): #для всех элементов
    if arr[i] % 2 == 3: #если остаток от деления на 2 = 3
        summ += arr[i] #добавляем элемент в сумму

print('summ = ', summ) #выводим результат
