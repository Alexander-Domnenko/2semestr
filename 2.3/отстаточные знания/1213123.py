# import time
# time_start = time.clock()
# time_elapsed = (time.clock() - time_start)
# import resource
# resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

# Задача 1
def task1():
    a = input('Введите значение a: ')
    b = input('Введите значение b: ')
    c = input('Введите значение c: ')
    b, c, a = c, a, b


# Задача 2.1
def task2():
    flag=True
    while flag:
        try:
            num1, num2=input('Введите числа через пробел ').split()
            num1=float(num1)
            num2=float(num2)
            flag=False
        except ValueError:
            print('Это не числа, либо количество введеных значений больше 2')
            flag=True
# Задача 2.2
def task2_2():
    flag = True
    try:
        n = int(input('Сколько чисел вы хотите ввести? '))
        list = []
        while flag:
            for i in range(n):
                i = int(input())
                list.append(i)
            flag = False
    except ValueError:
        print('Это не числа')
        flag = True
# Задача 3.1
def task3_1():
    try:
        num = int(input('Введите число от 0 до 100'))
        if num >= 0 and num <= 100:
            print(num**5)
        else:
            print('num >= 0 and num <= 100')
    except ValueError:
        print('Это не число')


# Задача 3.2
def task3_2():
    try:
        num = int(input('Введите число от 0 до 100'))
        if num >= 0 and num <= 100:
            print(num*num*num*num*num)
        else:
            print('num >= 0 and num <= 100')
    except ValueError:
        print('Это не число')



#Задача 12
def task12():
    a=[1,2,3,4,5,6,7,8,9]
    print(a[::-1])
#Задача 11
def task11():
    a=[1,2,3,4,5,6,7,8,9]
    print(a[-1])
    print(a[len(a)-1])
    for i in a:
        r=i
    print(r)

#Задача 5
def task5_1():
    month = int(input ('Choose a month'))
    if month == 1 or month == 2 or month == 12:
        print ('Зима')
    elif month == 3 or month == 4 or month == 5:
        print ('Весна')
    elif month == 6 or month == 7 or month == 8:
        print ('Лето')
    elif month == 9 or month == 10 or month == 11:
        print ('Осень')
    else:
        print ('Неверное число')



def task5_2():
    times_of_year = {'Зима': (1, 2, 12),
           'Осень': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}
 
    month = int(input('Введите номер месяца: '))
    for key in times_of_year.keys():
        if month in times_of_year[key]:
            print(key)


#Задача 6
def task6():
    n=int(input())
    chet=[]
    nechet=[]
    for i in range(1,n+1):
        if i%2==0:
            chet.append(i)
        else:
            nechet.append(i)
    sumchet=sum(chet)
    sumnechet=sum(nechet)
    kolchet=len(chet)
    kolnechet=len(nechet)

#Задача 4

def task4():
    n=int(input())
    if n>=0 and n<=250:
        if ((5*(n**2)+4)**0.5)%1==0 or ((5*(n**2)-4)**0.5)%1==0:
            print('True')
        else:
            print('False')

# Задача 8
def task8():
    n=int(input())
    m=int(input())
    for a in range(n,m):
        for b in range(a,m):
            for c in range(b,m):
                if a*a+b*b==c*c:
                    print(a,b,c)
#Задача 7
def task7():
    n=int(input())
    r=[]
    if n>=1 and n<=250:
        for i in range(1,int(n/2+1)):
            if (n%i==0):
                r.append(i)
    print(n, len(r))


#Задача 13
def task13(list):
    if list==[]:
        return 0
    else:
        return list[0]+task13(list[1:])


# n = int(input())

# for i in range(1, n + 1):
#     for j in range(1, n):
#         print(i * j, end=' ')
#     print(i * n)

# def dop():
#     r=[]
#     for i in range(1,int(n/2+1)):
#         if (n%i==0):
#             r.append(i)
#     return r


# n=4
# res=[]
# for j in range(2,len(res)<n):
#     a =sum(dop(j)) 
#     if a==j:
#         res.append(j)
# print(res)