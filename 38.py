'''
38. Дані про направлення вітру (північний, південний, східний, західний) і
силі вітру за декаду листопада зберігаються в масиві. Визначити, скільки днів дув південний вітер з силою, що перевищує 8 м/с.
'''

import random #для заполнения массива

arr = [[0] * 10 for i in range(2)] #инициализация массива

directions = 'news' #направления ветра

for i in range(10): #для 10 дней
    arr[0][i] = random.choice(directions) #выбираем направление
    arr[1][i] = random.randrange(1, 16) #и скорость в диапазоне [1, 15]

print(arr)

count = 0 #количество дней

for i in range(10): #для всех дней
    if arr[0][i] == 's' and arr[1][i] > 8: #если ветер южный и скорость > 8 
        count += 1 #увеличиваем количество на 1

print('\nsouth wind with speed > 8 m/s was', count, 'times')

