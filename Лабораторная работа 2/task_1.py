money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0
perv_mes = salary + money_capital - spend
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while perv_mes >= 0:
    spend = spend + spend*increase
    perv_mes = perv_mes + salary -spend
    month += 1
print("Количество месяцев, которое можно протянуть без долгов:", month)
