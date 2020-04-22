'''
57. Відомість на зарплату представлена як дві таблиці. Одна містить
прізвища працівників цеху, а друга їх зарплату за поточний місяць. Знайдіть прізвище працівника, зарплата якого найменш відхиляється від середньої зарплати всіх працівників за поточний місяць. Знайдіть прізвища двох працівників з найбільшою заробітною платою. Видаліть з відомості на зарплату відомості про працівника, зарплата якого мінімальна.
'''

import numpy as np

surnames = ['a' , 'b' ,  'c',  'd',  'e',  'f',  'g' ]
salaries = [4000, 5000, 6000, 7000, 8000, 9000, 10000]

average = sum(salaries) / len(salaries) #средняя зарплата
print('average sallary :', average)

delta = [] #массив отклонений от средней зарплаты

for i in range(len(salaries)): #для всех зарплат
    delta.append(abs(average - salaries[i])) #отклонение равно модулю разности между текущей и средней

idx_max_1 = (np.where(np.array(salaries) == max(salaries)))[0][0] #индекс самого большого элемента массива

m = salaries[0] #второй по величине элемент массива изначально равен первому
for i in range(1, len(salaries)): #от 2 и до последнего
    if salaries[i] > m and salaries[i] < max(salaries): #если следующий больше предыдущего и меньше максимального
        m = salaries[i] #он становится новым вторым по величине

idx_max_2 = (np.where(np.array(salaries) == m))[0][0] #индекс второго по величине элемента

print(surnames[idx_max_1], 'and', surnames[idx_max_2], 'have biggest sallary')

idx_min = (np.where(np.array(salaries) == min(salaries)))[0][0] #индекс минимального элемента

#убираем из массивов соответствия минимальному
surnames.pop(idx_min)
salaries.pop(idx_min)

#выводим
print(surnames)
print(salaries)
