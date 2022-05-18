'''4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.'''
while True:
    try:
        n = float(input('Введите количество элементов: '))
    except ValueError:
        print('Неверный формат')
        break
    i = 0
    range_number = 1
    sum = 0
    while i < n:
        sum += range_number
        range_number /= -2
        i += 1

    print(f'Сумма {sum}')
    break