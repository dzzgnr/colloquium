'''
28. Знайти кількість парних елементів одновимірного масиву.
'''

#функция, которая принимает на вход массив и возвращает количество чётных элементов массива
def even_count(list):
    count = 0
    for i in range(len(list)):
        if list[i] % 2 == 0:
            count += 1
    return count

arr = [1, 2, 3, 4, 5]

print(even_count(arr))
