from math import *

trip_price = float(input())

puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzles_price = puzzles * 2.60
dolls_price = dolls * 3.0
bears_price = bears * 4.1
minions_price = minions * 8.20
trucks_price = trucks * 2.0

total_items = puzzles + dolls + bears + minions + trucks
total_price = float(puzzles_price + dolls_price +
                    bears_price + minions_price + trucks_price)

if total_items >= 50:
    total_price = total_price - (total_price * 0.25)

total_price = total_price - (total_price * 0.1)

money_left = total_price - trip_price

if money_left >= 0:
    print(f"Yes! {money_left:.2f} lv left.")
else:
    print(f"Not enough money! {abs(money_left):.2f} lv needed.")
