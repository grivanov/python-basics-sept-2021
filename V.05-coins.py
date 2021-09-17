from typing import Counter


change = float(input())
count_coins = 0

change_in_cents = change * 100

while change_in_cents > 0:

    if change_in_cents % 200 != change_in_cents:
        count_coins += 1
        print("coin 2 lv")
        change_in_cents = change_in_cents % 200

    elif change_in_cents % 100 != change_in_cents:
        count_coins += 1
        print("coin 1 lv")
        change_in_cents = change_in_cents % 100

    elif change_in_cents % 50 != change_in_cents:
        count_coins += 1
        print("coin 0.50 lv")
        change_in_cents = change_in_cents % 50

    elif change_in_cents % 20 != change_in_cents:
        count_coins += 1
        print("coin 0.20 lv")
        change_in_cents = change_in_cents % 20

    elif change_in_cents % 10 != change_in_cents:
        count_coins += 1
        print("coin 0.10 lv")
        change_in_cents = change_in_cents % 10

    elif change_in_cents % 5 != change_in_cents:
        count_coins += 1
        print("coin 0.05 lv")
        change_in_cents = change_in_cents % 5

    elif change_in_cents % 2 != change_in_cents:
        count_coins += 1
        print("coin 0.02 lv")
        change_in_cents = change_in_cents % 2
        if change_in_cents == 0:
            continue
    elif change_in_cents % 1 != change_in_cents:
        count_coins += 1
        print("coin 0.01 lv")
        change_in_cents = change_in_cents % 1

    else:
        break


print(count_coins)
