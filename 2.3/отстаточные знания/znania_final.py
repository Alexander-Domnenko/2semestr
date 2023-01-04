from datetime import datetime
from tkinter import *
from tkinter.ttk import Combobox
from memory_profiler import memory_usage


def print_task_1():
    print()
    print('''Cоставить программу обмена значениями трех переменных а, b, c: так, 
чтобы b присвоилось значение c, с присвоить значение а, a присвоить значение b.
Сколько времени и памяти затратилось на выполнение программы?''')
    print()


def print_task_2_1():
    print()
    print('''Консольная программа.
Пользователь вводит 2 числа. Проверьте, что это именно числа, если это не так, 
то выведите пользователю ошибку и попросите ввести число снова.
Когда пользователь ввел числа, выведите сумму этих чисел''')
    print()


def print_task_2_2():
    print()
    print('''Доработайте задачу так, чтобы пользователь мог вводить n разных чисел. 
Предоставьте возможность ввести n самому пользователю''')
    print()


def print_task_3_1():
    print()
    print('''Дано число x, которое принимает значение от 0 до 100. Вычислите чему будет равно x^5''')
    print()


def print_task_3_2():
    print()
    print('''Измените задачу так, чтобы для вычисления степени использовалось только умножение.
Посмотрите сколько времени и памяти занимают оба метода. Что можно сделать для оптимизации данной задачи?''')
    print()


def print_task_4():
    print()
    print('''Пользователь может вводить число от 0 до 250. Проверьте, принадлежит ли введенное число числам фибоначи''')
    print()


def print_task_5():
    print()
    print('''Реализуйте программу двумя способами на определение времени года в зависимости от введенного месяца года.''')
    print()


def print_task_6():
    print()
    print('''Посчитайте сумму, количество четных и нечетных чисел от 1 до n. N вводит пользователь''')
    print()


def print_task_7():
    print()
    print('''Для каждого из чисел от 1 до n, где n меньше 250 выведите количество делителей. N вводит пользователь.
Выведите число и через пробел количество его делителей. Делителем может быть 1.
Сколько памяти и времени занимает программа, что сделано для оптимизации затрачиваемых ресурсов?''')
    print()


def print_task_8():
    print()
    print('''Найти все различные пифагоровы тройки из интервала от N до М.''')
    print()


def print_task_9():
    print()
    print('''Найти все целые числа из интервала от N до M, которые делятся на каждую из своих цифр.''')
    print()


def print_task_10():
    print()
    print('''Натуральное число называется совершенным, если оно равно сумме всех своих делителей, включая единицу. 
Вывести первые N (N<5) совершенных чисел на экран.''')
    print()


def print_task_11():
    print()
    print('''Задайте одномерный массив в коде и выведите в консоль последний элемент данного массива тремя способами. 
Сравните их по времени выполнения.''')
    print()


def print_task_12():
    print()
    print('''Задайте одномерный массив в коде и выведите в консоль массив в обратном порядке''')
    print()


def print_task_13():
    print()
    print('''Реализуйте нахождение суммы элементов массива через рекурсию. Массив можно задать в коде.''')
    print()


def print_task_14_1():
    print()
    print('''Реализуйте оконное приложение-конвертер рублей в доллары. Создайте окно ввода для суммы в рублях''')
    print()


def print_task_14_2():
    print()
    print('''Доработайте приложение так, чтобы можно было переводить доллары в рубли.''')
    print()


def print_task_15():
    print()
    print('''Реализуйте вывод таблицы умножения в консоль размером n на m которые вводит пользователь,
но при этом они не могут быть больше 20 и меньше 5''')
    print()


def get_memory_consumption():
    return memory_usage()


