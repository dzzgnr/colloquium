9. З 8 до 20 години температура повітря вимірювалася щогодини. Відомо,
що протягом цього часу температура знижувалася. Визначте, о котрій годині було вперше зафіксовано від'ємну температуру.
'''

import numpy as np #библиотека для использования функции случайных чисел

#функция для поиска индекса первого отрицательного элемента в массиве
def first_neg(list):
    for count, number in enumerate(list):
        if number < 0:
            return count

temp = np.random.randint(-5, 16, size = 13) #создание массива из 13 случайных чисел в диапазоне [-5; 15], которые соответствуют температуре в каждый час измерения от 8 до 20

regr_temp = np.sort(temp)[::-1] #новый, который соответствует порядку убывания температуры

print('temp:', regr_temp)

print('temp drops below zero at', 8 + first_neg(regr_temp), 'o`clock') #поиск и вывод момента времени
