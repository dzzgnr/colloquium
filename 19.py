import numpy as np
import random
while True:
    try:
        a = np.array([random.randint(200,300) for i in range(20)])
        s = 0
        for i in range(len(a)):
            if a[i] % 2 == 3:
                s += a[i]
        print("Масив: ",a)
        print("Добуток: ",s)
    except ValueError:
        print("Не коректне значення")

    print("Щоб запустити програму спочатку натисніть  1. Для виходу будь яке інше значення")
    choise = input()
    if choise == "1":
        continue
    else:
        break