def all_divisor_number(n):
    r = []
    for i in range(1, n//2+1):
        if n % i == 0:
            r.append(i)
    return r


def task_1():
    '''Задача 1'''
    # Потребление памяти 40 Мб затрачено времени 0.992ms
    print_task_1()
    a = input('Введите a: ')
    b = input('Введите b: ')
    c = input('Введите c: ')
    b, c, a = c, a, b
    print(a, b, c)


def task_2_1():
    '''Задача 2.1'''
    print_task_2_1()
    try:
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
        print(a + b)
    except ValueError:
        print("введите корректное число")
        task_2_1()


def task_2_2():
    '''Задача 2.2'''
    print_task_2_2()
    try:
        n = int(input('Сколько чисел вы хотите ввести? '))
        lst = []
        for i in range(n):
            i = float(input('Введите число '))
            lst.append(i)
        print(sum(lst))
    except ValueError:
        print('введите корректное число')
        task_2_2()


def task_3_1():
    '''Задача 3.1'''
    # Потребление памяти 39Мб затрачено времени 0.277ms
    print_task_3_1()
    try:
        num = int(input('Введите число от 0 до 100: '))
        start = datetime.now()
        if num >= 0 and num <= 100:
            print(num**5)
        else:
            print('число должно быть от 0 до 100')
    except ValueError:
        print('введите корректное число')
        task_3_1()


def task_3_2():
    '''Задача 3.2'''
    # Потребление памяти 40Мб затрачено времени 0.998ms
    print_task_3_2()
    try:
        num = float(input('Введите число от 0 до 100: '))
        if num >= 0 and num <= 100:
            print(num*num*num*num*num)
        else:
            print('число должно быть от 0 до 100')
    except ValueError:
        print('введите корректное число')
        task_3_2()


def task_4():
    '''Задача 4'''
    print_task_4()
    try:
        n = float(input('Введите число для проверки: '))
        if n >= 0 and n <= 250:
            if ((5*(n**2)+4)**0.5) % 1 == 0 or ((5*(n**2)-4)**0.5) % 1 == 0:
                print(True)
            else:
                print(False)
        else:
            print('число должно быть от 0 до 250')
            task_4()
    except ValueError:
        print('введите корректное число')
        task_4()


def task_5_1():
    '''Задача 5'''
    print_task_5()
    try:
        month = float(input('Введите номер месяца: '))
        if month == 1 or month == 2 or month == 12:
            print('Зима')
        elif month == 3 or month == 4 or month == 5:
            print('Весна')
        elif month == 6 or month == 7 or month == 8:
            print('Лето')
        elif month == 9 or month == 10 or month == 11:
            print('Осень')
        else:
            print('Неверное число')
    except ValueError:
        print('введите корректное число')
        task_5_1()


def task_5_2():
    '''Задача 5 другим способом'''
    print_task_5()
    try:
        times_of_year = {'Зима': [1, 2, 12],
                         'Весна': [3, 4, 5],
                         'Лето': [6, 7, 8],
                         'Осень': [9, 10, 11]}
        month = float(input('Введите номер месяца от 1 до 12: '))
        if month <= 12 and month >= 1:
            for key in times_of_year.keys():
                if month in times_of_year[key]:
                    print(key)
        else:
            print('неверный номер месяца')
            task_5_2()
    except ValueError:
        print('введите корректное число')
        task_5_2()


def task_6():
    '''Задача 6'''
    print_task_6()
    try:
        n = int(input('введите кол-во чисел '))
        chet = []
        nechet = []
        for i in range(1, n+1):
            if i % 2 == 0:
                chet.append(i)
            else:
                nechet.append(i)
        sumchet = sum(chet)
        sumnechet = sum(nechet)
        kolchet = len(chet)
        kolnechet = len(nechet)
        print(
            f'сумма и кол-во четных {sumchet},{kolchet} \nсумма и кол-во нечетных {sumnechet},{kolnechet}')
    except ValueError:
        print('введите корректное число')
        task_6()


def task_7():
    '''Задача 7'''
    # Потребление памяти 39Мб затрачено времени 0.994ms
    print_task_7()
    try:
        n = int(input('введите n < 250: '))
        r = []
        if n >= 1 and n <= 250:
            for i in range(1, int(n/2+1)):
                if (n % i == 0):
                    r.append(i)
        else:
            print('неверное n')
            print_task_7()
        print(f'кол-во делителей числа {n} = {len(r)}')
    except ValueError:
        print('введите корректное число')
        task_7()


def task_8():
    '''Задача 8'''
    print_task_8()
    try:
        n = int(input('Введите N: '))
        m = int(input('Введите M: '))
        for a in range(n, m):
            for b in range(a, m):
                for c in range(b, m):
                    if a*a+b*b == c*c:
                        print(a, b, c)
    except ValueError:
        print('Введите корректное число')
        task_8()


def task_9():
    '''Задача 9'''
    print_task_9()
    try:
        r = []
        c = 0
        n = int(input('введите N: '))
        m = int(input('введите M: '))
        for j in range(n, m+1):
            for i in str(j):
                if int(i) != 0 and j % int(i) == 0:
                    c += 1
            if c == len(str(j)):
                r.append(j)
            c = 0
        print(r)
    except ValueError:
        print('введите корректное число')
        task_9()


def task_10():
    '''Задача 10'''
    print_task_10()
    r = []
    n = 0
    c = 2
    while n < 4:
        if c == sum(all_divisor_number(c)):
            r.append(c)
            c += 1
            n += 1
        else:
            c += 1
    print(r)


def task_11_1():
    '''Задача 11 первый способ'''
    # Затрачено времени 0.995ms
    print_task_11()
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in a:
        r = i
    print(f'изначальный список {a}, последний элемент {r}')


def task_11_2():
    '''Задача 11 второй способ'''
    # затрачено времени 0.996ms
    print_task_11()
    start = datetime.now()
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f'изначальный список {a}, последний элемент {a[-1]}')


