'''
29. Знайти кількість парних елементів одновимірного масиву до першого
зустрінутого числа рівного наперед заданому числу а.
'''

#функция, которая принимает на вход массив и число и возвращает количество чётных элементов массива до того, как в массиве встретится переданное в функцию число
def even_count(list, num):
    count = 0 
    i = 0
    while list[i] != num:
        if list[i] % 2 == 0:
            count += 1
        i += 1
    return count

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

num = int(input('enter number : '))

print(even_count(arr, num))

