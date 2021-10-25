revenue = int(input('Введите прибыль компании: '))
costs = int(input('Введите издержки компании: '))
income = revenue - costs

if income < 0:
    print('Убытки фирмы:', income)
elif income > 0 or income == 0:
    print('Прибыль фирмы:', income)
    profitability = int((income / revenue) * 100)
    print(profitability)
    employees = int(input('Введите число сотрудников: '))
    income_per_employee = int(income - int(income / employees))
    print(income_per_employee)
