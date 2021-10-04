import timeit
import os
from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored
#Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Style: DIM, NORMAL, BRIGHT, RESET_ALL

def ins_sort(arr):  #сортировка вставками(в порядке возрастания)
    for i in range(len(arr)):  #проходим по элементам массива
        j = i - 1  #счётчик
        key = arr[i]  #присвоить буферному элементу первый индекс(в неотсортированной секции)
        while arr[j] > key and j >= 0:  #пока arr[j] больше key и j >= 0
            arr[j + 1] = arr[j]  #смещаем все элементы на 1 позицию влево
            j -= 1  #уменьшаем j на единицу
        arr[j + 1] = key  #присваиваем элементу с индексом j + 1 буферный элемент

def sel_sort(arr):  #сортировка выбором(в порядке возрастания)
    for i in range(len(arr) - 1):  #проходим по элементам массива
        m = i  #m - индекс минимального элемента в текущей секции массива
        j = i + 1  #индекс соседнего элемента
        while j < len(arr):  #проходим по необработанным элементам массива
            if arr[j] < arr[m]:  #если j-ый элемент массива меньше m-го
                m = j  #присваиваем индексу минимального элемента j
            j = j + 1  #увеличиваем левую границу неотсортированной секции массива на 1(смещаем на 1 позицию вправо)
        arr[i], arr[m] = arr[m], arr[i]  #меняем местами элементы массива

init( )
a = [53, 12, 68, 63, 3, 47, 50, 61, 41]
a1 = [53, 12, 68, 63, 3, 47, 50, 61, 41]

print(colored("Сортировка вставками", "yellow"))
print("Неотсортированный массив:" + str(a))
start = timeit.default_timer( )
ins_sort(a)
end = timeit.default_timer( )
print(colored("Время выполнения {0} секунд".format("%.7f" % float(end - start)), "blue"))
print("Отсортированный массив:" + str(a) + "\n")

print(colored("Сортировка выбором", "yellow"))
print("Неотсортированный массив:" + str(a1))
start = timeit.default_timer( )
sel_sort(a1)
end = timeit.default_timer( )
print(colored("Время выполнения {0} секунд".format("%.7f" % float(end - start)), "blue"))
print("Отсортированный массив:" + str(a1) + "\n")

os.system("pause")
