'''
34. Дано два лінійних масиву однаково ї розмірності. Скласти третій масив з
добутку елементів перших двох масивів, що стоять на місцях з однак овим індексом.
'''

#функция которая создаёт новый массив из двух, переданных в функцию, перемножая элементы с одинаковыми индексами
def new_arr(list1, list2):
    new_list = [] #новый массив
    for i in range(len(list1)): #для всех элементов массива1 и массива2
        new_list.append(list1[i] * list2[i]) #добавляем в новый массив произведение элементов с одинаковыми индексами
    return new_list

arr1 = [1, 2, 3, 4]
arr2 = [4, 3, 2, 1]

print(new_arr(arr1, arr2))
