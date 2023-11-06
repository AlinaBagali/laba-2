salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
minus_list = []
for month in range(9):
    spend = spend + spend*increase
    sr = salary - spend
    minus_list.append(sr)
    minus_list_pr = sum(minus_list)
    mm = minus_list_pr*(-1) + 1000
    money_capital = round(mm, 2)
    months = 10
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:",  money_capital)
