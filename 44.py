'''
44. Підрахуйте кількість елементів одновимірного масиву, які збігаються зі своїм номером і при цьому кратні 3.
'''

#функция которая принимает на вход массив и возвращает количесто элементов кратных 3 и совпадающих со своим индексом
def count(list):
    res = 0 #количество
    for i in range(len(list)): #для всех элементов
        if list[i] == i and list[i] % 3 == 0: #если равен индексу и кратен 3
            res += 1 #увеличиваем количество на 1
    return res

arr = [0, 1, 2, 3, 4, 5, 6]

print(count(arr))