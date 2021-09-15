lilly_years = int(input())
wm_price = float(input())
toy_price = int(input())

money_received = int()
toys_received = int()
even_birthdays = 0

for num in range(1, lilly_years + 1):

    if num % 2 == 0:
        money_received += num * 5
        even_birthdays += 1
    else:
        toys_received += 1

money_received -= even_birthdays

toy_money = toys_received * toy_price

total_saved_money = money_received + toy_money

diff = total_saved_money - wm_price

if diff >= 0:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {abs(diff):.2f}")
