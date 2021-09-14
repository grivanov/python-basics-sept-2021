flowers = input()
flowers_amount = int(input())
budget = int(input())

price_per_flower = 0
perc_discount = 0
perc_overcharge = 0
total = 0

if flowers == "Roses":
    price_per_flower = 5

    if flowers_amount > 80:
        perc_discount = 0.1

    total = price_per_flower * flowers_amount
    total -= total * perc_discount

elif flowers == "Dahlias":
    price_per_flower = 3.8

    if flowers_amount > 90:
        perc_discount = 0.15

    total = price_per_flower * flowers_amount
    total -= total * perc_discount

elif flowers == "Tulips":
    price_per_flower = 2.8

    if flowers_amount > 80:
        perc_discount = 0.15

    total = price_per_flower * flowers_amount
    total -= total * perc_discount

elif flowers == "Narcissus":
    price_per_flower = 3

    if flowers_amount < 120:
        perc_overcharge = 0.15

    total = price_per_flower * flowers_amount
    total += total * perc_overcharge

else:
    price_per_flower = 2.5

    if flowers_amount < 80:
        perc_overcharge = 0.2

    total = price_per_flower * flowers_amount
    total += total * perc_overcharge

diff = budget - total

if budget >= total:
    print(
        f"Hey, you have a great garden with {flowers_amount} {flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(diff):.2f} leva more.")
