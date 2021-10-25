time_in_second = input('Введите время в секундах: ')

hours = int((int(time_in_second) / 60) / 60)
minutes = int(int(time_in_second) % 60)
seconds = (int(time_in_second) % 60)
print(f"{hours:02}:{minutes:02}:{seconds:02}")
