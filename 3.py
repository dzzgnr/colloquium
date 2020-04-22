'''
3. Створіть масив з п'яти прізвищ і виведіть їх на екран стовпчиком,
починаючи з останнього
'''

arr = [] #инициализация массива

print('enter 5 surnames : ')

for i in range(5):
    el = input() #ввод фамилии
    arr.append(el) #добавление в массив

print('\narr :', arr, '\n')

for i in range(5):
    print(arr[4 - i]) #вывод фамилий с конца

'''
4. Створіть масив з п'яти прізвищ і виведіть на екран ті з них, які
починаються з певної букви, яка вводиться з клавіатури.
'''

arr = [] #инициализация массива

print('enter 5 surnames : ')

for i in range(5):
    el = input() #ввод фамилии
    arr.append(el) #добавление в массив

print('\narr :', arr)

print('\nenter the letter for which surname will be displayed : ')

letter = input() #ввод буквы

print('\n')

for i in range(5):
    if (arr[i])[0] == letter: #если первая буква фамилии совпадает с вводом - выводим фамилию
        print(arr[i])
