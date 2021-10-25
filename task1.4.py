number = int(input('Введите число: '))
result = 0


while number > 0:
    var = number % 10
    if var > result:
        result = var
    number //= 10
print(result)

