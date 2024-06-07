name = str(input())
cost = int(input())
weight = int(input())
money = int(input())

name_line = name
cost_line = str(weight) + "кг * " + str(cost) + "руб/кг"
score_line = str(weight * cost) + "руб"
money_line = str(money) + "руб"
change_line = str(money - (weight * cost)) + "руб"

print("================Чек================")
print(f"Товар:{name_line:>29}")
print(f"Цена:{cost_line:>30}")
print(f"Итого:{score_line:>29}")
print(f"Внесено:{money_line:>27}")
print(f"Сдача:{change_line:>29}")
print("===================================")