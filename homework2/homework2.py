num = input("Введите число: ")
try:
    num = int(num)

    def bin(n):
        if n == 0:
            return ""
        else:
            return bin(n // 2) + str(n % 2)

    def oct(n):
        if n < 8:
            return str(n)
        else:
            return oct(n // 8) + str(n % 8)

    print("Двоичная: ", bin(num))
    print("Восьмеричная: ", oct(num))

except ValueError:
    print("Невозможно произвести код: введите целое число.")
