# Сложность - O(n^2)

import random # Функция для рандомизации массива


def insertion_sort(nums): # Функция сортировки
    for i in range(1, len(nums)): # Рассматриваем массив от 2 элемента
        insert = nums[i] # Текущий элемент
        # Перемещаем элементы nums [0… i-1], которые больше значения, на одну позицию впереди их текущей позиции.
        j = i - 1 
        while j >= 0 and nums[j] > insert: # Проверяем j и jый элемент сравниваем с текущим
            nums[j + 1] = nums[j] # Перемещаем элемент если условие выполнено
            j -= 1 # Меняем итератор
        nums[j + 1] = insert # Передаем следующее значение

n = 10 # Длина массива
mas = [random.randint(1, 100) for i in range(n)] # Составляем массив
insertion_sort(mas) # Применяем функцию
print(mas)
