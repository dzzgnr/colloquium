'''
39. Дані про температуру повітря і кількості опадів за декаду квітня
зберігаються в масивах. Визначити кількість опадів, що випали у вигляді дощу і у вигляді снігу за цю декаду.
'''

import random #для заполнения массива

arr = [[0] * 10 for i in range(2)] #инициализация массива

for i in range(10): #для 10 дней
    arr[0][i] = random.randrange(-5, 16) #выбираем температуру от -5 до 15 градусов
    arr[1][i] = random.randrange(0, 40) #и количество осадков от 0 до 40мм

print(arr)

snow = 0 #количество осадков в виде снега
rain = 0 #в виде дождя

for i in range(10): #для всех дней
    if arr[0][i] < 0: #если температура ниже 0
        snow += arr[1][i] #считаем осадки снегом
    else:
        rain += arr[1][i] #если выше - дождём

print('\ntotal precipitation as snow :', snow, 'mm')
print('\ntotal precipitation as rain :', rain, 'mm')
