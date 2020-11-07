revenue = float(input("Введите значение выручки - "))
costs = float(input("Введите значение издержек - "))
result = revenue - costs
if result > 0:
    print(f"Поздравляем! Ваша компания работает с прибылью {result}")
    print(f"Рентабельность выручки составила {result / revenue:3f}")
    personal_n = int(input("Сколько сотрудников работает в вашей компании?"))
    print(f"Если Вы раздадите прибыль сотрудникам, то каждый получит по {result / personal_n:.3f}")
elif result < 0:
    print(f"Жаль, ваша компания в убытке на {-result} ")
else:
    print(f"Старайтесь выйти в плюс!")