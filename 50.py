'''
50. У лотереї розігрувалося 100 квитків. Таблиця містить 10 номерів
виграшних квитків. Перевірте, чи є квиток з номером N виграшним.
'''

import numpy as np

winners = np.random.randint(1, 101, size = 10) #заполняем массив 10 случайными числами от 1 до 100

number = int(input('enter number :')) #ввод и запись номера

if number in winners: #если номер среди победителей
    print('you won')
else:
    print('you lost')
