'''
51. Дан одновимірний масив а. Сформувати новий масив, який складається
тільки з тих елементів масиву а, які перевищують свій номер на 10. Якщо таких елементів немає, то видати повідомлення.
'''

a = [0, 11, 1, 5, 4, 65, 65, 5, 11]

new_a = [] #новый массив

for i in range(len(a)): #для всех элементов массива
    if a[i] == 10 + i: #если элемент = 10 + свой индекс
        new_a.append(a[i]) #добавляем его в новый массив

if len(new_a) == 0: #если новый массив пуст
    print('no such elements') #сообщаем
else:
    print('new_a :', new_a) #если нет - выводим его
