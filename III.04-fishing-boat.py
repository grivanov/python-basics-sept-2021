budget = int(input())
season = input()
fishermen = int(input())
ship_price = 0

if season == "Spring":
    ship_price = 3000

elif season == "Summer" or season == "Autumn":
    ship_price = 4200

else:
    ship_price = 2600


if fishermen <= 6:
    ship_price -= ship_price * 0.1
elif fishermen > 6 and fishermen <= 11:
    ship_price -= ship_price * 0.15
elif fishermen >= 12:
    ship_price -= ship_price * 0.25


if fishermen % 2 == 0 and not(season == "Autumn"):
    ship_price -= ship_price * 0.05

diff = budget - ship_price

if budget >= ship_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(diff):.2f} leva.")
