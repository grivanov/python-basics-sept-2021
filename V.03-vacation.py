neeeded_money = float(input())
saved_money = float(input())
days_spend_count = 0
days_count = 0

while days_spend_count < 5:
    days_count += 1
    money_action = input()
    action_money = float(input())

    if money_action == "spend":
        days_spend_count += 1
        saved_money -= action_money

        if saved_money < 0:
            saved_money = 0

    else:
        days_spend_count = 0
        saved_money += action_money

        if saved_money >= neeeded_money:
            print(f"You saved the money for {days_count} days.")
            break


if days_spend_count == 5:
    print("You can't save the money.")
    print(days_count)
