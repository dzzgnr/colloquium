'''
43. Задано два натуральних числа a і b. Змінній w привласнити значення істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а і не кратний b.
'''

a = 2
b = 3

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

w = False #изначально омега = ложь

for i in range(len(arr)): #для всех элементов
    if arr[i] % a == 0 and arr[i] % b != 0: #если элемент делится на а и не делится на b
        w = True #ответ - истина

print(w)
