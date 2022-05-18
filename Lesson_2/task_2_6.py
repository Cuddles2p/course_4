'''6. В программе генерируется случайное целое число от 0 до 100.
 Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, то вывести загаданное число.'''
import random
number= random.randint(0,100)
print(number)
paht = 0

while True:
    user_number = input('Введите число: ')
    try:
        numb = int(user_number)
    except ValueError:
        print('Неверный формат!')
        break

    if numb == number and paht <=9:
        print(f'Вы угадали! число = {number}')
        print(f'Попытока: {paht} из 10')
        break
    elif numb > number and paht <= 9:
        print('Загаданное число меньше выбранного.')
        paht += 1
        print(f' Попытока: {paht} из 10')
    elif numb < number and paht <= 9:
        print('Загаданное число больше введенного числа.')
        paht += 1
        print(f'Попытока: {paht} из 10')
    elif paht == 10:
        print('Количество попыток израсходовано')
        break