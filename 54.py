'''
54. Введіть масив з 20 елементів і визначте, чи є в ньому елементи з
однаковим и значеннями.
'''

arr = [] #инициализация массива

print('enter 20 values :')

for i in range(20): #для всех элементов
    arr.append(input()) #вводим элемент и добалвяем в массив

if len(set(arr)) != len(arr): #если рамзер массива и размер сета отличаюся
    print('there are same elements') #значит есть повторы
else:
    print('all elements are different') #иначе - все элементы разные
