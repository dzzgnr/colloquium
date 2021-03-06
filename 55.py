'''
55. У будинку, що складається з 30 квартир, переселити мешканців так, щоб мешканці першої квартири переїхали в тридцяту, з тридцятого в першу, з другої в 29 і т.д., знайдіть кількість квартир, в яких проживає більше 5 осіб.
'''

import numpy as np

apartments = np.random.randint(1, 7, size = 30) #массив, которые соответствует количеству жителей в 30 квартирах, которые являются случайными числами от 1 до 6

print(apartments)
print('\nafter relocation :\n', np.flip(apartments)) #переворачиваем массив

count = 0 #количество квартир

for i in range(30): #для всех квартир
    if apartments[i] > 5: #если жителей больше 5
        count += 1 #увеличиваем количество на 1

print('\n', count, 'apartments has more than 5 inhabitants')
