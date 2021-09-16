account_sum = 0
add_sum = ""

while True:
    add_sum = input()

    if add_sum == "NoMoreMoney":
        break
    elif float(add_sum) < 0:
        print("Invalid operation!")
        break
    else:
        add_sum = float(add_sum)
        account_sum += add_sum
        print(f"Increase: {add_sum:.2f}")

print(f"Total: {account_sum:.2f}")
