'''
36. Знайти суму додатніх елементів лінійного масиву цілих чисел.
Розмірність масиву 10. Заповнення масиву здійснити з клавіатури.
'''

arr = [] #инициализация массива

print('enter 10 elements: ')

for i in range(10):
    arr.append(int(input())) #ввод и добавление в массив

print('\narr :', arr)

summ = 0 #

for i in range(10): #для всех элементов массива
    if arr[i] >= 0: #если он положительный
        summ += arr[i] #добавляем его

print('\nsumm of positive elements = ', summ) #вывод суммы
