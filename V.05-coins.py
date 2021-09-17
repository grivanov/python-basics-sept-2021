from math import floor

change = float(input())
count_coins = 0

change_in_cents = change * 100

while change_in_cents > 0:

    if change_in_cents / 200 >= 1:
        count_coins += floor(change_in_cents / 200)
        change_in_cents -= floor(change_in_cents / 200) * 200

    elif change_in_cents / 100 >= 1:
        count_coins += floor(change_in_cents / 100)
        change_in_cents -= floor(change_in_cents / 100) * 100

    elif change_in_cents / 50 >= 1:
        count_coins += floor(change_in_cents / 50)
        change_in_cents -= floor(change_in_cents / 50) * 50

    elif change_in_cents / 20 >= 1:
        count_coins += floor(change_in_cents / 20)
        change_in_cents -= floor(change_in_cents / 20) * 20

    elif change_in_cents / 10 >= 1:
        count_coins += floor(change_in_cents / 10)
        change_in_cents -= floor(change_in_cents / 10) * 10

    elif change_in_cents / 5 >= 1:
        count_coins += floor(change_in_cents / 5)
        change_in_cents -= floor(change_in_cents / 5) * 5

    elif change_in_cents / 2 >= 1:
        count_coins += floor(change_in_cents / 2)
        change_in_cents -= floor(change_in_cents / 2) * 2

    elif change_in_cents / 1 >= 1:
        count_coins += floor(change_in_cents / 1)
        change_in_cents -= floor(change_in_cents / 1) * 1

    else:
        break


print(count_coins)
