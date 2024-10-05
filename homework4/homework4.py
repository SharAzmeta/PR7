a = input("Введите a: ")
b = input("Введите b: ")
c = input("Введите c: ")
try:
    a=int (a)
    b=int (b)
    c=int (c)
    x = a*b+4*c
    print (x)
except ValueError:
    print("Невозможно произвести код: введите целое число.")
