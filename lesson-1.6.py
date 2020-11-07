def km(res_min, res_max, days):
    if res_min > res_max:
        return days
    else:
        return km(res_min * 1.1, res_max, days + 1)


print(km(int(input("Enter first param")), int(input("Enter second param")), 1))