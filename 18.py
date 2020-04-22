'''
18. Знайти добуток всіх елемен тів масиву цілих чисел, менших 0. Розмірність
масиву 10. Заповнення масиву здійснити за допомогою клавіатури.
'''

arr = [] #инициализация массива
neg_mult = 1

print('enter 10 values : ')

for i in range(10):
    el = float(input()) #ввод элемента
    arr.append(el) #добавление в массив
    if el < 0:
        neg_mult *= el

print('arr :', arr)
print('\nmultiplication of negative numbers = ', neg_mult)
