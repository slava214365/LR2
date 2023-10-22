money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
rate = 1 + increase # Коэффициент роста цен
month = 0

while money_capital > 0:
    money_capital += salary - spend * rate ** month
    if money_capital > 0:
        month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