def task_11_3():
    '''Задача 11 третий способ'''
    # затрачено времени 0.994ms
    print_task_11()
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f'изначальный список {a}, последний элемент {a[len(a)-1]}')


def task_12():
    '''Задача 12'''
    print_task_12()
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(
        f'изначальный список {a}, список с элементами в обратном порядке {a[::-1]}')


def task_13():
    '''Задача 13'''
    print_task_13()

    def task_13_do(lst=[1, 2, 3, 4]):
        print(lst)
        if lst == []:
            return 0
        else:
            return (lst[0]+task_13_do(lst[1:]))
    print(task_13_do([1, 2, 3, 4]))


def task_14_1():
    '''Задача 14'''
    print_task_14_1()

    def convert():
        try:
            result_title.config(text=f'{float(rubles_input.get())/70} $')
        except ValueError:
            result_title.config(
                text='Введите корректное значение', font=('Calibri', 20))

    tk = Tk()
    tk['bg'] = '#fafafa'
    tk.title('Конвертер рублей в доллары')
    tk.geometry('450x250')

    title = Label(tk, text='Введите кол-во рублей', font=('Calibri',
                  16), bg='gray', pady=5, padx=5, width=400, height=2)
    title.pack()

    rubles_input = Entry(tk, bg='white', width=400, font=('Calibri', 30))
    rubles_input.pack()

    btn = Button(tk, text='Конвертировать', bg='gray',
                 command=convert, width=400, height=2, font=('Calibri', 16))
    btn.pack()

    result_title = Label(tk, text='', font=('Calibri', 30),
                         bg='white', pady=5, padx=5, width=400, height=2)
    result_title.pack()
    tk.mainloop()


def task_14_2():
    '''Задача 14.2'''
    print_task_14_2()
    currency_name = ['USD', 'RUB']

    def convert():
        try:
            if combobox.get() == 'RUB':
                result_title.config(text=f'{float(rubles_input.get())/70} $')
            else:
                result_title.config(text=f'{float(rubles_input.get())*70} P')
        except ValueError:
            result_title.config(
                text='Введите корректное значение', font=('Calibri', 20))

    tk = Tk()
    tk['bg'] = '#fafafa'
    tk.title('Конвертер')
    tk.geometry('450x300')

    combobox = Combobox(tk, values=currency_name,
                        width=400, font=('Calibri', 20))
    combobox.current(1)
    combobox.pack()

    title = Label(tk, text='Введите кол-во валюты', font=('Calibri',
                  16), bg='gray', pady=5, padx=5, width=400, height=2)
    title.pack()

    rubles_input = Entry(tk, bg='white', width=400, font=('Calibri', 30))
    rubles_input.pack()

    btn = Button(tk, text='Конвертировать', bg='gray',
                 command=convert, width=400, height=2, font=('Calibri', 16))
    btn.pack()

    result_title = Label(tk, text='', font=('Calibri', 30),
                         bg='white', pady=5, padx=5, width=400, height=2)
    result_title.pack()

    tk.mainloop()


def task_15():
    '''Задача 15'''
    print_task_15()
    try:
        n = int(input('введите n>=5 & n<=20: '))
        m = int(input('введите m>=5 & m<=20: '))
        if n >= 5 and n <= 20 and m >= 5 and m <= 25:
            for i in range(n, m+1):
                for j in range(n, m+1):
                    print(f'{i*j:4}', end=' ')
                print()
        else:
            print('неверный диапозон')
    except ValueError:
        print('Введите корректное число')
        task_15()


def task_16():
    '''Задача 16'''
    pass


def select_action(functions):
    '''Выбор действия из доступных'''
    is_run = True
    while is_run:
        print('\nДоступные операции: ')
        for i, item in enumerate(functions):
            print(i, item.__name__)
        i = int(input('\nВыберете операцию: '))
        if i < len(functions):
            function = functions[i]
            function()
        else:
            is_run = False


def get_actions():
    '''Получение доступных действий'''
    return [task_1,
            task_2_1,
            task_2_2,
            task_3_1,
            task_3_2,
            task_4,
            task_5_1,
            task_5_2,
            task_6,
            task_7,
            task_8,
            task_9,
            task_10,
            task_11_1,
            task_11_2,
            task_11_3,
            task_12,
            task_13,
            task_14_1,
            task_14_2,
            task_15
            ]


select_action(get_actions())
