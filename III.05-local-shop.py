select_product = input()
select_city = input()
select_quantity = float(input())

item_price = 0

if select_city == "Sofia":
    if select_product == "coffee":
        item_price = 0.50
    elif select_product == "water":
        item_price = 0.80
    elif select_product == "beer":
        item_price = 1.20
    elif select_product == "sweets":
        item_price = 1.45
    elif select_product == "peanuts":
        item_price = 1.60
elif select_city == "Plovdiv":
    if select_product == "coffee":
        item_price = 0.40
    elif select_product == "water":
        item_price = 0.70
    elif select_product == "beer":
        item_price = 1.15
    elif select_product == "sweets":
        item_price = 1.30
    elif select_product == "peanuts":
        item_price = 1.50
elif select_city == "Varna":
    if select_product == "coffee":
        item_price = 0.45
    elif select_product == "water":
        item_price = 0.70
    elif select_product == "beer":
        item_price = 1.10
    elif select_product == "sweets":
        item_price = 1.35
    elif select_product == "peanuts":
        item_price = 1.55

print(select_quantity * item_price)