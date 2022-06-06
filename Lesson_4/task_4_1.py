import random
import timeit

'''1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.'''
print("\nЗадача 1")
# Немного усложенная задача из ДЗ к третьему уроку

def lst_generator_solution(lower, upper, devider_lower, devider_upper):
    print("Решение через сложный генератор списков в одну строку (полный перебор):",
          sum([(1 if sum(k) > 0 else 0) for k in
               [[(1 if (i % j == 0) else 0) for j in range(devider_lower, devider_upper)] for i in
                range(lower, upper)]]))


def normal_solution(lower, upper, devider_lower, devider_upper):
    n = 0
    for i in range(lower, upper):
        j = devider_lower
        while i % j != 0 and j <= devider_upper:
            j += 1
        n = (n + 1) if j <= devider_upper else n
    print("Нормальный алгоритм проверки (перебор до первого деления без остатка):", n)


def optimal_solution(lower, upper, devider_lower, devider_upper):

    prime_lst = [2]
    for chek_num in range(prime_lst[0] + 1, devider_upper + 1):
        for i in prime_lst:
            if chek_num % i == 0: break
            if i == prime_lst[-1]: prime_lst.append(chek_num)

    n = 0
    for i in range(lower, upper):
        for j in prime_lst:
            if i % j == 0:
                n += 1
                break
    print("Оптимальный алгоритм проверки (перебор до первого деления без остатка):", n)


print("Расчет кол-ва чисел в диапазоне 2-100000 кратных хотя бы одному числу от 2 до 500")
print("Время расчета:", timeit.timeit("normal_solution(2, 100000, 2, 500)", setup="from __main__ import normal_solution", number=1), "\n")
print("Время расчета:", timeit.timeit("optimal_solution(2, 100000, 2, 500)", setup="from __main__ import optimal_solution", number=1), "\n")
print("Время расчета:", timeit.timeit("lst_generator_solution(2, 100000, 2, 500)", setup="from __main__ import lst_generator_solution", number=1))
print("\nВыводы: Решени задачи через генератор списка более компактное и быстрее пишется но низкоэффективное.\nРазница с обычным перебором (до первого деления без остатка) до 10 раз и с оптимальным решением,\nкогда проверяется только делимость на простые числа разница порядка 50 раз!!!")

