import math


def addition(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return 'Помилка: Ділення на нуль'
    return a / b


def root(a):
    return math.sqrt(a)


def factorial(a):
    return math.factorial(a)

print('*********************')
while True:
    print("Вибери операцію")
    print('1. Додавання')
    print('2. Віднімання')
    print('3. Множення')
    print('4. Ділення')
    print('5. Корінь')
    print('6. Факторіал')
    print('7. Вихід')

    choice = input('Вибери операцію: ')

    if choice == '7':
        print('Вихід з програми...')
        break

    if choice not in ('1', '2', '3', '4', '5', '6'):
        print('Помилка: невірне число. Спробуй ще раз!')
        continue
    if choice in ('1', '2', '3', '4'):
        num1 = float(input('Введи перше число: '))
        num2 = float(input('Введи друге число: '))
    elif choice == '5':
        num1 = float(input('Введи число: '))
    elif choice == '6':
        num1 = int(input('Введи число: '))

    if choice == '1':
        print('Результат додавання: ', addition(num1, num2))
    elif choice == '2':
        print('Результат віднімання: ', minus(num1, num2))
    elif choice == '3':
        print('Результат множення: ', multiplication(num1, num2))
    elif choice == '4':
        print('Результат ділення: ', division(num1, num2))
    elif choice == '5':
        if num1 < 0:
            print('Помилка, відьемне число')
        else:
            print('Результат: ', root(num1))
    elif choice == '6':
        print('Результат: ', factorial(num1))

