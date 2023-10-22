salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
rate = 1 + increase # Коэффициент роста цен
money_capital = 0

for month in range(10):
    money_capital += spend * rate ** month - salary

money_capital = int(money_capital)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital  )
