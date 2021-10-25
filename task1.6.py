a = int(input('Кол-во км в первый день: '))
b = int(input('Общий результат: '))
result = 0
print(a)

while a < b:
    result = (a * 0.1) + a
    a = result
    print(a)