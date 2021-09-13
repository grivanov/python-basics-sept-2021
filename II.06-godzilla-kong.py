budget = float(input())
crew = int(input())
clothes_price = float(input())

decor = budget * 0.10
total_clothes = crew * clothes_price

if crew > 150:
    total_clothes = total_clothes - (total_clothes * 0.1)

total_sum = decor + total_clothes
diff = total_sum - budget

if total_sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {abs(diff):.2f} leva left.")
