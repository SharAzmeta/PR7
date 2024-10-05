num = input("Введите число: ")
try:
    num = int(num)

    def ter(n):
        if n < 3:
            return str (n)
        else:
            return ter(n//3) + str (n%3)

    print("Троичная: ", ter(num))

except ValueError:
    print("Невозможно произвести код: введите целое число.")
