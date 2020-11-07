time = int(input("Введите время в секундах: "))
hours = time // 3600
minutes = (time // 60) - (hours * 60)
second = time % 60
print(f"{hours:02}:{minutes:02}:{second:02}")